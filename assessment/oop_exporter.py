"""
handle file formats (TXT, CSV, JSON).
"""
import json
import csv
from collections import defaultdict

"""
Class creation for park analysis and the export methods
then we can call in main -> import oop_exporter and use it or import oop_exporter as exporter
"""
class ParkAnalyzer:
    def __init__(self, data):
        """
        init
        """
        self.data = data
        self._aggregated_data = self._aggregate_parks()

    def _aggregate_parks(self):
        """
        joins and process data
        """
        stats = defaultdict(lambda: {
            'total_reviews': 0,
            'positive_reviews': 0,
            'total_rating': 0,
            'locations': set()
        })

        for review in self.data:
            park = review.get('Branch', '').strip()
            rating = review.get('Rating')
            location = review.get('Reviewer_Location', '').strip()

            if park and rating is not None and location:
                stats[park]['total_reviews'] += 1
                stats[park]['total_rating'] += rating
                stats[park]['locations'].add(location)
                if rating >= 4:
                    stats[park]['positive_reviews'] += 1

        result = []
        for park, vals in stats.items():
            avg_score = vals['total_rating'] / vals['total_reviews'] if vals['total_reviews'] > 0 else 0
            result.append({
                'ParkName': park,
                'NumberOfReviews': vals['total_reviews'],
                'NumberOfPositiveReviews': vals['positive_reviews'],
                'AverageReviewScore': round(avg_score, 2),
                'NumberOfUniqueCountries': len(vals['locations'])
            })

        return sorted(result, key=lambda x: x['ParkName'])

    def get_aggregated_data(self):
        """Return park data."""
        return self._aggregated_data

    def export_to_txt(self, filename):
        """Export data."""
        if not filename.lower().endswith('.txt'):
            filename += '.txt'

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("Disneyland Park Report\n")
                f.write("="*40 + "\n\n")
                if not self._aggregated_data:
                    f.write("No data to report.\n")
                    return True

                for park_data in self._aggregated_data:
                    for key, value in park_data.items():
                        f.write(f"{key}: {value}\n")
                    f.write("-" * 30 + "\n")
            return True
        except IOError as e:
            print(f"Error writing file '{filename}': {e}")
            return False

    def export_to_csv(self, filename):
        """Export data to a CSV."""
        if not filename.lower().endswith('.csv'):
            filename += '.csv'

        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['ParkName', 'NumberOfReviews', 'NumberOfPositiveReviews', 'AverageReviewScore', 'NumberOfUniqueCountries']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                if self._aggregated_data:
                    writer.writerows(self._aggregated_data)
            return True
        except IOError as e:
            print(f"Error writing CSV '{filename}': {e}")
            return False

    def export_to_json(self, filename):
        """Export data to a JSON file."""
        if not filename.lower().endswith('.json'):
            filename += '.json'

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self._aggregated_data, f, indent=4)
            return True
        except IOError as e:
            print(f"Error writing JSON '{filename}': {e}")
            return False