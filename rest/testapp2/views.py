from testapp2.models import *
#reorder an object uisng django admin page. 

def reorder():
    order  = 0
    for item in create_super_book.objects.all():
        order += 1
        item.my_order = order
        item.save()
    print('Order value is stored')

#reorder()

def CheckDataOrder():
    for item in create_super_book.objects.all():
        print(item.title)

#CheckDataOrder()
