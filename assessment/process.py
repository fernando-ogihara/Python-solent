"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv
from collections import defaultdict

def load_data(file_path):
    """
    Load CSV
    Converts 'Rating' to int, 0 if null or invalid
    Returns list and the row count.
    """
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Rating'] = int(row.get('Rating', 0)) if row.get('Rating', '').isdigit() else 0
                data.append(row)
        return data, len(data)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
    return [], 0

def get_reviews_by_park(data, park_name):
    """
    Returns all reviews for a given park (case-insensitive).
    """
    target = park_name.lower().strip()
    return [
        r for r in data
        if r.get('Branch', '').lower().strip() == target
    ]


def get_review_count_by_park_and_location(data, park_name, location):
    """
    Counts how many reviews a park received from a specific location.
    """
    park = park_name.lower().strip()
    loc = location.lower().strip()

    return sum(
        1 for r in data
        if r.get('Branch', '').lower().strip() == park
        and r.get('Reviewer_Location', '').lower().strip() == loc
    )


def get_average_score_by_park_and_year(data, park_name, year):
    """
    Calculates the avg rating for a park in a given year.
    """
    park = park_name.lower().strip()
    total, count = 0, 0

    for r in data:
        # check park and year
        if (
            r.get('Branch', '').lower().strip() == park
            and r.get('Year_Month', '').startswith(year)
        ):
            total += r.get('Rating', 0)
            count += 1

    return total / count if count else None


def get_park_rev(data, park_name):
    """
    Counts the num of reviews per park.
    => highest to lowest.
    """
    counts = defaultdict(int)

    for r in data:
        counts[r.get('Branch', '')] += 1

    return sorted(counts.items(), key=lambda x: x[1], reverse=True)


def get_average_scores_per_park(data):
    """
    calc the avg rating for each park.
    sorted alphabetically by park name.
    """
    scores = defaultdict(lambda: {'total': 0, 'count': 0})

    for r in data:
        scores[r.get('Branch', '')]['total'] += r.get('Rating', 0)
        scores[r.get('Branch', '')]['count'] += 1

    return sorted(
        [
            (park, vals['total'] / vals['count'])
            for park, vals in scores.items()
            if vals['count']
        ],
        key=lambda x: x[0]
    )


def get_top_locations_by_avg_rating_for_park(data, park_name, top_n=10):
    """
    Returns the top N reviewer locations by avg.
    """
    park = park_name.lower().strip()
    scores = defaultdict(lambda: {'total': 0, 'count': 0})

    for r in data:
        if r.get('Branch', '').lower().strip() == park:
            loc = r.get('Reviewer_Location', '').strip()
            scores[loc]['total'] += r.get('Rating', 0)
            scores[loc]['count'] += 1

    averages = [
        (loc, v['total'] / v['count'])
        for loc, v in scores.items()
        if v['count']
    ]

    return sorted(averages, key=lambda x: x[1], reverse=True)[:top_n]


def get_average_rating_by_month_for_park(data, park_name):
    """
    calc the avg per month for a given park.
    Returns a dictionary
    """
    park = park_name.lower().strip()
    month_names = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    monthly = defaultdict(lambda: {'total': 0, 'count': 0})

    for r in data:
        if r.get('Branch', '').lower().strip() == park:
            try:
                month_idx = int(r['Year_Month'].split('-')[1]) - 1
                month = month_names[month_idx]
                monthly[month]['total'] += r.get('Rating', 0)
                monthly[month]['count'] += 1
            except (IndexError, ValueError):
                # ignore badly formatted entries
                continue

    return {
        m: s['total'] / s['count']
        for m, s in monthly.items()
        if s['count']
    }


def get_average_score_per_park_by_location(data):
    """
    calc avg per park
    => rating in descending order.
    """
    results = defaultdict(lambda: defaultdict(lambda: {'total': 0, 'count': 0}))

    for r in data:
        park = r.get('Branch', '').strip()
        loc = r.get('Reviewer_Location', '').strip()
        results[park][loc]['total'] += r.get('Rating', 0)
        results[park][loc]['count'] += 1

    return {
        park: sorted(
            [
                (loc, d['total'] / d['count'])
                for loc, d in locs.items()
                if d['count']
            ],
            key=lambda x: x[1],
            reverse=True
        )
        for park, locs in results.items()
    }