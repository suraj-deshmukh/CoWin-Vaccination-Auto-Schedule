# CoWin-Vaccination-Auto-Schedule
## A Python 3 Script to Conitnuosly Monitor Vaccine Availability and Schedule CoWin Vaccination Appointment. This supports Capcha.  

### Please add/change REGISTERED_MOBILE_NUMBER, Beneficiaries_Ids, DOSE, VACCINE and PINCODES as per your choice before following below steps.

Requirements:
Python 3 and requests library

Steps:

1. execute book.py script using ```python book.py``` command

    Once you start the script, it will iterate over the given PINCODES indefinately and would check the availability of vaccines. 
    
    you will get log message given below
    
    ```
    Checking for pincode: 411001

    Checking for pincode: 411006

    Checking for pincode: 411002

    Checking for pincode: 411011

    Checking for pincode: 411017

    Checking for pincode: 411026

    Checking for pincode: 425412
    
    Checking for pincode: 411001

    Checking for pincode: 411006

    Checking for pincode: 411002

    Checking for pincode: 411011

    Checking for pincode: 411017

    Checking for pincode: 411026

    Checking for pincode: 425412
    ``` 
    
   As soon as vaccine slots becomes available to any of the given pincodes script would first attemp to login
   
   you will get log message given below
   
    ```
    sending otp..........
    OTP SENT SUCCESSFULLY
    Transaction ID: {'txnId': 'b09b5a70-f381-43ae-8393-88c638af5f3e'}
    Press y/Y to continue if you received OTP.
    Press n/N to retry. Max Retry limit:3
    ===>
    ```  

      -  Once you get OTP on your registered number then press ```y``` or ```Y``` and then ```enter``` key to continue.
          You will see log message like shown below.

          ```
          Enter OTP received on 1234567890: 
          ```

          Enter the OTP and press ```enter``` key

      -   If you don't get OTP within 3 minutes then press ```n``` or ```N``` and then ```enter``` key to retry. Limit is 3. If you don't get OTP in 3 trials then script will continue to monitor pincodes.

2.  Once you enter correct OTP you will see below message.

    ```sending otp..........
    OTP SENT SUCCESSFULLY
    Transaction ID: {'txnId': 'b09b5a70-f381-43ae-8393-88c638af5f3e'}
    Press y/Y to continue if you received OTP.
    Press n/N to retry. Max Retry limit:3
    ===>y      
    Enter OTP received on 1234567890: 380906
    OTP SUCCESSFULLY VERIFIED
    ```
3.  After successfull login, script will try to book the slot. ***Script won't ask you to choose center/slots/vaccine or any of the parameter if its first dose and for 2nd dose it will choose the vaccine given by you in config.py file***. 
    API needs capcha output as well. Script will download capcha in html format as ```svg.html``` in same working directory as ```book.py```. Script will ask you to enter the captcha. Open ```svg.html``` in browser and enter the capcha and press ```enter```(***capcha is case sensitive***)
    
    You will get log message given below
    
    ```
    Trying to book: {'center_id': 687758, 'session_id': '0d66a93e-7325-48a9-8375-1b5f3bc5fddd', 'beneficiaries': ['19403282229890'], 'slot': '09:00AM-11:00AM', 'dose': 1}
    captcha downloaded successfully
    Enter Captcha:5muwy
    Scheduled Successfully.
    response: {'appointment_confirmation_no': '32c5b4d3-abcf-42fd-8913-da98898bac11'}
    booking successfull
    ```
    
Note: 

*This Script will book appointment for next day by default. If you wish to change this behaviour you can edit DATE variable in config.py*

*It is very basic script. Use it on your own risk.*   



![1](https://user-images.githubusercontent.com/14833831/117652838-4b902e00-b1b1-11eb-90c0-4289f2ec62c4.png)
![2](https://user-images.githubusercontent.com/14833831/117652861-52b73c00-b1b1-11eb-9441-1f2f5cf509b9.png)
![3](https://user-images.githubusercontent.com/14833831/117652865-534fd280-b1b1-11eb-9b71-1c497a052f34.png)



