import base64
import requests
import os
import json

#the api endpoint for the job application. Send resumes and personal information to this URL via a POST request!
url = "https://api.perka.com/1/communication/job/apply"



#define what type of content this script is sending
headers = {
        'Content-Type': 'application/json',
    }
#encode pdf into base 64 format for use by payload
with open("JerryWangResume.pdf", "rb") as pdf_file:
    encoded_resume = base64.b64encode(pdf_file.read())

#the dictionary that will be serialized to JSON format and sent to Perka's server using their api endpoint
payload = {
        'first_name' : 'Jerry',
        'last_name' : 'Wang',
        'email' : 'jerry.wang.ct@gmail.com',
        'position_id' : 'GENERALIST',
        'explanation' : 'First, I refreshed my memory on how to make an http api post request. I decided to write a simple python script to make the http request. Next, I looked up testing servers that would accept http post requests, to ensure that whatever I sent to the server would be received in its proper format. I used base64, a python library, to encode my pdf into the base64 string and attached it to my json body. Finally, once I was satisfied that the code performed the POST request correctly using the testing server, I executed the python script and made the POST request to the API endpoint specified. Hopefully you guys will be able to read this, it was actually a very fun exercise and very much different from the normal resume submission process!',
        'projects': ['https://itunes.apple.com/us/app/songbrush/id1437937682?mt=8','https://jerrywang.org','https://github.com/notimeleft'],
        'source' : 'Glassdoor',
        'resume': encoded_resume
    }
#the final api request, which stores the response (hopefully a 200!)
response = requests.request("POST", url, json = payload, headers=headers)


print(response.text)
print(response.status_code)

# test whether the base 64 encoding worked, by decoding the same result and writing to desktop
with open(os.path.expanduser('~/Desktop/test.pdf'), 'wb') as fout:
     fout.write(base64.decodestring(encoded_resume))

