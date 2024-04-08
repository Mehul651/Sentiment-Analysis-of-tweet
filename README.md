**How users can make sense of their social Network **

Welcome to our repository dedicated to helping you understand your social network better through sentiment analysis. In today's digital world, it's essential to grasp the feelings and opinions hidden within our online interactions.

Sentiment analysis is like a superpower that helps us uncover the emotions and attitudes expressed in social media posts. By using advanced technology, we can see trends, find out who's influential, and understand how people feel overall.

While sentiment analysis is great, there are other ways to understand social networks too, like looking at connections between people, categorizing content, or finding common topics. In this repository, we'll explore these methods to give you a complete toolkit for understanding your social circle.

**Dataset** 
This dataset comprises of 1.6 million tweets which are extracted using twitter API, these tweets have been already labeled as per sentiments (0 = negative, 4 = positive, 2 = neutral) and contains six total columns, target = polarity of tweets (positive, negative , neutral), id = The id of tweet, date: the date when the tweet was uploaded, flag: The query (lyx) and if there is no query this value is NO_QUERY, user: the name of the user, and text: The actual tweet. 
After the dataset is been created three ML models have been build to predict future sentiments of statement
To showcase the analysis of sentiments through models a flask application has been created where user can input any statement and it will show sentiment from all three models

