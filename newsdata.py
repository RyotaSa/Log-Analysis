#! /usr/bin/env python
import psycopg2


# Question 1
def topArticles():
    # Connect to an database
    conn = psycopg2.connect("dbname = news")
    # Open a cursor to perform database
    cur = conn.cursor()
    # Make a query
    query = """
            Select articles.title, count(*) as views from articles,
             log where log.path = concat('/article/', articles.slug)
             group by articles.title order by views desc limit 3;
            """
    # Execute a command
    cur.execute(query)
    rows = cur.fetchall()
    print('The Most Popular Articles:')
    for i in rows:
        print(i[0] + ' -- ' + str(i[1]) + 'views')
    print ('\n')
    # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()
    return rows


# Question 2
def topAuthors():
    conn = psycopg2.connect("dbname = news")
    # Open a cursor to perform database
    cur = conn.cursor()
    # Make a query
    query = """
            Select authors.name, count(*) as views from articles, log,
             authors where log.path = concat('/article/', articles.slug)
             and articles.author = authors.id group by authors.name
              order by views desc;
            """
    # Execute a command
    cur.execute(query)
    rows = cur.fetchall()
    print('The Most Popular Authors:')
    for i in rows:
        print(i[0] + ' -- ' + str(i[1]) + 'views')
    print ('\n')
    # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()
    return rows


# Question 3
def error():
    conn = psycopg2.connect("dbname = news")
    # Open a cursor to perform database
    cur = conn.cursor()
    # Make some queries with views
    query1 = """
            Create view query1 as select time ::timestamp::date as date,
             count(*) as total from log group by date order by total desc;
            """
    query2 = """
            Create view query2 as select time ::timestamp::date as date,
             count(*) as fail from log where status != '200 OK' group by
             date order by fail desc;
            """
    query3 = """
            Create view query3 as select query2.date,
             cast(query2.fail as decimal)/cast(query1.total as decimal)
             as error from query1, query2 where query1.date = query2.date
             order by error desc;
            """
    query4 = """
            Create view query4 as select query3.date,
             round(100 * (error), 3) as error_percentage from query3
             order by error_percentage desc;
            """
    query5 = """
            Select date, error_percentage from query4
             where error_percentage >= 1;
            """
    # Execute a command
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    cur.execute(query4)
    cur.execute(query5)
    rows = cur.fetchall()
    print('Days in which more than 1% of requests lead to errors:')
    for i in rows:
        print(i[0].strftime('%B %d, %Y') + ' -- ' + str(i[1]) + '% error')
    print ('\n')
    # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()
    return rows


if __name__ == "__main__":
    topArticles()
    topAuthors()
    error()
