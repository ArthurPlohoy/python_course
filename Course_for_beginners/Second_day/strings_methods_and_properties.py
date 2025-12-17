first_name = "John"
first_two_letters = first_name[:2]
print(first_two_letters)  # Output: Jo
last_letter = first_name[-1]
print(last_letter)  # Output: n

#concatenate strings

new_first_name = first_two_letters + "hnnnn" + last_letter
print(new_first_name)  # Output: Johnnnn

full_name = new_first_name + " Doe"
print(full_name)  # Output: Johnnnn Doe


#multiply strings
repeated_name = first_name * 3
print(repeated_name)  # Output: JohnJohnJohn
print(first_name.upper())  # Output: JOHN
print(first_name.lower())  # Output: john
print(first_name.capitalize())  # Output: John
print(first_name.count("o"))  # Output: 1
print(first_name.replace("o", "a"))  # Output: Jahn
print(first_name.find("h"))  # Output: 2
print(first_name.startswith("J"))  # Output: True