from .models import UserData
from hashlib import sha1
import base64

def save_details(full_name, phone_number, email_address, password, location):
    encoded_plain = base64.b64encode(bytes(password, 'utf-8'))
    encoded_password = sha1(encoded_plain).hexdigest()
    row = UserData(full_name = full_name,
                    phone_number = phone_number,
                    email_address = email_address,
                    password = encoded_password,
                    location = location)
    row.save()

def new_user(email_address):
    row = UserData.objects.filter(email_address = email_address)
    if(len(row)==0):
        return True
    return False
