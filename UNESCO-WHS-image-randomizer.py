import requests
import webbrowser
import random

random_integer = random.randrange(1, 1200, 1)  

# URL of the webpage you want to open
url_template = "https://whc.unesco.org/en/list/"
url_2 = "/gallery/"
final_url = url_template + str(random_integer) + url_2
print(final_url)


# Use the requests library to get the webpage content
response = requests.get(final_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Open the webpage in the default web browser
    webbrowser.open(final_url)
else:
    print("Failed to open the webpage. Status code:", response.status_code)