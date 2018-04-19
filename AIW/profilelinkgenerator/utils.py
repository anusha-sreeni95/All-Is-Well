from profilelinkgenerator.models import UrlTokens

def validate_token(token, email_address):
    return UrlTokens.objects.filter(token=token, email_address=email_address).exists()
