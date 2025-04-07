import os
import time
questions = [
    ["What is the capital of India?","B",
    ["A- Mumbai", "B- New Delhi", "C- Kolkata", "D- Chennai"],10000],

    ["What is the capital of India?","B",
    ["A- Mumbai", "B- New Delhi", "C- Kolkata", "D- Chennai"],20000],

    ["What is the capital of India?","B",
    ["A- Mumbai", "B- New Delhi", "C- Kolkata", "D- Chennai"],40000],

    ["What is the capital of India?","B",
    ["A- Mumbai", "B- New Delhi", "C- Kolkata", "D- Chennai"],80000]
]

def clear_screen():
    # Clear the screen depending on the OS windows or mac
    # os.system("cls")  # For Windows
  
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For macOS and Linux
        os.system("clear")

# Display questions in screen
for inner_list in questions:
#for i, inner_list in enumerate(questions):B
   print(inner_list[0])
   # print(inner_list[2])
   for options in inner_list[2]:
       print(options)
   correctoptionbyuser=input("Enter your correct option:")
   try:
        if correctoptionbyuser == inner_list[1]:
            print(f"Correct Answer you have won:{inner_list[3]}")
        else:
            print("Wrong Answer you have lost this KBC Competition")
            break
   except ValueError:
       print("Invalid Option Input by the user")
           
    # Pause to let the user see the question
   time.sleep(5)  # Wait 2 seconds
    # Clear the screen before the next iteration
   clear_screen()