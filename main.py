import time
from replit import clear

end_calculation = False
while not end_calculation:
    print("\33[32mWelcome to the tip calculator.\33[0m\n\nThis calculator will help calculate the tip required to tip the staff at a food establishment.\nWith the help of this calculator for calculating tips, you will be able to calculate the exact tip needed to tip by giving you tips along the way.\n")
    
    total_bill = float(input("What was the total bill? I promise I won't judge your exorbitant spending. $"))
    
    tip = int(input("\nWhat percentage tip would you like to give?\nNot trying to make you look cheap or anything, but please choose 10, 12, or 15. "))
    tip_percentage = tip / 100 + 1
    
    num_people = int(input("\nLastly, how many people, willing or not, are going to split the bill? "))
    
    tip_toPay = (total_bill / num_people) * tip_percentage
    tip_toPay_rounded = round(tip_toPay, 2)
    tip_toPay_rounded = "{:.2f}".format(tip_toPay) # This is the format to get 2 d.p. accuracy, including any "0" behind.
    
    print(f"\nSo to recap on your wise expenditure today: Your total bill is ${total_bill}, plus a percentage tip of {tip}% split among {num_people} people.")
    
    clear()
    
    print("\nCalculating.")
    time.sleep(0.5)
    print("Calculating..")
    time.sleep(0.5)
    print("Calculating...\n")
    time.sleep(0.5)
    
    clear()
    
    print(f"Each person should pay: ${tip_toPay_rounded}.\nPay up!")
    should_continue = input("---\nIs there another bill for me to calculate? Y/N ").lower()
    if should_continue == "y":
        print("\nUgh... Fine. Let me restart this whole program again. ")
        time.sleep(2)
        clear()
        print("Restarting...")
        time.sleep(2)
        clear()
    elif should_continue == "n":
        end_calculation = True
        print("\nFinally I can sleep.")
        time.sleep(1)
        print("\n\33[31m---Shutting down---\33[0m")