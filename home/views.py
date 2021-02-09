from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from . models import customer,resume
# Create your views here.
def home(request):
    data=resume.objects.all()
    return render(request,'sravan1.html',{'data':data})
c=[8,6,7]
def cust(request):
    if request.method=="POST":
        name=request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        c[0]=name
        c[1]=email
        c[2]=subject
        x=customer(name=name,email=email,subject=subject)
        x.save()
        from twilio.rest import Client
        # Your Account Sid and Auth Token from twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = 'ACf8f08b760c3e6c77cfa020c41f7b042c'
        auth_token = '5f8d4b3f55d965d5b98e43d14ed85bc0'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="name {} "
                 "email {}"
                 " subject {} ".format(c[0], c[1], c[2]),
            from_='+16099007744',
            to='+919010926456'
        )

        print(message.sid)
        messages.success(request,"message sent")
        return redirect('/')
def mess(request):
    import os
    import twilio
    from twilio.rest import Client
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = 'ACf8f08b760c3e6c77cfa020c41f7b042c'
    auth_token = '5f8d4b3f55d965d5b98e43d14ed85bc0'
    client = Client(account_sid, auth_token)

    message = client.messages .create(
        body="name {} email {} subject {} ".format(c[0],c[1],c[2]),
        from_='+16099007744',
        to='+919010926456'
    )

    print(message.sid)
    messages.info(request,"message sent to sravan")
    return redirect('/')