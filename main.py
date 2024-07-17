import csv
import json
import argparse

def csv_to_json(csv_file, json_file):
    insights = []

    # Open the CSV file
    with open(csv_file, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        
        # Iterate through each row in the CSV
        for row in csv_reader:
            # Split tags by ';' and remove any leading/trailing whitespace, and filter out empty tags
            tags = [tag.strip() for tag in row['TAGS'].split(';') if tag.strip()]
            headline = row['HEADLINE'].strip()
            explanation = row['EXPLANATION'].strip()
            source = row['SOURCE'].strip()
            
            # Create insight dictionary
            insight = {
                'tags': tags,
                'headline': headline,
                'explanation': explanation,
                'source': source
            }
            
            # Add insight to insights list
            insights.append(insight)
    
    # Write insights list to JSON file
    with open(json_file, mode='w', encoding='utf-8') as json_out_file:
        json.dump(insights, json_out_file, indent=2, ensure_ascii=False)
    
    print(f'JSON file "{json_file}" created successfully.')

def main():
    parser = argparse.ArgumentParser(description='Convert CSV to JSON')
    parser.add_argument('csv_file', help='Path to the input CSV file')
    parser.add_argument('json_file', help='Path to the output JSON file')
    
    args = parser.parse_args()
    
    csv_to_json(args.csv_file, args.json_file)

if __name__ == '__main__':
    main()
