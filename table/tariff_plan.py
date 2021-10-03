from db_utils.db_utilits import DB_Utilits
from confdata.conf_data import TableProperty
from datetime import datetime, timedelta


class TariffPlan:
    def __init__(self, table_name, conn):
        self.table_name = table_name
        self.session = DB_Utilits(connections=conn)

    def create_table(self):
        self.session.create_table(table_property=TableProperty.tariff_palan)

    def paste_data(self):
        self.session.insert_data(data=([234, "Tariff One"],
                                       [156, "Tariff Two"],
                                       [464, "Tariff Tree"],
                                       [235, "Tariff Four"],
                                       [352, "Tariff Five"],
                                       [567, "Tariff Six"]), 
        table_name=self.table_name)

    def name_tariff_for_top_5_service(self):
        query = f"""SELECT T.v_name FROM {self.table_name} T
        INNER JOIN services SS ON SS.id_tariff_plan = T.id_tariff_plan 
        INNER JOIN contracts C ON SS.id_contracts_inst = C.id_contracts_inst 
        INNER JOIN departmens D ON D.id_department = C.id_department
        GROUP BY T.v_name
        ORDER BY COUNT(D.id_department)
        LIMIT 5"""
        res = self.session.execute_request(request=query)
        print(f"=========================\n\
TOP 5 TARIFF PLAN TASK 8 ------>>>\n\
{res}\n\
=========================")
