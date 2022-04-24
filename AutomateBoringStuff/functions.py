def function1():
    print('ahhhh')
    print('ahhhhhhhh')
print('this is outside the function')
function1()

def function2(x):
    return 2*x
a = function2(3)
print(function2(6))

def function3(x,y):
    return x+y
print(function3(5,6))

def function5(some_arg):
    print(some_arg)
    print('weeee')
function5('lil piggy says...')

def bmi_calc(name, height, weight):
    bmi = weight / (height ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + "is not overweight"
    else:
        return name + "is overweight"

name1 = "phil"
height1 = 10
weight1 = 200

name2 = "angela"
height2 = 9
weight2 = 180

result1 = bmi_calc(name1, height1, weight1)
print(result1)
bmi_calc(name2, height2, weight2)



