import sqlite3
import Hasher

class LoginManager():
    def __init__(self,database):
        self.db=sqlite3.connect(database)
        cur=self.db.execute('select user,password from users')
        self.couples=(dict(username=row[0], password=row[1]) for row in cur)

    def UserLogin(self,username,password):
        for user in self.couples:
            if user['username']==username and user['password']==Hasher.hash(password):
                return True
                break
        else:
            return False
        
    def UserExists(self,user_):
        for user in self.couples:
            if user['username']==user_:
                return True
                break
        else:
            return False

    def UserInsert(self,username,password):
        if not self.user_exists(username):
            self.db.execute('insert into users (user,password) values (?,?)',[username,Hasher.hash(password)])
            self.db.commit()
            return True
        else:
            return False

