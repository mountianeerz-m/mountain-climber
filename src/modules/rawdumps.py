import re
import pprint
from pprint import pp
import asyncio

class BaseModule:
    name = "base"

    async def search(self, query):
        raise NotImplementedError


class TextParse(BaseModule):
    name = "test"
    def search(self, file=None, query=None):
        final = []
        with open(file) as file:
            Pre1 = []
            for line in file:
                line = line.strip()
                
                if not line:
                    continue
                
                if re.search(r".+:|->|=.+", line):
                    Pre1.append(line)
                if query:
                    
                        if isinstance(query, list):
                            for item in query:
                                q = re.findall(rf"{re.escape(item)}.*", line)
                                Pre1.extend(q)
                                
                        elif isinstance(query, str):
                            print("query asked for...")
                            q = re.findall(rf"{query}.*", line)
                            Pre1.extend(q)
                            
                        else:
                            pass
            sor = sorted(set(Pre1))
            map1 = {s: i + 1 for i, s in enumerate(sor)}
            return map1
        
        # fetch data
        # return normalized results

t = TextParse()
pp(t.search("src/modules/dump.txt", "root"))

watchlist = ["username", "password", "email"]


