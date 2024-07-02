import pandas as pd
from pathlib import Path


def load_facility_hh_data(facility_id: int) -> pd.DataFrame:
    """Load half-hourly data for a facility."""
    dummy_dataf = pd.read_csv(r"data_csv/dummy_data.csv", index_col=0)
    col_index = facility_id % len(dummy_dataf.columns)
    print(col_index, len(dummy_dataf.columns))
    return dummy_dataf.iloc[:, col_index]


if __name__ == "__main__":
    print(load_facility_hh_data(1))
