
![Elon Musk vs Stocks](https://inteng-storage.s3.amazonaws.com/img/iea/bjOLrKEe6e/sizes/elon-musk-tweet-stock-high-420_resize_md.jpg)
##### Image credit [interesting Engineering](https://interestingengineering.com/teslas-stock-hits-420-elon-musk-tweets-the-stock-is-so-high)

# Tesla Stocks Vs Elon Musk's Tweets

Here we are taking Tesla Stock data and Elon Musk's tweets. We are Extracting the data, transforming it, and loading it into a SQL database.

You can access the Tesla Stock Data [here](Resources/TSLA.csv).

The first 3/4's of Elon's tweets can be found [here](Resources/ElonTweets_2010-2017.csv).

The rest of his tweets are [here](Resources/ElonTweets_2017-2020.jsonl).

-----------

## Where is the data coming from? 
[Tesla's stock data](https://www.kaggle.com/timoboz/tesla-stock-data-from-2010-to-2020) and the first third of [Elon's tweets](https://www.kaggle.com/kingburrito666/elon-musk-tweets) are from Kaggle. 

The last bit of [Elon's tweets](https://data.world/barbaramaseda/elon-musk-tweets/workspace/file?filename=user-tweets.jsonl) are from Data World.



-----------------------------
## Where is the data going to?

We will be putting it all into a sqlite database using sqlalchemy. 

-------------------------
## How will the data be structured?

</br>The Stock Data will have its own table and be structured as follows:

### Stocks

Date | Open | Close | Percent Change
------------ | ------------- | ------------ | ---------
Date | Float | Float | Float
</br>
</br>The Tweet Data will have its own table and be structured as follows:

### Tweets

Date | Time | Tweet
--- | --- | ---
Date | Time | String

------------------------

## What tasks must be carried out?

* Brandon Damore - Cleaning the stock data and calculating the percent change for each day.
* Kellie Cox - Combine the two tweet datasets and make sure there is no overlap.
* Laura Bullard - Creating the database and the schema.
