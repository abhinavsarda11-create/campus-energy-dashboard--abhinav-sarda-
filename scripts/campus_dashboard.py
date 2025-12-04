import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime


DATA_DIR = Path("data")
OUTPUT_DIR = Path("output")
CLEAN_DIR = OUTPUT_DIR / "cleaned"
SUMMARY_DIR = OUTPUT_DIR / "summaries"

OUTPUT_DIR.mkdir(exist_ok=True)
CLEAN_DIR.mkdir(exist_ok=True)
SUMMARY_DIR.mkdir(exist_ok=True)




class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = pd.to_datetime(timestamp)
        self.kwh = float(kwh)


class Building:
    def __init__(self, name):
        self.name = name
        self.readings = []

    def add_reading(self, reading: MeterReading):
        self.readings.append(reading)

    def to_dataframe(self):
        if not self.readings:
            return pd.DataFrame(columns=["timestamp", "kwh", "building"])

        df = pd.DataFrame(
            [{"timestamp": r.timestamp, "kwh": r.kwh} for r in self.readings]
        )
        df["building"] = self.name
        return df

    def summary(self):
        df = self.to_dataframe()
        if df.empty:
            return None

        total_kwh = df["kwh"].sum()
        avg_kwh = df["kwh"].mean()
        peak_row = df.loc[df["kwh"].idxmax()]

        return {
            "building": self.name,
            "total_readings": len(df),
            "total_kwh": round(total_kwh, 2),
            "avg_kwh": round(avg_kwh, 2),
            "peak_kwh": round(peak_row["kwh"], 2),
            "peak_timestamp": str(peak_row["timestamp"])
        }




def clean_dataframe(df):
    df.columns = df.columns.str.strip().str.lower()

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["kwh"] = pd.to_numeric(df["kwh"], errors="coerce")
    df = df.dropna(subset=["timestamp", "kwh"])

    df = df[df["kwh"] >= 0]              
    df = df.sort_values("timestamp")
    df = df.reset_index(drop=True)
    return df



def load_buildings():
    buildings = {}

    for file in DATA_DIR.glob("*.csv"):
        name = file.stem.replace("_usage", "").replace("_", " ").title()

        df = pd.read_csv(file)
        df = clean_dataframe(df)

        b = Building(name)

        for _, row in df.iterrows():
            b.add_reading(MeterReading(row["timestamp"], row["kwh"]))

        buildings[name] = b

    return buildings




def generate_report():
    buildings = load_buildings()
    campus_rows = []
    campus_frames = []

    print("\n========== CAMPUS ENERGY REPORT ==========\n")

    for name, building in buildings.items():
        df = building.to_dataframe()

        
        cleaned_path = CLEAN_DIR / f"{name}_cleaned.csv"
        df.to_csv(cleaned_path, index=False)

        info = building.summary()
        if info is None:
            continue

        
        summary_path = SUMMARY_DIR / f"{name}_summary.csv"
        pd.DataFrame([info]).to_csv(summary_path, index=False)

        
        print(f"Building: {info['building']}")
        print(f"Total Readings: {info['total_readings']}")
        print(f"Total Energy Consumed: {info['total_kwh']} kWh")
        print(f"Average Consumption: {info['avg_kwh']} kWh per hour")
        print(f"Peak Reading: {info['peak_kwh']} kWh at {info['peak_timestamp']}")
        print("-" * 45)

        campus_rows.append(info)
        campus_frames.append(df)

    
    if campus_frames:
        combined_df = pd.concat(campus_frames, ignore_index=True)
        combined_df.to_csv(OUTPUT_DIR / "campus_cleaned.csv", index=False)

    
    campus_summary = pd.DataFrame(campus_rows)
    campus_summary.to_csv(OUTPUT_DIR / "campus_summary.csv", index=False)

    print("\nCleaned and summarized CSV files generated in 'output/' folder.\n")


if __name__ == "__main__":
    generate_report()
