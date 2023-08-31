def add_time(start, duration, day = None):

    def split_time(time):
        
        time_obj = {
            "hours": None,
            "minutes": None,
            "time_of_day": None,
        }

        split_time = time.split(":")
        time_obj["hours"] = int(split_time[0])
        
        if "AM" in split_time[1] or "PM" in split_time[1]:
            minutes = split_time[1].split(" ")[0]
            time_of_day = split_time[1].split(" ")[1]

            time_obj["minutes"] = int(minutes)
            time_obj["time_of_day"] = time_of_day
        else:
            time_obj["minutes"] = int(split_time[1])

        return time_obj
    
    start_time_obj = split_time(start)
    duration_time_obj = split_time(duration)

    calculated_time_obj = {
        "hours": start_time_obj["hours"] + duration_time_obj["hours"],
        "minutes": start_time_obj["minutes"] + duration_time_obj["minutes"],
        "time_of_day": start_time_obj["time_of_day"],
        "day": day,
        "days_apart": None
    }
    
    if calculated_time_obj["minutes"] >= 60:
        calculated_time_obj["minutes"] = calculated_time_obj["minutes"] - 60
        calculated_time_obj["hours"] += 1

    twenty_four_hour_format = calculated_time_obj["hours"] % 24

    calculated_time_obj["time_of_day"] = (
        "AM" if twenty_four_hour_format < 12 and calculated_time_obj["time_of_day"] == "AM" else 
        "AM" if twenty_four_hour_format > 11 and calculated_time_obj["time_of_day"] == "PM" else

        "PM" if twenty_four_hour_format < 12 and calculated_time_obj["time_of_day"] == "PM" else
        "PM" if twenty_four_hour_format > 11 and calculated_time_obj["time_of_day"] == "AM" else 
        False
    )
    #calculated_time_obj["hours"] = twenty_four_hour_format

    
    if calculated_time_obj["time_of_day"] == "PM" and calculated_time_obj["hours"] < 24:
        calculated_time_obj["days_apart"] = calculated_time_obj["days_apart"]
    else:
        calculated_time_obj["days_apart"] = round(calculated_time_obj["hours"] / 24)
        
    print(f'{calculated_time_obj["hours"]}:{calculated_time_obj["minutes"]:02d} {calculated_time_obj["time_of_day"]} {calculated_time_obj["days_apart"] if calculated_time_obj["days_apart"] != None else ""}\n')

    # days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    # calculated_time_obj["days_apart"] = (
    #     round(duration_time_obj["hours"] / 24) if duration_time_obj["hours"] > 24 else 
    #     round(duration_time_obj["hours"] / 12) if duration_time_obj["hours"] < 24 else 
    #     1 if round(duration_time_obj["hours"] / 24) == 1 else
    #     calculated_time_obj["days_apart"]
    # )
    
    # if day != None:
    #     if calculated_time_obj["days_apart"] < 1:
    #         calculated_time_obj["day"] = day.capitalize()
    #     else:
    #         day_index = days.index(day.lower())
    #         calculated_day_index = day_index + calculated_time_obj["days_apart"]
    #         calculated_time_obj["day"] = days[calculated_day_index % len(days)].capitalize()
            
    # if calculated_time_obj["hours"] > 12:
    #     calculated_time_obj["hours"] = calculated_time_obj["hours"] - 12

    # for i in calculated_time_obj:
    #     if type(calculated_time_obj[i]) == int:
    #         calculated_time_obj[i] = str(calculated_time_obj[i])
    #         if i == "minutes" and len(calculated_time_obj[i]) < 2:
    #             calculated_time_obj[i] = calculated_time_obj[i].zfill(2)

    # time_format = f'{calculated_time_obj["hours"]}:{calculated_time_obj["minutes"]} {calculated_time_obj["time_of_day"]}'
    
    # time_day_format = f'{calculated_time_obj["hours"]}:{calculated_time_obj["minutes"]} {calculated_time_obj["time_of_day"]}, {calculated_time_obj["day"]}'

    # time_days_apart_format = f'{calculated_time_obj["hours"]}:{calculated_time_obj["minutes"]} {calculated_time_obj["time_of_day"]} {"(" + calculated_time_obj["days_apart"] + " days apart" + ")" if int(calculated_time_obj["days_apart"]) > 1 else "(next day)" if int(calculated_time_obj["days_apart"]) == 1 or (int(calculated_time_obj["days_apart"]) <= 1 and calculated_time_obj["time_of_day"] == "AM") and int(calculated_time_obj["days_apart"]) != 0 else ""}'

    # full_time_format = f'{calculated_time_obj["hours"]}:{calculated_time_obj["minutes"]} {calculated_time_obj["time_of_day"]}, {calculated_time_obj["day"]} {"(" + calculated_time_obj["days_apart"] + " days apart" + ")" if int(calculated_time_obj["days_apart"]) > 1 else "(next day)" if int(calculated_time_obj["days_apart"]) == 1 or (int(calculated_time_obj["days_apart"]) <= 1 and calculated_time_obj["time_of_day"] == "AM") and int(calculated_time_obj["days_apart"]) != 0 else ""}'

    # new_time = (
    #     full_time_format.strip() if calculated_time_obj["day"] != None and calculated_time_obj["days_apart"] != None else
    #     time_day_format.strip() if calculated_time_obj["day"] != None and calculated_time_obj["days_apart"] == None else
    #     time_days_apart_format.strip() if calculated_time_obj["days_apart"] != None and calculated_time_obj["day"] == None else
    #     time_format.strip()
    # )

    # print(new_time, "\n")
    
    
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)