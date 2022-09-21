#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.\nThis calculator will help calculate the tip required to tip the staff at a food establishment.\nWith the help of this calculator for calculating tips, you will be able to calculate the exact tip needed to tip by giving you tips along the way.\n")

total_bill = float(input("Firstly, without being judgmental, what was the total bill? $"))

tip = int(input("\nWhat percentage tip would you like to give?\nNot trying to make you look cheap or anything, but please choose 10, 12, or 15. "))
tip_percentage = tip / 100 + 1

num_people = int(input("\nLastly, how many people, willing or not, are going to split the bill? "))

tip_toPay = (total_bill / num_people) * tip_percentage
tip_toPay_rounded = round(tip_toPay, 2)
tip_toPay_rounded = "{:.2f}".format(tip_toPay) # This is the format to get 2 d.p. accuracy, including any "0" behind.

print(f"\nSo to recap on your wise expenditure today: Your total bill is ${total_bill}, plus a percentage tip of {tip}% split among {num_people} people.")

print("\nCalculating.")
print("Calculating..")
print("Calculating...\n")

print(f"Each person should pay: ${tip_toPay_rounded}.\nPay up!")
