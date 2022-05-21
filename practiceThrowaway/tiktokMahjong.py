import random

items = ['1','1','1','1','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5']
new_order = []
random.shuffle(items)
# next order []
# print order not items
print("welcome to tiktok mahjong")
print('  1   2   3   4   5  ')
print('  =   =   =   =   =  ')
print( '| ' + items[0] + ' | ' + items[1] + ' | ' + items[2] + ' | ' + items[3] + ' | ' + items[4] + ' | ')
print('  =   =   =   =   =  ')
print( '| ' + items[5] + ' | ' + items[6] + ' | ' + items[7] + ' | ' + items[8] + ' | ' + items[9] + ' | ')
print('  =   =   =   =   =  ')
print( '| ' + items[10] + ' | ' + items[11] + ' | ' + items[12] + ' | ' + items[13] + ' | ' + items[14] + ' | ')
print('  =   =   =   =   =  ')
print( '| ' + items[15] + ' | ' + items[16] + ' | ' + items[17] + ' | ' + items[18] + ' | ' + items[19] + ' | ')
print('  =   =   =   =   =  ')
