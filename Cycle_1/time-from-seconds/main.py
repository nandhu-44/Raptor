time = int(input("Enter time in seconds: "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time - (hours * 3600) - (minutes * 60)
print(f"The time is {hours}H {minutes}M {seconds}S")