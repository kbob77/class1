print("this is our first program with python")

print('this class is at whitworth')

print("looking forward to this class")

print("this is a lot better than hello world")

bill = input("what is the total of the bill: ")
bill = float(bill)

tip10 =.10
tip20 =.20
tip25 =.25
tip30 =.30

total10 = (bill*tip10)+bill
total20 = (bill*tip20)+bill
total25 = (bill*tip25)+bill
total30 = (bill*tip30)+bill

print ("this is a 10% tip ", total10)
print ("this is a 20% tip ", total20)
print ("this is a 25% tip ", total25)
print ("this is a 30% tip ", total30)

game1 = input("what was diana's points for game 1:")
game2 = input("what was diana's points for game 2:")
game3 = input("what was diana's points for game 3:")
game4 = input("what was diana's points for game 4:")
game5 = input("what was diana's points for game 5:")

print("diana's average points for five games was: ", (float(game1)+float(game2)+float(game3)+float(game4)+float(game5))/5.0)

hourly = input("how much do you make an hour: ")
hours = input("how many hours did you work this week: ")

print("you made this much this week: ", float(hourly)*float(hours))
