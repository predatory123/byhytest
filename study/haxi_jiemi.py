from cryptography.fernet import Fernet

# 产生密钥， 密钥是加密解密必须的
key = Fernet.generate_key()
f = Fernet(key)


src = "白月黑羽网站学习Python真好啊"
# 源信息，必须是字节串对象
# 字符串对象需要encode一下
srcBytes = src.encode()

# 生成加密字节串
token = f.encrypt(srcBytes)
print(token)

# 解密，返回值是字节串对象
sb = f.decrypt(token)
print(sb.decode())