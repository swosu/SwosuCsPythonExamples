class Data_Loader:
    def __init__(self):
        self.city_count = 0
        self.df = None
        self.file_name = None

    def load_data(self):
        import pandas as pd
        # Load the data
        self.file_name = str(self.city_count) + '.csv'
        
        file = open(self.file_name, 'r')

        # save the data into a data structure
        self.df = pd.read_csv(file)

        


        