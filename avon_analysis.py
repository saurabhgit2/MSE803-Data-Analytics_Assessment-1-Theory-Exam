import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# ── Load data ──────────────────────────────────────────────────────────────────
df = pd.read_excel("Data_Set_Assignmnet_1-V0.1_20426.xlsx", header=1)
df = df.dropna(subset=["Site ID", "Date"])
df["Date"] = pd.to_datetime(df["Date"])

water = df[["Site ID", "Date", "Temperature (°C)", "pH", "Dissolved Oxygen (mg/L)"]].copy()
fish  = df[["Site ID.1", "Date.1", "Species", "Count", "Avg. Size (cm)"]].copy()
fish.columns = ["Site ID", "Date", "Species", "Count", "Avg Size (cm)"]
fish = fish.dropna(subset=["Species"])

COLORS = {"AV-1": "#2196F3", "AV-2": "#4CAF50", "AV-3": "#FF5722"}
SPECIES_COLORS = {
    "Brown Trout":   "#8B4513",
    "Shortfin Eel":  "#4682B4",
    "Longfin Eel":   "#2E8B57",
    "Inanga":        "#DAA520",
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
})

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Āvon River Water Quality & Fish Population Analysis",
             fontsize=16, fontweight="bold", y=0.98)

# ── 1. Scatter Plot: Temperature vs Dissolved Oxygen by Site ──────────────────
ax1 = axes[0, 0]
for site, grp in water.groupby("Site ID"):
    ax1.scatter(grp["Temperature (°C)"], grp["Dissolved Oxygen (mg/L)"],
                label=site, color=COLORS[site], alpha=0.75, s=60, edgecolors="white", linewidth=0.5)

z = np.polyfit(water["Temperature (°C)"], water["Dissolved Oxygen (mg/L)"], 1)
x_line = np.linspace(water["Temperature (°C)"].min(), water["Temperature (°C)"].max(), 100)
ax1.plot(x_line, np.poly1d(z)(x_line), color="grey", linestyle="--", linewidth=1.2, label="Trend")

ax1.set_title("Scatter Plot: Temperature vs Dissolved Oxygen", fontweight="bold")
ax1.set_xlabel("Temperature (°C)")
ax1.set_ylabel("Dissolved Oxygen (mg/L)")
ax1.legend(title="Site ID", framealpha=0.8)

# ── 2. Line Chart: Temperature over Time by Site ──────────────────────────────
ax2 = axes[0, 1]
for site, grp in water.groupby("Site ID"):
    grp_sorted = grp.sort_values("Date")
    ax2.plot(grp_sorted["Date"], grp_sorted["Temperature (°C)"],
             label=site, color=COLORS[site], linewidth=1.8, marker="o", markersize=4, alpha=0.9)

ax2.set_title("Line Chart: Water Temperature Over Time by Site", fontweight="bold")
ax2.set_xlabel("Date")
ax2.set_ylabel("Temperature (°C)")
ax2.legend(title="Site ID", framealpha=0.8)
ax2.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%b %d"))
ax2.tick_params(axis="x", rotation=30)

# ── 3. Bar Chart: Total Fish Count per Species ────────────────────────────────
ax3 = axes[1, 0]
species_totals = fish.groupby("Species")["Count"].sum().sort_values(ascending=False)
bars = ax3.bar(species_totals.index, species_totals.values,
               color=[SPECIES_COLORS.get(s, "#999") for s in species_totals.index],
               edgecolor="white", linewidth=0.7)

for bar in bars:
    ax3.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
             str(int(bar.get_height())), ha="center", va="bottom", fontsize=9, fontweight="bold")

ax3.set_title("Bar Chart: Total Fish Count by Species", fontweight="bold")
ax3.set_xlabel("Species")
ax3.set_ylabel("Total Count")
ax3.tick_params(axis="x", rotation=15)

# ── 4. Grouped Bar Chart: Fish Count per Species per Site ─────────────────────
ax4 = axes[1, 1]
pivot = fish.groupby(["Site ID", "Species"])["Count"].sum().unstack(fill_value=0)
species_list = pivot.columns.tolist()
sites = pivot.index.tolist()

x = np.arange(len(species_list))
width = 0.25
offsets = np.linspace(-(len(sites) - 1) * width / 2, (len(sites) - 1) * width / 2, len(sites))

for i, site in enumerate(sites):
    vals = [pivot.loc[site, sp] for sp in species_list]
    bars = ax4.bar(x + offsets[i], vals, width, label=site,
                   color=COLORS[site], edgecolor="white", linewidth=0.5, alpha=0.9)

ax4.set_title("Grouped Bar Chart: Fish Count by Species & Site", fontweight="bold")
ax4.set_xlabel("Species")
ax4.set_ylabel("Total Count")
ax4.set_xticks(x)
ax4.set_xticklabels(species_list, rotation=15)
ax4.legend(title="Site ID", framealpha=0.8)

plt.tight_layout()
plt.savefig("water_quality_charts.png", dpi=150, bbox_inches="tight")
print("Saved: water_quality_charts.png")