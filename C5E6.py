#CAlories from Fat and Carbohydrates
def calculate_calories(fat_grams, carb_grams):
    calories_from_fat = fat_grams * 9
    calories_from_carbs = carb_grams * 4
    return calories_from_fat, calories_from_carbs

fat_input = float(input("Enter the number of fat grams consumed in a day: "))
carb_input = float(input("Enter the number of carbohydrate grams consumed in a day: "))

fat_calories, carb_calories = calculate_calories(fat_input, carb_input)

print(f"Calories from fat: {fat_calories:.2f} calories")
print(f"Calories from carbs: {carb_calories:.2f} calories")
