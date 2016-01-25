import json 

def runToTextInData(data, text, depth, path):
    
    if type(data) == dict:
        for someKey in data:

            if len(path) <= depth:
                path.append(str(someKey))
            else:
                path[depth] = str(someKey)
            
            someValue = data[someKey]

            if type(someValue) == dict:
             
                runToTextInData(someValue, text, depth + 1, path)

            if type(someValue) == type([]):
                
                runToTextInData(someValue, text, depth + 1, path)

            if type(someValue) is type('str'):
               
                if str(someValue) == text:
                    output = ''
                    for element in path: 
                        if path.index(element) == 0: 
                            output += element 
                        if element[:1].startswith('['): 
                            output += element 
                        else: 
                            output += '/' + element
                    print("Successfully determined path to: " + text + ": " + output)
                    return
    
    if type(data) == type([]) : 

        for someValue in data:
            if len(path) <= depth:
                path.append( "[" + str(data.index(someValue)) + "]")
            else:
                
                path[depth] = ("[" + str(data.index(someValue)) + "]")

            if type(someValue) == dict:
                
                runToTextInData(someValue, text, depth + 1, path)
            if type(someValue) == type([]):
                
                runToTextInData(someValue, text, depth + 1, path)
            if type(someValue) is type('str'):
               
                if str(someValue) == text:
                
                    output = ''
                    for elements in path: 
                        if path.index(element) == 0: 
                            output += element 
                        if element[:1].startswith('['): 
                            output += element 
                        else: 
                            output += '/' +  element 

                    print("Successfully determined path to: " + text + " as: " + output)
                    return

globalPath = []

serializedData = '{"itemList": {"items": [{"id": "item1"},{"id": "item2","label": "Item 2"},{"id": "item3"},{"id": "item4"},{"id": "item5"},{"id": "subItem1","subItems": [{"id": "subItem1Item1","label": "SubItem 1"},{"id": "subItem1Item2","label": "SubItem 2"},{"id": "subItem1Item3","label": "SubItem 3"}]},{"id": "item6"},{"id": "item7","label": "Item 7"},{"id": "subItem2","subItems": {"id": "item1","label": "SubItem 2 item1"}}]}}'

deserializedData = json.loads(serializedData)
runToTextInData(deserializedData, "item2", 0, globalPath)
runToTextInData(deserializedData, "subItem1", 0, globalPath)









