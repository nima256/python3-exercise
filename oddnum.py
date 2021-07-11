# this command print for you odd number in list
list = [25 , 64 , 79 , 87 , 125 , 100]
for x in list:
    if x %2 == 1:
        print(x)
# output ==> 25 , 79 , , 87 , 125

# this code give you all even number between number that you want
start = int(input("please enter start of range : "))
end = int(input("please enter end of range :"))
for x in range(start , end + 1 ):
    if x % 2 == 1:
        print(x)