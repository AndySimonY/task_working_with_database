from db_utils.db_utilits import DB_Utilits
from confdata.conf_data import TableProperty
from datetime import datetime


class Services:
    def __init__(self, table_name, conn):
        self.table_name = table_name
        self.session = DB_Utilits(connections=conn)

    def create_table(self):
        self.session.create_table(table_property=TableProperty.services)

    def paste_data(self):
        self.session.insert_data(data=([1, 1, 234, 1,"2021-09-22", "2021-09-29"],
                                       [2, 2, 156, 2,"2021-09-19", "2021-09-30"],
                                       [3, 3, 464, 3,"2021-09-15", "2021-10-01"],
                                       [4, 4, 235, 4,"2021-09-23", "2021-09-27"],
                                       [5, 5, 352, 5,"2021-09-21", "2021-09-25"],
                                       [6, 6, 567, 6,"2021-09-20", "2021-09-30"]), 
        table_name=self.table_name)

    def cursor(self):
        now_time = datetime.now().strftime('%Y-%m-%d')
        query = f"""UPDATE services SET dt_stop = CAST('{now_time}' as DATE) 
                    WHERE id_service != 1234 AND id_tariff_plan = 567"""
        self.session.execute_request_update(request=query)
        query = f"""SELECT dt_stop FROM services WHERE id_service != 1234 AND id_tariff_plan = 567"""
        dt_stop = self.session.execute_request(request=query)
        print(f"=========================\n\
UPDATE DATE STOP TASK 6------>>>\n\
dt_stop after update {dt_stop}")


        

