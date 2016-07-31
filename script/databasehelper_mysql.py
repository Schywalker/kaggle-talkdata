          #database class
import pymysql as MySQLdb
import sys

class DbHelper:
    global host
    global port
    global user
    global passwd
    global dbname
    global charset

    host = "west2-mysql-instance1.ctrzwyr54voz.us-west-2.rds.amazonaws.com"
    port = 3306
    user = "awsuser"
    passwd = "nellierova"
    #host = "localhost"
    #user = "root"
    dbname = "db_talkdata"
    charset='utf8mb4'

    COLUMN_GENDER = 'gender'
    COLUMN_AGE = "age"
    COLUMN_GROUP = "group"
    COLUMN_PHONE_BRAND = "phone_brand"
    COLUMN_DEVICE_MODEL = "device_model"
    COLUMN_DEVICE_COUNT = "count"

    TBL_AGE_BRAND = "tbl_age_bran"

    def __init__(self):
        status = self.connect_db()

    def connect_db(self):
        try:
            self._db = MySQLdb.connect(host = host, user = user, 
                                 passwd = passwd, port = port, db = dbname, charset = charset)
            self._cursor = self._db.cursor()        
            self._cursor.execute("SELECT VERSION()")
            results = self._cursor.fetchone()
            # Check if anything at all is returned
            if results:
                return True
            else:
                return False
        except MySQLdb.Error, e:
            try:
                print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                print "MySQL Error: %s" % str(e)
                # Print results in comma delimited format
                print "ERROR IN CONNECTION" + str(MySQLdb.Error)
        return False

    def get_connection(self):
        return self._db

    def execute(self, query, params):
        c = self._db.cursor()
        status = c.execute(query, params)
        self._db.commit()
        return status

    def close(self):
      if self._db is not None:
        self._db.close()

    def main():
        main


if __name__ == "__main__":
    main()

    