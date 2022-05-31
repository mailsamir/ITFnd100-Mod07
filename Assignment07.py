# ------------------------------------------------- #
# Title: Exception handling and pickling
# Description: A simple example of Exception handling and pickling
# ChangeLog: (Who, When, What)
# Samir Abad,05.29.2022,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
# Declare variables and constants
fName = 'newfile.dat'
lstItemsPrice = []

def write_to_file(filename, list_of_items):
    file=open(filename,"wb")
    pickle.dump(list_of_items,file)
    file.close()


try:
    item = str(input("Enter name of item:"))
    if not item.isalpha():
        raise Exception('Do not use numbers for the item name. No special characters(Space, #, $, etc.) are allowed as input!')
except Exception as e:
    print('There was a non-specific error!')
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
    exit()

else:
    try:
        price=input("Enter item price in $:")
        if not price.isnumeric():
            raise Exception('Use integer values to input the price. No special characters(Space, #, $, etc.) are allowed as input!')
    except Exception as e:
        print('There was a non-specific error!')
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
        exit()

lstItemsPrice=[item,price]

write_to_file(fName,lstItemsPrice)
print("Success")