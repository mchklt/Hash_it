try :

    import hashlib
    import base64
    import platform

except Exception as e :
    print(e)
    exit()

if platform.system().startswith("Linux", "Termux") :
	red , green , yellow , blue , endc = '\033[91m' , '\033[92m' ,'\033[93m' , '\033[94m' , '\033[0m'
else :
	red = green = yellow = blue = endc = ""
print(green + '''
    1-  MD5
    2-  SHA1
    3-  BLAKE2B
    4-  SHA3_256
    5-  SHA3_512
    6-  BLAKE2S
    7-  SHA256
    8-  SHA512
    9-  SHA3_224
    10- SHA3_384
    11- BASE64
    12- BASE32
    13- BASE16
''' + endc)

text = input("Enter Your Text: ").encode("utf-8")
choice = input("Enter You Choice: ")

vars = {1  : lambda : hashlib.md5(text).hexdigest(),
        2  : lambda : hashlib.sha1(text).hexdigest(), 
        3  : lambda : hashlib.blake2b(text).hexdigest(), 
        4  : lambda : hashlib.sha3_256(text).hexdigest(), 
        5  : lambda : hashlib.sha3_512(text).hexdigest(), 
        6  : lambda : hashlib.blake2s(text).hexdigest(), 
        7  : lambda : hashlib.sha256(text).hexdigest(), 
        8  : lambda : hashlib.sha512(text).hexdigest() ,
        9  : lambda : hashlib.sha3_224(text).hexdigest(), 
        10 : lambda : hashlib.sha3_384(text).hexdigest(), 
        11 : lambda : base64.b64encode(text).decode(), 
        12 : lambda : base64.b32encode(text).decode(), 
        13 : lambda : base64.b16encode(text).decode()}

print("\n" + yellow + "[+] Your Hash is : " + endc + green + vars[int(choice)]())
