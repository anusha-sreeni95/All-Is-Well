from .models import UserData

def save_details(first_name, last_name, phone_number, email_address, password):
    row = UserData(first_name = first_name,
                    last_name = last_name,
                    phone_number = phone_number,
                    email_address = email_address,
                    password = password)
    row.save()

def new_user(email_address):
    row = UserData.objects.filter(email_address = email_address)
    if(len(row)==0):
        return True
    return False
