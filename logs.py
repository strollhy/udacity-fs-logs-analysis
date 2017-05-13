#!/usr/bin/env python
#
# logs.py -- implementation of logs analysis system
#

import psycopg2


def connect(database_name="news"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Failed to connect the database.")


def getPopularArticles():
    """Return the most popular 3 articles"""
    db, cursor = connect()

    query = "SELECT * FROM popular_articles;"
    cursor.execute(query)
    results = cursor.fetchmany(3)
    db.close()
    if results:
        return ["'{0[0]}' - {0[1]} views".format(r) for r in results]


def getPopularAuthors():
    """Return the most popular authors"""
    db, cursor = connect()

    query = "SELECT * FROM popular_authors;"
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    if results:
        return ["{0[0]} - {0[1]} views".format(r) for r in results]


def getErrorRate(rate):
    """Return the days on which error rate excceeds a bar

    Args:
      rate: the error rate bar
    """
    db, cursor = connect()

    query = "SELECT * FROM error_rates WHERE error_rate > %s;" % rate
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    if results:
        return ["{0[0]:%m,%d,%Y} - {0[1]:.2f}% errors".format(r) for r in results]
