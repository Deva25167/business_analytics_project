from src.data_cleaning import DataCleaner

if __name__ == "__main__":
    input_path = "data/retail_sales_dataset.csv"
    output_path = "data/retail_sales_dataset.csv"

    cleaner = DataCleaner(input_path)
    cleaned_df = cleaner.clean(output_path)

    print("\n  Cleaned Data Preview:")
    print(cleaned_df.head())
