
import pandas as pd
import numpy as np
import random as rd

def data_loader(path,limit=0,chunksize_=10000,thrs = 100000):
    """ Description: this function will load data for each file and specified path

        Parameters:
        -----------
        path: path of the json file compressed with bz2
        limit: will limit the number of chunck loaded if bigger than 0
        chunksize_ = the number of quotes extracted for each chunk

        Total number of quotes = limit*chunksize_
        if you want to load all quotes put limit = 0

        Outputs:
        --------
        df_quotes: pandas dataframe quotes with necessary columns

    """
    eps=1e-1 # precision for progression

    print(f"\nLoading file: \"{path}\"")
    print("Beginning: Loading Quotes...")


    df_reader = pd.read_json(path, lines=True, compression='bz2', chunksize = chunksize_, nrows=1e12) # here we only loaded the quotes from 2016, but we can simply change the year to have the others

    for i,chunk in enumerate(df_reader):

        # Keep track of progression
        if limit!=0 and (i/limit%0.1<eps):
            # Chunk loading
            print(f"    Loading... {i/limit*100:.2f} %")

        # We don't want to read it all as long as we do not have the final code
        if i>=limit and limit!=0:
            break



    # Initialize the DataFrame columns with first chunk
        if i == 0:
          df_quotes = pd.DataFrame(chunk)
        else:
          # Concatenation of new chunk into the DataFrame
           df_quotes = pd.concat([df_quotes,chunk])




    df_quotes = clean_data(df_quotes)

    df_quotes = consistency(df_quotes,thrs)

    print(f"Number of quotes loaded in {path}:", len(df_quotes))

    return df_quotes


def consistency(df_quotes, thrs):

    sizes = data_by_month(df_quotes)

    for i,size_month in enumerate(sizes):
        limit_quotes = thrs

        if size_month > limit_quotes:

            n_to_drop = size_month-limit_quotes
            index_ = df_quotes[df_quotes.date.dt.month == i+1].index
            index_to_drop = rd.sample(list(index_.values),k=n_to_drop)
            df_quotes.drop(index_to_drop,inplace=True)

    return df_quotes

def data_by_month(df_quotes):

    size = []
    for month in range(1,13):
        df_month = df_quotes[df_quotes.date.dt.month == month]
        size.append(len(df_month))


    return size


def clean_data(data):
    """ Description: this function will load data for each file and specified path

        Parameters:
        -----------
        data: pandas dataframe from the quotebank datasets

        Outputs:
        --------
        df_quotes: pandas dataframe quotes without the phase and qids columns

    """
    eps=1

    # Drop duplicated rows
    data.drop_duplicates(subset="quoteID")

    # Drop columns: phase and qids that are not of interest to us
    data.drop(columns=['phase','qids'])

    return data
