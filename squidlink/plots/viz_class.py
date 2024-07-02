from dataclasses import dataclass, field
from sqlalchemy.orm import Session
import pandas as pd

from schemas import Sector
from database import queries
import models
from plots import functions


@dataclass
class Facility:
    db: Session
    facility_id: int
    sector: str | None = None
    hh_elec_data: pd.DataFrame = field(default_factory=pd.DataFrame)
    hh_gas_data: pd.DataFrame = field(default_factory=pd.DataFrame)
    floor_area: float = 0

    def __post_init__(self):
        if self.sector is None:
            self.sector = queries.get_sector(self.db, self.facility_id)
        if len(self.hh_elec_data) == 0:
            self.hh_elec_data = self.convert_meter_reading_to_df(
                queries.get_meter_readings(self.db, self.facility_id))

    def convert_meter_reading_to_df(
            self, list_data: list[models.ReadMeterReading]) -> pd.DataFrame:
        return pd.DataFrame(list_data)

    def calculate_electricity_intensity(self) -> float:
        return self.hh_elec_data.sum() / self.floor_area

    def calculate_gas_intensity(self) -> float:
        return self.hh_gas_data.sum() / self.floor_area

    def get_elec_benchmark(self) -> float:
        benchmark_data = pd.read_csv('../data/benchmark_data.csv')
        return benchmark_data.loc[self.sector.value,
                                  'Electricity benchmark (kWh/m2)'].value[0]

    def viz_avg_elec_data(self) -> str:
        return functions.create_avg_daily_consumption_chart(self.hh_elec_data)

    def viz_avg_elec_and_carbon_data(self) -> str:
        return functions.create_avg_consumption_and_carbon_intensity_chart(
            self.hh_elec_data)

    def viz_overall_chart(self) -> str:
        return functions.create_overall_chart(self.hh_elec_data)
