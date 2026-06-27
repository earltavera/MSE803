"""
Extract and preprocess NZ Wellbeing time-series data from Stats NZ Excel file.
Data spans 2014, 2016, 2018 (biennial survey).
"""
import pandas as pd
import numpy as np

FILEPATH = "/mnt/user-data/uploads/wellbeing-statistics-2014-18-time-series.xlsx"

SHEET_MAP = {
    "Life Satisfaction (Mean)":     ("1. Overall life satisfaction",  11, 13),
    "Life Worthwhile (Mean)":       ("2. Life worthwhile",            11, 13),
    "Financial Inadequacy (%)":     ("3. Financial wellbeing",        12, 14),
    "Health Excellent (%)":         ("7. Self-rated general health",  11, 13),
    "Loneliness None (%)":          ("10. Loneliness",                11, 13),
    "Generalised Trust Low (%)":    ("11. Generalised trust",         11, 13),
    "Job Very Satisfied (%)":       ("19. Job satisfaction",          12, 14),
}

MEAN_COLS = {"Life Satisfaction (Mean)", "Life Worthwhile (Mean)"}

def extract_total_population_series():
    """Extract total population rows (first 3 data rows) for each indicator."""
    records = {}
    years = [2014, 2016, 2018]

    for label, (sheet, row_start, row_end) in SHEET_MAP.items():
        df = pd.read_excel(FILEPATH, sheet_name=sheet, header=None)
        vals = []
        for r in range(row_start, row_end + 1):
            row = df.iloc[r]
            year_val = row[1]
            if pd.isna(year_val):
                continue
            # Mean rating is in col 13 for satisfaction sheets, col 2 for others
            if label in MEAN_COLS:
                v = row[13]  # mean rating column
            else:
                v = row[2]   # first estimate column
            try:
                vals.append(float(v))
            except (ValueError, TypeError):
                vals.append(np.nan)
        records[label] = vals

    df_out = pd.DataFrame(records, index=years)
    df_out.index.name = "Year"
    return df_out


def get_additional_indicators():
    """Extract more indicators for richer dataset."""
    extra = {}
    years = [2014, 2016, 2018]

    # Housing condition
    df = pd.read_excel(FILEPATH, sheet_name="20. Housing condition", header=None)
    housing_vals = []
    for r in [11, 12, 13]:
        try:
            v = float(df.iloc[r, 2])
            housing_vals.append(v)
        except Exception:
            housing_vals.append(np.nan)
    extra["Housing Problem (%)"] = housing_vals

    # Culture identity
    df = pd.read_excel(FILEPATH, sheet_name="18. Culture and identity", header=None)
    culture_vals = []
    for r in [11, 12, 13]:
        try:
            v = float(df.iloc[r, 2])
            culture_vals.append(v)
        except Exception:
            culture_vals.append(np.nan)
    extra["Cultural Belonging (%)"] = culture_vals

    # Safety
    df = pd.read_excel(FILEPATH, sheet_name="8. Safety and security", header=None)
    safety_vals = []
    for r in [11, 12, 13]:
        try:
            v = float(df.iloc[r, 2])
            safety_vals.append(v)
        except Exception:
            safety_vals.append(np.nan)
    extra["Feel Safe (%)"] = safety_vals

    return pd.DataFrame(extra, index=years)


if __name__ == "__main__":
    df_main = extract_total_population_series()
    df_extra = get_additional_indicators()
    df_all = pd.concat([df_main, df_extra], axis=1)
    print("Extracted dataset:")
    print(df_all.to_string())
    df_all.to_csv("/home/claude/nz_wellbeing_forecast/data/wellbeing_data.csv")
    print("\nSaved to wellbeing_data.csv")
