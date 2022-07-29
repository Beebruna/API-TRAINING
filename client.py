import requests

response = requests.get('http://127.0.0.1:8000/test', stream=True)


for r in response.iter_lines():
    print(r)
    print('passei uma linha')
