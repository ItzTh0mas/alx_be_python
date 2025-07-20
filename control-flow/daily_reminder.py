task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        if time_bound == "no":
            print(f"{task} is high priority but not time bound. Keep in mind.")
        elif time_bound == "yes":
            print(f" WARNING: {task} is high priority and time bound. Conclude ASAP")
    case "medium":
        if time_bound == "no":
            print(f"{task} is medium priority and not time bound. Do not forget.")
        elif time_bound == "yes":
            print(f"{task} is time bound and medium priority. Advice start now")
    case "low":
        if time_bound == "no":
            print(f"{task} is low priority. Consider in your free time.")
        elif time_bound  == "yes":
            print(f"{task} is low priority yet time bound. Get it out the way now.")
