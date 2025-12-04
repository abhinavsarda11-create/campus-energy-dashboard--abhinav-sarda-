# campus-energy-dashboard--abhinav-sarda-
python assignment 5 (Capstone)
📊 Campus Energy-Use Dashboard
End-to-End Energy Consumption Analysis and Visualization
📘 Overview

This project is a capstone assignment for Programming for Problem Solving using Python.
The goal is to build a complete data pipeline that reads electricity usage data for multiple campus buildings, processes it, performs analysis, visualizes trends, and outputs a final executive summary.

The project applies concepts such as file handling, data cleaning, OOP design, aggregation logic, and data visualization.

🎯 Objectives

By completing this project, you will:

Read and validate multiple CSV datasets using Pandas

Automate ingestion of building-wise monthly energy usage

Apply time-series and categorical aggregations

Build OOP structures to model buildings and meter readings

Create a multi-chart Matplotlib dashboard

Export cleaned data, summary statistics, and executive reports

📂 Project Structure
campus-energy-dashboard/
│
├── data/                         # Raw building-wise CSV files
├── output/                       # Generated dashboard, reports, cleaned CSVs
│   ├── dashboard.png
│   ├── cleaned_energy_data.csv
│   ├── building_summary.csv
│   └── summary.txt
├── src/
│   ├── data_ingestion.py         # Task 1
│   ├── aggregation.py            # Task 2
│   ├── models.py                 # Task 3 (OOP classes)
│   ├── dashboard.py              # Task 4
│   └── main.py                   # Master script to run all tasks
└── README.md

🧩 Task Breakdown
Task 1: Data Ingestion & Validation

Automatically scan the /data/ folder for .csv files

Load them using pandas.read_csv()

Handle missing/corrupt files with exception handling

Merge all building data into a single DataFrame

Add metadata (building name, month) if missing

Output:
df_combined — consolidated dataset
Logs for invalid or missing files

Task 2: Core Aggregation Logic

Functions compute:

Daily totals using .resample('D')

Weekly aggregates using .resample('W')

Building-wise summary metrics (mean, min, max, total)

Output:

Daily & weekly consumption DataFrames

Summary dict per building

Task 3: Object-Oriented Modeling

Classes implemented:

Building

Stores building name & meter readings

Methods:

add_reading()

calculate_total_consumption()

generate_report()

MeterReading

Attributes: timestamp, kWh value

BuildingManager

Maintains collection of Building objects

Aggregates & generates combined reports

Output:
Fully OOP-structured processing pipeline

Task 4: Matplotlib Dashboard

Generates a multi-chart dashboard consisting of:

Line Chart: Daily energy consumption trend

Bar Chart: Weekly average usage per building

Scatter Plot: Peak-hour consumption

All charts are combined into one figure and saved as:

📁 output/dashboard.png

Task 5: Persistence & Executive Summary

Exports:

Cleaned dataset → cleaned_energy_data.csv

Building summary table → building_summary.csv

Executive summary → summary.txt containing:

Total campus consumption

Most energy-consuming building

Peak load time

Trends and patterns

▶️ How to Run

Place all CSV files in the data/ folder

Run:

python src/main.py


Outputs will be generated inside the output/ folder.
