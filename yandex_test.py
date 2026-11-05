from yandex_music import Client

def on_code(code):
    print(f"Откройте {code.verification_url} и введите код: {code.user_code}")

auth_client = Client()
token = auth_client.device_auth(on_code=on_code)

print(f"access_token={token.access_token}")

client = Client(token.access_token).init()
print(client.me.account.login)
