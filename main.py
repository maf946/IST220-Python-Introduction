def print_x(text_to_print, number_of_times):
    for y in range(number_of_times):
        print(text_to_print)

name = input("What's your name? ")
print_x("That's one small step for man, one giant leap for " + name + ".", 5)
