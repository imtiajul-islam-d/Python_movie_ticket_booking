class Star_Cinema:
    __hall_list = []
    def entry_hall(self,hall):
        Star_Cinema.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)
    def entry_show(self,id, movie_name, time):
        show = (id,movie_name,time)
        self.__show_list.append(show)
        seatPlan = []
        for x in range(self.__rows):
            l = []
            for y in range(self.__cols):  
                l.append(0)
            seatPlan.append(l)
        self.__seats.update({id:seatPlan})
    def book_seats(self,id, seat):
        showId = id
        row = seat[0]
        col = seat[1]
        # check is entered movie id valid
        idFound = False
        showObject = {}
        for x in self.__show_list:
            if x[0] == showId:
                idFound = True
                showObject = x
        if idFound != True:
            print("Sorry, Movie ID is not correct!")
        else:
            # Check is the entered seat number valid
            if row <= len(self.__seats[showId])  and col <= len(self.__seats[showId][0]):
                ## entered seat number is valid
                # Now check is the desired seat already booked
                if self.__seats[showId][row-1][col-1] == 0:
                    ## desired seat is available
                    # book that seat for the user now
                    self.__seats[showId][row-1][col-1] = 1
                    print(f"Congratulations!!! We have booked your desired seat for the movie '{showObject[1]}'. Your seat row number is {row} and the column number is {col}")
                else:
                    # seat is already book, suggest user to try another seat number
                    print("OPPS!!! Your desired seat is already booked! Please try another one...")
            else:
                # entered seat number is not valid
                print("Your entered seat number is invalid! Please enter a correct one.")
    def view_show_list(self):
        print("---------------RUNNING SHOWS ARE----------------")
        for x in self.__show_list:
            print(f"MOVIE NAME:{x[1]}({x[0]}), SHOW ID: {x[0]} TIME: {x[2]}")
    def view_available_seats(self, showId):
        # check is entered movie id valid
        idFound = False
        for x in self.__show_list:
            if x[0] == showId:
                idFound = True
        if idFound != True:
            print("Sorry, Movie ID is not correct!. Please enter a correct movie ID to see the available seats...") 
        else:
            # Entered movie ID is correct, show the available seats for that movie
            print(f"-----------AVAILABLE SEATS ARE--------------")
            # print(f"Available seats are for your desired movie in the below... 0 indicates seat is available and 1 indicates seat is booked")
            for i in range(len(self.__seats[showId])):
                for j in range(len(self.__seats[showId][i])):
                    if self.__seats[showId][i][j] == 0:
                        print(0, end=" ")
                    else:
                        print(1, end=" ")
                print("")

            
    
        
hall = Hall(13,11,199)
hall.entry_show(3,"Jawaan", "1:59pm")
hall.entry_show(5,"Spider man", "6:59pm")

while True:
    flag = 0
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. Exit")
    flag = int(input("Enter your option: "))
    if flag == 1:
        hall.view_show_list()
    elif flag == 2:
        movieId = int(input("Enter show ID: "))
        hall.view_available_seats(movieId)
    elif flag == 4:
        break
    else:
        continue

# hall.book_seats(3,(10,11))
# hall.book_seats(3,(10,10))
# hall.book_seats(3,(3,10))

# hall.view_available_seats(3)
