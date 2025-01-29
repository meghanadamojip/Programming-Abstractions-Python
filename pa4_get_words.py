#===== Problem B function begins
# follow the instruction below
# DO NOT change the function signature!
def getTopWords(words: 'List[str]', K: int) -> 'List[str]':
    '''
    - Parameters:
      - words: a list of words
      - K: The number of words to return (K most frequent words)
    - Returns:
      - List[str]: list of words sorted by the frequency from highest to lowest
    '''
    #===== Your implementation begins here
    words = [word.lower() for word in words]  # converting all uppercase words to lowercase

    # Filter out the stop words
    words = [word for word in words if word not in STOPWORDS]  # filtering out all the STOPWORDS as given in template code

    word_dict = {}  # creating a dictionary for frequency of words
    for word in words:  # using for loop to traverse through words
        if word in word_dict:  # if in the dictionary, increment frequency
            word_dict[word] += 1
        else:
            word_dict[word] = 1  # if not, initialize to 1

    # Returning K most frequent words sorted by frequency
    frequent_words = sorted(word_dict, key=word_dict.get, reverse=True)[:K]
    return frequent_words
    #===== Your implementation ends here

