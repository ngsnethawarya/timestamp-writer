from datetime import datetime

# get current date and time as a string
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# open (or create) a file and add the timestamp
with open("timestamps.log", "a") as f:
    f.write(now + "\n")

print("saved timestamp:", now)
