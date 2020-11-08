import base64
import sys

from Crypto.Cipher import AES

# 补足字符串长度为32的倍数
def add_to_32(s):
    while len(s) % 32 != 0:
        s += '\0'
    return s

# 补足字符串长度为32的倍数
def add_to_32_b(s):
    while len(s) % 32 != 0:
        s += b'\0'
    return s

# 补足字符串长度为32的倍数
def add_to_32_ret_bytes(s):
    s = str.encode(s)
    while len(s) % 32 != 0:
        s += b'\0'
    return s
    # return str.encode(s, encoding='utf8')  # 返回bytes

def main():
    # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
    key = input("pwd:")
    key_32 = add_to_32(key)
    aes = AES.new(str.encode(key_32), AES.MODE_ECB)  # 初始化加密器，本例采用ECB加密模式

    result_path = "jiamihou.txt"

    shuruCanshuShuliang = len(sys.argv)

    if shuruCanshuShuliang > 1:
        key_QueRen = input("re input pwd:")
        if key != key_QueRen:
            print("密码错误")
            return -1
        print("encode")
        path = sys.argv[1]

        if shuruCanshuShuliang > 2:
            result_path = sys.argv[2]

        with open(path, 'rb') as file:
            content = file.read()
            if type(content) is str:
                content = add_to_32_ret_bytes(content)
            elif type(content) is bytes:
                content = add_to_32_b(content)
            encrypted_text = str(base64.encodebytes(aes.encrypt(content)),
                                 encoding='utf8').replace('\n', '')  # 加密

            f = open(result_path, 'w')
            f.write(encrypted_text)
            print('加密值：', encrypted_text)

    else:
        print("decode")
        with open(result_path) as file:
            content = file.read()

            decrypted_text = str(
                aes.decrypt(base64.decodebytes(bytes(content, encoding='utf8'))).rstrip(b'\0').decode(
                    "utf8"))  # 解密
            print('解密值：\n', decrypted_text)

if __name__ == '__main__':
    main()
