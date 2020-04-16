from django.shortcuts import render
from django.db import DatabaseError, transaction, IntegrityError
from .models import Book

def ModelManager():
    BookIns = Book.objects.all()
    print(BookIns)
    # Calling model manager function. 
    Book_Ins = Book.objects.title_count(keyword="maths")
    print(Book_Ins)

# database atomic transactions . 
def CheckAtomicTransaction():
    try:
        with transaction.atomic():
            bookIns = Book.objects.create(
                title ="Science" 
                )
    except IntegrityError:
        print('Integrity error')
    except DatabaseError:
        print('Db error')

#CheckAtomicTransaction()
