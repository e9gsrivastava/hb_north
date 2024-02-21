
"""
find the most recent data based on the minimum sequence
"""
import csv

def get_most_recent_data(file_path):
    """
    find the most recent data based on the minimum sequence
    number for each unique combination of "node," "fordate," and "shape" from the csv file.
    """
    most_recent_data = {}

    with open(file_path, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for entry in reader:
            entry["sequence"] = int(entry["sequence"])

            key = (entry["node"], entry["fordate"], entry["shape"])

            current_sequence = most_recent_data.get(key, {}).get("sequence", float("inf"))

            if entry["sequence"] < current_sequence:
                most_recent_data[key] = entry

    result = sorted(most_recent_data.values(), key=lambda x: x["fordate"])
    return result


def write_most_recent_data_to_csv(data, output_file_path):
    """
    write the result to a csv file
    """
    fieldnames = data[0].keys()
    with open(output_file_path, "w", newline="", encoding="utf-8") as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    CSVFILEPATH = "HB_NORTH_CRR.csv"
    OUTPUTCSVPATH = "most_recent_data_sorted.csv"

    most_recent_data_from_csv = get_most_recent_data(CSVFILEPATH)

    write_most_recent_data_to_csv(most_recent_data_from_csv, OUTPUTCSVPATH)
