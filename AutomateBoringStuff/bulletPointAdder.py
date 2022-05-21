#adds bulletpoints from clip to clipboard

import pyperclip

text = pyperclip.paste()

lines = text.split(' ')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)

# turns
# pizza burgers fries pop
# into
# * pizza
# * burgers
# * fries
# * pop