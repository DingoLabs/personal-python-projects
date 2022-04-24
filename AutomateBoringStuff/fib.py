from timeit import default_timer as timer


# a b c
#   a b c
#     a b c
# 0 1 1 2 3 5 8 13P


def fib(num):
    start = timer()
    a=0
    b=1
    #print(a)
    for i in range(1,num):    
        #print(b)
        c = a + b
        a = b
        b = c
    end = timer()
    return(end - start)
#fib(1000)



def fib2(num):
    start = timer()
    a=0
    b=1
    #print(a)
    for i in range(1,num):    
        #print(b)               
        a, b = b, a + b
    end = timer()
    #print(end - start)
    return(end - start)
#fib2(1000)   

print(fib(100_000))
print(fib2(100_000))

def test(num1,num2):
    a=1
    b=2
    return a + b


print(str(test(1,2)))