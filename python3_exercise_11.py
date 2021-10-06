# here creat a school class
class school:
    # here i creat a number of student to understand student that go in school
    num_of_student = 0
    # here init methond that give first name , last name , score and field
    def __init__(self , first , last , score , field):
        # and save it with self
        self.firstt = first
        self.lastt = last
        self.scoree = score
        self.fieldd = field
        # here i write this to add 1 to the number of studen to know how many student thay are in school
        school.num_of_student += 1
    # here field method is student name , last name and his/her field
    def field(self):
        print("\nname:" , self.firstt , "\nlast name:"  , self.lastt , "\nfield:" , self.fieldd)
    # here at time methode every field has time for it i wrote time in this method
    def time(self):
        if self.fieldd == "expreimental":
            print("you have to come to school at 7 oclock in the morning")
        elif self.fieldd == "humanities":
            print("you have to come to school at 12 oclock in the noon")
        elif self.fieldd == "mathematics and physics":
            print("you have to come to school at 6 oclock in the evening")

    # books method is method that say when student come to school to give them books
    def books(self):
        if self.fieldd == "expreimental" :
            print("\nok your field is expreimental" , "  so  " , "you have to come to school on monday to teke your books")
        elif self.fieldd == "humanities" :
            print("ok your field is humanities" , "  so  " , "you have to come to school on wednesday to take your books")
        elif self.fieldd == "mathematics and physics" :
            print("ok your field is mathematics and physics" , "  so  " , "you have to come to school on sunday to take your books")

    # teachers method say teachers name for each field
    def teachers(self):
        if self.fieldd == "expreimental":
            print("well , your tracher is mr.mahdi")
        elif self.fielddv == "humanities":
            print("well , your teacher is mr.saiidi")
        elif self.fieldd == "mathematics and physics":
            print("well , your teacher is mr.alvansaz")

    def score(self):
        if self.scoree > 17 :
            print("oh very good you are smart student")
        elif self.score < 17 :
            print("you are good student")
    # telegram group method say telegram group id for them field (the id is fake)
    def telegram_gr(self):
        if self.fieldd == "expreimental":
            print("your class telegram group is expreimental_school_gr")
        elif self.fieldd == "humanities":
            print("your class telegram group is humanities_school_gr")
        elif self.fieldd == "mathematics and physics":
            print("your class telegram group is mathematics_and_physics_school_gr")
    # here i write same last name method that perhaps student have same last name with their teacher
    def same_last(self):
        if self.lastt == "mahdi":
            print("you have same last name with on tacher n the school")
        elif self.lastt == "saiidi":
            print("you have same last name with on tacher n the school")
        elif self.lastt == "alvansaz":
            print("you have same last name with on tacher n the school")
    # uniform method say that each field what uniform have to wear when they are at school
    def uniform(self):
        if self.fieldd == "expreimental":
            print("you have to wear red uniform")
        elif self.fieldd == "humanities":
            print("you have to wear blue uniform")
        elif self.fieldd == "mathematics and physics":
            print("you have to weat brown uniform")
    # day of the weeks say that each field when have to come to school
    def day_of_weeks(self):
        if self.fieldd == "expreimental":
            print("expreimental : " , "\nyou have to come to school on saturday,monday,wednesday")
        elif self.fieldd == "humanities":
            print( "humanities : " , "you have to come to school on sunday,tusday,saturday")
        elif self.fieldd == "mathematics and physics":
            print("mathematics and physics : " , "you have to come school on sunday,monday,thursday")

# and pritn
stu1 = school('nima' , 'mahdi' , 19 , 'expreimental')
stu2 = school('shayan' , 'alvansaz' , 20 , 'mathematics and physics')
stu3 = school('mohsen' , 'saiidi' , 18 , 'humanities')

print(stu1.firstt)
print(stu1.lastt)
print(stu1.scoree)
print(stu1.fieldd)

stu1.field()
stu1.time()
stu1.books()
stu1.teachers()
stu1.score()
stu1.telegram_gr()
stu1.uniform()
stu1.same_last()
stu1.day_of_weeks()


print(school.num_of_student)