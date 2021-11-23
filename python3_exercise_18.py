# here we want to write dictionary , synonym and antonym(if the word has)
# this word is about book that i read it every day in institut
# this code will be update when i learn new lesson and put the important word here  
# book is american english file 2 

# describe for user
print("\nwelcome\n")
print("\nhere you can see dictionary , synonym and antonym of the new word and hard word american english file 2 book\n")
# input to undrestand what is user want 
Input = input("what do you want?  [dic(dictionary) , syn(synonym) , ant(antonym) ] =>")
# error handling
while Input != "dic" and Input != "syn" and Input != "ant":
    print("try again!!")
    Input = input("what do you want?  [dic(dictionary) , syn(synonym) , ant(antonym) ] =>")
# put dictionary in the dictiomary
dic = {
'experiment' : 'a scientific test to find out how something react' 
, 'sociable' : 'when somebody is sociable he/she is friendly and enjoy being with other people' 
, 'get along' : 'if two or more people get along they have a friendly relationship'
, 'sence of humor' : 'someone that always look for funny things'
, 'beard' : "hair that grows around man's chin and cheeks"
, 'literature' : 'books,plays,poems that people think they are important'
, 'compatible' : 'when two people are compatible they can have good relationship'
, 'attendant' : 'someone that her/him job is helping coustomer'
, 'hostel' : 'a place where people can stay and eat cheaply'
, 'atmosphere' : 'the feeling that an event or plave gives you'  
, 'paradise' : 'a place or situation that is pleasant , beautiful'
, 'sunbath' : 'when you laying on the neach and enjoy sun'
, 'flirting' : 'when you are talking to opposite gender'
, 'cruise' : 'a holiday on large ship'
, 'complain' : 'to say you are annoyed'
, 'snack' : 'a small amount of food that is eaten between main meals ot insted of meal'
, 'convention' : 'a large meeting for people who be long to the same profession or organization'
, 'discover' : 'to find out something that you did not know it'
, 'election' : 'when people vote to choose someone for an official position'
, 'announce' : 'to tell people about something'
, 'emotional' : 'having strong feelings and showing them to other people, especially by crying'
, 'aristocrat' : 'someone who in the highest social class'
, 'property' : 'the thing or things that someone owns'
, 'rebel' : 'someone who fight against people in authority'
, 'madly' : 'in very strong way'
, 'impression' : 'a feeling you have about something or someone as first'
, 'chemistry' : 'when two people find attractive with each other'
, 'consider' : 'to think about something befor choose'
, 'dress' : 'decorate clothe'
, 'approximately' : 'more or less than a number'
, 'aim' : 'something you hope to achive it by doing'
, 'separate' : 'away by something'
, 'divorce' : 'when two people married and they decided to break up'
, 'infidelity' : 'when two people was married and one of them has relationship with another person'
, 'sight seeing' : 'a beautiful landscape or beautiful view'
, 'punctual' : 'when you are care about your time you are punctual'
, 'introduce' : 'when you tell somebody another person and say his/her name for first time'
, 'murder' : 'the crime of deliberately killing someone'
, 'fault' : 'if you do something bad and it was your fault you have to balmed for it'
, 'irritate' : 'when you do something that someone annoyed'
, 'jealous' : 'when someone is jealous she/he does not want to see somebody is happy'
, 'demonstration' : 'when something bad happend people go in the street it is demonstration'
, 'politic' : 'the activities associated with the governance of a country'
, 'revelotion' : 'social order in favor of a new system'
, 'notice' : ' if you notice something actuly you can feel it, hear it and see it'
, 'anniversary' : 'when you have relationship the first day that you see your partner that day is anniversary'
, 'injury' : 'when your part of body damage called it injury'
, 'intensive care' : 'a part of hospital that when somebody is very ill take him/her to there'
, 'license plates' : 'a number for your car that is infront of it and behind it'
, 'nightmare' : 'a very frightening dream'
, 'security' : 'a person or thing that keep or look after something'
, 'delay' : 'when something does not happen and you have to wait for it'
, 'faciliti' : 'a special part of a piece of equipment'
, 'indoor' : 'inside building'
, 'dozen' : 'a group ir set if twelve'
, 'treatment' : 'care about your skin'
, 'entetain' : 'provide someone with enjoyment things'
, 'medical' : 'doctors equipment'
, 'laundry' : ' a place or business where clothes etc are washed and ironed'
, 'schedule' : 'program'
}

# put synonym in dictionry
syn = {
'experiment' : 'TEST' , 'sociable' : 'FRIENDLY' , 'get along' : 'BE FRIENDLY'
, 'sence of humor' : 'FUNNY' , 'beard' : 'FACIAL HAIR' , 'literature' : 'LETTER' 
, 'compatible' : 'well suited' , 'attendant' : 'WAITER' , 'hostel' : 'CHEAP HOTEL'
, 'atmosphere' : 'BARLEY' , 'paradise' : 'HEAVEN' , 'sunbath' : 'BASK'
, 'flirting' : 'CHAT UP' , 'cruise' : 'VOYAGE' , 'complain' : 'REPINE'
, 'convention' : 'BIG MEETING' , 'discover' : 'REALAZED' , 'announce' : 'MAKE PUBLIC'
, 'emotional' : 'STRONG FEELING' , 'aristocrat' : 'TOP CLASS' , 'property' : 'POSSESSIONS'
, 'rebel' : 'RIOTER' , 'madly' : 'INSANELY' , 'impression' : 'FIRST FEELING'
, 'chemistry' : 'COMMON', 'consider' : 'THINKING ABOUT' , 'dress' : 'TAILOR'
, 'approximately' : 'ROUGHLY' , 'aim' : 'OBJECT' , 'separate' : 'APART'
, 'infidelity' : 'UNFAITHFULNESS' , 'sight seeing' : 'BEAUTIFUL VIEW'
, 'murder' : 'KILLING' , 'irritate' : 'ANNOY' , 'jealous' : 'ENVIOUS'
, 'notice' : 'CARE' , 'injury' : 'HURT' , 'nightmare' : 'MARE'
, 'security' : 'SAFETLY' , 'delay' : 'LATE' , 'faciliti' : 'EQUIPMENT'
, 'indoor' : 'INTERNAL'
}
# put antonym in dictionary
ant = {
'sociable' : 'UNSOCIABLE' , 'get along' : 'ARGUE' , 'sence of humor' : 'SERIOUS'
, 'compatible' : 'UNSUITABLE' , 'paradise' : 'HELL' , 'announce' : 'CONCEAL'
, 'emotional' : 'low feeling' , 'aristocrat' : 'low class' , 'approximately' : 'precisely'
, 'separate' : 'NEAR' , 'divorce' : 'MARRIED' , 'infidelity' : 'FIDELITY'
, 'jealous' : 'UNENVIOUS' , 'security' : 'DANGER' , 'delay' : 'EARLY'
}

# if user type dic
if Input == "dic":
    # ask him/her what word does she/he want
    dic_input = input("\n\nwhat word do want?")
    # loop for rotate in dictionary
    for x in dic:
        # if input same with the dictionary
        if dic_input == x:
            # print it dictionary
            print(f"\nthe dictionary of {dic_input} is {dic[x]}")
        # elif input is not in the dictionary
        elif dic_input not in dic:
            # reson for why it is not in dictionary
            print("sorry we do not have dictionary of this word or there is not dictionary for this word or this is simple word (:\n \ntry again!!\n")
            # error handling
            while dic_input not in dic:
                # ask him/her what word does she/he want
                dic_input = input("\n\nwhat word do want?")
                # loop for rotate in dictionary
                for x in dic:
                    # if input same with the dictionary
                    if dic_input == x:
                        # print it dictionary
                        print(f"\nthe dictionary of {dic_input} is {dic[x]}")
                    # elif input is not in the dictionary
                    elif dic_input not in dic:
                        # reson for why it is not in dictionary
                        print("sorry we do not have dictionary of this word or there is not dictionary for this word or this is simple word (:\n \ntry again!!\n")
                        break
            break
        
# elif user type syn
elif Input == "syn":
    # ask him/her what word does she/he want
    syn_input = input("what word do you want?=>")
    # loop for rotate in dictionary
    for i in syn:
        # if input same with the dictionary
        if syn_input == i:
            # print it dictionary
            print(f"the synonym of {syn_input} is {syn[i]}")
        # elif input is not in the dictionary
        elif syn_input not in dic:
            # reson for why it is not in dictionary
            print("sorry we do not have synonym of this word or there is not synonym for this word or this is simple word (:\n \ntry again!!\n")
            # error handling
            while syn_input not in dic:
                # ask him/her what word does she/he want
                syn_input = input("\n\nwhat word do want?")
                # loop for rotate in dictionary
                for x in dic:
                    # if input same with the dictionary
                    if syn_input == x:
                        # print it dictionary
                        print(f"\nthe dictionary of {syn_input} is {dic[x]}")
                    # elif input is not in the dictionary
                    elif syn_input not in dic:
                        # reson for why it is not in dictionary
                        print("sorry we do not have synonym of this word or there is not synonym for this word or this is simple word (:\n \ntry again!!\n")
                        break
            break
        
# elif user type ant
elif Input == "ant":
    # ask him/her what word does she/he want
    ant_input = input("what word do you want?=>")
    # loop for rotate in dictionary
    for z in ant:
        # if input same with the dictionary
        if ant_input == z:
            # print it dictionary
            print(f"the antonym of {ant_input} is {ant[z]}")
                # elif input is not in the dictionary
        elif ant_input not in dic:
            # reson for why it is not in dictionary
            print("sorry we do not have antonym of this word or there is not antonym for this word or this is simple word (:\n \ntry again!!\n")
            # error handling
            while ant_input not in dic:
                # ask him/her what word does she/he want
                ant_input = input("\n\nwhat word do want?")
                # loop for rotate in dictionary
                for x in dic:
                    # if input same with the dictionary
                    if ant_input == x:
                        # print it dictionary
                        print(f"\nthe dictionary of {ant_input} is {dic[x]}")
                    # elif input is not in the dictionary
                    elif ant_input not in dic:
                        # reson for why it is not in dictionary
                        print("sorry we do not have antonym of this word or there is not antonym for this word or this is simple word (:\n \ntry again!!\n")
                        break
            break
        

# thanks for reading (:
