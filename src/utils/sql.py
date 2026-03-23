import sqlite3
import re
from pathlib import Path
import json


class SqlManagement:
    def __init__(self, db_path):
        self.db = db_path

    def _safe_name(self, name):
        if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name):
            raise ValueError("Invalid table name")
        return name
    
    def table_exists(self, table_name):
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()
            query = """
            SELECT name FROM sqlite_master WHERE type='table' AND name=?;
            """
            cursor.execute(query, (table_name,))
        
            result = cursor.fetchone()
        
            if result is not None:
                print(f"table exists {table_name}")
                return True
            else:
                d = input(f"No table named '{table_name}' found. Would you like to create a table with said name? Y/N")
                if d == "Y":
                    self.create_id_table(str(table_name))
                elif d == "N":
                    pass
    
    def create_id_table(self, tname):
        if self.table_exists():
            name = self._safe_name(tname)

            conn = sqlite3.connect(self.db)
            cur = conn.cursor()

            cur.execute(f'''
                CREATE TABLE IF NOT EXISTS {tname} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            uuid TEXT NOT NULL
            )
            ''')

            conn.commit()
            conn.close()
        else:
            print("table not found.")
            

        
    def IDtablecommit(self, tname, name, id):
        tname = self._safe_name(tname)  

        conn = sqlite3.connect(self.db)
        cur = conn.cursor()

        cur.execute(
            f"INSERT INTO {tname} (name, uuid) VALUES (?, ?)",
            (name, id)  
        )

        conn.commit()
        conn.close()
    

        
        
    def FetchIDTable(self, tname):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        
        cur.execute(rf"SELECT * FROM {tname}")
        rows = cur.fetchall()\
            
        columns = [description[0] for description in cur.description]
        results_list = [dict(zip(columns, row)) for row in rows]
        
        json_output = json.dumps(results_list, indent=4)
        
        conn.close()
        
        return json_output

