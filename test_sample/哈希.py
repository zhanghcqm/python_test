import hashlib
md=hashlib.md5()
md.update('18328042970ZHC'.encode('utf-8'))
print(md.hexdigest())

