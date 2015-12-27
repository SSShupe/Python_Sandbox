import hashlib
secretkey = 'bgvyzdsv'
for i in xrange(10000000):
    addon = str(i)
    secretkey1 = secretkey + str(addon)
    hashed = hashlib.md5(secretkey1).hexdigest()
    if str(hashed).startswith('000000'):
        print secretkey1
        break