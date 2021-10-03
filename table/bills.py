from db_utils.db_utilits import DB_Utilits
from confdata.conf_data import TableProperty
from datetime import datetime, timedelta


class Bills:
    def __init__(self, table_name, conn):
        self.table_name = table_name
        self.session = DB_Utilits(connections=conn)

    def create_table(self):
        self.session.create_table(table_property=TableProperty.bills)

    def paste_data(self):
        self.session.insert_data(data=([1,1, 12300, '2021-09-25', 12], 
                                       [2,2, 1300, '2021-09-22', 9], 
                                       [3,3, 4465, '2021-09-29', 9], 
                                       [4,4, 2900, '2021-10-01', 7], 
                                       [5,5, 6788, '2021-09-23', 12], 
                                       [6,6, 39045, '2021-10-01', 8]), table_name=self.table_name)

    def account(self, date=None):
        query = f"SELECT f_sum FROM {self.table_name} WHERE dt_event = CAST('{date}' as DATE)"

        res = self.session.execute_request(request=query)
        print(f"=========================\n\
ACCOUNT TASK 4 ------>>>\n\
{res}")
