import databasehelper_mysql as dbhelper
from databasehelper_mysql import DbHelper
import pandas
import datasource_age_bran
import matplotlib.pyplot as plt
import numpy as np

COLUMN_GENDER = DbHelper.COLUMN_GENDER
COLUMN_AGE = DbHelper.COLUMN_AGE
COLUMN_GROUP = DbHelper.COLUMN_GROUP
COLUMN_PHONE_BRAND = DbHelper.COLUMN_PHONE_BRAND
COLUMN_DEVICE_MODEL = DbHelper.COLUMN_DEVICE_MODEL
COLUMN_DEVICE_COUNT = DbHelper.COLUMN_DEVICE_COUNT


def main():
    tblAgeBrand = datasource_age_bran.TblAgeBrand()
    df_data = tblAgeBrand.read_sql_to_dataframe()
    print "plotting..."
    #plt.figure()

    #histogram
    #df_data[COLUMN_DEVICE_COUNT].hist(by=df_data[COLUMN_GROUP])

    #bar plot for - Gender + Age
    #df_data.plot(x=[COLUMN_GENDER, COLUMN_AGE], y=COLUMN_DEVICE_COUNT)
    #bar plot for - Gender + brand
    #df_data.plot(x = [COLUMN_GENDER, COLUMN_PHONE_BRAND], y = COLUMN_DEVICE_COUNT)

    #bar plot
    df_data[[COLUMN_GENDER, COLUMN_PHONE_BRAND, COLUMN_DEVICE_COUNT]].plot.bar(stacked=True)
    plt.show()


if __name__ == "__main__":
        main()