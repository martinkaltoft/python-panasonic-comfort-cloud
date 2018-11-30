try:
    # Python 3
    from urllib.parse import quote_plus
except ImportError:
    # Python 2
    from urllib import quote_plus

BASE_URL = 'https://accsmart.panasonic.com'

def login():
    return '{base_url}/auth/login'.format(
        base_url=BASE_URL)

def get_groups():
    return '{base_url}/device/group'.format(
        base_url=BASE_URL)

def overview(guid): 
    return '{base_url}/deviceStatus/now/{guid}'.format(
        base_url=BASE_URL,
        guid=guid
    )

def control(): 
    return '{base_url}/deviceStatus/control'.format(
        base_url=BASE_URL
    )