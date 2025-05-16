import pandas as pd

def load_data() :
    return pd.read_csv("data/health_information_2023.csv")

def drink() :
    df = load_data()
    tp = df.groupby("음주여부").size()

    return tp