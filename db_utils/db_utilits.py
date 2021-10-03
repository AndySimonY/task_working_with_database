
class DB_Utilits():
    def __init__(self, connections):
        self.conn = connections

    def create_table(self, table_property=None):
        
        cursor = self.conn.cursor()

        if isinstance(table_property, list or tuple):
            for table in table_property:
                sub_query = ''
                try:
                    table_name = table['table_name'].upper()  
                except KeyError:
                    raise f'В свойствах таблицы отсутствует поле table_name, пожалуйста добавьте его в свойства'
                for col_name,col_type in table.items():
                    if col_name == 'table_name':
                        continue
                    col_name, col_type = str(col_name).upper(), str(col_type).upper()
                    sub_query += f'{col_name} {col_type}, '
                sub_query = sub_query[:-2]
                query = f"""CREATE TABLE IF NOT EXISTS {table_name} ({sub_query})"""
                print(f"Table '{table_name} was created'")
                cursor.execute(query)
        else:
            try:
                table_name = table_property['table_name'].upper()  
            except KeyError:
                raise f'В свойствах таблицы отсутствует поле table_name, пожалуйста добавьте его в свойства'
            sub_query = ''
            for col_name,col_type in table_property.items():
                    if col_name == 'table_name':
                        continue
                    col_name, col_type = str(col_name).upper(), str(col_type).upper()
                    sub_query += f'{col_name} {col_type}, '
            sub_query = sub_query[:-2]
            query = f"""CREATE TABLE IF NOT EXISTS {table_name} ({sub_query})"""
            print(f"Table {table_name} created successfully")
            cursor.execute(query)

    def insert_data(self, table_name, data=None, connections=None):
        cursor = self.conn.cursor()
        collect_data = []
        collect_values = ''
        query = None
        if isinstance(data[0], dict):
            for query_inst in data:
                    sub_str_col = sub_str_val = ''
                    for col, val in query_inst.items():
                        sub_str_col += f'{col}, '
                        if isinstance(val, str):
                            sub_str_val += f"'{val}', "
                        else:  sub_str_val += f"{val}, "
                    collect_values += f'({sub_str_val[:-2]}), '
                    query = f"""INSERT INTO {table_name} ({sub_str_col[:-2]}) VALUES {collect_values[:-2]}"""  
            print(f'succesfully inserted data in "{table_name}"')
            cursor.execute(query)
    
        if not isinstance(data, dict) and isinstance(data[0], list or tuple):
            for q in data:
                columns = list(map(lambda c: c[0], self.select_col(table_name=table_name, 
                                                                      cursor=cursor)))
                dat = {col:val for col, val in zip(columns, q)}
                collect_data.append(dat)
            
            self.insert_data(connections=connections,
                                table_name=table_name, 
                                data=collect_data)

    def execute_request(self, request):
        cursor = self.conn.cursor()
        cursor.execute(request)
        res = []
        for i in cursor:
            if len(i) == 1:
                res.append(i[0])
            else:
                res.append(i)
        return list(res)

    def execute_request_update(self, request):
        cursor = self.conn.cursor()
        cursor.execute(request)

    def delete_table(self, table_list=None):
        cursor = self.conn.cursor()   
        table = ', '.join(table_list)
        query = f"""DROP TABLE IF EXISTS {table}"""
        cursor.execute(query)
        print('Deleted successfully!')

    @staticmethod
    def select_col(table_name, cursor):
        query = f"""SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'"""
        cursor.execute(query)
        return cursor