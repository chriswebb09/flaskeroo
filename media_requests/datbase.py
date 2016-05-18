import sys
from datetime import datetime
from pymongo import Connection
from pymongo.errors import ConnectionFailure

class DatabaseConnect(oject):
    def __init__(self):
        self.host = 'localhost'
        self.port = 27017

    def connect_db(self):
        try:
            self.connect = Connection(host=self.host, port=self.port)
            print "[*] Connection to database has been established..."
        except ConnectionFailure, e:
            sys.stderr.write("[-] Connection to database: %s could not be established..." % e)
            sys.exit(1)

    def
def main():
    try:
        c = Connection(host='localhost', port=27017)
        print 'Connected successfully.'
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e )
        sys.exit(1)
    dbh = c["mydb"]
    assert dbh.connection == c
    user_doc = {
        "username" : "janedoe",
        "firstname" : "Jane",
        "surname": "Doe",
        "dateofbirth" : datetime(1974, 4, 12),
        "email" : "janedoe74@example.com",
        "score" : 0
    }

    dbh.users.insert(user_doc, safe=True)
    print "Sucessfully inserted document: %s" % user_doc

    print "Sucessfully set up database handle!"

if __name__ == "__main__":
    main()























