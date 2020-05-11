from django.shortcuts import render

# Create your views here.
# Tips to write a better code in python 
def Check():
    digit_1 = 10_00_000
    print(digit_1)
    a, b, _ = (1, 2, 3)
    print(a)
    print(b)
    lst = [1,2,3]
    print(f"List = {lst}")

def check_2():
    # BAD CODE 
    status = False
    if status:
        print('well')
    else:
        print('unwell')
    # Good code
    result = "well" if status else "unwell"
    print(result)
    # list comprehension. 
    input_list = [1,2,3]
    input_list = [i*10 for i in input_list]
    print(input_list)

#Check()
#check_2()
