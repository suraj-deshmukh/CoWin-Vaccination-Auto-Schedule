from datetime import timedelta, datetime
DATE = (datetime.today() + timedelta(1)).strftime("%d-%m-%Y")
LIMIT = 3 #otp retry limit

PINCODES = [411001,411006] #list of pincodes by your preference.  

REGISTERED_MOBILE_NUMBER = 1234567890 # 10 digit mobile number in int 

Beneficiaries_Ids = { 
    '18':["",""],
    '45':[""]
} #beficiary ids in str format

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json',
    'Origin': 'https://selfregistration.cowin.gov.in',
    'Connection': 'keep-alive',
    'Referer': 'https://selfregistration.cowin.gov.in/',
    'TE': 'Trailers',
}
