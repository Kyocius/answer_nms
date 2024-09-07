import requests
import time
import json

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
    username = "kyoci"
    user_data = signup(username)
    token = login(username, user_data["password"])

    last_heartbeat_time = time.time()
    last_info_time = time.time()

    while True:
        try:
            current_time = time.time()

            # 每8秒更新一次token
            if current_time - last_heartbeat_time > 8:
                token = heartbeat(token)
                last_heartbeat_time = current_time
                print("Token updated")

            # 每10秒获取并提交一次info
            if current_time - last_info_time > 10:
                code = get_info(token)
                result = validate(token, code)
                last_info_time = current_time
                print(f"Submitted code: {code}, Result: {result}")

            time.sleep(1)  # 休眠1秒，避免过于频繁的请求

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            time.sleep(5)  # 如果发生错误，等待5秒后继续
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            time.sleep(5)  # 如果发生JSON解析错误，等待5秒后继续
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(5)  # 如果发生其他错误，等待5秒后继续


if __name__ == "__main__":
    main()
