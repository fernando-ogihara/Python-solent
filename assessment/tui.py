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
    error msg
    """
    print("Invalid choice. Please try again.\n")

def display_exit_message():
    """
    exit msg
    """
    print("Thanks for using our application !\n")

def display_view_data_submenu_and_get_choice():
    """
    Displays the 'View Data' submenu options and prompts for user choice.
    Returns:
        str: The user's submenu choice as an uppercase string.
    """
    print("Please enter one of the following options:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per year by Park")
    print("[D] Average Score per Park by Reviewer Location")
    return input().strip().upper()

def display_visualise_data_submenu_and_get_choice():
    """
    Displays the 'Visualise Data' submenu options and prompts for user choice.
    Returns:
        str: The user's submenu choice as an uppercase string.
    """
    print("Please enter one of the following options:")
    print("[A] Most Reviewed Parks")
    print("[B] Average Scores")
    print("[C] Park Ranking by Nationality")
    print("[D] Most Popular Month by Park")
    return input().strip().upper()

def get_park_name():
    """
    asks the user the park name
    """
    return input("Enter the Disneyland park name (e.g., 'Disneyland_Paris'): ").strip()

def get_location():
    """
    asks the user the location
    """
    return input("Enter the reviewer's location (e.g., 'United States'): ").strip()

def get_year():
    """
    asks the user the year
    """
    while True:
        year = input("Enter the year (e.g., '2019'): ").strip()
        if year.isdigit() and len(year) == 4:
            return year
        print("Invalid format. Please enter a 4-digit year - YYYY.")

def display_reviews(reviews, park_name):
    """
    shows the reviews for a specific park
    """
    if not reviews:
        print(f"No reviews found for '{park_name}'. Please check the park name.\n")
        return

    print(f"\n--- Reviews for {park_name} ({len(reviews)} reviews) ---")
    for i, review in enumerate(reviews, start=1):
        print(f"Review {i}:")
        print(f"  Rating: {review.get('Rating', 'N/A')}/5")
        print(f"  Date: {review.get('Year_Month', 'N/A')}")
        print(f"  Location: {review.get('Reviewer_Location', 'N/A')}")
        print("-" * 20)
    print("------------------------------------------\n")

def display_review_count(count, park_name, location):
    """
    shows the num of reviews for a specifica park and location
    """
    print(f"\n'{park_name}' received {count} reviews from '{location}'.\n")
    if count == 0:
        print("Check if the data entered is typed correctly.\n")

def display_avg(avg_score, park_name, year):
    """
    shows the avg for a specifiv park/year
    """
    if avg_score is not None:
        print(f"\nThe average rating for '{park_name}' in {year} is: {avg_score:.2f}/5\n")
    else:
        print(f"No reviews found for '{park_name}' in {year}.\n")

def display_avg_park_location(park_avg_scores_by_location):
    """
    shows the avg per park/location
    """
    if not park_avg_scores_by_location:
        print("No average available.\n")
        return

    print("\n--- Average Scores per Park by Reviewer Location ---")
    for park, scores in park_avg_scores_by_location.items():
        print(f"\nPark: {park}")
        if not scores:
            print("  No data available.")
            continue
        #Sort locations by descending
        for location, avg in sorted(scores, key=lambda x: x[1], reverse=True):
            print(f"  - {location}: {avg:.2f}/5")
    print("--------------------------------------------------\n")

