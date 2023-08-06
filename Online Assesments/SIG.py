def solution(queryType, query):
    dic = {}
    keyhist = []
    valhist = []
    addkey, addval, lvl = 0,0,0

    def get(x):
        return dic[x]
    def addToKey(x):
        nonlocal dic
        store = []
        for key in dic.keys():
            store.append((key,dic[key]))
        dic = {}
        for k, v in store:
            dic[k+x] = v 
    def addToValue(y):
        store = []
        for key in dic.keys():
            dic[key] = dic[key]+y
    def insert(x,y):  
        nonlocal addkey, addval 
        addToValue(addval)     
        addToKey(addkey)
        addkey = 0
        addval = 0
        dic[x] = y    
    tot = 0
    for i in range(len(queryType)):
        qry, val = queryType[i], query[i]
        if qry == 'insert':
            insert(val[0],val[1])
        elif qry == 'get':
            tot += get(val[0])
        elif qry == 'addToValue':
            addval += val[0]
        elif qry == 'addToKey':
            addkey += val[0]

    return tot

print(solution(["insert", "insert", "addToValue", "addToKey", "get"], [[1,2], [2,3], [2], [1], [3]]))