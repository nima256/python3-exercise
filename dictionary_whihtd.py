# here i want to give all the dictionary of the user 
you = {'your name' : '' ,  'your last name' : ''  ,  'your age' : '' , 'where do you live' : '' }

# now i write print and i see that all the particulars are empty
print(you)

# here i want to give user particulars
your_name = input("please enter your name...>")
your_last_name = input("please enter your last name....>")
your_age = int(input("please enter your age.......>"))
where_do_you_live = input("please enter place that you live.....>")

# now i want to placement the particulars
you['your name'] = your_name
you['your last name'] = your_last_name
you['your age'] = your_age
you['where do you live'] = where_do_you_live
#here the particulars are placement and it is not empty

for x in you:
    print(x)
    print(you[x])