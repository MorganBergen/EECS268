'''
@file		outbreak.py
@author		Morgan Bergen
@date		March 28 2022
@brief		Exercise 2:  Outbreak Returns
			Flu season is upon us and the number of people getting sick is growing.
			On day 1, there was only 6 people had the flu
			On day 2, it jumped to 20.
			On day 3, there were 75
			Every day since, the number of people who have the flu is equal to the last 3 days combined
			You will make a program that will ask the user for what day they want a count of people with the flu for. Then display the amount. You must use recursion to solve the calculation of infected for a given day. Assume the user will input a valid day.

day 1 = 6 people
day 2 = 20 people
day 3 = 75 people
day 4 = ((4 - 1) people + (4 - 2) people + (4 - 3) people)
day n = ((n - 1) + (n - 2) + (n - 3)) people
'''


# HELLO IM GOING TO PUSH THIS NEW CHANGE
# HELLO IM GOING TO PUSH THIS NEW CHANGE 2.0

def main():
    print("OUTBREAK!")
    days = input("What day do you want a sick count for?: ")
    if int(days) == 0:
        print("Invalid day")
    else:
        print(f"Total people with flu: ", end="")
        print(outbreak(int(days)))


def outbreak(days):
    if days == 0:  # base_case_0
        return (0)
    elif days == 1:  # base_case_1
        return (6)
    elif days == 2:  # base_case_2
        return (20)
    elif days == 3:  # base_case_3
        return (75)
    else:
        # recursive_case(recursive solution)
        return outbreak(days - 1) + outbreak(days - 2) + outbreak(days - 3)


main()
