from signupmanager.models import UserData
from hashlib import sha1
import base64

def verify_credentials(email_address, password):
    rows = UserData.objects.filter(email_address = email_address)
    for row in rows:
        encoded_plain = base64.b64encode(bytes(password, 'utf-8'))
        encoded_password = sha1(encoded_plain).hexdigest()
        if(encoded_password == row.password):
            return True
        else:
            return False
