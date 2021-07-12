# this command print for you even number in list
list = [102 , 53 , 24 , 45 , 47 , 98 , 100]
for x in list:
    if x %2 == 0:
        print(x)
# output ==> 102 , 24 , 98 , 100

# this code give you all even number between number that you want
start = int(input("please enter start of range : "))
end = int(input("please enter end of range :"))
for x in range(start , end + 1 ):
    if x % 2 == 0:
        print(x)