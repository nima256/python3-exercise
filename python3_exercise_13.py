# hello 
# here we want to write a script to when we take a number it will give us a binary number for us

# firs we give an input 
Input = int(input("enter a number..>"))
# after that we creat a list to save the binary number in it
binary = []
# then a while that when the Input will 0 it will break
while Input !=0:
    # a variable to give left over of the input
    left_over = Input%2
    print(left_over)
    # add it in the list beacause we want it
    binary.append(left_over)
    # and a out of place of the input that we want to division the out of place of the input too
    Input = Input//2
# we reverse it beacause when we reverse it , it will be right
binary.reverse()
# finall print it
print(binary)