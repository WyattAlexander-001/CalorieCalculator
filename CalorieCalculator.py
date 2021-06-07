'''
Calorie Calculator 

Men
BMR = 66.47 + ( 6.24 × weight in pounds ) + ( 12.7 × height in inches ) − ( 6.755 × age in years )

Women
BMR = 655.1 + ( 4.35 × weight in pounds ) + ( 4.7 × height in inches ) − ( 4.7 × age in years )

'''
def main():
    gender = input("Your Gender, Enter M for Male F for Female:\n").lower()
    
    age = float(input('Your age:\n'))
    height = float(input('Enter Height in Inches:\n'))
    weight = float(input('Enter weight in lbs:\n'))
    
    print('''
    Enter your activty level
    Sedentary = 1.2
    Lightly Activity = 1.3
    Moderately Active= 1.55
    Very Active = 1.725
    Extremely Active = 1.9
    ''')
    
    activity = float(input('Activity Level:\n'))
    
    maleBmr = (66.47 + (6.24 * weight) + (12.7 * height) - (6.755 * age)) * activity
    
    maleBmr = round(maleBmr)
    
    femaleBmr = (655.1 + (4.35 *weight) + (4.7 * height)- (4.7 * age)) * activity
    femaleBmr = round(femaleBmr)
    
    if gender == 'm':
    	print("Your Daily Calorie Needs:")
    	print(f'{maleBmr} Calories')
    	print("Your Weekly Calorie Needs:")
    	print(f'{maleBmr *7} Calories')
    elif gender == 'f':
    	print('Your Daily Calorie Needs:')
    	print(f'{femaleBmr}Calories')
    	print('Your Weekly Calorie Needs:')
    	print(f'{femaleBmr * 7}Calories')
    else:
    	print('You input an incorrect value')
	
   
    x = input('Try again? Type Yes or No:\n\n').lower()
    if x == 'yes':
        main()
    else:
        print('Error')


main()