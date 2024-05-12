import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv.zip", compression = "zip", index_col=0)

reviews_per_country = pd.DataFrame(reviews.country.value_counts())
avgpts = pd.DataFrame(reviews.groupby("country").points.mean().round(1))

combined = pd.concat([reviews_per_country,avgpts],axis=1,join="inner")
combined.to_csv("reviews-per-country.csv",encoding="utf-8")