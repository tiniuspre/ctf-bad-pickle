# Bad Pickle

As the name suggests this is about pickling (dill)
If you do a simple analysis of the file you will see that it is base64 and inside is a pickled python object.


### Pickled file

The "decoded" from base64.
Here lies several hints that it has to do with python.
Hints:
- dill
- __init__
- __module__
- And gerneally python keywords.
```pickle
���      �
dill._dill��_create_type���(h �
_load_type����type���R��ZNxDV�h�object���R���}�(�
__module__��__main__��__init__�h �_create_function���(h �_create_code���(C  �KK K KKKCR� t        |�      | _        t        |�      | _        || _        y �N��(�encrypt��rUjLC��SQcWV��ynchl�t�(�self�hhht��1/Users/tinius/PycharmProjects/badPickle/source.py�h�ZNxDV.__init__�K0C� ��U�^��
��U�^��
���
�C �))t�R�}��__name__�hshNNt�R�}�}�(�__annotations__�}�(hh�str���R�hh/hh�bytes���R�u�__qualname__�h u��bh%(�encrypt�h(h(C
L$D�KK K KKKB@  �� ddl m} ddlm} dd l}|j
                  ��fd�}|j
                   || �      j                  d�      �      }  ||j
                  �      }|j                  t        |j                  |��      }|j
                  ||j                  | �      z   �      S �(NK �AES����get_random_bytes���h(h"KK K KKKCb�� | �t        | �      �z  z
  t        �t        | �      �z  z
  �      z  z   S �h�len��chr����s���h�<lambda>��encrypt.<locals>.<lambda>�KC0�� �A��c�!�f�r�k�)�S��c�!�f�r�k�1A�-B�B�B� �h"�BS���)t�R��utf8��key��mode��iv���t�(�Cryptodome.Cipher�h8�Cryptodome.Random�h:�base64��
block_size��	b64encode��encode��new��__key__��MODE_CFB�ht�(�raw�h8h:hQ�pad�hL�cipher�t�hhhKC|�� �%�2��	���B�
B�C�
�
�
�3�s�8�?�?�6�2�
3�C�	�#�.�.�	)�B�
�W�W��s�|�|��W�
;�F����B�����!4�4�5�5�h")hE��t�R�}�h&hshNNt�R�}�}�h+}�s��bha(�__key__�C �=kQh��A�0�D��W�Bm{����(�v��Ӟ��len��builtins��len����chr�hk�chr���u0�__key__�hi�len�hm�chr�hpu0�get_username_password�h(h(C�KK K KKKCp� | j                  | j                  �      | j                  | j                  �      d�S �N�username��password������_decrypt�hh��h��hht�ZNxDV.get_username_password�K5C*� � �M�M�$�*�*�5�4�=�=�QU�Q[�Q[�C\�]�]�h"))t�R�}�h&hshtNNt�R�}�}�(h+}�h3h~u��bh{h(h(C"N�KK K KK	KB:  � ddl m} dd l}|j                  |�      }|d |j                   }|j                  | j                  |j                  |�      }| j                  |j                  |j                  ||j                  d  �      �      j                  d�      �      S �(NK h9hIt�(hOh8hQ�	b64decode�hRhUhhW�_unpad��decrypt��decode�t�(h�enc�h8hQhLh[t�hh{�ZNxDV._decrypt�K8C|� �)�����s�#��
��#�.�.�
!��������S�\�\�2�6���{�{�6�+�+�F�N�N�3�s�~�~��;O�,P�Q�X�X�Y_�`�a�a�h"))t�R�}�h&hsh{NNt�R�}�}�(h+}�h3h�u��bh�h(h(C�KK K KKKC&� |d t        |dd  �        S �NJ�������ord���hh@��hh��ZNxDV._unpad�KAC� ���3�q���v�;�,���h"))t�R�}�h&hsh�NNt�R�}�}�(h+}�h3h�u��bh��ord�hk�ord���s0�__doc__�N�
__slotnames__�]�ut�R�hk�setattr���h�h3h��R0)��}�(hC8tfAMf6S8VkUrjgxD5tFg1+jY6OCjhDGTcscGf6B4s5EglJlYDnVVhg==�hC8bZKYYeJXk3Ef0uZxEQbNI8OmdrTm5hR8kLUPSoQRimPJO5pnLbK1Nw==�hhiub.
```

### Analysing the file:
```python
import base64
import dill

with open('output/task.txt', 'r') as f:
    pickle_data = base64.b64decode(f.read())

    obj = dill.loads(pickle_data)

print(dir(obj))

>>> ['SQcWV', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', '_decrypt', '_unpad', 'get_username_password', 'rUjLC', 'ynchl']
```
When looking at the object we see that it has a method called `get_username_password` which is a good hint that this is something worth looking into.



### Solve
```python
import base64
import dill

with open('output/task.txt', 'r') as f:
    pickle_data = base64.b64decode(f.read())

    obj = dill.loads(pickle_data)

print(obj.get_username_password())

>>> {'username': 'CTFkom{pickles_or_d', 'password': 'ill_is_bad!}'}

```