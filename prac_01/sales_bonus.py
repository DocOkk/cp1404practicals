"""Calculate sales bonuses until a negative sales amount is entered.

Sales below $1,000 earn a 10% bonus; sales of $1,000 or more earn 15%.
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus_rate = 0.10
    else:
        bonus_rate = 0.15
    bonus = sales * bonus_rate
    print(f"Bonus: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
