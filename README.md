# Creating an event time-line from 2015 to 2020 using only newspaper quotes


## The data story website: **https://estersimkova.github.io/ADAventurers_proj/**

## Authors

The ADAventurers - Lucas Brunschwig, Ioannis Mavrothalassitis, Axelle Piguet, Ester Simkova, in the framework on the EPFL Applied Data Analysis course (CS-401)

## Table of contents

0. [Abstract](#1)
1. [Research Questions](#2)
2. [Methods](#3)
3. [Individual contributions](#4)
4. [Repository Organisation](#5)

## 0. Abstract: <a name="1"></a>

The motivation behind the project is to be able to see if quotes in newspapers are really representative of the events happening in the world and how an event highly covered in the news can shift the sentiment regarding its domain.

## 1. Research Questions: <a name="2"></a>

Our research questions are the following:

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



## 4. Repository Organisation:

Main_branch: 
- [arrows_timeline:](https://github.com/epfl-ada/ada-2021-project-adaventurers/tree/master/arrows_timeline) folder containing the png images to plot nice timeline
- results: folder which contains two subfolders with different results
  - [figures:](https://github.com/epfl-ada/ada-2021-project-adaventurers/tree/master/results/figures) contains the topic analysis figures generated by the notebook and integrated in the website
  - [top_topics:](https://github.com/epfl-ada/ada-2021-project-adaventurers/tree/master/results/top_topics) contains a file for each year, inside each file you will find the most hot topics for each month and the top 6 quotes associated
  - [Adaventurers-Project:](https://github.com/epfl-ada/ada-2021-project-adaventurers/blob/master/Adaventurers-Project.ipynb) the unique notebook that covers our entire journey inside the project, the notebook can be ran independently of the rest, you just need to add the data and directory indicated below


## 5. Additional Data:

The notebook is made to be ran with two types of data if you want to run it entirely. 

### 5.1 Raw Data
The first part of the notebook is used to generate the topics classification from the raw data. if you. You can load the quotes-xxxx.json.bz2 on [here](https://zenodo.org/record/4277311#.Ybz7l2jMJPY) and should be put in a folder called "data" in the main repository

### 5.2 Processed Data
The second part of the notebook should be run with the processed data. Each year consists of 2 files, one with the topics and their definition (xxxx_topics_by_month) and one for the quotes associated with the topic number and the probability to be associated to the same topic (xxxx_quotes_with_topic). These data needs to be put in the results folder inside a folder called "bertopic". They can be found [here](https://drive.google.com/drive/folders/1NuLnwk5nhxyMmiGOKBniL6AWK3uuE0cd?usp=sharing)

