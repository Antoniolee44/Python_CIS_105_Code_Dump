import math
# define function to calculate the odds
def calculate_odds(propability):
    return propability / (1 - propability)
    # the formula for odds is: odds = propability / (1 - propability)
propability = float(input("enter the propability of the event (between 0 and 1):"))
#calculate the odds
odds = calculate_odds(propability) 
#print results
print(f"the odds of the event happening are: {odds:.2f} to 1")