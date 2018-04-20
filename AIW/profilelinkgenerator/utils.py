from profilelinkgenerator.models import UrlTokens

def get_email_address(token):
    if(UrlTokens.objects.filter(token=token).exists()):
        return UrlTokens.objects.filter(token=token)[0].email_address
    else:
        return None
