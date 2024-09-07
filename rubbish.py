import requests
import time

# 设置 API 地址
API_URL = 'http://127.0.0.1:1323'

# 用户名
username = 'byr'

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

# 提交次数
submission_count = 0

while True:
    # 更新 token
    try:
        heartbeat_url = f'{API_URL}/api/heartbeat'
        headers = {'Authorization': f'Bearer {token}'}
        heartbeat_response = requests.get(heartbeat_url, headers=headers)
        
        heartbeat_response.raise_for_status()  # 检查响应状态码
        token = heartbeat_response.json()['token']
        print(f"Token 更新成功")

    except requests.exceptions.RequestException as e:
        if e.response.json()['message'] == 'Bad Gateway':
            print(f"未能更新 Token: {e}")
            time.sleep(8)
        else:
            print(f"未能更新 Token: {e}")
            time.sleep(8)

    try:
        # 获取信息
        info_url = f'{API_URL}/api/info'
        info_response = requests.get(info_url, headers=headers)
        info_response.raise_for_status()  # 检查响应状态码
        code = info_response.json()['code']

        # 提交信息
        validate_url = f'{API_URL}/api/validate'
        validate_data = {'code': code}
        validate_response = requests.post(
            validate_url, headers=headers, data=validate_data)

        # 打印结果
        print(f"提交信息: {code}, 响应: {validate_response.text}")

        # 计数
        submission_count += 1
        print(f"已提交 {submission_count} 次")

    except requests.exceptions.RequestException as e:
        # 如果服务器不可用，则等待 5 秒
        if e.response.json()['message'] == 'Bad Gateway':
            print(f"服务器不可用: {e}")
            time.sleep(8)
        else:
            print(f"请求错误: {e}")
            time.sleep(8)

    # 等待 1 秒
    time.sleep(1)
