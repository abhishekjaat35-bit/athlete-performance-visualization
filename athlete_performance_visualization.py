import pandas as pd
import matplotlib.pyplot as plt


print("=" * 75)
print("              ATHLETE PERFORMANCE VISUALIZATION")
print("=" * 75)


# ------------------------------------------
# Load Data
# ------------------------------------------

data = pd.read_csv("athlete_performance_data.csv")

data["Date"] = pd.to_datetime(data["Date"])

data = data.sort_values(
    ["Athlete", "Date"]
).reset_index(drop=True)


# ------------------------------------------
# Display Dataset
# ------------------------------------------

print("\n" + "=" * 75)
print("ATHLETE PERFORMANCE DATA")
print("=" * 75)

print(data.to_string(index=False))


# ------------------------------------------
# Dataset Information
# ------------------------------------------

print("\n" + "=" * 75)
print("DATASET INFORMATION")
print("=" * 75)

print(f"Number of observations : {len(data)}")
print(f"Number of athletes     : {data['Athlete'].nunique()}")
print(
    f"Date range             : "
    f"{data['Date'].min().date()} to "
    f"{data['Date'].max().date()}"
)


# ------------------------------------------
# Athlete Summary
# ------------------------------------------

athlete_summary = (
    data.groupby("Athlete")
    .agg(
        Average_Training_Load=("Training_Load", "mean"),
        Average_Wellness=("Wellness_Score", "mean"),
        Average_Readiness=("Readiness_Score", "mean"),
        Average_Jump=("Jump_Height_cm", "mean"),
        Average_Sprint=("Sprint_Time_s", "mean"),
        Average_Strength=("Strength_Score", "mean")
    )
    .reset_index()
)


print("\n" + "=" * 75)
print("ATHLETE PERFORMANCE SUMMARY")
print("=" * 75)

print(
    athlete_summary.to_string(
        index=False,
        formatters={
            "Average_Training_Load": "{:.1f}".format,
            "Average_Wellness": "{:.1f}".format,
            "Average_Readiness": "{:.1f}%".format,
            "Average_Jump": "{:.1f}".format,
            "Average_Sprint": "{:.2f}".format,
            "Average_Strength": "{:.1f}".format
        }
    )
)


# ------------------------------------------
# Team Summary
# ------------------------------------------

print("\n" + "=" * 75)
print("TEAM PERFORMANCE SUMMARY")
print("=" * 75)

print(
    f"Average Training Load : "
    f"{data['Training_Load'].mean():.1f} AU"
)

print(
    f"Average Wellness      : "
    f"{data['Wellness_Score'].mean():.1f}/25"
)

print(
    f"Average Readiness     : "
    f"{data['Readiness_Score'].mean():.1f}%"
)

print(
    f"Average Jump Height   : "
    f"{data['Jump_Height_cm'].mean():.1f} cm"
)

print(
    f"Average Sprint Time   : "
    f"{data['Sprint_Time_s'].mean():.2f} s"
)

print(
    f"Average Strength      : "
    f"{data['Strength_Score'].mean():.1f}"
)


# ------------------------------------------
# Highest Training Load
# ------------------------------------------

highest_load = data.loc[
    data["Training_Load"].idxmax()
]

print("\n" + "=" * 75)
print("HIGHEST TRAINING LOAD")
print("=" * 75)

print(f"Athlete       : {highest_load['Athlete']}")
print(f"Date          : {highest_load['Date'].date()}")
print(f"Training Load : {highest_load['Training_Load']} AU")


# ------------------------------------------
# Highest Readiness
# ------------------------------------------

highest_readiness = data.loc[
    data["Readiness_Score"].idxmax()
]

print("\n" + "=" * 75)
print("HIGHEST READINESS")
print("=" * 75)

print(f"Athlete   : {highest_readiness['Athlete']}")
print(f"Date      : {highest_readiness['Date'].date()}")
print(f"Readiness : {highest_readiness['Readiness_Score']}%")


# ------------------------------------------
# Best Jump Performance
# ------------------------------------------

best_jump = data.loc[
    data["Jump_Height_cm"].idxmax()
]

print("\n" + "=" * 75)
print("BEST JUMP PERFORMANCE")
print("=" * 75)

print(f"Athlete : {best_jump['Athlete']}")
print(f"Date    : {best_jump['Date'].date()}")
print(f"Jump    : {best_jump['Jump_Height_cm']} cm")


# ------------------------------------------
# Best Sprint Performance
# Lower time = better
# ------------------------------------------

best_sprint = data.loc[
    data["Sprint_Time_s"].idxmin()
]

print("\n" + "=" * 75)
print("BEST SPRINT PERFORMANCE")
print("=" * 75)

print(f"Athlete : {best_sprint['Athlete']}")
print(f"Date    : {best_sprint['Date'].date()}")
print(f"Time    : {best_sprint['Sprint_Time_s']:.2f} s")


# ------------------------------------------
# Visualization 1
# Training Load Trend
# ------------------------------------------

plt.figure(figsize=(10, 6))

for athlete in data["Athlete"].unique():

    athlete_data = data[
        data["Athlete"] == athlete
    ]

    plt.plot(
        athlete_data["Date"],
        athlete_data["Training_Load"],
        marker="o",
        label=athlete
    )

plt.title("Training Load Trend")
plt.xlabel("Date")
plt.ylabel("Training Load (AU)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(
    "training_load_trend.png",
    dpi=300
)
plt.show()


# ------------------------------------------
# Visualization 2
# Readiness Trend
# ------------------------------------------

plt.figure(figsize=(10, 6))

for athlete in data["Athlete"].unique():

    athlete_data = data[
        data["Athlete"] == athlete
    ]

    plt.plot(
        athlete_data["Date"],
        athlete_data["Readiness_Score"],
        marker="o",
        label=athlete
    )

plt.title("Athlete Readiness Trend")
plt.xlabel("Date")
plt.ylabel("Readiness (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(
    "readiness_trend.png",
    dpi=300
)
plt.show()


# ------------------------------------------
# Visualization 3
# Average Training Load
# ------------------------------------------

plt.figure(figsize=(8, 6))

plt.bar(
    athlete_summary["Athlete"],
    athlete_summary["Average_Training_Load"]
)

plt.title("Average Training Load by Athlete")
plt.xlabel("Athlete")
plt.ylabel("Average Training Load (AU)")
plt.tight_layout()
plt.savefig(
    "average_training_load.png",
    dpi=300
)
plt.show()


# ------------------------------------------
# Visualization 4
# Average Jump Height
# ------------------------------------------

plt.figure(figsize=(8, 6))

plt.bar(
    athlete_summary["Athlete"],
    athlete_summary["Average_Jump"]
)

plt.title("Average Jump Height by Athlete")
plt.xlabel("Athlete")
plt.ylabel("Jump Height (cm)")
plt.tight_layout()
plt.savefig(
    "average_jump_height.png",
    dpi=300
)
plt.show()


# ------------------------------------------
# Visualization 5
# Training Load vs Readiness
# ------------------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    data["Training_Load"],
    data["Readiness_Score"]
)

plt.title("Training Load vs Readiness")
plt.xlabel("Training Load (AU)")
plt.ylabel("Readiness (%)")
plt.tight_layout()
plt.savefig(
    "training_load_vs_readiness.png",
    dpi=300
)
plt.show()


# ------------------------------------------
# Correlation Analysis
# ------------------------------------------

correlation = data[
    [
        "Training_Load",
        "Wellness_Score",
        "Readiness_Score",
        "Jump_Height_cm",
        "Sprint_Time_s",
        "Strength_Score"
    ]
].corr()


print("\n" + "=" * 75)
print("CORRELATION MATRIX")
print("=" * 75)

print(correlation.round(2).to_string())


# ------------------------------------------
# Export Summary
# ------------------------------------------

athlete_summary.to_csv(
    "athlete_performance_summary.csv",
    index=False
)

correlation.to_csv(
    "performance_correlation_matrix.csv"
)


# ------------------------------------------
# Final Output
# ------------------------------------------

print("\n" + "=" * 75)
print("ANALYSIS COMPLETE")
print("=" * 75)

print("Files created:")

print("1. training_load_trend.png")
print("2. readiness_trend.png")
print("3. average_training_load.png")
print("4. average_jump_height.png")
print("5. training_load_vs_readiness.png")
print("6. athlete_performance_summary.csv")
print("7. performance_correlation_matrix.csv")

print("\n" + "=" * 75)
print("VISUALIZE • ANALYZE • INTERPRET • PERFORM")
print("=" * 75)