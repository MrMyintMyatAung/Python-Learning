
with open("dat_secret1", "rb") as f:
    dat_secret1 = f.read()

text = ""
for b in dat_secret1:
    text += chr(((b >> 4) | ((b << 4) & 0xf0)) ^ 0x41)

print(text)