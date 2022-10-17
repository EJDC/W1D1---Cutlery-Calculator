# function to check if input is actually yes or no
def check(word):
    if word.lower() == 'yes' or word.lower() == 'y':
        return (True)
    elif word.lower() == 'no' or word.lower() == 'n':
        return (False)
    else:
        print('You need to answer yes or no to the questions.  Please try again.')
        exit()

#Begins...
print('Welcome to Cutlery Calculator!')

# some loops that demand the user input an integer for number of courses and diners
try:
    courses = int(input('How many courses are there?\n'))
except ValueError:
    print("Number of courses must be an integer please!")
    exit()

try:
    diners = int(input('How many diners are there?\n'))
except ValueError:
    print("Number of diners must be an integer please!")
    exit()

# initate variables
reg_knives = diners * courses
reg_forks = diners * courses

# soup is -1 fork and +1 butter knife and +1 soup spoon
# asks user if there is soup, checks answer via check function, initates variables.
soup = input('Is the starter a soup?\n')
soup = check(soup)
soup_spoons = 0
butter_knife = 0
# if there is soup, does maths.
if soup:
    reg_forks = reg_forks - diners
    soup_spoons =+ 1 * diners
    butter_knife =+ 1 * diners

# pudding is -1 reg knife and +1 dessert spoon
# asks user if there is pudding, checks answer via check function, initates variables.
pudding = input('Is the final course pudding?\n')
pudding = check(pudding)
des_spoons = 0
if pudding:
    reg_knives = reg_knives - diners
    des_spoons =+ 1 * diners

#  fish is -1 reg fork, +1 fish fork
# asks user if there is fish, checks answer via check function, initates variables.
fish = input('Is one of the courses fish?\n')
fish = check(fish)
fish_forks = 0
if fish:
    reg_forks = reg_forks - diners
    fish_forks =+ 1 * diners


# prints output
print()
print("You'll Need:")
if reg_knives != 0:
    print(f"Knives:  {reg_knives}")
if reg_forks != 0:
    print(f"Forks:  {reg_forks}")
if soup_spoons != 0:
    print(f"Soup Spoons: {soup_spoons}")
if butter_knife != 0:
    print(f"Butter Knives: {butter_knife}")
if des_spoons != 0:
    print(f"Dessert Spoons: {des_spoons}")
if fish_forks != 0:
    print(f"Fish Forks: {fish_forks}")

print()

if pudding == False:
    print("What no pudding??")
    print()