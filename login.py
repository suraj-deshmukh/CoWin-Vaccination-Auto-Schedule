from config import *
import requests
import json
import hashlib
import sys, time

session = requests.Session()
session.headers = headers

def retry(func):
    def _retry():
        for i in range(LIMIT):
            print("sending otp..........")
            txn=func()
            if txn != False:
                is_otp_received = input("Press y/Y to continue if you received OTP.\nPress n/N to retry. Max Retry limit:3\n===>")
                if is_otp_received == 'y' or is_otp_received == 'Y':
                    return txn
                elif is_otp_received == 'n' or is_otp_received == 'N':
                    continue
        print("Max Retries Exceeded")
        return False
    return _retry #this is the fun_obj mentioned in the above content

@retry
def generateOTP():
    data = {"secret":"U2FsdGVkX196RKSOE31ozbO/QRHGJ6RuEqacJuqWO4NQaA+7SO/1Ixzhqe/fkMtk4HjsB7Bjy1GKdC7qGOHeBg==","mobile": REGISTERED_MOBILE_NUMBER}
    resp = session.post('https://cdn-api.co-vin.in/api/v2/auth/generateMobileOTP', data=json.dumps(data))
    if resp.status_code == 200:
        print("OTP SENT SUCCESSFULLY")
        out_json = resp.json()
        print(f"Transaction ID: {out_json}")
        return out_json
    else:
        print(f"Generate otp Status code: {resp.status_code}\n{resp.text}")
        return False


def validateOTP(txnId=None):
    otp = input(f"Enter OTP received on {REGISTERED_MOBILE_NUMBER}: ")
    pin = hashlib.sha256(bytes(otp, 'utf-8')).hexdigest()
    validate = {}
    validate["otp"] = pin
    validate["txnId"] = txnId  
    resp = session.post('https://cdn-api.co-vin.in/api/v2/auth/validateMobileOtp', data=json.dumps(validate))
    if resp.status_code == 200:
        print("OTP SUCCESSFULLY VERIFIED")
        out_json = resp.json()
        return out_json
    else:
        print(f"Validate otp Status code: {resp.status_code}\n{resp.text}")
        return False# sys.exit('Terminated')
    
def get_authenticated_session():
    # session = requests.Session()
    txn = generateOTP()
    if txn != False:
        token_json = validateOTP(txnId=txn['txnId'])
        if token_json != False: 
            token = token_json['token']
            header = {'Authorization': f"Bearer {token}"}
            session.headers.update(header)
            return True
        else:
            print("Login Failed")
            return False
    else:
        print("LOGIN Failed")
        return False
        
        
if __name__ == '__main__':
    session = get_authenticated_session()