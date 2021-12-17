# Creating an event time-line from 2015 to 2020 using only newspaper quotes


## The data story website: **https://estersimkova.github.io/ADAventurers_proj/**

## Authors

The ADAventurers - Lucas Brunschwig, Ioannis Mavrothalassitis, Axelle Piguet, Ester Simkova, in the framework on the EPFL Applied Data Analysis course (CS-401)

## Table of contents

0. [Abstract](#1)
1. [Research Questions](#2)
2. [Methods](#3)
3. [Individual contributions](#4)

## 0. Abstract: <a name="1"></a>

Our project goals are two-fold:

- First, we would like to use the quotes from 2015 to 2020 in the QuoteBank dataset to create a time-line of major events that occurred in the world during this period. We plan on doing this by finding some “hot topics” emerging from the quotes. Once we have created the time-line, we will compare it to an external time-line and see if it corresponds.
- Then, once we have created this time-line of events, we would like to do a sentiment analysis on the quotes regarding a certain topic before and after an event occurred, to see if the general sentiment changes, in general and in the country where the event occured. We are not fixed on a topic nor event for now, since we have to see which events emerge from the time-line.

The motivation behind the project is to be able to see if quotes in newspapers are really representative of the events happening in the world and how an event highly covered in the news can shift the sentiment regarding its domain.

## 1. Research Questions: <a name="2"></a>

As said above, our research questions are the following:

1. Are newspapers’ quotes representative of events occurring in the world ? Meaning, can we deduce a time-line of important events that happened in the world during a certain time-frame only from topics emerging from newspaper quotes ?
2. When an important event occurs, does the general sentiment from quotes regarding the topic evolve ? We will take a more concrete example of an event when we have our re-created time-line.


## 2. Methods: <a name="3"></a>

#### Finding topics from quotes

The Quotebank dataset provides more than 100 millions quotes over 12 years. We decided to focus on the years 2015-2020. For each of these years, we selected a maximum of 100’000 quotes each month. Then, we used the NLP (natural language processing) model [BERTopic](https://github.com/MaartenGr/BERTopic) to extract the topics and associate each quote to a specific topic with a given probability. Using the 20 monthly hottest topics, meaning the ones that have the most quotes associated with them, we looked into the quotes associated with the topic with the most probability.
Using this information, we chose for each month the most meaningful topics to be kept.
Then, we created a script to visually represent the chosen topics on a time-line for every year.

#### Analysing the sentiment change before and after an event

To answer the second question, and so to perform sentiment analysis, we used a [fine-tuning algorithm for BERT](https://skimai.com/fine-tuning-bert-for-sentiment-analysis/), training the BERT sentiment classifier with data from Twitter - using 1700 complaining (negative sentiment) and 1700 non-complaining (positive sentiment) tweets. We then passed our quotes, previously regrouped into topics by BERTopic, into the trained BERT sentiment classifier and observed the evolution in percentage of positive vs negative quotes regarding a certain topic, before and after certain events occurred.


## 3. Individual contributions: <a name="4"></a>

- Lucas Brunschwig: data creation, notebook manager, topic extraction and analysis
- Ioannis Mavrothalassitis: sentiment analysis
- Axelle Piguet: time-line creation 
- Ester Simkova: website creation, help with topic extraction and sentiment analysis

