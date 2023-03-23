import requests
import json
import pandas

print(1)
class Notion:
    
    def __init__(self,token,databaseId):
        self.token = token
        self.databaseId = databaseId
    
    def read_databese(self):
        readUrl = "https://api.notion.com/v1/databases/"+self.databaseId+"/query"
        headers = {
            'Authorization':f'Bearer {self.token}',
            'Notion-Version': '2022-06-28',
            "Content-Type": "application/json"
        }
        res = requests.post(readUrl,headers=headers)
        print(res.status_code)

        dataj = res.json()
        
        with open('data.json','w',encoding='UTF-8') as f:
            json.dump(dataj,f,ensure_ascii=False,indent=4)


    def create_page(self):
        pass
    def update_page(self):
        pass
token = "secret_oEkWWjweqPPpeFsA7zbq5ULVrBRng2Bbh62hzw7xo1v"
databaseId = "f877683414614c8e85d60c95a4ab25c8"
Notion(token,databaseId).read_databese()
