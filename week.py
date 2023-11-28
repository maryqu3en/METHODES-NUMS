week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]



weekdays = week[:6]
print("the weekdays: ", weekdays)
weekends = week[5:]
print("the weekends: ", weekends)

print("the weekdays: ")
for day in range(5): 
    print(week[day])


print("the weekends: ")
for day in range(5, 7): 
    print(week[day])