import pandas as pd

def load_data():
    df = pd.read_csv(
        "backend/data/Copy of Housing_Pipeline_Long_List_External_Hackathon(Longlist).csv",
        encoding="latin1",
        usecols=[
            "Project Name ",
            "Pipeline First Cut ",
            "Number Of Units ",
            "Planning  Status ",
            "One Line Summary "
        ]
    )
    return df


def smart_filter(df, column, user_value):
    return df[df[column].astype(str).str.lower().str.contains(user_value.lower())]


