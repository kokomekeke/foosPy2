from threading import Thread, current_thread


class BookTicket():
    def __init__(self, available_seats):
        self.available_seats = available_seats

    def Bookseat(self, seatToBeBooked):
        print(f"{self.available_seats} seat was available before booking.")
        name = current_thread().name
        if seatToBeBooked <= self.available_seats:
            self.available_seats -= seatToBeBooked
            print(f"{seatToBeBooked} seat has been allocated to {name}")
        else:
            print("Sorry, we are out of seats.")


obj = BookTicket(1)
T1 = Thread(target=obj.Bookseat, kwargs={"seatToBeBooked": 1}, name="Walter White")
T2 = Thread(target=obj.Bookseat, kwargs={"seatToBeBooked": 1}, name="Jesse Pinkman")
T1.start()
T2.start()