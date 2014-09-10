from Models.Users import Users


users = Users()
def handler(arr):
    if arr.has_key('fname'):
        fname = arr['fname'].value
        lname = arr['lname'].value
        email = arr['user'].value
        password = arr['pass'].value

        email = email.strip()
        password = password.strip()

        uid, name, true = users.signup(fname, lname, email, password)
        return uid, name, true
    else:
        email = arr['user'].value
        password = arr['pass'].value

        email = email.strip()
        password = password.strip()

        uid, name, true = users.login(email, password)
        return uid, name, true

def logout(temp):
    logId = uid.strip()
    return users.logout(logId)
    
