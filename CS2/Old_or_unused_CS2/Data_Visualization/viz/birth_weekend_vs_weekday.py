import pandas as pd

class BirthsAnalysis:
    def __init__(self, url):
        """Initialize with the dataset URL and load the data."""
        self.url = url
        self.data = None
        self.weekday_avg = None
        self.weekend_avg = None

    def load_data(self):
        """Load the dataset from the provided URL."""
        try:
            self.data = pd.read_csv(self.url)
            print("Data loaded successfully!")
        except Exception as e:
            print(f"Error loading data: {e}")

    def preprocess_data(self):
        """Add a 'category' column to classify days as 'Weekday' or 'Weekend'."""
        if self.data is not None:
            self.data['category'] = self.data['day_of_week'].apply(
                lambda x: 'Weekend' if x in [6, 7] else 'Weekday'
            )
        else:
            print("Data is not loaded. Please load the data first.")

    def analyze(self):
        """Calculate the average births for weekdays and weekends."""
        if self.data is not None:
            self.weekday_avg = self.data[self.data['category'] == 'Weekday']['births'].mean()
            self.weekend_avg = self.data[self.data['category'] == 'Weekend']['births'].mean()
        else:
            print("Data is not loaded. Please load the data first.")

    def report(self):
        """Print the results of the analysis."""
        if self.weekday_avg and self.weekend_avg:
            print(f"Average Weekday Births: {self.weekday_avg:.2f}")
            print(f"Average Weekend Births: {self.weekend_avg:.2f}")

            if self.weekday_avg > self.weekend_avg:
                print("It is more likely that someone is born on a weekday.")
            else:
                print("It is more likely that someone is born on a weekend.")
        else:
            print("Analysis not complete. Please run the analysis.")

# Initialize the class with the dataset URL

#url= "https://raw.githubusercontent.com/fivethirtyeight/data/master/births/births.csv"
#url= "https://github.com/fivethirtyeight/data/blob/master/births/US_births_2000-2014_SSA.csv"
url = "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/births/US_births_2000-2014_SSA.csv"
analysis = BirthsAnalysis(url)

# Execute the steps
analysis.load_data()
analysis.preprocess_data()
analysis.analyze()
analysis.report()
