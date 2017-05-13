# logs-analysis
The project it to create a reporting tool that prints out reports (in plain text) based on the data in the database.  
This reporting tool is a Python program using the psycopg2 module to connect to the database.  

The database given has three tables:
1. authors, it contains the authors.
2. articles, it contains the articles that are writen by above authors.
3. log, it includes one entry for each time a user has accessed the site.

And my code will answer the three questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than x% of requests lead to errors?


## Setup the database before running the code:  
```
First unzipe newsdata.sql

$ psql
> CREATE DATABASE news;
> \c news;
> \i newsdata.sql
> \i logs.sql
```

To run the code:  
```
python
>> from logs import *
>> getPopularArticles() # It returns three most popular articles with (name, views)
>> getPopularAuthors()  # It returns a list of the most popular authers (name, views)
>> getErrorRate(<rate>) # It returns a list of days which error rate is higher than the bar (date, rate)
```
