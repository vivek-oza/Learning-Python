# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def bookTicket (self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo}, from  {fro}, to {to}")

    def getSeatsStatus(self):
        print("On time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo}, from  {fro}, to {to}, is {randint(222, 5555)}")



passanger1 = Train(1234)
passanger1.bookTicket("Gnr","Del")
passanger1.getFare("Gnr","Del")
passanger1.getSeatsStatus()