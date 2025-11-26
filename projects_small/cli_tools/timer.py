import time

print("Simple Timer")
seconds = int(input("Enter number of seconds: "))

for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)

print("Time’s up!")
