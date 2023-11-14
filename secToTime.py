seconds = int(input("enter number of seconds: "))
hours = 0
minutes = 0
# METHOD 1
# while seconds>59:
#     seconds -=60
#     minutes +=1
# while minutes>59:
#     minutes-=60
#     hours+=1

# METHOD 2
minutes = seconds // 60
seconds %= 60
hours = minutes // 60
minutes %= 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
