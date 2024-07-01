import csv
import openpyxl


def read_prototypes_from_header_file(filename):

    with open(filename, "r") as file:
        file_lines = file.readlines()

    prototypes = []
    for ID, prototype in enumerate(file_lines, start=1):
        prototype = prototype.rstrip("\n")
        prototype_dict = {"Function Prototype": prototype, "Unique ID": f"IDX{ID:03}"}
        prototypes.append(prototype_dict)

    return prototypes


def write_csv(prototypes, file_path):
    with open(file_path, "w", newline="\n") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(prototypes[0].keys())
        for dic in prototypes:
            writer.writerow(dic.values())


def write_excel(prototypes, file_path):
    workbook = openpyxl.Workbook()
    new_sheet = workbook.create_sheet(title="newSheet")

    # Remove the default sheet
    default_sheet = workbook["Sheet"]
    workbook.remove(default_sheet)

    # Write the header row
    header = list(prototypes[0].keys())
    new_sheet.append(header)

    # Write data rows
    for dic in prototypes:
        new_sheet.append(list(dic.values()))

    # Save the workbook
    workbook.save(file_path)


def main():
    # File paths
    header_file_path = "header_file.h"
    csv_output_path = "output.csv"
    excel_output_path = "prototypes.xlsx"

    prototypes = read_prototypes_from_header_file(header_file_path)

    # Write to CSV
    write_csv(prototypes, csv_output_path)

    # Write to Excel
    write_excel(prototypes, excel_output_path)


if __name__ == "__main__":
    main()
