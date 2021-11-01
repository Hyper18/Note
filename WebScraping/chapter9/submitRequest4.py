import requests
params = {"username": "test", "password": "123456"}
r = requests.post(
    "http://pythonscraping.com/pages/cookies/welcome.php", params)
print(r.cookies.get_dict())
print("to next page")
r = requests.post(
    "http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)

print(r.text)

session = requests.Session()
# similar moves
s = session.post(
    "http://pythonscraping.com/pages/cookies/welcome.php", params)
print(s.cookies.get_dict())
print("to next page")
s = session.post(
    "http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
