from login import *
import os

def get_beneficiaries():
    beneficiaries = session.get('https://cdn-api.co-vin.in/api/v2/appointment/beneficiaries')
    if beneficiaries.status_code == 200:
        print("Successfully Fetch Beneficiaries")
        print(beneficiaries.json())
    else:
        print(f"Beneficiaries Status_code: {beneficiaries.status_code}\n{beneficiaries.text}")

def book_slot(book):
    out = get_authenticated_session()
    if out == False: raise Exception("Failed to login")
    print(f"Trying to book: {book}")
    get_captcha()
    book["captcha"] = input("Enter Captcha:")
    book = json.dumps(book)
    resp = session.post("https://cdn-api.co-vin.in/api/v2/appointment/schedule", data=book)
    if resp.status_code == 200:
        print("Scheduled Successfully.")
        print(f"response: {resp.json()}")
        return True
    else:
        print(f"booking error. {resp.status_code}\n{resp.text}")
        return False

def get_captcha():
    out = session.post("https://cdn-api.co-vin.in/api/v2/auth/getRecaptcha")
    if out.status_code == 200:
        captcha = out.json()['captcha']                                                                                                                                                                     
        with open("svg.html", "w") as f: 
            f.write(captcha)
        os.system("start svg.html")
        print("captcha downloaded successfully")
                
def book_appointment(center_details, age=18):
    sessions = center_details['sessions']
    print(f"\ncenter name: {center_details['name']}, capacity: {sessions['available_capacity']}, slots: {sessions['slots']}")
    if DOSE == 2 and VACCINE != sessions['vaccine']:
        print(f"looking for {VACCINE} but availability is for {sessions['vaccine']}")
        return False
    book = {
        "center_id": center_details['center_id'],
        "session_id": sessions['session_id'],
        "beneficiaries": Beneficiaries_Ids[f"{age}"],
        "slot": sessions['slots'][0],
        "dose": DOSE
    }
    print(f"book: {book}")
    stop = book_slot(book)
    # stop = True
    if stop:
        print("booking successfull")
        return True
    else:
        print("booking failed")
            
def find_centers(age=18):
    for pincode in PINCODES:
        print(f"Checking for pincode: {pincode}\n")
        out = session.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={DATE}")
        if out.status_code == 200:
            for center in out.json()['centers']:
                if center['fee_type'] != VACCINE_FEE: continue
                for sessions in center['sessions']:
                    capacity = sessions.get(f'available_capacity_dose{DOSE}', None)
                    if capacity == None: continue
                    if capacity >= len(Beneficiaries_Ids[f"{age}"]) and sessions['min_age_limit'] == age:
                        center_details = {
                            'name': center['name'],
                            'center_id': center['center_id'],
                            'sessions': sessions
                        }
                        print(f"\nbooking available for below center:\n{center_details} and vaccine: {sessions['vaccine']}")
                        status = book_appointment(center_details, age)
                        if status:
                            return True
        else:
            print(f"Unable to find centers.\nstatus code: {out.status_code}")
            print(f"response: {out.text}")
        time.sleep(RATE)
        

        
if __name__ == '__main__':
    while True:
        try:
            out = find_centers(age=18)
            if out:
                break
        except Exception as e:
            print(f"error: {e}")
