# Control Flow # REVIEW:
# Great job! We covered a ton of material in this lesson and we’ve increased the number of tools in our Python toolkit by several-fold. Let’s review what we’ve learned this lesson:

# Boolean expressions are statements that can be either True or False
# A boolean variable is a variable that is set to either True or False.
# We can create boolean expressions using relational operators:
# ==: Equals
# !=: Not equals
# >: Greater than
# >=: Greater than or equal to
# <: Less than
# <=: Less than or equal to
# if statements can be used to create control flow in your code.
# else statements can be used to execute code when the conditions of an if statement are not met.
# elif statements can be used to build additional checks into your if statements
# print("I have information for the following planets:\n")

# Assigning numbers to planets
Venus = 1
Mars = 2
Jupiter = 3
Saturn = 4
Uranus = 5
Neptune = 6

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

#inserting Boxer's weight & planet number
weight = 185
planet = 5

# Write an if statement below:
if planet == 1:
    print("Your weight in Venus is", round(weight * 0.91, 2))
elif planet == 2:
    print("Your weight in Mars is", round(weight * 0.38, 2))
elif planet == 3:
    print("Your weight in Jupiter is", round(weight * 2.34, 2))
elif planet == 4:
    print("Your weight in Saturn is", round(weight * 1.06, 2))
elif planet == 5:
    print("Your weight in Uranus is", round(weight * 0.92, 2))
elif planet == 6:
    print("Your weight in Neptune is", round(weight * 1.19, 2))
else:
    print("Not in my Solar System")
