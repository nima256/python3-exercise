# here we enter binary number
# tip: you have to write your binary number from left to right
eights_binary_bit = int(input("enter your eighth binary bit (1/0)=>"))
seventh_binary_bit = int(input("enter your seventh binary bit (1/0)=>"))
sixth_binary_bit = int(input("enter your sixth binary bit (1/0)=>"))
fifth_binary_bit = int(input("enter your fifth binary bit (1/0)=>"))
forth_binary_bit = int(input("enter your forth binary bit (1/0)=>"))
third_binary_bit = int(input("enter your third binary bit (1/0)=>"))
second_binary_bit = int(input("enter your second binary bit (1/0)=>"))
first_binary_bit = int(input("enter your first binary bit (1/0)=>"))

# here we creat list to at the final we can put the number and after that sum it
binary = []
# zeros list is for zero number that it does not important we just creat it to put zero in it
zeros = []
# the eight place in the binary number is 128 in the decimal number so if the eights number be 1 we save 128 in list
if eights_binary_bit == 1:
    binary.append(128)
# it is just for save the zero
elif eights_binary_bit == 0:
    zeros.append(0)
# error handling
else:
    print("you enter incorrect number")

# the seventh place in the binary number is 64 in the decimal number so if the seventh number be 1 we save 64 in list
if seventh_binary_bit == 1:
    binary.append(64)
# it is just for save the zero
elif seventh_binary_bit == 0:
    zeros.append(0)
# error handling
else:
    print("you enter incorrect number")
# the sixth place in the binary number is 32 in the decimal number so if the sixth number be 1 we save 32 in list
if sixth_binary_bit == 1:
    binary.append(32)
# it is just for save the zero
elif sixth_binary_bit == 0:
    zeros.append(0)
# error handling
else:
    print("you enter incorrect number")
# the fifth place in the binary number is 16 in the decimal number so if the fifth number be 1 we save 16 in list
if fifth_binary_bit == 1:
    binary.append(16)
# it is just for save the zero
elif fifth_binary_bit == 0:
    binary.append(0)
# error handling
else:
    print("you enter incorrect number")
# the forth place in the binary number is 8 in the decimal number so if the forth number be 1 we save 8 in list
if forth_binary_bit == 1:
    binary.append(8)
# it is just for save the zero
elif forth_binary_bit == 0:
    zeros.append(0)
# error handling
else:
    print("you enter incorrect number")
# the third place in the binary number is 4 in the decimal number so if the third number be 1 we save 4 in list
if third_binary_bit == 1:
    binary.append(4)
# it is just for save the zero
elif third_binary_bit == 1:
    zeros.append(0)
# error handling
else:
    print("you enter incorrect number")
# the second place in the binary number is 2 in the decimal number so if the second number be 1 we save 2 in list
if second_binary_bit == 1:
    binary.append(2)
# it is just for save the zero
elif second_binary_bit == 0:
    zeros.append(0)
# error handling
else:
    print("you enter incorrect number")
# the first place in the binary number is 1 in the decimal number so if the first number be 1 we save 1 in list
if first_binary_bit == 1:
    binary.append(1)
# it si just for save the zero
elif first_binary_bit == 0:
    zeros.append(0)
else:
    print("you enter incorrect number")
# it's number that is saved
print(binary)
# this is you decimal number
print(sum(binary))