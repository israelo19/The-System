import time, sys, os, getpass, random
from InquirerPy import inquirer
from art import text2art

#The standard
print(text2art("The  System.", font="standard"))
#getting the username
username = getpass.getuser()
#selection system
choice = inquirer.select(
    message="Welcome {}".format(username),
    choices=[
        "[1] Access The System",
        "[2] Exit"
    ],
).execute()

# choice 1 or choice 2
if choice == "[1] Access The System":
    print("Accessing The System...")
    time.sleep(1)
    # print("Please wait...")
    time.sleep(1)

# first progress bar
rfloat = random.random()
def progress(total=50, delay=0.05):
    for i in range(total + 1):
        filled = int(30 * i / total)
        bar = "[" + "#" * filled + "-" * (30 - filled) + "]"
        percent = int(100 * i / total)
        sys.stdout.write(f"\r{bar} {percent:3d}%")
        sys.stdout.flush()
        time.sleep(rfloat)
    print()  # newline
progress(5, rfloat)
time.sleep(0.5)
os.system("clear")

# what I want it to do :
# ask for password and if incorrect, display incorrect password and ask for password again on clear screen
pass_correct = False
# print(f'Enter Password: ', end= '')
print(f'\rEnter Password: ', end= '')
while pass_correct == False:    
    password = input()
    if password == 'abc':
        pass_correct = True
    else:
        print('Incorrect Password')
        time.sleep(0.4)
        os.system("clear")
        print(f'Enter Password: ', end='')
progress(10, rfloat)
time.sleep(1)
os.system("clear")
time.sleep(0.5)
print(text2art("Welcome.", font="cybersmall"))


if choice == "[2] Exit":
    print("Exiting...")
    time.sleep(1)
    sys.exit()



# import base64

# encoded = base64.b64encode(b'Hello World!')
# print(encoded)

# x = 0
# while x < 5:
#     # time.sleep(5)
#     # print("...")
#     sys.stdout.write(".")
#     time.sleep(1)
#     sys.stdout.flush()
#     x += 1


print('Access Granted')

# from time import sleep
# import random
# from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
# rfloat = random.random()
# print(rfloat)

# with Progress(
#     SpinnerColumn(),
#     TextColumn("[bold]Initializing[/]"),
#     BarColumn(),
#     TextColumn("{task.percentage:>3.0f}%"),
#     TimeElapsedColumn(),
# ) as progress:
#     task = progress.add_task("main", total=25)
#     for _ in range(100):
#         sleep(rfloat)
#         progress.update(task, advance=1)


# import sys, time, random
# rfloat = random.random()
# print(rfloat)

# def progress(total=50, delay=0.05):
#     for i in range(total + 1):
#         filled = int(30 * i / total)
#         bar = "[" + "#" * filled + "-" * (30 - filled) + "]"
#         percent = int(100 * i / total)
#         sys.stdout.write(f"\r{bar} {percent:3d}%")
#         sys.stdout.flush()
#         time.sleep(rfloat)
#     print()  # newline

# print("Authenticating...")
# progress()
# print("Access granted.")
