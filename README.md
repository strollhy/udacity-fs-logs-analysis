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
> \q
```


## Example of output:
```python
>>> from logs import *
>>> getPopularArticles()
["'Candidate is jerk, alleges rival' - 338647 views", "'Bears love berries, alleges bear' - 253801 views", "'Bad things gone, say good people' - 170098 views"]
>>> getPopularAuthors()
['Ursula La Multa - 507594 views', 'Rudolf von Treppenwitz - 423457 views', 'Anonymous Contributor - 170098 views', 'Markoff Chaney - 84557 views']
>>> getErrorRate(1)
['07,17,2016 - 2.26% errors']
```