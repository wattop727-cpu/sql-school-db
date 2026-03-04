import base64
from urllib.parse import quote, unquote
# ASCII encoding
text = "This is Encoding"
for ch in text:
    print("This is ASCII Value")
    print(f"{ch} => {ord(ch)}")

#Base 64 encoding
encoded = base64.b64encode(text.encode()).decode()
decoded = base64.b64decode(encoded).decode()
print(f"\nOriginal : {text}")
print(f"Encoded Base64 : {encoded}")
print(f"Decoded  : {decoded}")

# url encoding
url = "name=Swarnim limbu &city=Kathmandu Nepal"
enc_url = quote(url)
dec_url = unquote(enc_url)
print(f"\nOriginal : {url}")
print(f"Encoded URL : {enc_url}")
print(f"Decoded  : {dec_url}")

# hexa base 16 enocding
text = "Swarnim limbu"

print("This is Hex (Base16) Value")
for ch in text:
    print(f"{ch} => {ord(ch)} => {hex(ord(ch))}")

hex_encoded = text.encode().hex()
hex_decoded = bytes.fromhex(hex_encoded).decode()
print(f"\nOriginal    : {text}")
print(f"Hex Encoded : {hex_encoded}")
print(f"Hex Decoded : {hex_decoded}")