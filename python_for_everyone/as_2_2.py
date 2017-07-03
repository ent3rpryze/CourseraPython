
def week_pay(hours, wage):
    if hours > 40:
        pay = 40*wage + (hours - 40)*(wage*1.5)
    else:
        pay = hours*wage

    return pay

hours = float(input("Enter hours: "))
wage = float(input("Enter your wage per hour: "))

result = week_pay(hours,wage)
print(result)
