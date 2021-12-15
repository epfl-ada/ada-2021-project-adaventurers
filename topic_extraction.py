from data_loader import data_loader, clean_data
from bert import get_year_topics

import pandas as pd
#--------------------------------------------------------#
# Initialize

year = 2016
limits = 8
chunk_ =  100
threshold = 100000

files_to_load = f"quotes-{year}.json.bz2"
data_year = pd.DataFrame()

#--------------------------------------------------------#
# Load data

print("\nBeginning: Loading File\n")

data_year = data_loader("data/"+files_to_load, limit = limits, chunksize_ = chunk_,thrs = threshold)

print("Done: Loading File\n")

#--------------------------------------------------------#
# Bert Topic Analysis

print("\nBeginning: Bert Topic Analysis\n")

topic_assignation, prob_assignation, topic_list= get_year_topics(data_year)

topics_assignation = [element  for month in topic_assignation  for element in month ]
prob_assignation = [element  for month in prob_assignation  for element in month ]

data_year.sort_values(by=['date'], inplace=True, ascending=True)

data_year["topic_number"]=topics_assignation
data_year["topic_prob"]=prob_assignation


print("\nExample of the format")
print(data_year.columns)
print(data_year.head())
print()
print(topic_list.columns)
print(topic_list.head())

print("\nDone: Bert Topic Analysis\n")

#--------------------------------------------------------#
# Saving Topics

print("Saving Data:")
data_year.to_pickle(f"results/bertopic/{year}_quotes_with_topics_{len(data_year)}.pkl")
topic_list.to_pickle(f"results/bertopic/{year}topics_by_month_{len(data_year)}.pkl")
print("Done savings Data")

#--------------------------------------------------------#
# End of topic extractions
print("\nYou can find the results in \"results/bertopic/\" folder")
