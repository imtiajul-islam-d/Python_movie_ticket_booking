class Star_Cinema:
    __hall_list = []
    def entry_hall(self,hall):
        Star_Cinema.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)
    def entry_show(self,id, movie_name, time):
        show = (id,movie_name,time)
        self.show_list.append(show)
        seatPlan = []
        for x in range(self.rows):
            l = []
            for y in range(self.cols):  
                l.append(0)
            seatPlan.append(l)
        self.seats.update({id:seatPlan})
    def book_seats(self,id, seat):
        row = seat[0]
        col = seat[1]
        
hall = Hall(10,10,199)
hall.entry_show(3,"movie", "time")
hall.entry_show(5,"movie", "time")
print(hall.seats)
