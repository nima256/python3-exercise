# enter 10 number to sum it for you

fake_num0 = []
num0 = []

for x in range(10):
    num = int(input("please enter 10 number:"))
    fake_num0 = num
    num0.append(fake_num0)

print(sum(num0)) 