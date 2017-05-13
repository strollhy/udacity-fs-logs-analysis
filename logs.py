#!/usr/bin/env python
#
# logs.py -- implementation of logs analysis system
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")


def getPopularArticles():
    """Return the most popular 3 articles"""
    db = connect()
    db_cursor = db.cursor()
    query = "SELECT * FROM popular_articles;"
    db_cursor.execute(query)
    results = db_cursor.fetchmany(3)
    db.close()
    if results:
        return results


def getPopularAuthors():
    """Return the most popular authors"""
    db = connect()
    db_cursor = db.cursor()
    query = "SELECT * FROM popular_authors;"
    db_cursor.execute(query)
    results = db_cursor.fetchall()
    db.close()
    if results:
        return results


def getErrorRate(rate):
    """Return the days on which error rate excceeds a bar

    Args:
      rate: the error rate bar
    """
    db = connect()
    db_cursor = db.cursor()
    query = "SELECT * FROM error_rates WHERE error_rate > %s;" % rate
    db_cursor.execute(query)
    results = db_cursor.fetchall()
    db.close()
    if results:
        return results
