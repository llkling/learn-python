weekly_temps = [28, 32, 35, 29, 31, 26, 33]

def analyze_heatwave(temperatures, threshold):
    hot_day_count = 0

    for temp in temperatures:
        if temp >= threshold:
            hot_day_count +=1
    return hot_day_count

result=analyze_heatwave(weekly_temps, 30)

print("Total hot days:", result)