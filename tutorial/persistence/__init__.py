import sqlite3

acfun_db = sqlite3.connect("acfun.db")
acfun_db.execute("""
CREATE TABLE IF NOT EXISTS ACFUN_ARTICLE_INFO(
  ARTICLE_ID PRIMARY KEY ,
  TITLE VARCHAR(128) ,
  LINK VARCHAR(128), 
  AUTHOR VARCHAR(128),
  PUBLISH_DATE  VARCHAR,
  INTRODUCTION VARCHAR(1024),
  HINT_COMMENT VARCHAR (128)
) 
""")


def insert_acfun_item(item):
    acfun_db.execute("""
    INSERT INTO ACFUN_ARTICLE_INFO(ARTICLE_ID,AUTHOR, TITLE, LINK, PUBLISH_DATE, INTRODUCTION, HINT_COMMENT) 
    VALUES ('%s','%s','%s','%s','%s','%s','%s')
    """ % (item["article_id"], item["author"], item["title"], item["link"], item["publish_date"], item["introduction"],
           item["hint_comment"]))
    acfun_db.commit()
    pass


def get_connection():
    return acfun_db
