import logging
import sys
import pandas as pd

logging.basicConfig(
    level = logging.DEBUG,
    format = "{asctime}:{levelname}:{message}",
    style = "{",
    datefmt = "%Y-%m-%d %H:%M"
)

def extract_data(
        filepath,
        delimiter = ",",
        encoding = "utf-8"
):
    logging.info("Beginning execution...")
    logging.info("Ingesting data...")

    try:
        df = pd.read_parquet(filepath)

        if df.empty:
            logging.warning(f"{filepath} contains no data.")
        
        else:
            logging.info("Success.")
            return df

    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
        raise
    except Exception as e:
        logging.error(f"An exception occurred: {e}")
        raise



def main():
    filepath = "./data/yellow_tripdata_2024-01.parquet"

    try:
        df = extract_data(filepath)

        logging.info("Data successfully ingested.")
        print(df.head())

        return 0
    

    except FileNotFoundError:
        logging.critical(f"Pipeline failure: {filepath} not found.")
        return 1
    
    except Exception as e:
        logging.critical(f"Pipeline failed with unexpected error: {e}")
        return 2


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)

# refactor ingest into function
# create test for ingest function
# implement Jenkins



### INSIGHTS ###
# Could calculate busiest days?
# Could calculate tip percentage based on trip duration or whether to airport?
# Could calculate tip based on number of passengers?