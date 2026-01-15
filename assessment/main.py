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

    # debugging
    print(f"Loaded {row_count} reviews from the data file.\n")

# main() fn called
if __name__ == "__main__":
    main()                     