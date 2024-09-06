import requests

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiVHMyIiwiZXhwIjoxNjk1NjE5ODE4fQ.pE87ZmJc5QmVpBtEiG4a0P_OVdSiD2XyNhzyHNNjL_Y',
}

response = requests.get('http://127.0.0.1:1323/api/heartbeat', headers=headers)

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiVHMyIiwiZXhwIjoxNjk1NjE5ODE4fQ.pE87ZmJc5QmVpBtEiG4a0P_OVdSiD2XyNhzyHNNjL_Y',
}

response = requests.get('http://127.0.0.1:1323/api/info', headers=headers)

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiVHMyIiwiZXhwIjoxNjk1NjE5ODE4fQ.pE87ZmJc5QmVpBtEiG4a0P_OVdSiD2XyNhzyHNNjL_Y',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'code': '79db02dec4',
}

response = requests.post(
    'http://127.0.0.1:1323/api/validate', headers=headers, data=data)


def signup(username):
    data = {
        'username': f'{username}',
    }
    response = requests.post('http://127.0.0.1:1323/signup', data=data)
    return response


def login(username='kyoci', password=''):
    data = {
        'username': f'{username}',
        'password': f'{password}',
    }
    response = requests.post('http://127.0.0.1:1323/login', data=data)
    return response
