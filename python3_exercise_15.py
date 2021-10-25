# in this script we want to assemble pc that user want it

class PC:

    number_of_buyers = 0
    # the input is only name and last name
    def __init__(self , name , last_name):
        self.name = name
        self.last_name = last_name
        PC.number_of_buyers += 1
        print(f"hi mr/ms {name}\nyour name is {name} and your last name is {last_name}")
    
    # memory ram that user must choose one of them
    def memory_ram(self):
        memory_ram = int(input("How much space of memory ram do you want to have?  1 = 4gb , 2 = 6gb , 3 = 8gb , 4 = 12gb , 5 = 16gb , 6 = 32gb =>"))
        if memory_ram == 1:
            self.memory_ram = "4gb"
        elif memory_ram ==2:
            self.memory_ram = "6gb"
        elif memory_ram ==3:
            self.memory_ram = "8gb"
        elif memory_ram ==4:
            self.memory_ram = "12gb"
        elif memory_ram ==5:
            self.memory_ram = "16gb"
        elif memory_ram ==6:
            self.memory_ram = "32gb"
        else:
            print("you enter incorrect number ): try again")
        # error handling
        while memory_ram !=1 and memory_ram !=2 and memory_ram !=3 and memory_ram !=4 and memory_ram !=5 and memory_ram !=6:
            memory_ram = int(input("How much space of memory ram do you want to have?  1 = 4gb , 2 = 6gb , 3 = 8gb , 4 = 12gb , 5 = 16gb , 6 = 32gb =>"))
            if memory_ram == 1:
                self.memory_ram = "4gb"
            elif memory_ram ==2:
                self.memory_ram = "6gb"
            elif memory_ram ==3:
                self.memory_ram = "8gb"
            elif memory_ram ==4:
                self.memory_ram = "12gb"
            elif memory_ram ==5:
                self.memory_ram = "16gb"
            elif memory_ram ==6:
                self.memory_ram = "32gb"
            else:
                print("you enter incorrect number ): try again")
    # here user most choose cpu 
    # i don't write all of the cpu only two of them
    def cpu(self):
        cpu = int(input("what kind of cpu do you want?  1 = intel I7 , 2 = intal I5 =>"))
        if cpu == 1:
            self.cpu = "intel I7"
        elif cpu == 2:
            self.cpu = "intel I5"
        else:
            print("you enter incorrect number ): try again")
        while cpu !=1 and cpu !=2:
            cpu = int(input("what kind of cpu do you want?  1 = intel I7 , 2 = intal I5 =>"))
            if cpu == 1:
                self.cpu = "intel I7"
            elif cpu == 2:
                self.cpu = "intel I5"
            else:
                print("you enter incorrect number ): try again")
    # here the graphic i do not write all of the storage of tehm
    def graphic_card(self):
        graphic_card = int(input("what storage of the graphic do you want?  1 = 2gb , 2 = 4gb , 3 = 8gb =>"))
        if graphic_card == 1:
            self.graphic_card = "2gb"
        elif graphic_card == 2:
            self.graphic_card = "4gb"
        elif graphic_card == 3:
            self.graphic_card = "8gb"
        else:
            print("you enter incorrect number ): try again")
        # error handling
        while graphic_card !=1 and graphic_card !=2 and graphic_card !=3:
            graphic_card = int(input("what storage of the graphic do you want?  1 = 2gb , 2 = 4gb , 3 = 8gb =>"))
            if graphic_card == 1:
                self.graphic_card = "2gb"
            elif graphic_card == 2:
                self.graphic_card = "4gb"
            elif graphic_card == 3:
                self.graphic_card = "8gb"
            else:
                print("you enter incorrect number ): try again")
    # the hard disk method that user choose one of them
    def hard_disk(self):
        hard_disk = int(input("how much do you want to your haed disk be?  1 = 250gb , 2 = 500gb , 3 = 750gb , 4 = 1tr , 5 = 2tr =>"))
        if hard_disk == 1:
            self.hard_disk = "250bg"
        elif hard_disk == 2:
            self.hard_disk = "500gb"
        elif hard_disk == 3:
            self.hard_disk = "750gb"
        elif hard_disk == 4:
            self.hard_disk = "1tr"
        elif hard_disk == 5:
            self.hard_disk = "2tr"
        else:
            print("you enter incorrect number ): try again")
        # error handling
        while hard_disk !=1 and hard_disk !=2 and hard_disk !=3 and hard_disk !=4 and hard_disk !=5:
            hard_disk = int(input("how much do you want to your haed disk be?  1 = 250gb , 2 = 500gb , 3 = 750gb , 4 = 1tr , 5 = 2tr =>"))
            if hard_disk == 1:
                self.hard_disk = "250bg"
            elif hard_disk == 2:
                self.hard_disk = "500gb"
            elif hard_disk == 3:
                self.hard_disk = "750gb"
            elif hard_disk == 4:
                self.hard_disk = "1tr"
            elif hard_disk == 5:
                self.hard_disk = "2tr"
            else:
                print("you enter incorrect number ): try again")
    # the keyboard type that is write 3 most popular of them to user choose it for picture you can google it 
    def keyboard_type(self):
        keyboard = int(input("what mark of the keyboard do you want? 1 = razer huntsman elite , 2 = apple kagic keyboard , 3 = logitech mx keys mini =>"))
        if keyboard == 1:
            self.keyboard = "razer huntsman elite"
        elif keyboard == 2:
            self.keyboard = "apple kagic keyboard"
        elif keyboard == 3:
            self.keyboard = "logitech mx keys mini"
        else:
            print("you enter incorrect number ): try again")
        # error handling
        while keyboard !=1 and keyboard !=2 and keyboard !=3:
            keyboard = int(input("what mark of the keyboard do you want? 1 = razer huntsman elite , 2 = apple kagic keyboard , 3 = logitech mx keys mini =>"))
            if keyboard == 1:
                self.keyboard = "razer huntsman elite"
            elif keyboard == 2:
                self.keyboard = "apple kagic keyboard"
            elif keyboard == 3:
                self.keyboard = "logitech mx keys mini"
            else:
                print("you enter incorrect number ): try again")
    # the mouse type that i write 4 most popular of them and user can choose it for picture of them you can google it
    def mouse_type(self):
        mouse_type = int(input("what mouse type type do you want to your mouse type be?  1 = logitech mx master 3 , 2 = logitech m325 , 3 = microsoft classic intellimouse , 4 = logitech mx vertical =>"))
        if mouse_type == 1:
            self.mouse_type = "logitech mx master 3"
        elif mouse_type == 2:
            self.mouse_type = "logitech m325"
        elif mouse_type == 3:
            self.mouse_type = "microsoft classic intellimouse"
        elif mouse_type == 4:
            self.mouse_type = "logitech mx vertical"
        else:
            print("you enter incorrect number ): try again")
        # error handling
        while mouse_type !=1 and mouse_type !=2 and mouse_type !=3 and mouse_type !=4:
            mouse_type = int(input("what mouse type do you want to your mouse type be?  1 = logitech mx master 3 , 2 = logitech m325 , 3 = microsoft classic intellimouse , 4 = logitech mx vertical =>"))
            if mouse_type == 1:
                self.mouse_type = "logitech mx master 3"
            elif mouse_type == 2:
                self.mouse_type = "logitech m325"
            elif mouse_type == 3:
                self.mouse_type = "microsoft classic intellimouse"
            elif mouse_type == 4:
                self.mouse_type = "logitech mx vertical"
            else:
                print("you enter incorrect number ): try again") 
    def monitor_resolution(self):
        monitor_resolution = int(input("what resolution do you want for your monitor?  1 = FHD , 2 = 2K , 3 = 4K =>"))
        if monitor_resolution == 1:
            self.monitor_resolution = "FHD"
        elif monitor_resolution == 2:
            self.monitor_resolution = "2K"
        elif monitor_resolution == 3:
            self.monitor_resolution = "4K"
        else:
            print("you enter incorrect number ): try again")
        while monitor_resolution !=1 and monitor_resolution !=2 and monitor_resolution !=3:
            monitor_resolution = int(input("what resolution do you want for your monitor?  1 = FHD , 2 = 2K , 3 = 4K =>"))
            if monitor_resolution == 1:
                self.monitor_resolution = "FHD"
            elif monitor_resolution == 2:
                self.monitor_resolution = "2K"
            elif monitor_resolution == 3:
                self.monitor_resolution = "4K"
            else:
                print("you enter incorrect number ): try again")
    def case_type(self):
        case_type = int(input("what type of case do you want to use for your pc?   1 = fractal design meshify 2 compact , 2 = lian li q58 , 3 = fractal design define 7 =>"))
        if case_type == 1:
            self.case_type = "fractal design meshify 2 compact"
        elif case_type == 2:
            self.case_type = "lian li q58"
        elif case_type == 3:
            self.case_type = "fractal design define 7"
        else:
            print("you enter incorrect number ): try again")
        while case_type !=1 and case_type !=2 and case_type !=3:
            case_type = int(input("what type of case do you want to use for your pc?   1 = fractal design meshify 2 compact , 2 = lian li q58 , 3 = fractal design define 7 =>"))
            if case_type == 1:
                self.case_type = "fractal design meshify 2 compact"
            elif case_type == 2:
                self.case_type = "lian li q58"
            elif case_type == 3:
                self.case_type = "fractal design define 7"
            else:
                print("you enter incorrect number ): try again")


buyer1 = PC("nima" , "mahdi")
print("\n\n")
buyer1.memory_ram()
print("\n\n")
buyer1.cpu()
print("\n\n")
buyer1.graphic_card()
print("\n\n")
buyer1.hard_disk()
print("\n\n")
buyer1.keyboard_type()
print("\n\n")
buyer1.mouse_type()
print("\n\n")
buyer1.monitor_resolution()
print("\n\n")
buyer1.case_type()
print("\n\n")
print(buyer1.__dict__)
