import pandas as pd
import sys
class Extract:
    def __init__(self, file_name):
        self.file_name = file_name     
    def get_data(self):
        # check file exists
        try:
            self.df = pd.read_csv(self.file_name)
            return self.df
        except FileNotFoundError:
            print(f"File {self.file_name} not found")
            # Terminal process
            sys.exit(1)   