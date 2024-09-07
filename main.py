import requests
import time
import json

# 服务器地址
BASE_URL = "http://127.0.0.1:1323"


def signup(username):
    response = requests.post(f"{BASE_URL}/signup", data={"username": username})
    return response.json()


def login(username, password):
    response = requests.post(
        f"{BASE_URL}/login", data={"username": username, "password": password})
    return response.json()["token"]


def heartbeat(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/api/heartbeat", headers=headers)
    return response.json()["token"]


def get_info(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/api/info", headers=headers)
    return response.json()["code"]


def validate(token, code):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(
        f"{BASE_URL}/api/validate", headers=headers, data={"code": code})
    return response.text


def main():
    succuss = False
    token = None
    
    while succuss is False:
        try:
            username = "kyoci"
            user_data = signup(username)
            token = login(username, user_data["password"])
            succuss = True
        except Exception as e:
            print(f"登录失败，因为 {e}")
            time.sleep(2)

    print(f"登录成功，{token}")

    while True:
        try:
            token = heartbeat(token)
            print(f"Token 更新成功")

            code = get_info(token)
            result = validate(token, code)
            print(f"提交代码: {code}, 结果: {result}")
            
            time.sleep(2)

        except requests.exceptions.ConnectionError as e:
            print(f"连接错误: {e}")
            time.sleep(5)
        except requests.exceptions.Timeout as e:
            print(f"请求超时: {e}")
            time.sleep(5)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP 错误: {e}")
            time.sleep(5)
        except Exception as e:
            print(f"Unexpected error: {e}")
            try:
                token = login(username, user_data["password"])
            except Exception as e:
                print(f"嵌套内登录错误")
                time.sleep(5)
            time.sleep(5)  # 如果发生其他错误，等待5秒后继续


if __name__ == "__main__":
    main()
