from time import ctime
from Models.Posts import *

def create(form):
    title = form['title'].value
    author = form['uid'].value
    time = str(ctime())
    pid = str(hash(author + time))
    content = form['content'].value
    return save(author, pid, title, content)

    
def delete(path):
    temp = path[1:]
    parts = temp.split('/')
    uid = parts[0]
    pid = parts[1]
    return delete(uid, pid)
