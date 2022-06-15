import requests
import json

url = "http://127.0.0.1:8081/users"

payload = json.dumps({
  "ime": "Djordje",
  "prezime": "Stevanovic",
  "smer": "RI",
  "username": "djstevanovic17",
  "predmeti": [
    {
	  "espb": "6",
      "ime": "PDS"
    },
	{
	  "espb": "6",
      "ime": "NDS"
	}
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
