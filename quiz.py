print("Hello,Contosoville!")
# This is a comment that won't be interpreted as a command

# Use a variable named year to "remembar" the value 1990
year = 1990

print(f"The yesr is {year}...")

year = year +36

# print a message to see what year is now
print(f"The year is now {year}")

# if we're in 1990
if year == 1990:
    print("I left you a message on your answering machine!")
# if we'ew in 2026
if year == 2026:
    print("I sent you a text message!")


# ask the candidata a question
activity = input( "How would you like to spend your evening ?\n(A) Reding a book\n(B) Attending a party\n")

# print out which activity they chose
print( f"You chose {activity}")

# if they chose reading a book
if activity == "A":
    print("Nice choice!")
