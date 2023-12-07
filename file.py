import pandas as pd 
import os

# A class for binding the report's general insights
class Reports:
    def __init__(self):

        '''  the init contains the file path to be read   '''
        current_directory = os.getcwd()
        excel_file_path = os.path.join(current_directory,'finacialreport2008.xlsx')
        self.file_dict = None
        self.df = None
        try:
            # Try reading the excel file into a pandas Dataframe
            self.df = pd.read_excel(excel_file_path)
    
            # if sucessful,convert the Dataframe to a dictionary using ('records')
            self.file_dict = self.df.to_dict('records')

        except FileNotFoundError:
            print(f"Error: File '{excel_file_path}' not found.")

        except PermissionError:
            print(f"Error: Permission denied for file '{excel_file_path}'.")

        except pd.errors.ParserError:
            print(f"Error: Unable to parse the Excel file '{excel_file_path}'. Please check the file format.")

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    
    def date(self):
        return self.df['date'].tolist()

    def revenue(self):
        return self.df['revenue'].tolist()

    def expenses(self):
        return self.df['expenses'].tolist()

    def profits(self):
        return self.df['profits'].tolist()



    
        