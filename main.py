# FitBuddy - Your Personal Fitness Companion

workouts = []
water_intake = 0
meals = []

def log_workout():
    name = input("Enter workout name: ")
    duration = input("Enter duration (mins): ")
    calories = input("Enter calories burned: ")
    workouts.append({"name": name, "duration": duration, "calories": calories})
    print("Workout logged!")

def track_water():
    global water_intake
    water = int(input("Enter water in ml: "))
    water_intake += water
    print(f"Total water: {water_intake} ml")

def log_meal():
    meal = input("Enter meal: ")
    cal = input("Enter calories: ")
    meals.append({"meal": meal, "cal": cal})
    print("Meal logged!")

def suggestions():
    goal = input("Goal (weight loss / muscle gain / fitness): ").lower()
    if "weight loss" in goal:
        print("Suggestion: 30 mins Cardio + 15 mins HIIT")
    elif "muscle" in goal:
        print("Suggestion: Pushups, Squats, Bench Press 4x12")
    else:
        print("Suggestion: 20 mins Yoga + 20 mins Walking")

def show_summary():
    print("\n===== DAILY SUMMARY =====")
    print(f"Workouts: {len(workouts)}")
    for w in workouts:
        print(f"- {w['name']} {w['duration']}mins {w['calories']}cal")
    print(f"Water: {water_intake} ml")
    print(f"Meals: {len(meals)}")

def main():
    while True:
        print("\n=== FitBuddy Menu ===")
        print("1.Log Workout 2.Track Water 3.Log Meal 4.Suggestions 5.Summary 6.Exit")
        choice = input("Enter choice: ")
        if choice == '1': log_workout()
        elif choice == '2': track_water()
        elif choice == '3': log_meal()
        elif choice == '4': suggestions()
        elif choice == '5': show_summary()
        elif choice == '6': break
        else: print("Invalid choice")

if __name__ == "__main__":
    main()
