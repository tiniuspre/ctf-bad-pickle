import base64
import types

import dill
import hashlib

flag = 'CTFkom{pickles_or_dill_is_bad!}'


dill.settings['recurse'] = True
__key__ = hashlib.sha256(b'AhzR*j4Vsh+UPCDXNrxFDfYCxTXeUT=t ').digest()

def encrypt(raw):
    from Cryptodome.Cipher import AES
    from Cryptodome.Random import get_random_bytes
    import base64

    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    raw = base64.b64encode(pad(raw).encode('utf8'))
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key=__key__, mode=AES.MODE_CFB, iv=iv)
    return base64.b64encode(iv + cipher.encrypt(raw))


def remove_file_paths(obj):
    if hasattr(obj, '__code__'):
        code = obj.__code__
        new_code = types.CodeType(
            code.co_argcount,
            code.co_posonlyargcount,
            code.co_kwonlyargcount,
            code.co_nlocals,
            code.co_stacksize,
            code.co_flags,
            code.co_code,
            code.co_consts,
            code.co_names,
            code.co_varnames,
            code.co_filename.replace('/Users/tinius/PycharmProjects/badPickle/source.py', ''),  # Replace the file path with an empty string
            code.co_name,
            code.co_firstlineno,
            code.co_lnotab,
            code.co_freevars,
            code.co_cellvars
        )
        obj.__code__ = new_code
    return obj


class ZNxDV(object):
    def __init__(self, rUjLC: str, SQcWV: str, ynchl: bytes):
        self.rUjLC = encrypt(rUjLC)
        self.SQcWV = encrypt(SQcWV)
        self.ynchl = ynchl

    def get_username_password(self):
        return {'username': self._decrypt(self.rUjLC), 'password': self._decrypt(self.SQcWV)}

    def _decrypt(self, enc):
        from Cryptodome.Cipher import AES
        import base64

        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.ynchl, AES.MODE_CFB, iv)
        return self._unpad(base64.b64decode(cipher.decrypt(enc[AES.block_size:])).decode('utf8'))

    def _unpad(self, s):
        return s[:-ord(s[-1:])]


flag1, flag2 = flag[:len(flag) // 2], flag[len(flag) // 2:]
user = ZNxDV("CTFkom{pickles_or_d", "ill_is_bad!}", ynchl=__key__)
#user = remove_file_paths(user)
print(user.get_username_password())

with open('data.pkl', 'wb') as s:
  dill.dump(user, s)


with open('data.pkl', 'rb') as f:
    data = f.read()
    data_base64 = base64.b64encode(data).decode('utf-8')

with open('output/task.txt', 'w') as f:
    f.write(data_base64)
