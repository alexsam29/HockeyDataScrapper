import csv


class CSVWriter:
    def __init__(self, file_name, folder_path=""):
        """
        Initializes a CSVWriter object.

        Args:
            file_name (str): The name of the CSV file to write.
            folder_path (str, optional): The folder path where the CSV file will be saved. Defaults to "".

        """
        self.file_name = file_name
        self.folder_path = folder_path

    def write(self, rows):
        """
        Writes the given rows to the CSV file.

        Args:
            rows (list): A list of rows to write to the CSV file.

        """
        save_dest = ""
        if self.folder_path:
            save_dest = self.folder_path + "/" + self.file_name
        else:
            save_dest = self.file_name

        with open(save_dest, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(
                file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            for row in rows:
                writer.writerow(row)
