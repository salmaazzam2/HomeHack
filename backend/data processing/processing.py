import pandas as pd

df = pd.read_csv("backend/data/Copy of Housing_Pipeline_Long_List_External_Hackathon(Longlist).csv", 
                encoding="latin1",
                usecols=["Project Name ", "Pipeline First Cut ", "Number Of Units ", "Planning  Status ", "One Line Summary "]
                )
print(df)