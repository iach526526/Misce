# 說明

- #### main.py中的index和P2ret很可疑又很無用，是什麼呢？
- 執行
```py
print(base64.b64decode(Secret[0]).decode('utf-8'))
```