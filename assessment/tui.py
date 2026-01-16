"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

def display_title(title):
    """
    Show an string - Title
    count the title length to create the border as required
    """
    border = "-" * len(title)
    print(f"\n{border}")
    print(title)
    print(f"{border}\n")

def check_data(row_count):
    """
    check if the data is loaded and display properly
    """
    print("Dataset finished.")
    print(f"There are {row_count} rows in the dataset.\n")

def display_main_menu():
    """
    show the main menu
    """
    print("Please enter the letter which corresponds with your desired menu choice:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[C] Export Data")
    print("[X] Exit")
    # get the user input, strip extra spaces and set o UPPER to prevent issues
    return input().strip().upper()

def confirm_choice(choice, menu_type):
    """
    confirmt the user's choice
    """
    menus = {
        "main": {
            'A': "View Data",
            'B': "Visualise Data",
            'C': "Export Data",
            'X': "Exit"
        },
        "view_data_submenu": {
            'A': "View Reviews by Park",
            'B': "Number of Reviews by Park and Reviewer Location",
            'C': "Average Score per year by Park",
            'D': "Average Score per Park by Reviewer Location"
        },
        "visualise_data_submenu": {
            'A': "Most Reviewed Parks",
            'B': "Average Scores",
            'C': "Park Ranking by Nationality",
            'D': "Most Popular Month by Park"
        },
        "export_submenu": {
            'T': "Export to Text file (.txt)",
            'C': "Export to CSV file (.csv)",
            'J': "Export to JSON file (.json)"
        }
    }

    if menu_type in menus and choice in menus[menu_type]:
        print(f"You have chosen option {choice} - {menus[menu_type][choice]}\n")
    else:
        display_invalid_choice()

def display_invalid_choice():
    """
    display the error msg for invalid option
    """
    print("Invalid choice. Please try again.\n")

def display_exit_message():
    """
    exit msg
    """
    print("Thanks for using our application !\n")
