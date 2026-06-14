# Avon River Water Quality & Fish Population Analysis

This Python script generates a 2×2 dashboard of publication-quality visualisations analysing water quality parameters and fish population data from the Avon River monitoring programme. The script reads from an Excel dataset, processes water quality and fish population tables, and produces four complementary charts that communicate environmental findings to both technical and non-technical stakeholders.

---

### Dataset Requirements

**File:** `Data_Set_Assignmnet_1-V0.1_20426.xlsx`

**Structure:** The Excel workbook must contain a single worksheet with:
- **Header row at row 2** (the script skips row 1 and reads headers from row 2)
- **Water quality columns:** `Site ID`, `Date`, `Temperature (°C)`, `pH`, `Dissolved Oxygen (mg/L)`
- **Fish population columns:** `Site ID.1`, `Date.1`, `Species`, `Count`, `Avg. Size (cm)`

**Expected data characteristics:**
- Three monitoring sites: `AV-1`, `AV-2`, `AV-3`
- Monitoring period: October–December 2023
- Fish species: `Brown Trout`, `Shortfin Eel`, `Longfin Eel`, `Inanga`
- 71 rows total (small–medium dataset)

---

### Dependencies

| Package | Minimum Version | Purpose |
|---------|-----------------|---------|
| `pandas` | 1.3.0 | Data loading, cleaning, and transformation |
| `matplotlib` | 3.4.0 | Plotting and visualisation |
| `numpy` | 1.21.0 | Numerical operations (trend line fitting) |

**Install dependencies:**
```bash
pip install pandas matplotlib numpy openpyxl
```
*(Note: `openpyxl` is required as the pandas Excel engine for `.xlsx` files.)*

---

### Usage

1. **Place the dataset** in the same directory as the script:
   ```
   /your-project/
   ├── avon_analysis.py
   └── Data_Set_Assignmnet_1-V0.1_20426.xlsx
   ```

2. **Run the script:**
   ```bash
   python avon_analysis.py
   ```

3. **Output:** A PNG file `water_quality_charts.png` (150 DPI, 16×12 inches) is saved to the working directory.

---

### Visualisation Dashboard

The script produces four charts arranged in a 2×2 grid:

| Position | Chart Type | Title | Purpose |
|----------|-----------|-------|---------|
| Top-left | Scatter plot | Temperature vs Dissolved Oxygen by Site | Reveals the inverse relationship between temperature and dissolved oxygen solubility; colour-coded by site to identify location-specific clustering |
| Top-right | Line chart | Water Temperature Over Time by Site | Tracks seasonal warming trajectories across October–December; highlights AV-3's steeper thermal increase |
| Bottom-left | Bar chart | Total Fish Count by Species | Summarises species abundance across all sites and dates; Inanga dominance is immediately visible |
| Bottom-right | Grouped bar chart | Fish Count by Species & Site | Enables direct cross-site comparison of species distribution; reveals AV-1/AV-3 Inanga concentration and Brown Trout evenness |

---

### Design Choices

**Colour palette:**
- **Sites:** `AV-1` = blue (#2196F3), `AV-2` = green (#4CAF50), `AV-3` = orange (#FF5722) — intuitive and accessible for colour-blind audiences
- **Species:** Earth-tone and aquatic colours matching natural habitats (Brown Trout = saddle brown, eels = steel/sea green, Inanga = goldenrod)

**Styling:**
- Minimalist "data-ink" aesthetic: removed top/right spines, subtle gridlines
- DejaVu Sans font family for broad cross-platform compatibility
- White edge borders on markers/bars for depth separation
- Trend line overlay on scatter plot to reinforce correlation narrative

---

### Data Processing Pipeline

1. **Load:** Reads Excel with `header=1` (row 2)
2. **Clean:** Drops rows with missing `Site ID` or `Date`; drops fish records with missing `Species`
3. **Parse:** Converts `Date` columns to datetime objects
4. **Split:** Separates water quality and fish population tables
5. **Standardise:** Renames fish table columns for consistency
6. **Group:** Aggregates fish counts by species and by species-site combinations
7. **Fit:** Calculates linear regression (1st-order polynomial) for temperature-DO trend line
8. **Render:** Applies tight layout and saves at 150 DPI

---

### Limitations & Notes

- **Hard-coded paths:** The Excel filename is fixed; modify the `pd.read_excel()` call for different filenames
- **Date parsing:** Assumes dd/mm/yyyy or ISO format; may require `dayfirst=True` if ambiguous
- **Static output:** PNG only; modify `plt.savefig()` to `plt.show()` for interactive preview
- **No error handling:** Missing files or malformed columns will raise standard Python exceptions
- **Memory:** Designed for small datasets; scales poorly beyond ~10,000 rows without modification

---

### Academic Context

This script supports **MSE803: Data Analytics** — Assessment 1 (Theory Exam). The visualisations directly address Task 1-C (Tool Selection and Visualisation) by demonstrating Python's capability for reproducible, publication-quality environmental data communication. The charts are referenced in the accompanying report to support evidence-based recommendations for Avon River conservation management.

---

### Author

Saurabh Singh  
Student ID: 270732411  
Course: MSE803 Data Analytics  
Lecturer: Mohammad Norouzifard  
Submission:14th June 2026