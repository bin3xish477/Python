#! /usr/bin/env python

import smtplib 
  
# create SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("sender_email", "your_password") 
  
# message to be sent 
message = "write message here"
  
# sending the mail 
s.sendmail("sender_email", "receiver_email", message) 

# end session
s.quit() 
