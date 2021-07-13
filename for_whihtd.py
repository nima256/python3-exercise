# for loop 
# lets write code that we think here is a school and we need.. 
# .. name , last name , age , serial number 
# its enough

# i make variable to save particulars that user enter
# maybe you have question to why i make to variable for each other?
# if you want to know go in my what-i-have-to-do- repository and read for.py 
# i explain it if you cant okay i bring it here

# "when you print your variable that in it you ask user to ..
# .. enter number it only give you last number that user enter it"

# here you are 



fake_names = [] 
names = []

fake_last_names = []
last_names = []

fake_ages = []
ages = []

fake_serial_num = []
serial_nums = []

for x in range(3):
    name = input("next one \nplease enter your name:")
    last_name = input("please enter your last name:")
    age = int(input("please enter your age:"))
    serial_num = int(input("please enter your serial number:"))
    
    fake_names = name
    names.append(fake_names)

    fake_last_names = last_name
    last_names.append(fake_last_names)

    fake_ages = age
    ages.append(fake_ages)

    fake_serial_num = serial_num
    serial_nums.append(fake_serial_num)

print(names)
print(last_names)
print(ages)
print(last_names)

# i hope you enjoy ✋💓