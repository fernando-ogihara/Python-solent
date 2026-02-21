import matplotlib.pyplot as plt

def run():
    # Create the main figure
    fig = plt.figure(figsize=(10, 8))

    # Create 4 subplots (2 rows, 2 columns)
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    # User input
    n = int(input("Enter number of students: "))

    # Data
    c_s = ([5, 6, 1, 2, 3], [7, 1, 3, 4, 5])  # Coffee vs Sleep data
    ms = {"HP": 5, "Hercules": 3, "Samsung": 4, "iPhone": 2}
    ss = {"Rap": 8, "Pop": 4, "Classical": 2, "Rock": 3}

    # Plot 1: Coffee vs Sleep (scatter plot)
    ax1.plot(c_s[0], c_s[1], "rx")
    ax1.set_xlabel("Coffee intake (cups per day)")
    ax1.set_ylabel("Sleep in hours/night")
    ax1.set_title("Coffee vs Sleep")

    # Plot 2: Mobile brands (pie chart)
    ax2.pie(ms.values(), labels=ms.keys(), autopct="%.f%%")
    ax2.set_title("Mobile brand preference")

    # Plot 3: Music preference (pie chart)
    ax3.pie(ss.values(), labels=ss.keys(), autopct="%1.1f%%")
    ax3.set_title("Music preference")

    # Plot 4: Favourite characters (bar chart)
    ax4.bar(["Mickey Mouse", "Donald Duck", "SpongeBob", "Tom & Jerry"], [6, 10, 4, 8])
    ax4.set_title("Favourite characters")
    ax4.set_ylabel("Number of students")

    # Adjust layout and show the plots
    plt.tight_layout()
    plt.show()

# Run the program
run()