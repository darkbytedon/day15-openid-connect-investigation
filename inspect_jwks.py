import json

with open("google-jwks.json", "r") as file:
    jwks = json.load(file)

print("Number of public keys:", len(jwks["keys"]))

for key in jwks["keys"]:
    print("\nKey ID:", key["kid"])
    print("Key type:", key["kty"])
    print("Algorithm:", key.get("alg", "Not specified"))
    print("Key use:", key.get("use", "Not specified"))
    print("Public exponent:", key["e"])

