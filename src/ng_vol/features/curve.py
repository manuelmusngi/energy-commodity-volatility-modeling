def curve_slopes(df):
    df["m1_m3"] = df["M3"] - df["M1"]
    df["m1_m12"] = df["M12"] - df["M1"]
    return df
