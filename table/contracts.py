from db_utils.db_utilits import DB_Utilits
from confdata.conf_data import TableProperty
from datetime import datetime, timedelta


class Contracts:
    def __init__(self, table_name, conn):
        self.table_name = table_name
        self.session = DB_Utilits(connections=conn)

    def create_table(self):
            self.session.create_table(table_property=TableProperty.contracts)

    def paste_data(self):
        self.session.insert_data(data=([1,1,'2021-09-30',2346,'B'], [2,2,'2021-09-28',4339,'C'],
                                       [3,3,'2021-09-25',6234,'C'], [4,4,'2021-10-01',2339,'A'],
                                       [5,5,'2021-09-30',4349,'A'], [6,6,'2021-09-29',9565,'A']), table_name=self.table_name)

    def registration_dates(self):
        five_days_later = (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')
        query = f"""SELECT dt_reg FROM contracts"""
        res = self.session.execute_request(request=query)

        query = f"""SELECT dt_reg FROM contracts WHERE dt_reg >= CAST('{five_days_later}' as DATE)"""
        res2 = self.session.execute_request(request=query)
        print(f"=========================\n\
ALL DATE TASK 1------>>>\n\
{res} \n\
LAST 5 DAYS\n\
{res2}")

    def status_records(self):
            query = f"""SELECT v_status FROM {self.table_name}"""
            res = self.session.execute_request(request=query)
            status_A = len([i for i in res if i == 'A'])
            status_C = len([i for i in res if i == 'C'])
            status_B = len([i for i in res if i == 'B'])
            print(f"=========================\n\
STATUS CONTRACTS TASK 2------>>>\n\
{status_A} - активен status A \n\
{status_B} - заблокирован status B \n\
{status_C} - расторгнут status C")




        
        