# Formula Slug Intro Project

This project analyzes telemetry data from the Formula Slug endurance test.  
The data includes motor temperatures, brake pressures, and acceleration logs from the first half of the endurance run.

## What it does
- Reads real race telemetry data (CSV)
- Calculates basic vehicle statistics
- Visualizes:
  - Motor & Controller temperature trend
  - Front vs Rear brake correlation
  - Acceleration (Z-axis) distribution

## How to run
```bash
pip install pandas matplotlib
python3 analysis.py
