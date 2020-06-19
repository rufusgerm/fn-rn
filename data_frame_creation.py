import pandas as pd
from text_to_num_processing import *
import datetime


# Create each numerical dataframe from dataframe input
def create_num_df(dataframe):
    """
    Takes in a non-numerical dataframe (can be a subset) 
    of news articles and returns a numerical dataframe
    """
    if not isinstance(dataframe, pd.DataFrame):
        dataframe = convert_to_df(dataframe)
    df = pd.DataFrame()
#  Intro:
    print(f'\nBeginning Processing Of Dataframe')
    print(f'=================================')
    t_0 = datetime.datetime.now()
#  1.
    df['title_len'] = dataframe.title.apply(len)
    t_1 = datetime.datetime.now()
    print(
        f'...Title Length Processing Completed In... {diff_time_in_ms(t_1,t_0)}ms\n')
#  2.
    df['title_unique'] = dataframe.title.apply(unique_words)
    t_2 = datetime.datetime.now()
    print(
        f'...Unique Title Words Processing Complete... {diff_time_in_ms(t_2,t_1)}ms\n')
#  3.
    df['text_len'] = dataframe.text.apply(len)
    t_3 = datetime.datetime.now()
    print(
        f'...Text Length Processing Complete... {diff_time_in_ms(t_3,t_2)}ms\n')
#  4.
    df['text_unique'] = dataframe.text.apply(unique_words)
    t_4 = datetime.datetime.now()
    print(
        f'...Unique Text Words Processing Complete... {diff_time_in_ms(t_4,t_3)}ms\n')
#  5.

    df['avg_sentence_len'] = dataframe.text.apply(avg_sent_len)
    t_5 = datetime.datetime.now()
    print(
        f'...Average Sentence Length Processing Complete... {diff_time_in_ms(t_5,t_4)}ms\n')
#  6.
    df['neg'], df['neu'], df['pos'] = zip(*dataframe.text.apply(sent_analysis))
    t_6 = datetime.datetime.now()
    print(
        f'...Sentiment Analysis Complete... {diff_time_in_ms(t_6,t_5)}ms\n\n')

    return df


def convert_to_df(tup_or_series):
    if isinstance(tup_or_series, pd.Series):
        # Convert series to df
        new_df = pd.DataFrame(
            {'title': [tup_or_series.values[0]], 'text': [tup_or_series.values[1]]})
    elif isinstance(tup_or_series, tuple):
        # Convert tuple to df
        new_df = pd.DataFrame(
            {'title': [tup_or_series[0]], 'text': [tup_or_series[1]]})
    return new_df


def diff_time_in_ms(datetime_new, datetime_old):
    return ((datetime_new - datetime_old).total_seconds())*1000
