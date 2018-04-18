from signupmanager.models import UserData

def verify_credentials(email_address, password):
    rows = UserData.objects.filter(email_address = email_address)
    for row in rows:
        if(password == row.password):
            return True
        else:
            return False
