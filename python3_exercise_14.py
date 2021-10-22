"""
hello
in this code we want to write class of the laptops
the laptops have three same option and two special option
we have three of different mark of the laptops 
1 : lenovo
2 : asus
3 : microsoft
"""

# first lenovo laptop
class levono:
    # a variable to understand how many people buy of this mark of laptop
    number_of_buyers = 0
    # user most to enter a input
    def __init__(self , name , last_name , age , laptop):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.laptop = laptop
        levono.number_of_buyers += 1
        print(f"hello mr/ms thanks for choose us \nyour name is {name} and your last name is {last_name} \n your laptop is {laptop} you choose strong laptop")
    # color method that choose a laptop color
    def color_of_laptop(self):
        laptop_color = int(input("what color do you want to your laptop be?  1 = white , 2 = black , 3 = blue , 4 = pink , 5 = yellow =>"))
        if laptop_color == 1:
            self.laptop_color = "white"
        elif laptop_color == 2:
            self.laptop_color = "black"
        elif laptop_color == 3:
            self.laptop_color = "blue"
        elif laptop_color == 4:
            self.laptop_color = "pink"
        elif laptop_color == 5:
            self.laptop_color = "yellow"
        else:
            print("you say incorrect number try again ):")     
        # error handling
        while laptop_color!=1 and laptop_color!=2 and laptop_color!=3 and laptop_color!=4 and laptop_color!=5:
            laptop_color = int(input("what color do you want to your laptop be?  1 = white , 2 = black , 3 = blue , 4 = pink , 5 = yellow =>"))
            if laptop_color == 1:
                self.laptop_color = "white"
            elif laptop_color == 2:
                self.laptop_color = "black"
            elif laptop_color == 3:
                self.laptop_color = "blue"
            elif laptop_color == 4:
                self.laptop_color = "pink"
            elif laptop_color == 5:
                self.laptop_color = "yellow"
            else:
                print("you say incorrect number try again ):")
    # color of mouse method that choose a color of the mouse 
    def color_of_mouse(self):
        color_of_mouse = int(input("what color do you want to your mouse be? 1 = white , 2 = black , 3 = blue , 4 = pink , 5 = yellow =>"))
        if color_of_mouse == 1:
            self.color_of_mouse = "white"
        elif color_of_mouse == 2:
            self.color_of_mouse = "black"
        elif color_of_mouse == 3:
            self.color_of_mouse = "blue"
        elif color_of_mouse == 4:
            self.color_of_mouse = "pink"
        elif color_of_mouse == 5:
            self.color_of_mouse = "yellow"
        else:
            print("you say incorrect number try again ):")
        # error handling
        while color_of_mouse!=1 and color_of_mouse!=2 and color_of_mouse!=3 and color_of_mouse!=4 and color_of_mouse!=5:
            color_of_mouse = int(input("what color do you want to your mouse be? 1 = white , 2 = black , 3 = blue , 4 = pink , 5 = yellow =>"))
            if color_of_mouse == 1:
                self.color_of_mouse = "white"
            elif color_of_mouse == 2:
                self.color_of_mouse = "black"
            elif color_of_mouse == 3:
                self.color_of_mouse = "blue"
            elif color_of_mouse == 4:
                self.color_of_mouse = "pink"
            elif color_of_mouse == 5:
                self.color_of_mouse = "yellow"
            else:
                print("you say incorrect number try again ):")
    # operating system method that user change her/him operating system between ubuntu and windows
    def operating_system(self):
        operating_system = int(input("what operating system do you want to install on your laptop?   1 = windows  2 = linux 'i suggest you choose this(:' =>"))
        if operating_system == 2:    
            # linux has a lot of distribution software we enter a 3 most popular of it to user choose it 
            linux = int(input("what linux distribution software do you want?  1 = ubuntu , 2 = fedora , 3 = debian =>"))        
            if linux == 1:
                self.operating_system = "ubuntu"
            elif linux == 2:
                self.operating_system = "fedora"
            elif linux == 3:
                self.operating_system = "debian"
            else:
                print("you enter incorrect number ):")
            # error handling
            while linux !=1 and linux!=2 and linux!=3:
                linux = int(input("what linux distribution software do you want?  1 = ubuntu , 2 = fedora , 3 = debian =>"))        
                if linux == 1:
                    self.operating_system = "ubuntu"
                elif linux == 2:
                    self.operating_system = "fedora"
                elif linux == 3:
                    self.operating_system = "debian"
                else:
                    print("you enter incorrect number ):")    
        elif operating_system == 1:
            # windows also have a lot of distribution software too so i use three last of the windows vertion to user choose it
            windows = int(input("what windows distribution software do you want?  1 = windows 11 , 2 = windows 10 , 3 = windows 8.1 =>"))
            if windows == 1:
                self.operating_system = "windows 11"
            elif windows == 2:
                self.operating_system = "windows 10"
            elif windows == 3:
                self.operating_system = "windows 8.1"
            else:
                print("you enter incorrect number ):")
            # error handling
            while windows !=1 and windows!=2 and windows!=3:
                windows = int(input("what windows distribution software do you want?  1 = windows 11 , 2 = windows 10 , 3 = windows 8.1 =>"))
                if windows == 1:
                    self.operating_system = "windows 11"
                elif windows == 2:
                    self.operating_system = "windows 10"
                elif windows == 3:
                    self.operating_system = "windows 8.1"
                else:
                    print("you enter incorrect number ):")     
        else:
            print("you enter incorrect number ):")           
        # error handling
        while operating_system !=1 and operating_system !=2:
            operating_system = int(input("what operating system do you want to install on your laptop?   1 = windows  2 = linux(i suggest you choose this(:  )  =>"))
            if operating_system == 1:    
                linux = int(input("what linux distribution software do you want?  1 = ubuntu , 2 = fedora , 3 = debian =>"))        
                if linux == 1:
                    self.operating_system = "ubuntu"
                elif linux == 2:
                    self.operating_system = "fedora"
                elif linux == 3:
                    self.operating_system = "debian"
                else:
                    print("you enter incorrect number ):")
                while linux !=1 and linux!=2 and linux!=3:
                    linux = int(input("what linux distribution software do you want?  1 = ubuntu , 2 = fedora , 3 = debian =>"))        
                    if linux == 1:
                        self.operating_system = "ubuntu"
                    elif linux == 2:
                        self.operating_system = "fedora"
                    elif linux == 3:
                        self.operating_system = "debian"
                    else:
                        print("you enter incorrect number ):")    
            elif operating_system == 2:
                windows = int(input("what windows distribution software do you want?  1 = windows 11 , 2 = windows 10 , 3 = windows 8.1 =>"))
                if windows == 1:
                    self.operating_system = "windows 11"
                elif windows == 2:
                    self.operating_system = "windows 10"
                elif windows == 3:
                    self.operating_system = "windows 8.1"
                else:
                    print("you enter incorrect number ):")
                while windows !=1 and windows!=2 and windows!=3:
                    windows = int(input("what windows distribution software do you want?  1 = windows 11 , 2 = windows 10 , 3 = windows 8.1 =>"))
                    if windows == 1:
                        self.operating_system = "windows 11"
                    elif windows == 2:
                        self.operating_system = "windows 10"
                    elif windows == 3:
                        self.operating_system = "windows 8.1"
                    else:
                        print("you enter incorrect number ):")     
            else:
                print("you enter incorrect number ):")         
    # we enter in special option for lenovo
    # first option :fingerprint scanner method that ask a question from user that does he/she want this option or not
    def fingerprint_scanner(self):
        fingerprint_scanner = int(input("your laptop have two special option. first : fingerprint scanner do you want it in your laptop?  1 = yes , 2 = no=>"))
        if fingerprint_scanner == 1:
            self.fingerprint_scanner = "yes"
        elif fingerprint_scanner == 2:
            self.fingerprint_scanner = "no"
        else:
            print("you enter incorrect number ):")
        # error handling
        while fingerprint_scanner != 1 and fingerprint_scanner != 2:
            fingerprint_scanner = int(input("your laptop have two special option. first : fingerprint scanner do you want it in your laptop?  1 = yes , 2 = no=>"))
            if fingerprint_scanner == 1:
                self.fingerprint_scanner = "yes"
            elif fingerprint_scanner == 2:
                self.fingerprint_scanner = "no"
            else:
                print("you enter incorrect number ):")            
    # second option : cool pad we give a free cool pad for buyer and ask user does he/she want it or not
    def cool_pad(self):
        cool_pad = int(input("your laptop have two special option. second : cool pad we give you a perfect cool pad to your hardware do not hurt do you want to add this option for your laptop?  1 = yes , 2 = no =>"))
        if cool_pad == 1:
            self.cool_pad = "yes"
        elif cool_pad == 2:
            self.cool_pad = "no"
        else:
            print("you enter incorrect number ):")
        # error handling
        while cool_pad != 1:
            cool_pad = int(input("your laptop have two special option. second : cool pad we give you a perfect cool pad to your hardware do not hurt do you want to add this option for your laptop?  1 = yes , 2 = no =>"))
            if cool_pad == 1:
                self.cool_pad = "yes"
            elif cool_pad == 2:
                self.cool_pad = "no"
            else:
                print("you enter incorrect number ):")


# second asus laptop
class asus:
    

    number_of_buyers = 0
    # user most to enter a input
    def __init__(self , name , last_name , age , laptop):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.laptop = laptop
        levono.number_of_buyers += 1
        print(f"hello mr/ms thanks for choose us \nyour name is {name} and your last name is {last_name} \n your laptop is {laptop} you choose popular laptop")
    # color method that choose a laptop color
    def color_of_laptop(self):
        laptop_color = int(input("what color do you want to your laptop be?  1 = white , 2 = black , 3 = blue , 4 = pink , 5 = yellow =>"))
        if laptop_color == 1:
            self.laptop_color = "white"
        elif laptop_color == 2:
            self.laptop_color = "black"
        elif laptop_color == 3:
            self.laptop_color = "blue"
        elif laptop_color == 4:
            self.laptop_color = "pink"
        elif laptop_color == 5:
            self.laptop_color = "yellow"
        else:
            print("you say incorrect number try again ):")     
        # error handling
        while laptop_color!=1 and laptop_color!=2 and laptop_color!=3 and laptop_color!=4 and laptop_color!=5:
            laptop_color = int(input("what color do you want to your laptop be?  1 = white , 2 = black , 3 = blue , 4 = pink , 5 = yellow =>"))
            if laptop_color == 1:
                self.laptop_color = "white"
            elif laptop_color == 2:
                self.laptop_color = "black"
            elif laptop_color == 3:
                self.laptop_color = "blue"
            elif laptop_color == 4:
                self.laptop_color = "pink"
            elif laptop_color == 5:
                self.laptop_color = "yellow"
            else:
                print("you say incorrect number try again ):")
    # color of mouse method that choose a color of the mouse 
    def color_of_mouse(self):
        color_of_mouse = int(input("what color do you want to your mouse be? 1 = white , 2 = black , 3 = blue , 4 = pink , 5 = yellow =>"))
        if color_of_mouse == 1:
            self.color_of_mouse = "white"
        elif color_of_mouse == 2:
            self.color_of_mouse = "black"
        elif color_of_mouse == 3:
            self.color_of_mouse = "blue"
        elif color_of_mouse == 4:
            self.color_of_mouse = "pink"
        elif color_of_mouse == 5:
            self.color_of_mouse = "yellow"
        else:
            print("you say incorrect number try again ):")
        # error handling
        while color_of_mouse!=1 and color_of_mouse!=2 and color_of_mouse!=3 and color_of_mouse!=4 and color_of_mouse!=5:
            color_of_mouse = int(input("what color do you want to your mouse be? 1 = white , 2 = black , 3 = blue , 4 = pink , 5 = yellow =>"))
            if color_of_mouse == 1:
                self.color_of_mouse = "white"
            elif color_of_mouse == 2:
                self.color_of_mouse = "black"
            elif color_of_mouse == 3:
                self.color_of_mouse = "blue"
            elif color_of_mouse == 4:
                self.color_of_mouse = "pink"
            elif color_of_mouse == 5:
                self.color_of_mouse = "yellow"
            else:
                print("you say incorrect number try again ):")
    # operating system method that user change her/him operating system between ubuntu and windows
    def operating_system(self):
        operating_system = int(input("what operating system do you want to install on your laptop?   1 = windows  2 = linux 'i suggest you choose this(:' =>"))
        if operating_system == 2:    
            # linux has a lot of distribution software we enter a 3 most popular of it to user choose it 
            linux = int(input("what linux distribution software do you want?  1 = ubuntu , 2 = fedora , 3 = debian =>"))        
            if linux == 1:
                self.operating_system = "ubuntu"
            elif linux == 2:
                self.operating_system = "fedora"
            elif linux == 3:
                self.operating_system = "debian"
            else:
                print("you enter incorrect number ):")
            # error handling
            while linux !=1 and linux!=2 and linux!=3:
                linux = int(input("what linux distribution software do you want?  1 = ubuntu , 2 = fedora , 3 = debian =>"))        
                if linux == 1:
                    self.operating_system = "ubuntu"
                elif linux == 2:
                    self.operating_system = "fedora"
                elif linux == 3:
                    self.operating_system = "debian"
                else:
                    print("you enter incorrect number ):")    
        elif operating_system == 1:
            # windows also have a lot of distribution software too so i use three last of the windows vertion to user choose it
            windows = int(input("what windows distribution software do you want?  1 = windows 11 , 2 = windows 10 , 3 = windows 8.1 =>"))
            if windows == 1:
                self.operating_system = "windows 11"
            elif windows == 2:
                self.operating_system = "windows 10"
            elif windows == 3:
                self.operating_system = "windows 8.1"
            else:
                print("you enter incorrect number ):")
            # error handling
            while windows !=1 and windows!=2 and windows!=3:
                windows = int(input("what windows distribution software do you want?  1 = windows 11 , 2 = windows 10 , 3 = windows 8.1 =>"))
                if windows == 1:
                    self.operating_system = "windows 11"
                elif windows == 2:
                    self.operating_system = "windows 10"
                elif windows == 3:
                    self.operating_system = "windows 8.1"
                else:
                    print("you enter incorrect number ):")     
        else:
            print("you enter incorrect number ):")           
        # error handling
        while operating_system !=1 and operating_system !=2:
            operating_system = int(input("what operating system do you want to install on your laptop?   1 = windows  2 = linux 'i suggest you choose this(:'  =>"))
            if operating_system == 1:    
                linux = int(input("what linux distribution software do you want?  1 = ubuntu , 2 = fedora , 3 = debian =>"))        
                if linux == 1:
                    self.operating_system = "ubuntu"
                elif linux == 2:
                    self.operating_system = "fedora"
                elif linux == 3:
                    self.operating_system = "debian"
                else:
                    print("you enter incorrect number ):")
                while linux !=1 and linux!=2 and linux!=3:
                    linux = int(input("what linux distribution software do you want?  1 = ubuntu , 2 = fedora , 3 = debian =>"))        
                    if linux == 1:
                        self.operating_system = "ubuntu"
                    elif linux == 2:
                        self.operating_system = "fedora"
                    elif linux == 3:
                        self.operating_system = "debian"
                    else:
                        print("you enter incorrect number ):")    
            elif operating_system == 2:
                windows = int(input("what windows distribution software do you want?  1 = windows 11 , 2 = windows 10 , 3 = windows 8.1 =>"))
                if windows == 1:
                    self.operating_system = "windows 11"
                elif windows == 2:
                    self.operating_system = "windows 10"
                elif windows == 3:
                    self.operating_system = "windows 8.1"
                else:
                    print("you enter incorrect number ):")
                while windows !=1 and windows!=2 and windows!=3:
                    windows = int(input("what windows distribution software do you want?  1 = windows 11 , 2 = windows 10 , 3 = windows 8.1 =>"))
                    if windows == 1:
                        self.operating_system = "windows 11"
                    elif windows == 2:
                        self.operating_system = "windows 10"
                    elif windows == 3:
                        self.operating_system = "windows 8.1"
                    else:
                        print("you enter incorrect number ):")     
            else:
                print("you enter incorrect number ):")
    # we enter in the special option for asus
    # first option : sticker we give you a free sticker to put it on your laptop and it will very cool and cute and we ask question of the user that he/she want this option or not
    def sticker(self):
        sticker = int(input("your laptop have two special option. first : sticker put it on your laptop and it will very cool and cute do you want it in your laptop?  1 = yes , 2 = no =>"))
        if sticker == 1:
            self.sticker = "yes"
        elif sticker == 2:
            self.sticker = "no"
        else:
            print("you enter incorrect number")
        # error handling
        while sticker != 1 and sticker != 2:
            sticker = int(input("your laptop have two special option. first : sticker do you want it in your laptop?  1 = yes , 2 = no=>"))
            if sticker == 1:
                self.sticker = "yes"
            elif sticker == 2:
                self.sticker = "no"
            else:
                print("you enter incorrect number")
    # second option : keyboard backlight that you can enjoy it and when you turn on laptop at night you can use your keyboard easily
    def keyboard_backlight(self):
        keyboard_backlight = int(input("your laptop have two special option. second : keyboard backlight backlight that you can enjoy it and when you turn on laptop at night you can use your keyboard easily do you want it in your laptop?  1 = yes , 2 = no=>"))
        if keyboard_backlight == 1:
            color_of_backlight = int(input("what color do you want to your keybord backlight be?  1 = black and white , 2 = red and blue , 3 = 7-color keyboard =>"))
            if color_of_backlight == 1:
                self.keyboard_backlight = "black and white"
            elif color_of_backlight == 2:
                self.keyboard_backlight = "red and blue"
            elif color_of_backlight == 3:
                self.keyboard_backlight = "7-color keyboard"
            else:
                print("you enter incorrect number ):")
            # error handling
            while color_of_backlight != 1 and color_of_backlight != 2 and color_of_backlight != 3:
                color_of_backlight = int(input("what color do you want to your keybord backlight be?  1 = black and white , 2 = red and blue , 3 = 7-color keyboard =>"))
                if color_of_backlight == 1:
                    self.keyboard_backlight = "black and white"
                elif color_of_backlight == 2:
                    self.keyboard_backlight = "red and blue"
                elif color_of_backlight == 3:
                    self.keyboard_backlight = "7-color keyboard"
                else:
                    print("you enter incorrect number ):")                
        elif keyboard_backlight == 2:
            self.keyboard_backlight = "no"
        else:
            print("you enter incorrect number ):")
        # error handling
        while keyboard_backlight !=1 and keyboard_backlight !=2:
            keyboard_backlight = int(input("your laptop have two special option. second : keyboard backlight do you want it in your laptop?  1 = yes , 2 = no=>"))
            if keyboard_backlight == 1:
                color_of_backlight = int(input("what color do you want to your keybord backlight be?  1 = black and white , 2 = red and blue , 3 = 7-color keyboard =>"))
                if color_of_backlight == 1:
                    self.keyboard_backlight = "black and white"
                elif color_of_backlight == 2:
                    self.keyboard_backlight = "red and blue"
                elif color_of_backlight == 3:
                    self.keyboard_backlight = "7-color keyboard"
                else:
                    print("you enter incorrect number ):")
                # error handling
                while color_of_backlight != 1 and color_of_backlight != 2 and color_of_backlight != 3:
                    color_of_backlight = int(input("what color do you want to your keybord backlight be?  1 = black and white , 2 = red and blue , 3 = 7-color keyboard =>"))
                    if color_of_backlight == 1:
                        self.keyboard_backlight = "black and white"
                    elif color_of_backlight == 2:
                        self.keyboard_backlight = "red and blue"
                    elif color_of_backlight == 3:
                        self.keyboard_backlight = "7-color keyboard"
                    else:
                        print("you enter incorrect number ):")                
            elif keyboard_backlight == 2:
                self.keyboard_backlight = "no"
            else:
                print("you enter incorrect number ):")

# third microsoft laptop
class microsoft:
    

    number_of_buyers = 0
    # user most to enter a input
    def __init__(self , name , last_name , age , laptop):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.laptop = laptop
        levono.number_of_buyers += 1
        print(f"hello mr/ms thanks for choose us \nyour name is {name} and your last name is {last_name} \n your laptop is {laptop} you choose expensive laptop")
    # color method that choose a laptop color
    def color_of_laptop(self):
        laptop_color = int(input("what color do you want to your laptop be?  1 = white , 2 = black , 3 = blue , 4 = pink , 5 = yellow =>"))
        if laptop_color == 1:
            self.laptop_color = "white"
        elif laptop_color == 2:
            self.laptop_color = "black"
        elif laptop_color == 3:
            self.laptop_color = "blue"
        elif laptop_color == 4:
            self.laptop_color = "pink"
        elif laptop_color == 5:
            self.laptop_color = "yellow"
        else:
            print("you say incorrect number try again ):")     
        # error handling
        while laptop_color!=1 and laptop_color!=2 and laptop_color!=3 and laptop_color!=4 and laptop_color!=5:
            laptop_color = int(input("what color do you want to your laptop be?  1 = white , 2 = black , 3 = blue , 4 = pink , 5 = yellow =>"))
            if laptop_color == 1:
                self.laptop_color = "white"
            elif laptop_color == 2:
                self.laptop_color = "black"
            elif laptop_color == 3:
                self.laptop_color = "blue"
            elif laptop_color == 4:
                self.laptop_color = "pink"
            elif laptop_color == 5:
                self.laptop_color = "yellow"
            else:
                print("you say incorrect number try again ):")
    # color of mouse method that choose a color of the mouse 
    def color_of_mouse(self):
        color_of_mouse = int(input("what color do you want to your mouse be? 1 = white , 2 = black , 3 = blue , 4 = pink , 5 = yellow =>"))
        if color_of_mouse == 1:
            self.color_of_mouse = "white"
        elif color_of_mouse == 2:
            self.color_of_mouse = "black"
        elif color_of_mouse == 3:
            self.color_of_mouse = "blue"
        elif color_of_mouse == 4:
            self.color_of_mouse = "pink"
        elif color_of_mouse == 5:
            self.color_of_mouse = "yellow"
        else:
            print("you say incorrect number try again ):")
        # error handling
        while color_of_mouse!=1 and color_of_mouse!=2 and color_of_mouse!=3 and color_of_mouse!=4 and color_of_mouse!=5:
            color_of_mouse = int(input("what color do you want to your mouse be? 1 = white , 2 = black , 3 = blue , 4 = pink , 5 = yellow =>"))
            if color_of_mouse == 1:
                self.color_of_mouse = "white"
            elif color_of_mouse == 2:
                self.color_of_mouse = "black"
            elif color_of_mouse == 3:
                self.color_of_mouse = "blue"
            elif color_of_mouse == 4:
                self.color_of_mouse = "pink"
            elif color_of_mouse == 5:
                self.color_of_mouse = "yellow"
            else:
                print("you say incorrect number try again ):")
    # operating system method that user change her/him operating system between ubuntu and windows
    def operating_system(self):
        operating_system = int(input("what operating system do you want to install on your laptop?   1 = windows  2 = linux 'i suggest you choose this(:' =>"))
        if operating_system == 2:    
            # linux has a lot of distribution software we enter a 3 most popular of it to user choose it 
            linux = int(input("what linux distribution software do you want?  1 = ubuntu , 2 = fedora , 3 = debian =>"))        
            if linux == 1:
                self.operating_system = "ubuntu"
            elif linux == 2:
                self.operating_system = "fedora"
            elif linux == 3:
                self.operating_system = "debian"
            else:
                print("you enter incorrect number ):")
            # error handling
            while linux !=1 and linux!=2 and linux!=3:
                linux = int(input("what linux distribution software do you want?  1 = ubuntu , 2 = fedora , 3 = debian =>"))        
                if linux == 1:
                    self.operating_system = "ubuntu"
                elif linux == 2:
                    self.operating_system = "fedora"
                elif linux == 3:
                    self.operating_system = "debian"
                else:
                    print("you enter incorrect number ):")    
        elif operating_system == 1:
            # windows also have a lot of distribution software too so i use three last of the windows vertion to user choose it
            windows = int(input("what windows distribution software do you want?  1 = windows 11 , 2 = windows 10 , 3 = windows 8.1 =>"))
            if windows == 1:
                self.operating_system = "windows 11"
            elif windows == 2:
                self.operating_system = "windows 10"
            elif windows == 3:
                self.operating_system = "windows 8.1"
            else:
                print("you enter incorrect number ):")
            # error handling
            while windows !=1 and windows!=2 and windows!=3:
                windows = int(input("what windows distribution software do you want?  1 = windows 11 , 2 = windows 10 , 3 = windows 8.1 =>"))
                if windows == 1:
                    self.operating_system = "windows 11"
                elif windows == 2:
                    self.operating_system = "windows 10"
                elif windows == 3:
                    self.operating_system = "windows 8.1"
                else:
                    print("you enter incorrect number ):")     
        else:
            print("you enter incorrect number ):")           
        # error handling
        while operating_system !=1 and operating_system !=2:
            operating_system = int(input("what operating system do you want to install on your laptop?   1 = windows  2 = linux(i suggest you choose this(:  )  =>"))
            if operating_system == 1:    
                linux = int(input("what linux distribution software do you want?  1 = ubuntu , 2 = fedora , 3 = debian =>"))        
                if linux == 1:
                    self.operating_system = "ubuntu"
                elif linux == 2:
                    self.operating_system = "fedora"
                elif linux == 3:
                    self.operating_system = "debian"
                else:
                    print("you enter incorrect number ):")
                # error handling
                while linux !=1 and linux!=2 and linux!=3:
                    linux = int(input("what linux distribution software do you want?  1 = ubuntu , 2 = fedora , 3 = debian =>"))        
                    if linux == 1:
                        self.operating_system = "ubuntu"
                    elif linux == 2:
                        self.operating_system = "fedora"
                    elif linux == 3:
                        self.operating_system = "debian"
                    else:
                        print("you enter incorrect number ):")    
            elif operating_system == 2:
                windows = int(input("what windows distribution software do you want?  1 = windows 11 , 2 = windows 10 , 3 = windows 8.1 =>"))
                if windows == 1:
                    self.operating_system = "windows 11"
                elif windows == 2:
                    self.operating_system = "windows 10"
                elif windows == 3:
                    self.operating_system = "windows 8.1"
                else:
                    print("you enter incorrect number ):")
                # erroe handling
                while windows !=1 and windows!=2 and windows!=3:
                    windows = int(input("what windows distribution software do you want?  1 = windows 11 , 2 = windows 10 , 3 = windows 8.1 =>"))
                    if windows == 1:
                        self.operating_system = "windows 11"
                    elif windows == 2:
                        self.operating_system = "windows 10"
                    elif windows == 3:
                        self.operating_system = "windows 8.1"
                    else:
                        print("you enter incorrect number ):")     
            else:
                print("you enter incorrect number ):")
    # we enter in the special option for microsoft
    # first option : microsoft pen you can draw with your pen and use it for select items and more work.. and we ask question from user that she/he want this option or not
    def microsoft_pen(self):
        microsoft_pen = int(input("your laptop have two special option. first : microsoft pen you can draw with your pen and use it for select items and more work.. do you want it in your laptop?  1 = yes , 2 = no=>"))
        if microsoft_pen == 1:
            self.microsoft_pen = "yes"
        elif microsoft_pen == 2:
            self.microsoft_pen = "no"
        else:
            print("you enter incorrect number ):")
        # error handling
        while microsoft_pen != 1 and microsoft_pen != 2:
            microsoft_pen = int(input("your laptop have two special option. first : microsoft pen you can draw with your pen and use it for select items and more work.. do you want it in your laptop?  1 = yes , 2 = no=>"))
            if microsoft_pen == 1:
                self.microsoft_pen = "yes"
            elif microsoft_pen == 2:
                self.microsoft_pen = "no"
            else:
                print("you enter incorrect number ):")            
    # second option : keyboard cover is something that prevent dirt and dust of your keyboard
    def keyboard_cover(self):
        keyboard_cover = int(input("your laptop have two special option. first : second option : keyboard cover is something that prevent dirt and dust of your keyboard do you want it in your laptop?  1 = yes , 2 = no=>"))
        if keyboard_cover == 1:
            self.keyboard_cover = "yes"
        elif keyboard_cover == 2:
            self.keyboard_cover = "no"
        else:
            print("you enter incorrect number ):")
        # error handling
        while keyboard_cover != 1 and keyboard_cover != 2:
            keyboard_cover = int(input("your laptop have two special option. first : second option : keyboard cover is something that prevent dirt and dust of your keyboard do you want it in your laptop?  1 = yes , 2 = no=>"))
            if keyboard_cover == 1:
                self.keyboard_cover = "yes"
            elif keyboard_cover == 2:
                self.keyboard_cover = "no"
            else:
                print("you enter incorrect number ):")

buyer1 = levono("nima" , "mahdi" , 15 , "lenovo")
print("\n")
buyer1.color_of_laptop()
print("\n")
buyer1.color_of_mouse()
print("\n")
buyer1.operating_system()
print("\n")
buyer1.fingerprint_scanner()
print("\n")
buyer1.cool_pad()
print("\n")
print(buyer1.__dict__)

print("\n\n\n")

buyer2 = asus("shayan" , "alvansaz" , 22 , "asus")
print("\n")
buyer2.color_of_laptop()
print("\n")
buyer2.color_of_mouse()
print("\n")
buyer2.operating_system()
print("\n")
buyer2.sticker()
print("\n")
buyer2.keyboard_backlight()
print("\n")
print(buyer2.__dict__)

print("\n\n\n")

buyer3 = microsoft("dainyal" , "tajik" , 17 , microsoft)
print("\n")
buyer3.color_of_laptop()
print("\n")
buyer3.color_of_mouse()
print("\n")
buyer3.operating_system()
print("\n")
buyer3.microsoft_pen()
print("\n")
buyer3.keyboard_cover()
print("\n")
print(buyer3.__dict__)

# thank for reading (: