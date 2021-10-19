import random
from math import sqrt

class User:
    def __init__(self, username,point_dict,initial_score=0):
        self.__username = username
        self.point_dict = point_dict
        self.__initial_score = initial_score
        self.check_register()
        self.display_details()
        self.ret_point_card()

    def check_register(self):
        if self.__username not in self.point_dict.keys():
            self.point_dict[self.__username] = self.__initial_score

    def display_details(self):
        return self.__username, self.__initial_score

    def ret_point_card(self):
        return self.point_dict

class Shape:
    def __init__(self,j,shapename,point_dict,username,peri,area):
        self.username = username
        self.shapename = shapename
        self.peri = peri
        self.area = area
        self.point_dict = point_dict

    def displayinfo(self):
        print('Answer will be matched till the second decimal place')

class Square(Shape):
    def __init__(self, j, shapename, point_dict,username,peri,area,slength):
        super().__init__(j,shapename,point_dict,username,peri,area)
        self.slength = slength


    def check_output(self):
        correctaperi = float(4*self.slength)
        correctaarea = float(self.slength*self.slength)
        print('CORRECT PERIMETER : {}'.format(correctaperi))
        print('CORRECT AREA : {}'.format(correctaarea))
        if (round(correctaperi,2) == round(self.peri,2)):
            print('CONGRATULATIONS!!! CORRECT PERIMETER CALCULATION DONE\n')
            self.point_dict[self.username] = self.point_dict[self.username]+1
        else:
            print('INCORRECT PERIMETER CALCULATION DONE\n')
        if (round(correctaarea,2) == round(self.area,2)):
            print('CONGRATULATIONS!!! CORRECT AREA CALCULATION DONE\n')
            self.point_dict[self.username] = self.point_dict[self.username]+1
        else:
            print('INCORRECT AREA CALCULATION DONE\n')

    def displayinfo(self):
        print('Test for shape SQUARE has completed')

    def process_data(self):
        super().displayinfo()
        self.check_output()
        self.displayinfo()

class Rectange(Shape):
    def __init__(self, j, shapename, point_dict,username,peri,area,rlength,rheigth):
        super().__init__(j,shapename,point_dict,username,peri,area)
        self.rlength = rlength
        self.rheigth = rheigth

    def check_output(self):
        correctaperi = float(2*(self.rlength+self.rheigth))
        correctaarea = float(self.rlength*self.rheigth)
        print('CORRECT PERIMETER : {}'.format(correctaperi))
        print('CORRECT AREA : {}'.format(correctaarea))
        if (round(correctaperi,2) == round(self.peri,2)):
            print('CONGRATULATIONS!!! CORRECT PERIMETER CALCULATION DONE\n')
            self.point_dict[self.username] = self.point_dict[self.username]+1
        else:
            print('INCORRECT PERIMETER CALCULATION DONE\n')
        if (round(correctaarea,2) == round(self.area,2)):
            print('CONGRATULATIONS!!! CORRECT AREA CALCULATION DONE\n')
            self.point_dict[self.username] = self.point_dict[self.username]+1
        else:
            print('INCORRECT AREA CALCULATION DONE\n')

    def displayinfo(self):
        print('Test for shape RECTANGLE has completed')

    def process_data(self):
        super().displayinfo()
        self.check_output()
        self.displayinfo()

class Triangle(Shape):
    def __init__(self, j, shapename, point_dict,username,peri,area,length1):
        super().__init__(j,shapename,point_dict,username,peri,area)
        self.length1 = length1

    def check_output(self):
        correctaperi = float(3*self.length1)
        correctaarea = float(sqrt(3) / 4 * self.length1 * self.length1)
        print('CORRECT PERIMETER : {}'.format(correctaperi))
        print('CORRECT AREA : {}'.format(correctaarea))
        if (round(correctaperi,2) == round(self.peri,2)):
            print('CONGRATULATIONS!!! CORRECT PERIMETER CALCULATION DONE\n')
            self.point_dict[self.username] = self.point_dict[self.username]+1
        else:
            print('INCORRECT PERIMETER CALCULATION DONE\n')
        if (round(correctaarea,2) == round(self.area,2)):
            print('CONGRATULATIONS!!! CORRECT AREA CALCULATION DONE\n')
            self.point_dict[self.username] = self.point_dict[self.username]+1
        else:
            print('INCORRECT AREA CALCULATION DONE\n')

    def displayinfo(self):
        print('Test for shape TRIANGLE has completed')

    def process_data(self):
        super().displayinfo()
        self.check_output()
        self.displayinfo()

class Circle(Shape):
    def __init__(self, j, shapename, point_dict,username,peri,area,radius):
        super().__init__(j,shapename,point_dict,username,peri,area)
        self.radius = radius


    def check_output(self):
        correctaperi = float(2*3.14*self.radius)
        correctaarea = float(3.14*self.radius*self.radius)
        print('CORRECT PERIMETER : {}'.format(correctaperi))
        print('CORRECT AREA : {}'.format(correctaarea))
        if (round(correctaperi,2) == round(self.peri,2)):
            print('CONGRATULATIONS!!! CORRECT PERIMETER CALCULATION DONE\n')
            self.point_dict[self.username] = self.point_dict[self.username]+1
        else:
            print('INCORRECT PERIMETER CALCULATION DONE\n')
        if (round(correctaarea,2) == round(self.area,2)):
            print('CONGRATULATIONS!!! CORRECT AREA CALCULATION DONE\n')
            self.point_dict[self.username] = self.point_dict[self.username]+1
        else:
            print('INCORRECT AREA CALCULATION DONE\n')

    def displayinfo(self):
        print('Test for shape CIRCLE has completed')

    def process_data(self):
        super().displayinfo()
        self.check_output()
        self.displayinfo()

def quit_application():
    print("***********************************************")
    print('Thanks for playing')
    print("***********************************************")
    exit

def ViewScores(point_dict):
    if point_dict:
        print('User  Score')
        for user, score in point_dict.items():
            print('{} : {}'.format(user, score))
    else:
        print("No Registered Users\nPlease try another option")
        main()

def main():
    print("************************************")
    print("        TEST YOUR GEOMETRY")
    print("************************************\n")
    point_dict = {}
    menu(point_dict)


def input_answers():
    error_entry5 = True
    while error_entry5:
        try:
            peri = float(input('Enter the Perimeter of the SHAPE (Default unit = cm) : '))
        except ValueError:
            print("You have to enter a valid float value for this option.. Please try again")
            continue
        else:
            error_entry5 = False
    error_entry6 = True
    while error_entry6:
        try:
            area = float(input('Enter the Area of the SHAPE (Default unit = cm) : '))
        except ValueError:
            print("You have to enter a valid float value for this option.. Please try again")
            continue
        else:
            error_entry6 = False
    ans = [peri, area]
    return ans
def play(point_dict,username):
    error_entry2 = True
    while error_entry2:
        try:
            numbershape = int(input("Enter the number of shapes to play with [Maximum shapes available = 4]\nYour choice :- "))
            if numbershape not in (1, 2, 3, 4):
                print("Selected value is Invalid.. Please try again with one of the following values = 1,2,3,4")
                continue
        except ValueError:
            print("You have to enter a valid integer value for this option.. Please try again")
            continue
        else:
            error_entry2 = False
        print('All measures will be in centimeter(cm)\n')
        print('All the measures will lie between 1 cm to 10 cm\n')
        for i in range(numbershape):
            j = random.randint(1, 4)
            if (j==1):
                shapename = 'SQUARE'
                slength = random.randint(1, 10)
                print('SHAPE TYPE : SQUARE \nLength of SQUARE : {} cm '.format(slength))
                answer_list = input_answers()
                peri=answer_list[0]
                area=answer_list[1]
                square1 = Square(j, shapename, point_dict,username,peri,area,slength)
                square1.process_data()
            elif (j==2):
                shapename = 'RECTANGLE'
                rlength = random.randint(1, 10)
                rheigth = random.randint(1, 10)
                print('SHAPE TYPE : RECTANGLE \nLength of RECTANGLE : {} cm \nHeight of RECTANGLE : {} cm '.format(rlength, rheigth))
                answer_list = input_answers()
                peri = answer_list[0]
                area = answer_list[1]
                rectange1 = Rectange(j, shapename, point_dict,username,peri,area,rlength,rheigth)
                rectange1.process_data()
            elif (j==3):
                shapename = 'TRIANGLE'
                length1 = random.randint(1, 10)
                print("SHAPE TYPE : TRIANGLE \n Length 1 : {} cm ".format(length1))
                print('THIS IS AN EQUILATERAL TRIANGLE')
                answer_list = input_answers()
                peri = answer_list[0]
                area = answer_list[1]
                triangle1 = Triangle(j, shapename, point_dict,username,peri,area,length1)
                triangle1.process_data()
            elif (j==4):
                shapename = 'CIRCLE'
                radius = random.randint(1, 10)
                print('SHAPE TYPE : CIRCLE \nRadius of CIRCLE : {} cm '.format(radius))
                print('Take value of Pi = 3.14')
                answer_list = input_answers()
                peri = answer_list[0]
                area = answer_list[1]
                circle1 = Circle(j, shapename, point_dict,username,peri,area,radius)
                circle1.process_data()
        print('FINAL POINTS OF {} : {}'.format(username,point_dict[username]))
        error_entry4 = True
        while error_entry4:
            try:
                further_task = int(input('(1)Continue playing   (2)Go to the main menu \nYour Choice :  '))
            except ValueError:
                print("You have to enter a valid integer value for this option.. Please try again")
                continue
            else:
                error_entry4 = False
        if (further_task==1):
            play(point_dict,username)
        elif(further_task==2):
            menu(point_dict)
        else:
            print('Invalid option.. Quitting application\n')
            quit_application()
def menu(point_dict):
    error_entry = True
    while error_entry:
        try:
            option = int(input("(1)Register  (2)ViewScores  (3)Quit\nYour choice :- "))
        except ValueError:
            print("You have to enter a valid integer value for this option.. Please try again")
            continue
        else:
            error_entry = False
    if(option ==1):
        username = input("Enter your Name: ")
        user1 = User(username,point_dict)
        error_entry1 = True
        while error_entry1:
            try:
                playornot = int(input("(1)Play the Game  (2)Quit\nYour choice :- "))
            except ValueError:
                print("You have to enter a valid integer value for this option.. Please try again")
                continue
            else:
                error_entry1 = False
        if(playornot==1):
            play(point_dict,username)
        elif(playornot==2):
            quit_application()
        else:
            print("INVALID OPTION ENTERED...TRY AGAIN\n")
            menu(point_dict)
    elif(option==2):
        ViewScores(point_dict)
        quit_application()
    elif(option==3):
        quit_application()
    else:
        print("INVALID OPTION ENTERED...TRY AGAIN\n")
        menu(point_dict)

if __name__ == "__main__":
    main()