#input is 100
#After 6 hours: 50.00 mg
#six_hours=caffeine_mg/2
#After 12 hours: 25.00 mg
#After 24 hours: 6.25 mg
#caffeine_mg = float(input())
caffeine_mg = float(input("Caffeine Amount: "))
six_hours=caffeine_mg/2
twelve_hours=six_hours/2
twenty_four_hours=twelve_hours/4

print("After 6 hours:{:.2f}mg". format(caffeine_mg/2.0))
print("After 12 hours:{:.2f}mg". format(six_hours/2.0))
print("After 24 hours:{:.2f}mg". format(twelve_hours/4.0))
