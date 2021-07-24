import jwt

key = "secret"
encoded = jwt.encode({"some": "payload"}, key, algorithm="HS256")
encoded = jwt.encode({"some": "payload"}, key[:-1], algorithm="HS256")
try:
    decoded = jwt.decode(encoded, key, algorithms="HS256")
    print(decoded)

except (jwt.InvalidSignatureError, jwt.InvalidTokenError) as e:
    print("B")
except jwt.InvalidSignatureError as e:
    print("A")
except jwt.InvalidTokenError as e:
    print("HI")
    

