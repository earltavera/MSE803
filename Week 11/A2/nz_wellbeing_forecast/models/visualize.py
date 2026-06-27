"""Generate all charts for the NZ Wellbeing Forecasting project."""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import sys, os
sys.path.insert(0, "/home/claude/nz_wellbeing_forecast/models")
from forecast import run_all_models, YEARS, DATA

OUT = "/home/claude/nz_wellbeing_forecast/outputs"
os.makedirs(OUT, exist_ok=True)

COLORS = {
    "Linear Regression": "#2196F3",
    "XGBoost (GBM)":     "#4CAF50",
    "LSTM":              "#FF5722",
    "ANN":               "#9C27B0",
    "ARIMA(1,1,1)":      "#FF9800",
    "Actual":            "#212121",
}

metrics_df, summary_df, fc_df, model_results, series_dict = run_all_models()

# ── Chart 1: Model Comparison Bar Chart ──────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Model Performance Comparison — NZ Wellbeing Forecast", fontsize=14, fontweight="bold")

metrics_list = ["Avg RMSE", "Avg MAE", "Avg MAPE (%)"]
titles       = ["RMSE (lower = better)", "MAE (lower = better)", "MAPE % (lower = better)"]

for ax, metric, title in zip(axes, metrics_list, titles):
    colors = [COLORS.get(m, "#999") for m in summary_df["Model"]]
    bars = ax.barh(summary_df["Model"], summary_df[metric], color=colors, edgecolor="white")
    ax.set_title(title, fontsize=11, pad=8)
    ax.set_xlabel(metric)
    for bar, val in zip(bars, summary_df[metric]):
        ax.text(bar.get_width() + bar.get_width()*0.01, bar.get_y() + bar.get_height()/2,
                f"{val:.4f}", va="center", fontsize=8)
    ax.invert_yaxis()
    ax.spines[["top","right"]].set_visible(False)

plt.tight_layout()
plt.savefig(f"{OUT}/01_model_comparison.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved chart 1")

# ── Chart 2: Actual vs Fitted for each model (Life Satisfaction) ──────────────
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
fig.suptitle("Actual vs Fitted: Life Satisfaction Mean (All Models)", fontsize=13, fontweight="bold")
axes = axes.flatten()

y_actual = np.array(DATA["Life Satisfaction Mean"])
model_names = list(model_results.keys())
x_all = np.array([2014, 2016, 2018, 2020])

for idx, mname in enumerate(model_names):
    ax = axes[idx]
    fitted = model_results[mname]["Life Satisfaction Mean"]["fitted"]
    fc     = model_results[mname]["Life Satisfaction Mean"]["forecast"]
    color  = COLORS[mname]

    ax.plot(YEARS, y_actual, "o-", color=COLORS["Actual"], lw=2.5, ms=8, label="Actual", zorder=5)
    ax.plot(YEARS, fitted[:3], "s--", color=color, lw=2, ms=7, label="Fitted")
    ax.plot([2018, 2020], [y_actual[-1], fc], "^:", color=color, lw=2, ms=9, label=f"Forecast 2020: {fc:.3f}")
    ax.axvline(2018.5, color="gray", ls=":", alpha=0.6)
    ax.set_title(mname, fontsize=10, fontweight="bold", color=color)
    ax.set_xlabel("Year"); ax.set_ylabel("Mean Rating")
    ax.set_xticks([2014, 2016, 2018, 2020])
    ax.legend(fontsize=8)
    ax.spines[["top","right"]].set_visible(False)
    ax.set_ylim(7.4, 8.1)

axes[-1].set_visible(False)
plt.tight_layout()
plt.savefig(f"{OUT}/02_life_satisfaction_all_models.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved chart 2")

# ── Chart 3: Multi-Indicator Forecast Dashboard ───────────────────────────────
indicators = list(DATA.keys())
fig, axes = plt.subplots(2, 5, figsize=(22, 9))
fig.suptitle("2020 Forecasts by Indicator — All Models", fontsize=13, fontweight="bold")
axes = axes.flatten()

for idx, ind in enumerate(indicators):
    ax = axes[idx]
    y_actual = np.array(DATA[ind])

    ax.scatter(YEARS, y_actual, color=COLORS["Actual"], s=80, zorder=6, label="Actual")
    ax.plot(YEARS, y_actual, "-", color=COLORS["Actual"], lw=1.5, alpha=0.6)

    for mname, mres in model_results.items():
        fc = mres[ind]["forecast"]
        ax.scatter([2020], [fc], marker="^", s=90, color=COLORS[mname], zorder=5)
        ax.plot([2018, 2020], [y_actual[-1], fc], "--", color=COLORS[mname], lw=1.5, alpha=0.8)

    ax.set_title(ind, fontsize=8, fontweight="bold")
    ax.set_xticks([2014, 2016, 2018, 2020])
    ax.tick_params(labelsize=7)
    ax.spines[["top","right"]].set_visible(False)
    ax.axvline(2018.5, color="gray", ls=":", alpha=0.4)

# Legend
patches = [mpatches.Patch(color=COLORS[m], label=m) for m in model_results]
patches.append(mpatches.Patch(color=COLORS["Actual"], label="Actual"))
fig.legend(handles=patches, loc="lower center", ncol=6, fontsize=9,
           bbox_to_anchor=(0.5, -0.02), frameon=False)
plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig(f"{OUT}/03_all_indicators_forecast.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved chart 3")

# ── Chart 4: R² Heatmap per indicator per model ───────────────────────────────
pivot_r2 = metrics_df.pivot_table(values="R²", index="Indicator", columns="Model")
pivot_r2.columns = [c.split(" | ")[0] if " | " in c else c for c in pivot_r2.columns]

# Extract clean model names
models_ord = ["Linear Regression", "XGBoost (GBM)", "LSTM", "ANN", "ARIMA(1,1,1)"]

# Build matrix manually
r2_matrix = []
for ind in indicators:
    row = []
    for mname in models_ord:
        vals = metrics_df[(metrics_df["Indicator"] == ind) & (metrics_df["Model"].str.startswith(mname))]
        row.append(vals["R²"].values[0] if len(vals) > 0 else np.nan)
    r2_matrix.append(row)

r2_arr = np.array(r2_matrix)

fig, ax = plt.subplots(figsize=(12, 7))
im = ax.imshow(r2_arr, cmap="RdYlGn", vmin=-0.2, vmax=1.0, aspect="auto")
ax.set_xticks(range(len(models_ord))); ax.set_xticklabels(models_ord, rotation=25, ha="right", fontsize=10)
ax.set_yticks(range(len(indicators)));  ax.set_yticklabels(indicators, fontsize=9)
for i in range(len(indicators)):
    for j in range(len(models_ord)):
        v = r2_arr[i, j]
        ax.text(j, i, f"{v:.2f}", ha="center", va="center", fontsize=8,
                color="black" if 0.2 < v < 0.8 else "white")
plt.colorbar(im, ax=ax, label="R² Score")
ax.set_title("R² Score Heatmap by Indicator & Model", fontsize=13, fontweight="bold", pad=12)
plt.tight_layout()
plt.savefig(f"{OUT}/04_r2_heatmap.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved chart 4")

# ── Chart 5: Summary ranking table ───────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis("off")
summary_df["Rank"] = range(1, len(summary_df)+1)
cols = ["Rank", "Model", "Avg RMSE", "Avg MAE", "Avg R²", "Avg MAPE (%)"]
table_data = summary_df[cols].values.tolist()
col_labels = cols

tbl = ax.table(cellText=table_data, colLabels=col_labels, loc="center", cellLoc="center")
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.2, 1.8)

# Color header
for j in range(len(col_labels)):
    tbl[0, j].set_facecolor("#1565C0")
    tbl[0, j].set_text_props(color="white", fontweight="bold")
# Color best row green
for j in range(len(col_labels)):
    tbl[1, j].set_facecolor("#C8E6C9")

ax.set_title("Model Performance Summary — NZ Wellbeing Forecasting", fontsize=12,
             fontweight="bold", pad=20)
plt.tight_layout()
plt.savefig(f"{OUT}/05_summary_table.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved chart 5")

# ── Chart 6: MAPE per indicator per model (grouped bar) ──────────────────────
mape_data = {}
for mname in models_ord:
    vals = []
    for ind in indicators:
        row = metrics_df[(metrics_df["Indicator"] == ind) & (metrics_df["Model"].str.startswith(mname))]
        vals.append(row["MAPE (%)"].values[0] if len(row) > 0 else 0)
    mape_data[mname] = vals

fig, ax = plt.subplots(figsize=(16, 6))
x = np.arange(len(indicators))
width = 0.15
for i, mname in enumerate(models_ord):
    ax.bar(x + i*width, mape_data[mname], width, label=mname, color=COLORS[mname], alpha=0.85)

ax.set_xticks(x + width*2)
ax.set_xticklabels([ind[:20] for ind in indicators], rotation=30, ha="right", fontsize=8)
ax.set_ylabel("MAPE (%)")
ax.set_title("MAPE by Indicator & Model (lower = better)", fontsize=12, fontweight="bold")
ax.legend(fontsize=9)
ax.spines[["top","right"]].set_visible(False)
plt.tight_layout()
plt.savefig(f"{OUT}/06_mape_by_indicator.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved chart 6")

print("\nAll charts saved!")
