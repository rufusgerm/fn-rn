import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
from statistics import mean

nltk.download('stopwords')
nltk.download('vader_lexicon')


PARTIAL_PUNC = ['@', '!', '"', '#', '$', '%', '&', '\\',
                '(', ')', '*', '+', ',', '-', '/', ':', ';', '<', '=', '>', '?', '@', '\[', '\]', '^', '_', '`', '{', '|', '}', '~']
WHOLE_PUNC = ['.'] + PARTIAL_PUNC


# Get Unique Number Of Words From The Length Of A Counter Dict
# Which Is Sourced From A List Of All Words Within The Input String
def unique_words(input_str):
    return len(Counter(collect_all_words(input_str)))


# Individuates All Words Within The Input String Ignoring Stopwords And Coallesces Them Into A List
def collect_all_words(string):
    whole_nopunc_list = (
        ''.join(char for char in string if char not in WHOLE_PUNC)).split()
    return [word for word in whole_nopunc_list if word.lower() not in stopwords.words('english')]


# Returns The Mean Sentence Length Of The Input String
def avg_sent_len(input_str):
    sent_len_list = len_of_sentence(input_str)
    return round(mean(sent_len_list))


# Returns A List Of The Lengths Of All Sentences Within The Input String
# First Removes Unnecessary Punctuation And Then Counts Sentence Lengths By Period Placement
def len_of_sentence(input_str):
    part_nopunc_list = (
        ''.join(char for char in input_str if char not in PARTIAL_PUNC)).split()
    sentence_len = []
    count = 0
    for word in part_nopunc_list:
        count = count + 1
        if word[-1] == '.':
            sentence_len.append(count)
            count = 0
    sentence_len = [num for num in sentence_len if num > 2]
    return sentence_len


# Get three values of sentiment analysis
def sent_analysis(input_str):
    sid = SentimentIntensityAnalyzer()
    test = sid.polarity_scores(input_str)
    s_list = list(test.values())[:-1]
    return s_list[0], s_list[1], s_list[2]
