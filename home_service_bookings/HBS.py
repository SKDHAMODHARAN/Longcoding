user_info =[]
TypesOfServices =[]
BookedServices =[]

class userdetails:
    def __init__(self,userid,username,password,mail,Phone_no,Position,location):
         self.userid = userid
         self.username = username
         self.password = password
         self.mail = mail
         self.phone_no =Phone_no
         self.Position = Position
         self.location = location
    
    
    def addlist(self):
        user_info.append(self)
        return user_info 
    
    def login(self,name,pd):
        for data in user_info:
            if(data.username == name and data.password == pd):
                print("--------------------------------------")
                print("Login Success!!!")
                Sevicebooking.Display()
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
       Position = "Customer"
       location= input("Enter the Location :")
       user = userdetails(userid,username,password,mail,Phone_no,Position,location)
       user.addlist()
       print(user_info)
       print("Register SuccessFul!!!")
       Sevicebooking.Display()
    

    @staticmethod
    def welcome():
        global var
        print("----------------------------")
        print("WELCOM TO HomeService System")
        print("----------------------------")
        print("1.login")
        print("2.Rigister")
        print("----------------------------")
        var = int(input("Enter your choice :" ))
        return 0

class Services_list:
    def __init__(self,ser_id,ser_name,amount):
        self.ser_id = ser_id
        self.ser_name = ser_name
        self.amount = amount

class Booked_ser:
    def __init__(self,ser_name,amount):
        self.ser_name =ser_name
        self.amount =amount

    def addservice(self):
        BookedServices.append(self)
        return BookedServices
    
    def display():
        for Bs in BookedServices :
            print(Bs.ser_name,"\t",Bs.amount)

class Transactions(Booked_ser,Services_list):
    def __init__(self,ser_id, ser_name, amount):
        super().__init__(ser_id,ser_name, amount)

    def CancelBooking():
        CanSer =input("What  kind of service you want to canccel:")
        print("")
        for se in BookedServices:
            if CanSer == se.ser_name:
                BookedServices.remove(se.ser_name)
                print("Booking Cancel Succcessfully!!!")




class Sevicebooking(userdetails):
    def __init__(self, userid, username, password, mail, Phone_no, Position,location):
        super().__init__(userid, username, password, mail, Phone_no, Position,location)


    def Display():
        print("-------------------------------------------")
        print("1.Book Services")
        print("")
        print("2.Booked Services")
        print("")
        print("3.Cancel Booking")
        print("")
        print("3.Booking History")
        print("")
        print("4.Logout")
        print("")
        choice = int(input("Enter your Choice : "))
        print("")

        if choice == 1:
            print("Available Services !!!")
            print("")
            for s in TypesOfServices:
                print( s.ser_id, s.ser_name,"\t"," $",s.amount,"\t")

            while True:
                global Selected_Service,service
                print("")
                Selected_Service =input("What  kind of service you want  select with their id:")
                print("")
                for service in TypesOfServices:
                    if Selected_Service == service.ser_id:
                        print("You Choosed : ",service.ser_name)
                        print("Payment :", service.amount)
                        print("")
                        MyService = Booked_ser(service.ser_name,service.amount)
                        MyService.addservice()
                        Sevicebooking.Display()
                        break
                break

        if choice == 2:
            print("Active Booked Services :")
            print("")
            Booked_ser.display()
            Sevicebooking.Display()
        
        if choice == 3:
            Transactions.CancelBooking()
            print("Active Booked Services :")
            print("")
            Booked_ser.display()


if __name__ == "__main__":
    user = userdetails(101,"Ram","ram$123","rammeet1234@gmail.com",9790876507,"Customer","Chennai")
    user.addlist()
    user = userdetails(102,"Pugazh","Pugazh3","mepugazh3@gmail.com",6463444062,"Admin","Pune")
    user.addlist()
    user= userdetails(103,"Lashman12","lash#123","laks234@gmail.com",98657403847,"Customer","Thambaram")
    user.addlist()

    ser_1 = Services_list("1","Electrical","10,000")
    TypesOfServices.append(ser_1)
    ser_2 = Services_list("2","Plumbing","5,000")
    TypesOfServices.append(ser_2)
    ser_3 = Services_list("3","Carpenting","14,000")
    TypesOfServices.append(ser_3)
    ser_4 = Services_list("4","Cleaning","6,000")
    TypesOfServices.append(ser_4)
    ser_5 = Services_list("5","Beauty","12,000")
    TypesOfServices.append(ser_5)


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
