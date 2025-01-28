def washing_machine_time(weight, waterlevel):
  
    if weight < 0:
        return "INVALID INPUT"
    if weight > 7000:
        return "OVERLOADED"
    if weight == 0:
        return 0  
    if water_level == "low":
        if 0 < weight <= 2000:
            return 25
        else:
            return "INVALID INPUT"
    elif water_level == "medium":
        if 2001 <= weight <= 4000:
            return 35
        else:
            return "INVALID INPUT" 
    elif water_level == "high":
        if weight > 4000:
            return 45
        else:
            return "INVALID INPUT"   
    else:
        return "INVALID INPUT"
weight = int(input("Enter the weight of clothes in grams: "))
waterlevel = input("Enter the water level (low, medium, high): ")
timeneeded = washing_machine_time(weight, waterlevel)
print("Time needed:", timeneeded)
