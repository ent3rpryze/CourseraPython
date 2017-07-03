
score = float(input("Enter Score: "))
if score < 0.60:
    print ('F')
elif score < 0.70:
    print ('D')
elif score < 0.80:
    print ('C')
elif score < 0.90:
    print ('B')
elif score <= 1.00:
    print ('A')
else:
    print("You've entered an invalid score.")
    exit()
