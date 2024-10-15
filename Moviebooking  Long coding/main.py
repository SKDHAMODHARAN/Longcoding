user_info =[]
book_movie=[]
mov =[]
mov_timings=[]
Theatre_Datalist=[]
class userdetails:
    def __init__(self,userid,username,password,mail,Phone_no,Gender,Position):
         self.userid = userid
         self.username = username
         self.password = password
         self.mail = mail
         self.phone_no =Phone_no
         self.Gender = Gender
         self.Position = Position
    
    def addlist(self):
        user_info.append(self)
        return user_info
        
    def login(self,name,pd):
        for data in user_info:
            if(data.username == name and data.password == pd):
                print("--------------------------------------")
                print("Login Success!!!")
                Moviebooking.Display()
                return data
            elif(data.username == name or data.password == pd):
                print("--------------------------------------")
                print("Enter your Correct username && password")
            else:
                print("User Doesn't Exit")
                break
    
    def Register(self):
       userid=103
       userid =  userid + 1
       username  = input("Enter Your Username : ")
       password = input("Enter Your Password : ")
       mail  = input("Enter Your Mail ID: ")
       Phone_no  = int(input("Enter Your Phone_no : "))
       Gender  = input("Gender : ")
       Position = "Customer"
       user = userdetails(userid,username,password,mail,Phone_no,Gender,Position)
       user.addlist()
       print(user_info)
       print("Register SuccessFul!!!")
       Moviebooking.Display()
    
    @staticmethod
    def welcome():
        global var
        print("----------------------------")
        print("WELCOM TO BOOKMOVIE")
        print("----------------------------")
        print("1.login")
        print("2.Rigister")
        print("----------------------------")
        var = int(input("Enter your choice :" ))
        return 0
    

class Movie_listings:
    def __init__(self,Movie_id,Movie_name,Language,Ganere,length_time):
        self.Movie_id = Movie_id
        self.Movie_name = Movie_name
        self.Language = Language
        self.Ganere =Ganere
        self.lengeth_time =length_time

class Timing:
    def __init__(self,Timing_id,Timings):
        self.Timing_id =Timing_id
        self.Timings =Timings

class Theatre:
    def __init__(self,Theatre_id,Theatre_name,Location,Total_screen,seats):
        self.Theatre_id =Theatre_id
        self.Theatre_name =Theatre_name
        self.Location = Location
        self.Total_screen =Total_screen
        self.seats=seats


class Rating(userdetails):
    def __init__(self, userid, username, password, mail, Phone_no, Gender, Position):
        super().__init__(userid, username, password, mail, Phone_no, Gender, Position)

class Avail_movies(Movie_listings,Timing,Theatre):                                                    #multiple Inheritance
    def __init__(self, Movie_id, Movie_name, Language, Ganere, length_time,availmovie_id):
        super().__init__(Movie_id, Movie_name, Language, Ganere, length_time)
        self.availmovie_id = availmovie_id

class Moviebooking(userdetails):
    def __init__(self, userid, username, password, mail, Phone_no, Gender, Position):
        super().__init__(userid, username, password, mail, Phone_no, Gender, Position)
            

    def Display():
        print("-------------------------------------------")
        print("1.Book My Ticket!!!")
        print("")
        print("2.Booking History")
        print("")
        print("3.Logout")
        print("")
        choice = int(input("Enter your Choice : "))
        
        def logout(strlog):
            return strlog
        strlog ="logout Succesfully!!!"

        if choice == 1:
            movie_1 = Movie_listings("mov1","The Flash","English","Fantasy","2h 24m")
            mov.append(movie_1)
            movie_2 = Movie_listings("mov2","Aadhipurush","Tamil","Mythological","2h 59m")
            mov.append(movie_2)
            movie_3 = Movie_listings("mov3","Asvins","Tamil","Horror","2h 59m")
            mov.append(movie_3)

            Tyme_1 = Timing(1 ,"04.00 am")
            mov_timings.append(Tyme_1)
            Tyme_2 = Timing(2 ,"10.00 am")
            mov_timings.append(Tyme_2)
            Tyme_3 = Timing(3 ,"02.00 pm")
            mov_timings.append(Tyme_3)
            Tyme_4 = Timing(4,"06.00 pm")
            mov_timings.append(Tyme_4)

            theatre_1 = Theatre("Thtr1","Sahiyam Cinemas","Rayapettah",3,[['A01'],['A02'],['A03'],['B01'],['B02'],['B03']])
            Theatre_Datalist.append(theatre_1)
            theatre_2 = Theatre("Thtr2","S2 Cinemas","Perambur",2,[['A01'],['A02'],['A03'],['B01'],['B02'],['B03']])
            Theatre_Datalist.append(theatre_2)
            theatre_3 = Theatre("Thtr3","Kamala Cinemas","T.Nagar",2,[['A01'],['A02'],['A03'],['B01'],['B02'],['B03']])
            Theatre_Datalist.append(theatre_3)
            theatre_4 = Theatre("Thtr4","Rogini Movie Park","poonamalle",3,[['A01'],['A02'],['A03'],['B01'],['B02'],['B03']])
            Theatre_Datalist.append(theatre_4)
            
            for m in mov:
                print(m.Movie_id,":", m.Movie_name,"\t")
            

            global Selected_movie,movi
            Selected_movie =input("Select Movie :")
            for movi in mov:
                if Selected_movie == movi.Movie_name:
                    break
                else:
                    print("You Didn't Select Any Movie, Select Your Movie!!!")

            if Selected_movie == movi.Movie_name:
                for t in Theatre_Datalist:
                    print(t.Theatre_id, ":",t.Theatre_name,":",t.Location,"\t")

            global Selected_theatre,theater
            Selected_theatre = input("Select Theatre :")

            for theater in Theatre_Datalist:
                if(Selected_theatre == theater.Theatre_name):
                    break
            
            for tme in mov_timings:
                print(tme.Timing_id,tme.Timings)

            global Selected_tymid,thime
            Selected_tymid = int(input("Select Time When You Want To See!!! :"))

            for t in mov_timings:
                if Selected_tymid == t.Timing_id:
                    global Selected_tym
                    Selected_tym = t.Timings
                    print("------------------------------")
                    print("Your Seat Was Booked!!!")
                    break
        elif choice == 2:
            print("booking Histry...")
            print((f"name:{user_infousername}\n Gender:{user.Gender}"))
            
        elif choice == 3:
            print("------------------------")
            print(logout(strlog))
        

if __name__ == "__main__":
    user = userdetails(101,"Ram","ram$123","rammeet1234@gmail.com",9790876507,"Male","Customer")
    user.addlist()
    user = userdetails(102,"StarPugazh2","Pugazh3","mepugazh3@gmail.com",6463444062,"male","Admin")
    user.addlist()
    user= userdetails(103,"Lashman12","lash#123","laks234@gmail.com",98657403847,"Male","Customer")
    user.addlist()
    
    while True:
        print("")
        Greet = user.welcome()
        if var == 1:
            name = input("Enter your Username :")
            pd = input("Enter your Password :")
            user.login(name,pd)
        elif var == 2:
            user.Register()
        else:
            print("Please Enter Valid Choice!!!,Try Again... ")
    
