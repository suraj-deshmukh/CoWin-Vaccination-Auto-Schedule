# CoWin-Vaccination-Auto-Schedule
## A Python 3 Script to Schedule CoWin Vaccination Appointment. This script supports Capcha.  

### Please add/change REGISTERED_MOBILE_NUMBER, Beneficiaries_Ids and PINCODES as per your choice before following below steps.

Requirements:
Python 3 and requests library


Steps:

1. execute book.py script using ```python book.py``` command

    You should see below output
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

      -   If you don't get OTP within 3 minutes then press ```n``` or ```N``` and then ```enter``` key to retry. Limit is 3. If you don't get OTP in 3 trials then script will terminate itself.

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
3.  After successfull login, Script will iterate over given PINCODES and will try to book appointment directly where slots are availble to book. It is important to specify only desired PINCODES. Script won't ask you to choose center/slots/vaccine or any of the parameter. **
4.  Once script finds the available slot, it will automatically download captcha in ```svg.html``` file. Script will ask you to enter the captcha and press ```enter```. The ```svg.html``` file will be present under current working directory. Please note capcha is **case sensitive** .If you enter captcha correctly then you will get log message as below 

    ```Scheduled Successfully.``` 
    
    
Note: 

*This script will only help you to book the slot using given PINCODES if slots are available. If slots are already full script will stop automatically.*

*This Script will book appointment for next day by default. If you wish to change this behaviour you can edit DATE variable in config.py*

*Script is tested for both 18-44 and 45+ group for first dose only. It is very basic script. Use it on your own risk. Various vaccine availability notification scripts are available, this project is easy to integrate with such notification scripts.*   
