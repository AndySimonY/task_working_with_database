from table.services import Services
from table.tariff_plan import TariffPlan
from table.service import Service
from db_utils.db_utilits import DB_Utilits
from table.bills import Bills
from table.contracts import Contracts
from table.departmens import Departmens  
from db_utils.connector import connect
from confdata.conf_data import credentials



with connect(credentials=credentials) as conn:

    departmens = Departmens(table_name='departmens', conn=conn)
    contracts = Contracts(table_name='contracts', conn=conn)
    bills = Bills(table_name='bills', conn=conn)
    service = Service(table_name='service', conn=conn)
    tariff_plan = TariffPlan(table_name='tariff_plan', conn=conn)
    services = Services(table_name='services', conn=conn)


    def execute_preparation():
        departmens.create_table()
        contracts.create_table() # Создание таблиц
        bills.create_table()
        service.create_table()
        tariff_plan.create_table()
        services.create_table()

        departmens.paste_data()
        contracts.paste_data() # Вставка данных
        bills.paste_data()
        service.paste_data()
        tariff_plan.paste_data()
        services.paste_data()

    execute_preparation()

    def execute_task_conditions():
        """Таски"""

        """1"""
        contracts.registration_dates()

        """2"""
        contracts.status_records() 

        """3"""
        departmens.empty_branches()

        """4"""
        bills.account(date='2021-09-29')

        """5"""
        service.service_data(id=5) # or id=None

        """6"""
        services.cursor()

        """7"""
        service.unique_service_name(filial_name='Tree Filial')

        """8"""
        tariff_plan.name_tariff_for_top_5_service()

    execute_task_conditions()

    """Удаление таблиц"""
    DB_Utilits(connections=conn).delete_table([
        'departmens', 'contracts', 'bills', 'service', 'tariff_plan', 'services'
    ])