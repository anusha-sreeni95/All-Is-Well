from datetime import datetime
from .models import UserData
from hashlib import sha1
import base64
from profilelinkgenerator.models import UrlTokens

def __save_token_to_database(email_address, token):
    row = UrlTokens(email_address=email_address, token=token)
    row.save()

def unique_token_generator(full_name, email_address, password):
    time = datetime.now().isoformat()
    plain = full_name + '\0' + time + '\0' + email_address + '\0' + password
    encoded_plain = base64.b64encode(bytes(plain, 'utf-8'))
    token = sha1(encoded_plain).hexdigest()
    __save_token_to_database(email_address, token)
    return token

def generate_profile_link(request, full_name, email_address, password):
    unique_hash = unique_token_generator(full_name, email_address, password)
    absolute_uri=request.build_absolute_uri()
    if(absolute_uri.endswith('signup/')):
        absolute_uri=absolute_uri.replace('signup/','')
    unique_url = absolute_uri+'profile/'+unique_hash
    return unique_url

def save_details(full_name, phone_number, email_address, password, location, profile_link):
    encoded_plain = base64.b64encode(bytes(password, 'utf-8'))
    encoded_password = sha1(encoded_plain).hexdigest()
    row = UserData(full_name = full_name,
                    phone_number = phone_number,
                    email_address = email_address,
                    password = encoded_password,
                    location = location,
                    profile_link = profile_link)
    row.save()

def new_user(email_address):
    row = UserData.objects.filter(email_address = email_address)
    if(len(row)==0):
        return True
    return False
