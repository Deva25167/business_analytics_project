import pandas as pd


class DataCleaner:
    def __init__(self, input_path):
        self.input_path = input_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.input_path)

        # Clean column names (remove spaces)
        self.df.columns = self.df.columns.str.strip()

        print(" Data loaded successfully")
        print("Columns:", self.df.columns.tolist())

    def remove_duplicates(self):
        self.df.drop_duplicates(inplace=True)
        print(" Duplicates removed")

    def handle_missing_values(self):
        # Fill numeric columns
        for col in self.df.select_dtypes(include=['int64', 'float64']).columns:
            self.df[col].fillna(self.df[col].median(), inplace=True)

        # Fill categorical columns
        for col in self.df.select_dtypes(include=['object']).columns:
            if not self.df[col].mode().empty:
                self.df[col].fillna(self.df[col].mode()[0], inplace=True)
            else:
                self.df[col].fillna("Unknown", inplace=True)

        print(" Missing values handled")

    def fix_data_types(self):
        if 'Date' in self.df.columns:
            self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')

        print(" Data types fixed")

    def create_new_columns(self):

        # Try to find revenue column automatically
        for col in self.df.columns:
            if "amount" in col.lower() or "total" in col.lower():
                self.df.rename(columns={col: "Revenue"}, inplace=True)
                break

        # Date features
        if 'Date' in self.df.columns:
            self.df['Year'] = self.df['Date'].dt.year
            self.df['Month'] = self.df['Date'].dt.month
            self.df['Month_Name'] = self.df['Date'].dt.month_name()

        # Age group
        if 'Age' in self.df.columns:
            self.df['Age Group'] = pd.cut(
                self.df['Age'],
                bins=[0, 18, 30, 45, 60, 100],
                labels=['Teen', 'Young Adult', 'Adult', 'Senior', 'Old']
            )

        print(" New columns created")

    def save_cleaned_data(self, output_path):
        self.df.to_csv(output_path, index=False)
        print(" Cleaned data saved successfully")

    def clean(self, output_path):
        self.load_data()
        self.remove_duplicates()
        self.handle_missing_values()
        self.fix_data_types()
        self.create_new_columns()
        self.save_cleaned_data(output_path)

        return self.df
