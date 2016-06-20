#import regex
import re
import csv
import pprint
import nltk.classify
import codecs
import plotly.plotly as py
import plotly.graph_objs as go


#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL) 
    return pattern.sub(r"\1\1", s)
#end

#start process_tweet
def processTweet(tweet):
    # process the tweets
    
    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)    
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end 

#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')

    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end

#start getfeatureVector
def getFeatureVector(tweet, stopWords):
    featureVector = []  
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences 
        w = replaceTwoOrMore(w) 
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if it consists of only words
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*[a-zA-Z]+[a-zA-Z0-9]*$", w)
        #ignore if it is a stopWord
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector    
#end

#start extract_features
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features
#end


#Read the tweets one by one and process it
inpTweets = csv.reader(codecs.open('sampleTweets4.csv', 'r','utf-8')) #, delimiter=',', quotechar='|')
stopWords = getStopWordList('stopwords.txt')
count = 0;
featureList = []
tweets = []
for row in inpTweets:
    sentiment = row[0]
    tweet = row[1]
    processedTweet = processTweet(tweet)
    featureVector = getFeatureVector(processedTweet, stopWords)
    featureList.extend(featureVector)
    tweets.append((featureVector, sentiment));
#end loop

# Remove featureList duplicates
featureList = list(set(featureList))

# Generate the training set
training_set = nltk.classify.util.apply_features(extract_features, tweets)

# Train the Naive Bayes classifier
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)

# Test the classifier

'''testTweet = 'Good night #Twitter and #TheLegionoftheFallen.  5:45am cimes awfully early!'
processedTestTweet = processTweet(testTweet)
sentiment = NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet, stopWords)))
print("testTweet = %s, sentiment = %s\n" % (testTweet, sentiment))'''
'''
fp = codecs.open('sampleit.txt', 'r','utf-8')
testTweet = fp.readline()
#testTweet = 'Its very very good product'
for w in te:
    print(w)
    processedTestTweet = processTweet(w)
#processedTestTweet = processTweet(fp)
    sentiment = NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet, stopWords)))
    print("testTweet = %s, sentiment = %s\n" % (w, sentiment))
fp.close()
'''
p=0
n=0
ne=0
f = open('samj7.txt')
## Read the first line 
line = f.readline()

## If the file is not empty keep reading line one at a time
## till the file is empty
while line:
    #print(line)
    line = f.readline()
    processedTestTweet = processTweet(line)
#processedTestTweet = processTweet(fp)
    sentiment = NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet, stopWords)))
    print("testTweet = %s, sentiment = %s\n" % (line, sentiment))
    if sentiment=='positive':
        p=p+1;
    if sentiment=='negative':
        n=n+1;
    if sentiment=='neutral':
        ne=ne+1;
f.close()
p=p-1
print("positive==>",p)
print("negative==>",n)
print("neutral==>",ne)
total=p+n+ne

pn=(p/total)*100
nn=(n/total)*100
nen=(ne/total)*100



print("% positive==>",pn)
print("% negative==>",nn)
print("% neutral==>",nen)



fig = {
    'data': [{'labels': ['Positive', 'Negative', 'Neutral'],
              'values': [pn, nn, nen],
              'type': 'pie'}],
    'layout': {'title': 'pie chart for samsung J7 '}
     }

plot_url = py.plot(fig, filename='samsung J7')


