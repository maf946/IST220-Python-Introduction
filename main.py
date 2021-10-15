def print_x(text_to_print, number_of_times):
    for y in range(number_of_times):
        print(text_to_print)

name = input("What's your name? ")
dreamJob = input(("Hey there, " + name + ". What was your dream job you envisioned when you were a little kid? "))

print_x("Never forget that " + name + " still has time to achieve their dream job: " + dreamJob, 5)
