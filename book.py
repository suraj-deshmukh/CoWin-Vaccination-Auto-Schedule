from login import *

def get_beneficiaries():
    beneficiaries = session.get('https://cdn-api.co-vin.in/api/v2/appointment/beneficiaries')
    if beneficiaries.status_code == 200:
        print("Successfully Fetch Beneficiaries")
        print(beneficiaries.json())
    else:
        print(f"Beneficiaries Status_code: {beneficiaries.status_code}\n{beneficiaries.text}")

def book_slot(book):
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
        print("captcha downloaded successfully")
      

def book_appointment(age=18, dose=1):
    for i in PINCODES:
        out = session.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={i}&date={DATE}")
        if out.status_code == 200:
            for j in out.json()['centers']:
                for sessions in j['sessions']:
                    print(f"\ncenter name: {j['name']} capacity: {sessions['available_capacity']} slots: {sessions['slots']}")
                    if sessions['available_capacity'] > 0 and sessions['min_age_limit'] == age:
                        book = {
                            "center_id": j['center_id'],
                            "session_id": sessions['session_id'],
                            "beneficiaries": Beneficiaries_Ids[f"{age}"],
                            "slot": sessions['slots'][0],
                            "dose": dose
                        }
                        stop = book_slot(book)
                        if stop:
                            print("booking successfull")
                            return True
        else:
            print(f"status code: {out.status_code}")
            print(f"response: {out.text}")
    
        
if __name__ == '__main__':
    out = get_authenticated_session()
    if out != False:
        # get_beneficiaries()
        book_appointment(age=45) #fdefault to 18
        # book_appointment(age=45) # for 45+age group
    else:
        print("Failed to login")
