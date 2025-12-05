"""print("=== DAILY PERFORMANCE TRACKER ===")

sleep_hours = float(input("Enter sleep hours last night: "))
study_hours = float(input("Enter study hours today: "))
workout_minutes = int(input("Enter workout minutes today: "))
stress_level = int(input("Enter stress level (1-10): "))

print("\n--- DAILY SUMMARY ---")
print(f"Sleep: {sleep_hours} hours")
print(f"Study: {study_hours} hours")
print(f"Workout: {workout_minutes} minutes")
print(f"Stress level: {stress_level} /10")

print("\n--- PERFORMANCE FEEDBACK ---")

if sleep_hours >= 8:
    print(f"{sleep_hours} hours of sleep is great sleep! Your recovery is on point.")
elif sleep_hours >= 6:
    print(f"{sleep_hours} hours of sleep is decent sleep, but more would boost performance.")
else:
    print(f"{sleep_hours} hours of sleep is poor sleep.  This WILL affect your focus and health.")
    
    
if study_hours >= 3:
    print(f"{study_hours} study hours is strong study discipline today.")
elif study_hours >= 1:
    print(f"{study_hours} study hours is a light study day. Try to increase consistency.")
else:
    print("No studying logged. This is a red flag.")
    

if workout_minutes >= 60:
    print(f"{workout_minutes} workout minutes is a great training session.")
elif workout_minutes >= 30:
    print(f"{workout_minutes} workout minutes is a moderate workout. Still counts.")
else:
    print(f"{workout_minutes} workout minutes is very little movement today.  Your body needs work.")
    
    
if stress_level <= 3:
    print("Low stress. Mentally strong day.")
elif stress_level <= 6:
    print("Moderate stress. Be mindful tomorrow.")
else:
    print("High stress. You need recovery and balance.")"""
    
    












print("===MULTI-DAY PERFORMANCE TRACKER ===")

sleep_data = []
study_data = []
workout_data = []
stress_data = []

days = int(input("How many days do you want to log? "))

for day in range(1, days + 1):
    print(f"--- Day {day} ---")
    
    sleep = float(input("Enter sleep hours: "))
    study = float(input("Enter study hours: "))
    workout = int(input("Enter workout minutes: "))
    stress = int(input("Enter stress level (1-10): "))
    
    sleep_data.append(sleep) #the variable sleep gets added (appended) to the sleep_data list
    study_data.append(study)
    workout_data.append(workout)
    stress_data.append(stress)
    
avg_sleep = sum(sleep_data) / len(sleep_data)
avg_study = sum(study_data) / len(study_data)
avg_workout = sum(workout_data) / len(workout_data)
avg_stress = sum(stress_data) / len(stress_data)

print("\n=== WEEKLY PERFORMANCE SUMMARY")
print(f"Average Sleep: {avg_sleep:.2f} hours")
print(f"Average Study: {avg_study:.2f} hours")
print(f"Average Workout: {avg_workout:.2f} minutes")
print(f"Average Stress: {avg_stress:.2f} /10")


    
    
print("\n--- PERFORMANCE FEEDBACK ---")

if avg_sleep >= 8:
    print(f"Excellent recovery this week.")
elif avg_sleep >= 6:
    print(f"Solid sleep, but there's room to improve.")
else:
    print(f"Chronic sleep debt detected")
    
    
if avg_study >= 3:
    print(f"Strong academic discipline this week.")
elif avg_study >= 1:
    print(f"Light studying overall. Lock in harder.")
else:
    print("Major academic underperformance")
    

if avg_workout >= 60:
    print(f"Elite training volume.")
elif avg_workout >= 30:
    print(f"Moderate physical activity")
else:
    print(f"Training volume too low")
    
    
if avg_stress <= 3:
    print("Mental state is under control")
elif avg_stress <= 6:
    print("Stress is moderate. Manage it")
else:
    print("High stress risk detected.")

with open("weekly.report.txt", "w") as file:
    file.write("=== WEEKLY PERFORMANCE SUMMARY ===\n")
    file.write(f"Average Sleep: {avg_sleep:.2f} hours\n")
    file.write(f"Averge Study: {avg_study:.2f} hours\n")
    file.write(f"Average Workout: {avg_workout:.2f} minutes\n")
    file.write(f"Average Stress: {avg_stress:.2f} /10\n\n")
    
    file.write("=== WEEKLY PERFORMANCE FEEDBACK ===\n")
    
    if avg_sleep >= 8:
        file.write("Excellent recovery this week.\n")
    elif avg_sleep >= 6:
        file.write("Solid sleep, but there's room to improve.\n")
    else:
        file.write("Chronic sleep debt detected.\n")
    
    
    if avg_study >= 3:
        file.write("Strong academic discipline this week.\n")
    elif avg_study >= 1:
        file.write("Light studying overall. Lock in harder.\n")
    else:
        file.write("Major academic underperformance.\n")
    

    if avg_workout >= 60:
        file.write("Elite training volume.\n")
    elif avg_workout >= 30:
        file.write("Moderate physical activity\n")
    else:
        file.write("Training volume too low\n")
    
    
    if avg_stress <= 3:
        file.write("Mental state is under control\n")
    elif avg_stress <= 6:
        file.write("Stress is moderate. Manage it\n")
    else:
        file.write("High stress risk detected.\n")

print("\n Weekly report saved to 'weekly_report.txt'")
    
    