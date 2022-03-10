import requests

# URL = "https://cityhop-341920.ew.r.appspot.com/"
URL = "http://127.0.0.1:5000/"

test_url = URL + 'scooters'
# test_data = {"email": "sofia@mail.co.za", "f_name": "Sofia", "l_name": "Auger", "phone_num": "08192371123", "password": "password1",}

# response = requests.put(test_url, test_data)
response = requests.get(test_url)
print(response.json())