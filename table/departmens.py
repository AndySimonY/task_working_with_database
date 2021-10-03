from db_utils.db_utilits import DB_Utilits
from confdata.conf_data import TableProperty
from datetime import datetime, timedelta


class Departmens:
    def __init__(self, table_name, conn):
        self.table_name = table_name
        self.session = DB_Utilits(connections=conn)

    def create_table(self):

        self.session.create_table(table_property=TableProperty.departmens)
    
    def paste_data(self):
        self.session.insert_data(data=([1, 'One Filial'], 
                                       [2, 'Two Filial'], 
                                       [3, 'Tree Filial'], 
                                       [4, 'For Filial'], 
                                       [5, 'Five Filial'], 
                                       [6, 'Six Filial']), table_name=self.table_name)

    def empty_branches(self):
        query = f"""SELECT D.* FROM {self.table_name} D 
        INNER JOIN contracts C ON C.id_department = D.id_department 
        WHERE C.v_status = 'A'"""
        res = self.session.execute_request(request=query)
        print(f"=========================\n\
EMPTY BRANCHES TASK 3 ------>>>\n\
{res}")