import pandas as pd
import numpy as np
import bentoml
import re
import string
import nltk
from nltk.corpus import stopwords

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

import bentoml
from bentoml.io import JSON


df=pd.read_csv("FakeNewsNet.csv")



def clean_text(text):
    """
    Removes:
        - Texts in square brackets
        - Links
        - Punctuations
        - Words containing numbers

    Makes texts lowercase
    """
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def text_preprocessing(text):
    """
    - Tokenizes
    - Remove stopwords 
    - Clean text
    """
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    no_punctuation = clean_text(text)
    
    tokenized_text = tokenizer.tokenize(no_punctuation)
    remove_stopwords = [word for word in tokenized_text if word not in stopwords.words('english')]
    combined_text = ' '.join(remove_stopwords)
    
    return combined_text




df=df[["title","real"]]

df.dropna(axis=0, how='any', inplace=True)
print(len(df))
df['title'] = df['title'].apply(str).apply(lambda x : text_preprocessing(x))


X = pd.DataFrame(df, columns=['title'])
y = df.real
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42)


dv = CountVectorizer()
X_train = dv.fit_transform(X_train.title.values)
X_test = dv.transform(X_test.title.values)


## randomforest
model = RandomForestClassifier(n_estimators=110,
                            max_depth=15,
                            min_samples_leaf=1,
                            random_state=1,
                            class_weight='balanced')
model.fit(X_train, y_train)

y_pred = model.predict_proba(X_test)[:, 1]
print(model.score(X_test, y_test))


bentoml.sklearn.save_model('News_classification',
                            model,     
                            custom_objects={'CountVectorizer': dv}
                            )