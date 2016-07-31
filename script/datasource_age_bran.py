import databasehelper_mysql as dbhelper
from databasehelper_mysql import DbHelper
import pandas


class TblAgeBrand:

    COLUMN_GENDER = DbHelper.COLUMN_GENDER
    COLUMN_AGE = DbHelper.COLUMN_AGE
    COLUMN_GROUP = DbHelper.COLUMN_GROUP
    COLUMN_PHONE_BRAND = DbHelper.COLUMN_PHONE_BRAND
    COLUMN_DEVICE_MODEL = DbHelper.COLUMN_DEVICE_MODEL
    COLUMN_DEVICE_COUNT = DbHelper.COLUMN_DEVICE_COUNT

    def __init__(self):
        self._db = dbhelper.DbHelper()
        self._tblname = DbHelper.TBL_AGE_BRAND

    def open_conn(self):
        self._db = dbhelper.DbHelper()

    def read_sql_to_dataframe(self):
        sql = ("SELECT * " + " FROM " + self._tblname 
            # + " WHERE " + COLUMN_PLAYERID + " NOT IN ('" + "','".join(map(str, list_players))
            # + "')" 
            #+ " GROUP BY " + group_column_names_string
            )
        df_data = pandas.read_sql(sql, self._db.get_connection())
        #df = self.convert_to_unicode_dtype(df)
        return df_data

    def close(self):
        if self._db is not None:
            self._db.close()


def main():
    tblAgeBrand = TblAgeBrand()
    df_data = tblAgeBrand.read_sql_to_dataframe()
    print df_data


if __name__ == "__main__":
        main()