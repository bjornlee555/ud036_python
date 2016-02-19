from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC3160bf6f22338d062ff64bc2975ba3f9"
auth_token  = "c1767aaf28960462d858f99667e4b596"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="My name is Bjorn Lee?",
    to="+16502419660",    # Replace with your phone number
    from_="+16505177197") # Replace with your Twilio number
print message.sid