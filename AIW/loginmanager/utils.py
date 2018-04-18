from signupmanager.models import UserData

def verify_credentials(email_address, password):
    row = UserData.objects.filter(email_address = email_address)[0]
    if(password == row.password):
        return True
    else:
        return False
