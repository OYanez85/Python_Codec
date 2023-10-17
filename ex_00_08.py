# modifying strings
string_one = "Hello, "
string_two = "World! "
combo = string_one + string_two

print(combo)
# Output: Hello, World!

new_combo = combo * 2

print(new_combo)
# Output: Hello, World! Hello, World!

if "World" in new_combo:
  print("It's here!")
  # Output: It's here!
