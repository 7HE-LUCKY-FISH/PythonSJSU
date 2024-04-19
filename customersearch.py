import csv
from collections import defaultdict

def count_city_occurrences(file_path):
    city_occurrences = defaultdict(int)
    city_index = None  # This will be used to find the index of the 'City' column

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csvFile = csv.reader(file)
        headers = next(csvFile) 
        if 'City' in headers:
            city_index = headers.index('City')
        else:
            raise ValueError("CSV file does not contain 'City' column")
        for row in csvFile:
            if city_index is not None and city_index < len(row):
                city = row[city_index]
                city_occurrences[city] += 1
    return city_occurrences
 

def print_city_occurrences(occurrences):
    print("City Occurrences in the CSV:")
    for city, count in occurrences.items():
        print(f"{city}: {count}")


if __name__ == "__main__":
    file_path = r'C:\Users\bryan\Videos\VS stash\.vscode\Python\customers-100.csv'  # Make sure to update this path to where your file is located
    occurrences = count_city_occurrences(file_path)
    print_city_occurrences(occurrences)
