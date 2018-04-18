from .models import UserData
from hashlib import sha1
import base64

def save_details(full_name, phone_number, email_address, password, interests, location):
    encoded_plain = base64.b64encode(bytes(password, 'utf-8'))
    encoded_password = sha1(encoded_plain).hexdigest()
    environment = 0
    education = 0
    animal = 0
    medical = 0
    if('Environment' in interests):
        environment = 1
    if('Education' in interests):
        education = 1
    if('Animal' in interests):
        animal = 1
    if('Medical' in interests):
        medical = 1
    row = UserData(full_name = full_name,
                    phone_number = phone_number,
                    email_address = email_address,
                    password = encoded_password,
                    location = location,
                    environment = environment,
                    education = education,
                    animal = animal,
                    medical = medical)
    row.save()

def new_user(email_address):
    row = UserData.objects.filter(email_address = email_address)
    if(len(row)==0):
        return True
    return False
