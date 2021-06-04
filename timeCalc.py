print ("Welcome to simple time calculator!!!\n")
min1 = int(input("Enter 1st minutes: "))
hr1 = int(input("Enter 1st hours: "))
day1 = int(input("Enter 1st days: "))
print()
min2 = int(input("Enter 2st minutes: "))
hr2 = int(input("Enter 2st hours: "))
day2 = int(input("Enter 2st days: "))
print()

minw = min1 + min2
hrw = hr1 + hr2
dayw = day1 + day2

while (minw > 60):
    minw = minw - 60
    hrw = hrw + 1

while (hrw > 24):
    hrw = hrw - 24
    dayw = dayw + 1

print ("Driver has been driving for:")
print (minw, "minutes")
print (hrw, "hours")
print (dayw, "days")
