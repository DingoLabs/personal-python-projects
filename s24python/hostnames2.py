#wrote with Python 3.9.10

# print any 3 or 4 customer name hostname from clipboard
# removes duplicate hostnames, prints findings
# then copies hostnames back to clipboard


try:
    import pyperclip
except ImportError or ModuleNotFoundError:
    print("you dont have pyperclip installed")
    print("run 'python3 pip install pyperclip'")
    quit()


def is_hostname3(text):
    if len(text) != 11:
        return False
    for i in range(0,2):
        if not text[i].isalpha():
            return False
    if text[3] != '-':
        return False
    for i in range(4,8):
        if not text[i].isalpha():
            return False
    for i in range(9,10):
        if not text[i].isdigit():
            return False
    return True


def is_hostname4(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isalpha():
            return False
    if text[4] != '-':
        return False
    for i in range(5,9):
        if not text[i].isalpha():
            return False
    for i in range(10,11):
        if not text[i].isdigit():
            return False
    return True


text = pyperclip.paste()

hostlist = ''
hostname_count = 0

for i in range(len(text)):
    name = text[i:i+11]
    if is_hostname3(name):
        hostlist = hostlist + (name) + '\n'

for i in range(len(text)):
    name = text[i:i+12]
    if is_hostname4(name):
        hostlist = hostlist + (name)  + '\n'


def unique_list(text_str):
    global hostname_count
    l = text_str.split()
    temp = []
    for x in l:
        if x not in temp:
            temp.append(x)
            hostname_count = hostname_count + 1
    
    return '\n'.join(temp) 


hostlist = unique_list(hostlist)

print("--- found " + str(hostname_count) + " unique hostnames ---")
print(hostlist)

pyperclip.copy(hostlist)










