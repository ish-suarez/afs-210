# Source
# https://www.programiz.com/python-programming/methods/built-in/hash

# initializing objects
# Hashing The Number Value Using hash() Method
int_val = 4
hash_num = hash(int_val)
print(f'The integer hash value is: ')
print(f'{hash_num}')
print('')

# Hashing The String Value Using hash() Method
str_val = 'PythonIsBest'
hash_str = hash(str_val.encode())
print(f'The string hash value is: {hash_str}')
print('')

# Hashing The Float Value Using hash() Method
flt_val = 24.56
hash_flt = hash(flt_val)
print(f'The float hash value is: {hash_flt}')




# different Kinds of hashing using 'python' and 'hashlib'
# https://www.pythoncentral.io/hashing-strings-with-python/
# import hashlib

# hash_object = hashlib.sha512(str_val.encode())
# hex_dig = hash_object.hexdigest()
# print(hex_dig)


