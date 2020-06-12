from nltk.corpus import stopwords


def clean_string(string):
    my_punc = ['!', '"', '#', '$', '%', '&', '\\', '(', ')', '*', '+', ',', '-', '.', '/',
               ':', ';', '<', '=', '>', '?', '@', '\[', '\]', '^', '_', '`', '{', '|', '}', '~']

    """
    1. Tokenize Words
    2. Remove Punctuation
    3. Remove Stop Words
    """
    nopunc_list = (
        ''.join(char for char in string if char not in my_punc)).split()
    del_stopwords = [word for word in nopunc_list if word.lower(
    ) not in stopwords.words('english')]
    return del_stopwords
