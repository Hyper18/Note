import requests
params = {'firstname': 'Michael', 'lastname': 'Jordan'}
request = requests.post(
    "http://pythonscraping.com/files/processing.php", data=params)
print(request.text)
