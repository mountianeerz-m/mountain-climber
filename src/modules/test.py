import re
import pprint
from pprint import pp
import asyncio

class BaseModule:
    name = "base"

    async def search(self, query):
        raise NotImplementedError


class testModule(BaseModule):
    name = "test"

    async def search(self, query=None):
        
        final = []
        
        with open("src/modules/dump.txt") as file:
            for line in file:
                line = line.strip()
        
                if re.search(r".+:.+", line):
                    final.append(line)
                    
                elif query:
                    q = re.findall(rf"{query}.*", line)
                    print(q)
            
                    

            
        
        
        
        # fetch data
        # return normalized results


watchlist = ["username", "password", "email"]

final = []

final.clear()

with open("src/modules/dump.txt") as file:
    for line in file:
        line = line.strip()
        

        if re.search(r".+:.+", line):
            final.append(line)

pp(final)
        
        
        

        
        
        
        