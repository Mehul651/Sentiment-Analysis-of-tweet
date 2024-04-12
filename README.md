# How users can make sense of their social Network #

Welcome to our repository dedicated to helping you understand your social network better through sentiment analysis. In today's digital world, it's essential to grasp the feelings and opinions hidden within our online interactions.

Sentiment analysis is like a superpower that helps us uncover the emotions and attitudes expressed in social media posts. By using advanced technology, we can see trends, find out who's influential, and understand how people feel overall.

While sentiment analysis is great, there are other ways to understand social networks too, like looking at connections between people, categorizing content, or finding common topics. In this repository, we'll explore these methods to give you a complete toolkit for understanding your social circle.

# Dataset # 
This dataset comprises of 1.6 million tweets which are extracted using twitter API, these tweets have been already labeled as per sentiments (0 = negative, 4 = positive, 2 = neutral) and contains six total columns, target = polarity of tweets (positive, negative , neutral), id = The id of tweet, date: the date when the tweet was uploaded, flag: The query (lyx) and if there is no query this value is NO_QUERY, user: the name of the user, and text: The actual tweet. 
After the dataset is been extracted three ML models were build to predict future sentiments of statement
To showcase the analysis of sentiments through models a flask application has been created where user can input any statement and it will show sentiment from all three models 

# Data Preprocessing # 
The first step to start with sentiment analysis involves, data preprocessing. The data preprocessing techniques include: 
- Removing noise such as special character, URLs, and hashtags
- Tokenizing texts into individual words or phrases
- Normalizing texts by converting it into lowercase
- Removing stopwords (words that do not carry any meaning)

After the data is preprocessed some visualisations were performed for better understanding of the dataset. 

Lateron the data was split into training and testing to evaluate the performance of sentiment analysis for better accuracy

# Model creation # 
In this project we have concentrated on three main models for predicting sentiments of the texts. Those are: 
- Logistic Regression
- Naive Bayes theorem
- Linear Support Vector

After these models were created and trained, models are saved and loaded, this is necessary because it helps for faster running of the code and easy for deployment. And the saved model is then used in the flask application. 

# Output # 
After the models were trained and saved a basic flask application was created where in any user can input texts and hit analyze. The trained models will then predict the sentiment of the statement. 


# Purpose and Conclusion # 
The main purpose of this project was how can social media be made better for users, and what necessary steps could developers take to make it more engaging. By taking an idea from this small project of "Sentiment Analysis" developers on large scale can implement this to make interaction on social media much more interesting. People will always see what they want to see and what they like to see. More relatable content would be shown. In this project we have taken an example of textual data, we could also use image and audio based data, so whenever a user posts something about any topic on social media, the algorithm will show him similar to whatever he/she has posted moreover leading to categorizing people with similar interest.  
