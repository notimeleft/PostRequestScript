# PostRequestScript
A simple python script that makes a POST request to an API endpoint, to fulfill Perka's "apply by API" challenge

To run the script, execute this command after editing the filename in line 16 to suit whatever pdf you want to encode to base64. The script will also write your encoded file back to desktop by default. 
> python PostRequestScript.py 


Eh? Apply by API? What's that?
Perka had a normal job application process, and a slightly more interesting process where applicants could send their information and resume through an http POST request. 

Knowing little about making http requests and web APIs, I decided this was the perfect challenge with an appropriate Goldilocks level of difficulty to start learning about them. 


To send the resume, I encoded it into base 64 format (python has a built-in library for that) and packed it into a dictionary object, which would be serialized into JSON format before sending. 

I used http://httpbin.org and http://ptsv2.com to test the validity of what this script was sending. 

Being the paranoid schizophrenic that I am, I decoded the base64 resume and wrote its results back to desktop, just to make sure the resume had indeed been encoded/decoded correctly 

When I executed this script, I got back a success code '200' along with a response from Perka: 'You did it!'

Alas, I didn't get a reply from Perka regarding the job. But it was quite fun to take up the challenge, and I learned a lot of practical things about http requests. 
