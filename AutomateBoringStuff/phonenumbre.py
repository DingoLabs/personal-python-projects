# is this a phone number

def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(5,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False    
    return True

print('is 333-333-3333 a phone number?')
print(is_phone_number('333-333-3333'))
print('is 12a-aaa-aaaa a phone number?')
print(is_phone_number('aaa-aaa-aaaaaa'))