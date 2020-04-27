import sys

def rot(text, rot):
    charset = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    #can only encrypt alphabets
    for i in range(0, len(text)):
        crypt = (charset.find(text[i]) + int(rot)) % 26
        cipher += (charset[crypt])
    return cipher

while len(sys.argv)<2:
    print("Usage: python3 rot.py <text> <rot number>")
    break

while len(sys.argv)==2:
    print(f"ROT[13]: {rot(sys.argv[1], 13)}")
    break

while len(sys.argv)>2:
    print(f"ROT[{sys.argv[2]}]: {rot(sys.argv[1], sys.argv[2])}")
    break


