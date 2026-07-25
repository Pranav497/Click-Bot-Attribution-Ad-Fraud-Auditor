import pandas as pd
import numpy as np

INPUT_FILE = "data/processed/featured_ga4_data.csv"
OUTPUT_FILE = "data/processed/session_level_data.csv"

print("=" * 60)
print("SESSION-LEVEL FEATURE ENGINEERING")
print("=" * 60)

df = pd.read_csv(INPUT_FILE)

print("\nOriginal Dataset Shape:")
print(df.shape)

# ============================================================
# 1. IDENTIFY ACTUAL EVENTS
# ============================================================

events = df[df["event_name"].notna()].copy()

print("\nActual Event Rows:")
print(len(events))

# ============================================================
# 2. CREATE EVENT ORDER
# ============================================================

events = events.reset_index(drop=True)
events["event_id"] = events.index

# ============================================================
# 3. GET PARAMETER ROWS
# ============================================================

params = df[
    df["event_params.key"].notna()
].copy()

# ============================================================
# 4. CREATE PARAMETER VALUE
# ============================================================

params["param_value"] = params[
    "event_params.value.int_value"
]

# If integer value is missing, use string value
params["param_value"] = params[
    "param_value"
].fillna(
    params["event_params.value.string_value"]
)

# ============================================================
# 5. CREATE EVENT KEY USING USER + TIMESTAMP
# ============================================================

events["event_key"] = (
    events["user_pseudo_id"].astype("string")
    + "_"
    + events["event_timestamp"].astype("string")
)

params["event_key"] = (
    params["user_pseudo_id"].astype("string")
    + "_"
    + params["event_timestamp"].astype("string")
)

# ============================================================
# 6. PARAMETER TABLE
# ============================================================

parameter_table = (
    params[
        [
            "event_key",
            "event_params.key",
            "param_value"
        ]
    ]
    .drop_duplicates(
        subset=[
            "event_key",
            "event_params.key"
        ]
    )
)

# ============================================================
# 7. PIVOT PARAMETERS
# ============================================================

parameter_table = parameter_table.pivot(
    index="event_key",
    columns="event_params.key",
    values="param_value"
).reset_index()

# ============================================================
# 8. RENAME PARAMETERS
# ============================================================

parameter_table = parameter_table.rename(
    columns={
        "ga_session_id": "ga_session_id",
        "ga_session_number": "session_number",
        "engagement_time_msec": "engagement_time"
    }
)

# ============================================================
# 9. MERGE PARAMETERS INTO EVENTS
# ============================================================

events = events.merge(
    parameter_table,
    on="event_key",
    how="left",
    suffixes=("", "_parameter")
)

# ============================================================
# 10. CLEAN NUMERIC FEATURES
# ============================================================

events["ga_session_id"] = pd.to_numeric(
    events["ga_session_id"],
    errors="coerce"
)

events["session_number"] = pd.to_numeric(
    events["session_number"],
    errors="coerce"
).fillna(0)

events["engagement_time"] = pd.to_numeric(
    events["engagement_time"],
    errors="coerce"
).fillna(0)

# ============================================================
# 11. CREATE SESSION ID
# ============================================================

valid_session = (
    events["user_pseudo_id"].notna()
    & events["ga_session_id"].notna()
)

events["session_id"] = np.nan

events.loc[valid_session, "session_id"] = (
    events.loc[
        valid_session,
        "user_pseudo_id"
    ].astype(str)
    + "_"
    + events.loc[
        valid_session,
        "ga_session_id"
    ].astype(str)
)

# ============================================================
# 12. FALLBACK FOR EVENTS WITHOUT SESSION ID
# ============================================================

missing_session = events["session_id"].isna()

events.loc[missing_session, "session_id"] = (
    "unknown_session_"
    + events.loc[
        missing_session
    ].index.astype(str)
)

# ============================================================
# 13. EVENT FLAGS
# ============================================================

events["page_view_count"] = (
    events["event_name"] == "page_view"
).astype(int)

events["scroll_count"] = (
    events["event_name"] == "scroll"
).astype(int)

events["user_engagement_count"] = (
    events["event_name"] == "user_engagement"
).astype(int)

events["session_start_count"] = (
    events["event_name"] == "session_start"
).astype(int)

# ============================================================
# 14. ENTRANCE FLAG
# ============================================================

events["entrance_count"] = 0

if "entrances" in events.columns:

    events["entrance_count"] = (
        pd.to_numeric(
            events["entrances"],
            errors="coerce"
        )
        .fillna(0)
    )

# ============================================================
# 15. DATA QUALITY FEATURES
# ============================================================

events["missing_user_id"] = (
    events["user_pseudo_id"].isna()
).astype(int)

events["missing_device"] = (
    events["device.category"].isna()
).astype(int)

events["missing_browser"] = (
    events["device.web_info.browser"].isna()
).astype(int)

events["missing_country"] = (
    events["geo.country"].isna()
).astype(int)

events["missing_traffic_source"] = (
    events["traffic_source.source"].isna()
).astype(int)

# ============================================================
# 16. SESSION AGGREGATION
# ============================================================

session_df = (
    events
    .groupby("session_id")
    .agg(
        user_pseudo_id=(
            "user_pseudo_id",
            "first"
        ),

        ga_session_id=(
            "ga_session_id",
            "first"
        ),

        session_number=(
            "session_number",
            "max"
        ),

        total_engagement_time=(
            "engagement_time",
            "sum"
        ),

        event_count=(
            "event_name",
            "count"
        ),

        page_view_count=(
            "page_view_count",
            "sum"
        ),

        scroll_count=(
            "scroll_count",
            "sum"
        ),

        user_engagement_count=(
            "user_engagement_count",
            "sum"
        ),

        session_start_count=(
            "session_start_count",
            "sum"
        ),

        entrance_count=(
            "entrance_count",
            "sum"
        ),

        missing_user_id=(
            "missing_user_id",
            "max"
        ),

        missing_device=(
            "missing_device",
            "max"
        ),

        missing_browser=(
            "missing_browser",
            "max"
        ),

        missing_country=(
            "missing_country",
            "max"
        ),

        missing_traffic_source=(
            "missing_traffic_source",
            "max"
        ),

        device_category=(
            "device.category",
            "first"
        ),

        browser=(
            "device.web_info.browser",
            "first"
        ),

        country=(
            "geo.country",
            "first"
        ),

        traffic_source=(
            "traffic_source.source",
            "first"
        ),

        traffic_medium=(
            "traffic_source.medium",
            "first"
        )
    )
    .reset_index()
)

# ============================================================
# 17. DERIVED SESSION FEATURES
# ============================================================

session_df["avg_engagement_time"] = (
    session_df["total_engagement_time"]
    / session_df["event_count"].replace(0, np.nan)
)

session_df["avg_engagement_time"] = (
    session_df["avg_engagement_time"]
    .fillna(0)
)

session_df["engagement_per_page_view"] = (
    session_df["total_engagement_time"]
    / session_df["page_view_count"].replace(0, np.nan)
)

session_df["engagement_per_page_view"] = (
    session_df["engagement_per_page_view"]
    .fillna(0)
)

session_df["events_per_page_view"] = (
    session_df["event_count"]
    / session_df["page_view_count"].replace(0, np.nan)
)

session_df["events_per_page_view"] = (
    session_df["events_per_page_view"]
    .fillna(0)
)

session_df["zero_engagement"] = (
    session_df["total_engagement_time"] == 0
).astype(int)

session_df["high_engagement"] = (
    session_df["total_engagement_time"]
    > session_df["total_engagement_time"].median()
).astype(int)

# ============================================================
# 18. SAVE
# ============================================================

session_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ============================================================
# 19. VALIDATION
# ============================================================

print("\n" + "=" * 60)
print("VALIDATION")
print("=" * 60)

print(
    "\nOriginal flattened rows:",
    len(df)
)

print(
    "Actual event rows:",
    len(events)
)

print(
    "Generated sessions:",
    len(session_df)
)

print(
    "Total events represented:",
    session_df["event_count"].sum()
)

print(
    "Maximum events in one session:",
    session_df["event_count"].max()
)

print("\nTop Sessions:")

print(
    session_df[
        [
            "session_id",
            "event_count",
            "total_engagement_time",
            "page_view_count",
            "scroll_count"
        ]
    ]
    .sort_values(
        "event_count",
        ascending=False
    )
    .head(15)
    .to_string(index=False)
)

print("\nFeature Statistics:")

print(
    session_df[
        [
            "total_engagement_time",
            "avg_engagement_time",
            "engagement_per_page_view",
            "event_count",
            "page_view_count",
            "scroll_count",
            "user_engagement_count",
            "entrance_count"
        ]
    ].describe()
)

print("\n✅ Session-level dataset saved successfully!")