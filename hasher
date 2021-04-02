import hashlib
import base64
txt = input("text: ")
txt = txt.encode('utf-8')
print("types:\n 01- md4\n 02- md5\n 03- blake2b\n 04- sha1\n 05- sha3_256\n 06- sha3_512\n 07- sha384\n 08- blake2s\n 09- sha256\n 10- sha512\n 11- sha224\n 12- sha3_384\n 13- sha3_224\n 14- Base64\n 15- Base32\n 16- Base16")
x = input("type of hash: ")
def crypt():

    if x == "01":
        print(hashlib.md5(txt).hexdigest())
    elif x == "02":
        print(hashlib.md5(txt).hexdigest())
    elif x == "03":
        print(hashlib.blake2b(txt).hexdigest())
    elif x == "04":
        print(hashlib.sha1(txt).hexdigest())
    elif x == "05":
        print(hashlib.sha3_256(txt).hexdigest())
    elif x == "06":
        print(hashlib.sha3_512(txt).hexdigest())
    elif x == "07":
        print(hashlib.sha384(txt).hexdigest())
    elif x == "08":
        print(hashlib.blake2s(txt).hexdigest())
    elif x == "09":
        print(hashlib.sha256(txt).hexdigest())
    elif x == "10":
        print(hashlib.sha512(txt).hexdigest())
    elif x == "11":
        print(hashlib.sha224(txt).hexdigest())
    elif x == "12":
        print(hashlib.sha3_384(txt).hexdigest())
    elif x == "13":
        print(hashlib.sha3_224(txt).hexdigest())
    elif x == "14":
        message = txt.decode('utf-8')
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        print(base64_message)
    elif x == "15":
        message = txt.decode('utf-8')
        message_bytes = message.encode('ascii')
        base32_bytes = base64.b32encode(message_bytes)
        base32_message = base32_bytes.decode('ascii')
        print(base32_message)
    elif x == "16":
        message = txt.decode('utf-8')
        message_bytes = message.encode('ascii')
        base16_bytes = base64.b16encode(message_bytes)
        base16_message = base16_bytes.decode('ascii')
        print(base16_message)
    else:
        print("Not found")
while to_do == "keep":
    to_do = input("keep && exit: ")
    crypt()
