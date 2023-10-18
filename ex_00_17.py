# Boolean operators: OR
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
statement_one = True
statement_two = (9 + 5 <= 15) or (7 != 4 + 3)
statement_two = True

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements")

# you can't do the following
print(gpa == 2.5 or 2.0 or 1.5)
