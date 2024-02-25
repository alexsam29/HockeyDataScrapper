import csv


class CSVWriter:
    def __init__(self, file_name):
        """
        Initializes a CSVWriter object.

        Args:
            file_name (str): The name of the CSV file to write.

        """
        self.file_name = file_name

    def write(self, rows):
        """
        Writes the given rows to the CSV file.

        Args:
            rows (list): A list of rows to write to the CSV file.

        """
        with open(self.file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(
                file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            for row in rows:
                writer.writerow(row)
