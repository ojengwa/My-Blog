from sqlite3 import connect
from time import ctime

def save(author, pid, title, content):
    con = connect('Models/blog.db')
    c = con.cursor()
    time = str(ctime())
    c.execute("INSERT INTO posts VALUES ('%s', '%s', '%s', '%s', '%s')" % (author, pid, title, content, time))
    con.commit()

    con.close()

    return True, pid

def delete(uid, pid):
    con = connect('Models/blog.db')
    c = con.cursor()

    c.execute("DELETE FROM blog WHERE id = '%s' AND uid = '%s')" % (author, pid, title))
    con.commit()

    con.close()
    return True
