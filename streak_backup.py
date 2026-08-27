import os
import datetime

# Auto commit script to protect GitHub streak
with open("streak_log.txt", "a") as f:
    f.write(f"Updated on: {datetime.datetime.now()}\n")

os.system("git add .")
os.system('git commit -m "daily streak update"')
os.system("git push origin main")