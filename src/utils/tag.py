import random
import uuid 
import sqlite3
from pathlib import Path
import sql
db = Path("src/db/test.db")

class tags:
    
    @staticmethod
    
    def Strtag(str):
        dbm = sql.SqlManagement(db)
        
        f, l = str[0], str[-1]
        s = f + l
        print(f"tag created for string {str}: {f+l}")
        
        dbm.IDtablecommit("tags", str, s)
        
        return s

        
        
        
        
tags.Strtag("hello")