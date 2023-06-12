import time

My_time = int(input("Enter Time: "))

for x in range(My_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60)%60
    hours = int(x/3600)%12
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's Over")