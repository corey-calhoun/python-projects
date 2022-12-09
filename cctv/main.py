# Python Script for webcams using Windy API
import requests

base_uri = "https://api.windy.com/api/webcams/v2/list/country=CN/category=traffic?show=webcams:url"
headers = {
    'x-windy-key': 'Fd8E62dje11x7Wh6jwfOIIdoNNuAUUzd'
}
response = requests.get(base_uri, headers=headers)

print(response.json())
