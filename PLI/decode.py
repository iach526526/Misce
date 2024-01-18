import base64
def d(string):
    return base64.b64decode(string).decode('utf-8')