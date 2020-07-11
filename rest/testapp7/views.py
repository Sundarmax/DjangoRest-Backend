from django.shortcuts import render

# Create your views here.
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

account_sid = 'AC63dcfe5bb0fb7eb23d4862187fd0ccdd'
auth_token = '47affcb6b81719e9885edf56ed78a048'
client = Client(account_sid, auth_token)

def createNewVerificationService():
    service = client.verify.services.create(
                                     friendly_name='Aeiser'
                                 )
    print(service.sid)

def SendVerificationToken():
    
    verification = client.verify .services('VA97bb729fe157ecee4be496265bc9ee30') .verifications.create(to='', channel='sms')
    print(verification.status)


def CheckTokenVerification():
    verification_check = client.verify.services('VA97bb729fe157ecee4be496265bc9ee30').verification_checks.create(to='+919500490424', code='502999')
    print(verification_check.status)

#SendVerificationToken()
#createNewVerificationService()
#CheckTokenVerification()
