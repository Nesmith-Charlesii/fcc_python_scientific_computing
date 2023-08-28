def add_time(start_time, duration, day = None):
    
    def split_time(time):
        time_obj = {
            "hour": None,
            "minute": None,
            "time_of_day": None,
        }

        split_time = time.split(":")
        time_obj["hour"] = int(split_time[0])
        
        if "AM" in split_time[1] or "PM" in split_time[1]:
            minutes = split_time[1].split(" ")[0]
            time_of_day = split_time[1].split(" ")[1]

            time_obj["minute"] = int(minutes)
            time_obj["time_of_day"] = time_of_day
        else:
            time_obj["minute"] = int(split_time[1])

        return time_obj
        
    start_time_obj = split_time(start_time)
    duration_time_obj = split_time(duration)

    calculated_time = {
        "hours": (start_time_obj["hour"] + duration_time_obj["hour"]),
        "minutes": (start_time_obj["minute"] + duration_time_obj["minute"]),
        "time_of_day": start_time_obj["time_of_day"],
        "days_apart": "",
        "day": day if day != None else ""
    }
    given_time_of_day = calculated_time["time_of_day"]
    
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    
    if calculated_time["minutes"] >= 60:
        calculated_time["minutes"] = calculated_time["minutes"] - 60
        calculated_time["hours"] = calculated_time["hours"] + 1
    if calculated_time["hours"] >= 12:

        calculated_time["hours"] = calculated_time["hours"] % 12
        calculated_time["hours"] = (
            12 if calculated_time["hours"] == 24 else 
            12 if calculated_time["hours"] == 0 else
            calculated_time["hours"]
        )
        calculated_time["time_of_day"] = (
            "AM" if calculated_time["time_of_day"] == "PM" else
            "PM"
        )
        
        if given_time_of_day == "AM" and calculated_time["time_of_day"] == "PM":
            if day != None: calculated_time["day"] = day.lower().capitalize()
        elif given_time_of_day == "PM" and calculated_time["time_of_day"] == "AM":
            if day != None:
                day_index = days.index(day.lower())
                calculated_time["day"] = days[day_index + (round(duration_time_obj["hour"] / 24) + 1)].capitalize()

                calculated_time["days_apart"] = (
                    f'({(24 // calculated_time["hours"])} days later)' if 24 // calculated_time["hours"] > 1 else
                    f'(next day)' if 24 // calculated_time["hours"] <= 1 else
                    calculated_time["days_apart"]
                )
            elif day == None:
                calculated_time["days_apart"] = (
                    f'({round(duration_time_obj["hour"] / 24)} days later)' if round(duration_time_obj["hour"] / 24) > 1 else
                    f'(next day)' if round(duration_time_obj["hour"] / 24) <= 1 else
                    calculated_time["days_apart"]
                )

    print(f'{calculated_time["hours"]}:{calculated_time["minutes"]:02d} {calculated_time["time_of_day"]}{", " + calculated_time["day"] if calculated_time["day"] != "" else ""} {calculated_time["days_apart"] if calculated_time["days_apart"] != "" else ""}\n')
    
#add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

#add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

#add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

#add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

#add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

#add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)

add_time("11:55 AM", "3:12")
add_time("8:16 PM", "466:02")
add_time("9:15 PM", "5:30")
add_time("5:01 AM", "0:00")
add_time("11:40 AM", "0:25")
add_time("3:30 PM", "2:12")