import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('User_test', 'password')
r = requests.post(
    url="http://pythonscraping.com/pages/auth/login.php", auth=auth)

print(r.text)
