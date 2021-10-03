from db_utils.db_utilits import DB_Utilits
from confdata.conf_data import TableProperty
from datetime import datetime, timedelta


class Service:
    def __init__(self, table_name, conn):
        self.table_name = table_name
        self.session = DB_Utilits(connections=conn)

    def create_table(self):
        self.session.create_table(table_property=TableProperty.service)

    def paste_data(self):
        self.session.insert_data(data=([1, "Service One"],
                                       [2, "Service Two"],
                                       [3, "Service Tree"],
                                       [4, "Service Four"],
                                       [5, "Service Five"],
                                       [6, "Service Six"],), 
        table_name=self.table_name)

    def service_data(self, id=None):
        if id is not None:
            query = f"""SELECT S.*, COUNT(C.id_contracts_inst) FROM {self.table_name} S
            INNER JOIN services SS ON SS.id_service =  S.id_service 
            INNER JOIN contracts C ON SS.id_contracts_inst = C.id_contracts_inst 
            WHERE {id} = S.id_service
            GROUP BY S.id_service
            ORDER BY S.v_name
            """
            res = self.session.execute_request(request=query)
            print(f"=========================\n\
SERVICE DATA FOR ID SERVICE '{id}' TASK 5 ------>>>\n\
ID_SERVICE - {res[0][0]}\n\
NAME SERVICE - {res[0][1]}\n\
NUMBER OF SERVICES USER HAVE = {res[0][2]}")
        else:
            query = f"""SELECT * FROM {self.table_name}"""
            res = self.session.execute_request(request=query)
            print(f"=========================\n\
SERVICE DATA TASK 5 ------>>>\n\
{res}")

    def unique_service_name(self, filial_name):
        query = f"""SELECT DISTINCT N.v_name FROM {self.table_name} N
         INNER JOIN services SS ON SS.id_service = N.id_service 
         INNER JOIN contracts C ON SS.id_contracts_inst = C.id_contracts_inst 
         INNER JOIN departmens D ON D.id_department = C.id_department 
         WHERE D.v_name = '{filial_name}'"""
        res = self.session.execute_request(request=query)
        query = f"""SELECT DISTINCT D.v_name , N.v_name FROM {self.table_name} N
         INNER JOIN services SS ON SS.id_service = N.id_service 
         INNER JOIN contracts C ON SS.id_contracts_inst = C.id_contracts_inst 
         INNER JOIN departmens D ON D.id_department = C.id_department
         WHERE D.v_name != '{filial_name}'"""
        res_inst = res
        res2 = self.session.execute_request(request=query)
        [res_inst.remove(j) for i in res2 for j in res if j in i]
        print(f"=========================\n\
UNIQUE SERVICE FOR FILIAL '{filial_name}' TASK 7 ------>>>\n\
{res_inst}")