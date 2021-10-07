#hello
# here computer guss you a number

print('Please think of a number between 0 and 1000!')
low = 0
high = 1000
for x in range(10):
    num = (high+low)/2
    print(f'Is your secret number {num}')
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans=='h':
        high = num
    elif ans=='l':
        low = num
    elif ans=='c':
        print("Game over. Your secret number was:",num)
        break
    else:
        print("Sorry, I did not understand your input")
