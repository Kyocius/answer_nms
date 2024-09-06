import requests
import time

# 设置 API 地址
API_URL = 'http://127.0.0.1:1323'

# 用户名
username = 'kyoci'

# 获取密码
signup_url = f'{API_URL}/signup'
signup_data = {'username': username}
signup_response = requests.post(signup_url, data=signup_data)
password = signup_response.json()['password']

# 登录获取 token
login_url = f'{API_URL}/login'
login_data = {'username': username, 'password': password}
login_response = requests.post(login_url, data=login_data)
token = login_response.json()['token']

# 持续提交信息
while True:
  # 更新 token
  heartbeat_url = f'{API_URL}/api/heartbeat'
  headers = {'Authorization': f'Bearer {token}'}
  heartbeat_response = requests.get(heartbeat_url, headers=headers)
  token = heartbeat_response.json()['token']

  # 获取信息
  info_url = f'{API_URL}/api/info'
  info_response = requests.get(info_url, headers=headers)
  code = info_response.json()['code']

  # 提交信息
  validate_url = f'{API_URL}/api/validate'
  validate_data = {'code': code}
  validate_response = requests.post(validate_url, headers=headers, data=validate_data)

  # 打印结果
  print(f"提交信息: {code}, 响应: {validate_response.text}")

  # 等待 5 分钟
  time.sleep(5)