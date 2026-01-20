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
import oop_exporter

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
                # print("Most Reviewed Parks")
                park_counts = process.get_park_review_counts(data)
                if park_counts:
                    labels = [item[0] for item in park_counts]
                    sizes = [item[1] for item in park_counts]
                    visual.plot_pie_chart(labels, sizes, "Num of reviews: ")
                else:
                    tui.display_message("No data available to plot.")
            elif visualise_data_choice == 'B':
                avg_scores = process.get_average_scores_per_park(data)
                if avg_scores:
                    parks = [item[0] for item in avg_scores]
                    scores = [item[1] for item in avg_scores]
                    visual.plot_bar_chart(parks, scores, "AVG Review per Park", "Disneyland Park", "AVG Rating")
                else:
                    tui.display_message("No data available to plot.")
            elif visualise_data_choice == 'C':
                #print("Park Ranking by Nationality")
                park_name = tui.get_park_name()
                top_locations = process.get_top_locations_by_avg_rating_for_park(data, park_name)
                if top_locations:
                    locations = [item[0] for item in top_locations]
                    avg_ratings = [item[1] for item in top_locations]
                    visual.plot_bar_chart(locations, avg_ratings, f"Top 10 for {park_name}", "Reviewer Location", "AVG Rating")
                else:
                    tui.display_message(f"No data found for '{park_name}'.")
            elif visualise_data_choice == 'D':
                #print("Most Popular Month by Park")
                park_name = tui.get_park_name()
                monthly_avg_scores = process.get_month_avg(data, park_name)
                if monthly_avg_scores:
                    months_ordered = ["January", "February", "March", "April", "May", "June",
                                      "July", "August", "September", "October", "November", "December"]
                    scores_in_order = [monthly_avg_scores.get(month, 0) for month in months_ordered]

                    visual.plot_bar_chart(months_ordered, scores_in_order, f"Average Rating per Month for {park_name}", "Month", "Average Rating (out of 5)")
                else:
                    tui.display_message(f"No monthly review data found for '{park_name}'.")
            else:
                tui.display_invalid_choice()

        elif main_choice == 'C':
           #print("Export Data submenu selected.")
            export_choice = tui.display_export_menu_and_get_choice()
            tui.confirm_choice(export_choice, "export_submenu")

            analyzer = oop_exporter.ParkAnalyzer(data)
            aggregated_data = analyzer.get_aggregated_data()

            if not aggregated_data:
                tui.display_error_message("No aggregated data to export. Please ensure data is loaded correctly.")
                continue

            #Get filename from user
            file_name = tui.get_filename_input()

            if export_choice == 'T':
                success = analyzer.export_to_txt(file_name)
            elif export_choice == 'C':
                success = analyzer.export_to_csv(file_name)
            elif export_choice == 'J':
                success = analyzer.export_to_json(file_name)
            else:
                tui.display_invalid_choice()
                return

            if success:
                tui.display_export_success_message(file_name)
            else:
                tui.display_error_message(f"Failed to export data to {file_name}. Please try again.")

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