# BRIEF
"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

# IMPORTS
import tui, process, visual

# MAIN PROGRAM JOURNEY
def main():
    """
    Main fn runs the Disneyland Review Analyser application.
    manage the application flow, show the menus, and call/do the required tasks.
    """

    # title
    tui.display_title("Disneyland Review Analyser")

    #read/load csv
    file_path = 'data_source/disneyland_reviews.csv'
    data, row_count = process.load_data(file_path)

    # debugging -> put in tui later
    # print(f"Loaded {row_count} reviews from the data file.\n")

    if data is not None and row_count > 0:
        tui.check_data(row_count)
    else:
        tui.display_error_message(f"Failed to load data from {file_path} or dataset is empty. Exiting.")
        return #Exit
    
    #run the menu while true
    while True:
        #show to the user the main menu and get their choice.
        main_choice = tui.display_main_menu()

        tui.confirm_choice(main_choice, "main")

        #check the user choice
        if main_choice == 'A':
        
            # build view data submenu
            view_data_choice = tui.display_view_data_submenu_and_get_choice()
            tui.confirm_choice(view_data_choice, "view_data_submenu")

            #test options
            if view_data_choice == 'A':
                #reviews by Park
                park_name = tui.get_park_name()
                reviews = process.get_park_rev(data, park_name)
                tui.display_reviews(reviews, park_name)
            elif view_data_choice == 'B':
                #reviews by park and Location
                park_name = tui.get_park_name()
                location = tui.get_location()
                count = process.get_park_and_location(data, park_name, location)
                tui.display_review_count(count, park_name, location)
            elif view_data_choice == 'C':
                #avg per year/park
                park_name = tui.get_park_name()
                year = tui.get_year()
                avg_score = process.get_avg_park_year(data, park_name, year)
                tui.display_avg(avg_score, park_name, year)
            elif view_data_choice == 'D':
                #avg per park by Location
                avg_scores_loc = process.get_avg_park_location(data)
                tui.display_avg_park_location(avg_scores_loc)
            else:
                tui.display_invalid_choice()

        elif main_choice == 'B':

            # build view data submenu
            visualise_data_choice = tui.display_visualise_data_submenu_and_get_choice()
            tui.confirm_choice(visualise_data_choice, "visualise_data_submenu")

            if visualise_data_choice == 'A':
                print("Most Reviewed Parks")
            elif visualise_data_choice == 'B':
                print("Average Scores")
            elif visualise_data_choice == 'C':
                print("Park Ranking by Nationality")
            elif visualise_data_choice == 'D':
                print("Most Popular Month by Park")
            else:
                tui.display_invalid_choice()

        elif main_choice == 'C':
           print("Export Data submenu selected.")

        elif main_choice == 'X':
            #terminate the program
            tui.display_exit_message()
            break #Exit the while loop.
        else:
            #invalid choice.
            tui.display_invalid_choice()


# main() fn called
if __name__ == "__main__":
    main()                     