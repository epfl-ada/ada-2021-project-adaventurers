##################### IMPORTS #####################

# Useful for chronological ordering
from datetime import datetime, date ,time

# Exploratory Analysis
from wordcloud import WordCloud , STOPWORDS

#To do initial data handling
from gensim.utils import simple_preprocess
import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
from nltk.corpus import stopwords

# Import sentence transformer
from sentence_transformers import SentenceTransformer

# bertopic
from bertopic import BERTopic

# Used to store results
import pandas as pd
import numpy as np


def get_slice(df_quotes,month):

    # Sort by date
    if len(df_quotes)>0:
        df_quotes.sort_values(by=['date'], inplace=True, ascending=True)
        df_quotes = df_quotes[df_quotes.date.dt.month == month] # The 2016 United States elections were held on Tuesday, November 8, 2016, let's look around this period (this month)
        #df_quotes = df_quotes[df_quotes.date.dt.day <= MONTHS_DAY[month]]
        #df_quotes = df_quotes[df_quotes.date.dt.day >= 0]

    return df_quotes


def prep_data(df_quotes):

    df_quotes = df_quotes["quotation"].squeeze().tolist()

    return df_quotes

def get_topics_bert(docs):
    topic_model = BERTopic() # call BERTopic
    topics, probs = topic_model.fit_transform(docs)
    return topics,probs,topic_model

def topics_by_month(df_month,month,n_topics):

    #prepare the df quotes DataFrame
    docs = prep_data(df_month)

    # Calls bert topic
    topics,probs,topic_model = get_topics_bert(docs)

    # Initialize list
    tmp_list = []
    topics_numerotation = []

    for i in range(len(topic_model.get_topic_info())):
        tmp_list.append(topic_model.get_topic(i))
        topics_numerotation.append(topic_model.get_topic_info().iloc[i].Topic)

    # DataFrame of topics
    topics_month = topic_model.get_topic_info().copy()
    topics_month["Words"] = tmp_list
    topics_month["Topic"] = (np.array(topics_numerotation) + n_topics).tolist() # consistency with precedent topics
    topics_month["Month"]=month

    # Keeps consistency with topics assinged
    topic_assigned = (np.array(topics) + n_topics).tolist()
    probs_assigned = probs

    # Keep track of the number of topics
    n_topics+=len(tmp_list)

    return topics_month, topic_assigned, probs_assigned, n_topics

def get_year_topics(df_quotes):

    topic_assignation= []
    prob_assignation = []
    topic_df = pd.DataFrame(columns=["Topic", "Count", "Name", "Words", "Month"])
    months = range(1,13)
    n_topics = 0

    print("Year analysis:")

    for month in months:

        df_month = get_slice(df_quotes,month)

        print(f"    month: {month}, number of quotes: {len(df_month)}")
        if len(df_month) > 10 :

            topics_month, topic_assigned, probs_assigned, n_topics = topics_by_month(df_month,month,n_topics)

            topic_df = pd.concat([topic_df,topics_month],ignore_index=True)
            topic_assignation.append(topic_assigned)
            prob_assignation.append(probs_assigned)

    return topic_assignation, prob_assignation, topic_df
