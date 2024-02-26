class Table:
    def __init__(self, page):
        """
        Initializes a Table object.

        Parameters:
        - page: BeautifulSoup object representing the HTML page containing the table.
        """
        self.page = page

    def getRows(self):
        """
        Retrieves the rows of the table.

        Returns:
        - List of lists representing the rows of the table.
        """
        stats_table_header = self.page.find_all(name="thead")
        stats_table_header_rows = stats_table_header[0].find_all(name="tr")
        stats_table = self.page.find_all(name="tbody")
        stats_table_rows = stats_table[0].find_all(name="tr")
        header_row = []
        for data in stats_table_header_rows[1].find_all(name="th"):
            if not data.text == "Rk":
                header_row.append(data.text)

        rows = [header_row]
        for row in stats_table_rows:
            data_row = []
            for data in row.find_all(name="td"):
                data_row.append(data.text)
            if data_row:
                rows.append(data_row)
        
        return rows
