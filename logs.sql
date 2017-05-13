CREATE VIEW popular_articles AS
    SELECT title, count(*) AS views FROM log
    JOIN articles ON log.path LIKE CONCAT('%', articles.slug)
    GROUP BY title
    ORDER BY views DESC;

CREATE VIEW popular_authors AS
    SELECT name, count(*) AS views FROM authors
    JOIN articles ON articles.author = authors.id
    JOIN log ON log.path LIKE CONCAT('%', articles.slug)
    GROUP BY name
    ORDER BY views DESC;

CREATE VIEW visit_count AS
    SELECT CAST(time AS DATE) AS date , count(*) AS visits FROM log
    GROUP BY date
    ORDER BY date DESC;

CREATE VIEW error_count AS
    SELECT CAST(time AS DATE) AS date , count(*) AS errors FROM log
    WHERE log.status <> '200 OK'
    GROUP BY date
    ORDER BY date DESC;

CREATE VIEW error_rates AS
    SELECT visit_count.date, errors * 100.0 /visits AS error_rate FROM visit_count
    JOIN error_count
    ON error_count.date = visit_count.date
    ORDER BY visit_count.date DESC;
