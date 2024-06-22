import pandas as pd
import os
from fastapi import APIRouter
router = APIRouter()

@router.get("/readCsvFile")
def read_netflix_titles():
    try:
        # Adjust the file path as necessary
        file_path = os.path.join(os.path.dirname(__file__), 'netflix_titles.csv')
        # Read the CSV file with a specified encoding
        df = pd.read_csv(file_path, encoding='latin1')  # or encoding='cp1252' if 'latin1' doesn't work
        return df['director'].to_json()

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except pd.errors.ParserError as e:
        print(f"Parsing error: {e}")
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# if __name__ == "__main__":
#     df = read_netflix_titles()
#     if df is not None:
#         print(df.head())
