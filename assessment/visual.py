"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import matplotlib.pyplot as plt

def plot_pie_chart(labels, sizes, title):
    """
    build and display the required chart
    """
    if not sizes or sum(sizes) == 0:
        print("No data.")
        return

    fig, ax = plt.subplots(figsize=(6, 6))

    #percentages
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85
    )
    #style
    plt.setp(autotexts, size=10, weight="bold", color="white")
    plt.setp(texts, size=10, color="black")

    ax.set_title(title, fontsize=14, pad=15)
    ax.axis('equal')
    plt.tight_layout()  #take care to don't overlap
    plt.show()

def plot_bar_chart(x_labels, y_values, title, x_label, y_label):
    """
    build and display the required chart'
    """
    if not y_values or len(x_labels) != len(y_values):
        print("Invalid data.")
        return

    fig, ax = plt.subplots(figsize=(8, 5))

    bars = ax.bar(x_labels, y_values, color='skyblue')

    #set labels and title
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.set_title(title, fontsize=14)

    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.6)  #add lines

    #add labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.05,
                f"{height:.2f}", ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    plt.show()