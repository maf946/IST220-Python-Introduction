# Exploring Basic Python Syntax

Now that our Python scripting environment is set up, we can move on and learn a little bit about what Python can do for us. Specifically, I'd like to go over some material that will help you understand the scripts that you will be provided for Lab 4. Again, you don't need to fully understand them, but I think it would be great if you could; there is no impact to your grade either way. The topics we'll be covering are:

1. Printing
2. Variables
3. Taking user input
4. Functions
5. Looping

Please follow along with the instructions below for each of these five sections.

 ## Printing
 
You can safely delete all of the contents of main.py. In its place, copy and paste in (or re-type) the following, then Run the script, to see how it works.

```Python
# Any line that begins with "#" is a comment, and will not be interpreted

# Printing "Hello, World"

## We have to begin with the O.G.

print("Hello, World!")

## We are using the print() "function," which is built into python. We are saying, I would like to print, and then 
## including what we would like to print within the parentheses. We could also print an integer using the print function:

print(220)

## Each print statement below gets printed to its own line

print("We Are!")
print("Penn State!")

## We can also combine the text we want to print within one line, as below:

print("We Are!" + " Penn State!")

## Note that in the above I've added a space before the "P" so that it will look nice

## Sometimes it's nice to have tabular data, which looks like a table. We can do this using "\t", which is the 
## equivalent of pressing the "Tab" button on your keyboard:

print("Penn State Football Career Leaders in Passing Yards")
print("Player\t\t\t\t\tYards")
print("Sean Clifford\t\t\t10,661")
print("Trace McSorley\t\t\t9,899")
print("Christian Hackenberg\t8,427")
print("Zack Mills\t\t\t\t7,212")
```

## Variables

Again, replace the contents of main.py with the below:

```Python
## Just like in algebra, we can use variables to store different values. For example, consider:

port_number = 84

## This sets the variable called "port_number" to the value 84. We can modify it, such as with:

port_number = port_number - 1

## Now let's see what the current value of port_number is:

print(port_number)
```

## Taking User Input

You know what to do: replace the contents of main.py with the below, then Run and inspect what you see.

```Python
## So far, our programs haven't been interactive at all; they will always execute in exactly the same way
## Often, though, we want to become interactive, such as by taking input from the user. There are lots of ways to 
## take input, such as by noting where a user clicks a mouse or touches a screen, or by taking input over a socket. 
## For now, let's practice taking input via the keyboard:

## Add the line of code below. When you execute it, you will be prompted to enter a number; enter one, then press 
## return/enter.

packet_count = input("Please enter a number of packets: ")
print("You have entered " + packet_count + " as the number of packets.")

## Now we have used a second function, input(). The print() function simply printed out whatever we told it to. 
## The input() function is a little bit different, because it both displays something to the user (here, the prompt for 
## the number of packets), but also "returns" something to us: the number which the user enters. Here, we are taking 
## that returned number and storing it in a variable called packet_count.
```

## Functions

```Python
## Using built-in functions is cool, but you know what's really cool? Creating your own functions. We can do that
## very easily in Python. For example, we might want to create a function that lets you print a certain line of text
## five times in a row. Functions need to have names; for example, the print() function is called "print". Our
## function will need a name, too. Let's call it print_five. Let's begin by "defining" the function, 
## which means writing the code that will be run when somebody wants to use the function. Later,
## we will actually "call" the function, i.e., use it. First, the definition:

def print_five():
    print("TCP/IP")
    print("TCP/IP")
    print("TCP/IP")
    print("TCP/IP")
    print("TCP/IP")

## Note that the "def" keyword tells Python that we are defining a function. Then we name the function, then include
## empty parentheses (more on that later), and then have a colon. On the next line, and this is absolutely critical, 
## we start with a "tab" press on the keyboard. In Python, tabs and lines and spacing have meaning. In this case,
## Python relies on the tabs to help it figure out which lines of code are part of the function, and which are not.
## Often, if you are seeing error messages in your script, it is because you have a problem with indentation.
## More often, it's a simple typo, or you've used the wrong variable or function name.

## OK, with that out of the way, let's actually call print_five():

print_five()

## Pretty simple, right? Whenever the above line of code appears, Python will print "TCP/IP" five times.
## But what if we want to be able to print something other than "TCP/IP"? We can do that by "passing" a value 
## to a function, which we can then use within the function. So, let's make a function similar to print_five()
## which lets us do exactly that:

def print_five_x(what_to_print):
    print(what_to_print)
    print(what_to_print)
    print(what_to_print)
    print(what_to_print)
    print(what_to_print)

## Let's also go ahead and call print_five_x():

print_five_x("IST")

## As you can see, we call print_five_x() and pass it the value "IST". In the definition for print_five_x(), we 
## are passed a variable called what_to_print, which is pre-filled with the value from when the function was
## called, and then we can use it just like we can use any other variable.
```

## Looping

```Python
## To this point, our script is somewhat interactive, but will only run once, top to bottom, and then exit.
## Often we will want to have certain lines or blocks of code execute multiple times. One way to do this is to
## use the "while" loop in Python. Using the while loop, we can have a block of code execute repeatedly until a certain 
## condition is met. For example, let's create a while loop that prompts a user to enter some text, and will
## keep prompting them forever until they enter the text "stop":

user_text = ""

while user_text != "stop":
    user_text = input("Please enter some text; type stop to quit: ")

## Above, we first created a variable called user_text, and set it to be empty. We need to have this variable
## declared for the loop below. Everything that is below "while user_text != "stop":" and indented will run indefinitely, 
## as long as the text the user enters is not equal to "stop". The "!=" operator means "is not equal to."

## Last, but not least, let's combine a few concepts together. Let's create a new funciton that will print out
## the text that a user enters, however many times the user would like. 

def print_text_x(text_to_print, number_of_times):
    for y in range(number_of_times):
        print(text_to_print)
		
## We are using the for() loop here; the details aren't important for our purposes, but you can see that we have now
## "nested" indented code within other indented code. Again, having your indentation match up will be critical.
		
## Let's prompt the user for the text to print, and the number of times to run

text_to_print = input("What text would you like to print? ")
number_of_times = input("How many times would you like to run? ")

## Note that Python treats text and numbers differently. We want to make sure that number_of_times is treated 
## as a number, so we can convert it to its integer form:

number_of_times = int(number_of_times)

## Then, call print_text_x(), passing it both variables

print_text_x(text_to_print, number_of_times)
```

Great job, slugger. Now head on over to Canvas and complete the assignment. 

If you're interested in learning more about Python, I suggest:

* The slides for topic 2.7 
* The [O'Reilly Learning Platform](https://libraries.psu.edu/eresources/psu02110), including:
	* [The Python Crash Course](https://learning.oreilly.com/library/view/python-crash-course/9781492071266/)
	* [The Python Network Programming Cookbook](https://learning.oreilly.com/library/view/python-network-programming/9781786463999/)
* [LinkedIn Learning](https://lnkd.in/eQJ_t26)
	* Specifically, the course [“Learning Python”](https://www.linkedin.com/learning/learning-python/working-with-os-path-utilities?autoAdvance=true&autoSkip=false&autoplay=true&resume=true&u=76811570)

