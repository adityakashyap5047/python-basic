import time
print("\nNow at", time.strftime("\'%H %M %S\'"), end=" ---> ")
hour_time = int(time.strftime("%H"))

if hour_time>=5 and hour_time<12:
    print("good morning, sir !!! ")
elif hour_time>=12 and hour_time<4:
    print("good after noon, sir !!!")
elif hour_time>=4 and hour_time<6:
    print("good evevning, sir !!!")
else:
    print("good night, sir !!!")
print("\n")