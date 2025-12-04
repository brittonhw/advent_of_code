# file for input ingestion

def read_file(file_name):
    with open(file_name, 'r') as file:
        rows = file.readlines()
        rows = [row.strip() for row in rows]
        return rows
            

