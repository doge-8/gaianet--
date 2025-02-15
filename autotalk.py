import requests
import time
import json

while True:
    try:
        # 发送 HTTP 请求
        response = requests.post(
            "https://节点号.us.gaianet.network/v1/chat/completions",
            headers={"accept": "application/json", "Content-Type": "application/json"},
            data='{"messages":[{"role":"system", "content": "You are now a tour guide in Paris"}, {"role":"user", "content": "Please help me introduce the scenery and tourism culture of Paris"}]}'
        )

        # 打印响应结果
        try:
            print(response.json())
        except requests.exceptions.JSONDecodeError as e:
            print("JSON decode error:", e)
            print("Response text:", response.text)

        # 等待 1 秒钟
        time.sleep(1)

    except Exception as e:
        print("Error:", e)
