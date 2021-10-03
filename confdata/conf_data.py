credentials = {"database":"<name>", 
                "user":"postgres", 
                "password":"<password>", 
                "host":"127.0.0.1", 
                "port":"5432"}

class TableProperty:

    contracts =[{
        "table_name":"contracts",
        "id_contracts_inst":"serial PRIMARY KEY",
        "id_department":"int references departmens(id_department) default null",
        "dt_reg":"date default null",
        "v_ext_ident":"int default null",
        "v_status":"char(1) default null"
        }]

    departmens = [{
        "table_name":"departmens",
        "id_department":"serial PRIMARY KEY",
        "v_name":"text default null"
    }]

    bills = [{
        "table_name":"bills",
        "id_bills": "serial PRIMARY KEY",
        "id_contracts_inst":"int references contracts(id_contracts_inst) default null",
        "f_sum":"int default 0",
        "dt_event":"date default null",
        "id_manager": "int default null"
    }]

    service = [{
        "table_name":"service",
        "id_service": "serial PRIMARY KEY",
        "v_name": "text"
    }]

    tariff_palan = [{
            "table_name":'tariff_plan',
             "id_tariff_plan":"serial PRIMARY KEY",
             "v_name":"text default null"
    }]

    services = [{
        "table_name":'services',
        "id_service_inst":"serial PRIMARY KEY",
        "id_contracts_inst":"int references contracts(id_contracts_inst) default null",
        "id_tariff_plan":"int references tariff_plan(id_tariff_plan) default null",
        "id_service":"int references service(id_service) default null",
        "dt_start":"date",
        "dt_stop":"date"
    }]