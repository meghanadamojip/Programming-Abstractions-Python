# keep this section as is
STOPWORDS = [
'i','me','my','myself','we','our','ours','ourselves','you','your','yours',
'yourself','yourselves','he','him','his','himself','she','her','hers',
'herself','it','its','itself','they','them','their','theirs','themselves',
'what','which','who','whom','this','that','these','those','am','is','are',
'was','were','be','been','being','have','has','had','having','do','does',
'did','doing','a','an','the','and','but','if','or','because','as','until',
'while','of','at','by','for','with','about','against','between','into',
'through','during','before','after','above','below','to','from','up','down',
'in','out','on','off','over','under','again','further','then','once','here',
'there','when','where','why','how','all','any','both','each','few','more',
'most','other','some','such','no','nor','not','only','own','same','so',
'than','too','very','s','t','can','will','just','don','should','now'
]
#===== Provided Global variables section ends
#===== Helper classes/functions section begins
# You may add your own classes or functions within this section
# **class** and **function** only!
# any statement that is not encapsulated inside a class or function
# may result in 0 grade
#===== Helper classes/functions section ends
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
words = [word.lower() for word in words] #converting all upercase words to
lowercase
# Filter out the stop words
words = [word for word in words if word not in STOPWORDS] #filtering out all
the STOPWORDS as given in template code
word_dict = {} #creating a dictionary for frequency of words
for word in words: #using for loop traverse through words
if word in word_dict: #if in the dictionary add to frequency
word_dict[word] += 1
else:
word_dict[word] = 1 #if not leave as is
frequent_words = sorted(word_dict, key=word_dict.get, reverse=True)[:K]
#returning K, the most frequent words
return frequent_words
