try:
    import pyperclip
except ImportError or ModuleNotFoundError:
    print("you dont have pyperclip installed")
    print("run 'python3 pip install pyperclip'")
    quit()

    
#wrote with Python 3.9.10

# print any 3 or 4 customer name hostname from clipboard
# prints findings
# then copies hostnames back to clipboard



def is_hostname3(text):
    if len(text) != 11:
        return False
    for i in range(0,2):
        if not text[i].isalpha():
            return False
    if text[3] != '-':
        return False
    for i in range(4,10):
        if not text[i].isalnum():
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
    for i in range(5,11):
        if not text[i].isalnum():
            return False
    return True


text = pyperclip.paste()

hostlist = []

for i in range(len(text)):
    name = text[i:i+12]
    if is_hostname3(name):
        hostlist.append(name)
    if is_hostname4(name):
        hostlist.append(name)

print("--- found the following hostnames ---")
for host in hostlist:
    print(host)

# convert list to string becasue pypclip cant copy list to clipboard
hostname_string = '\n'.join(hostlist)

pyperclip.copy(hostname_string)





