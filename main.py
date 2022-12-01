class TreeStore:
    def __init__(self,items):
        self.items={}
        for item in items:
            self.items[item['id']] = item

    def getAll(self):
        print([item for key,item in self.items.items()])

    def getItem(self,id):
        try:
            print(self.items[id])
        except:
            print("No item")

    def getChildren(self,id):
        print([item for key,item in self.items.items() if item['parent']==id])

    def getAllParents(self,id):
        result=[]
        while(self.items[id]['parent']!='root'):
            result.append(self.items[self.items[id]['parent']])
            id = self.items[id]['parent']
        print(result)


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)
ts.getAll()
ts.getItem(1)
ts.getChildren(4)
ts.getChildren(5)
ts.getAllParents(7)