import json 
import copy

# def find_path (d,str):
#     len_d = len(d)

    
#     for key,value in d.items(): 
       



# def traverse (dict, path = None): 
#     if not path: 
#         path = []
#     for i in dict: 
#         local_path = path[:].append(i)
#         if i ['type'] == : 
#             for j in traverse( - , local path): 
#                 yield j, local_path 
#         elif i['type']==  : 
#             yield i, local_path 
#         elif i['type'] == 
    
def runToTextInData(data, text, path):
    if type(data) == dict :
        for someKey in data:
        #print("Testing " + str(someKey))
        #path += str(someKey)
            path += " -> "
            path += str(someKey)
            someValue = data[someKey]
            
            if type(someValue) == dict:
            #print("Found Dictionary: " + str(someValue))
                runToTextInData(someValue, text, copy.copy(path)) #recursion!
            if type(someValue) == type([]):
            #print("Found Array: " + str(someValue))
                runToTextInData(someValue, text, copy.copy(path))
            if type(someValue) == type("string"):
            #print("Found String: " + str(someValue))
                if str(someValue) == text:
                    print("Successfully determined path to: " + text + " as: " + path)

    if type(data) == type([]) : 
        for someValue in data:
            path += " -> "
            path += str(data.index(someValue))

            if type(someValue) == dict:
            #print("Found Dictionary: " + str(someValue))
                runToTextInData(someValue, text, copy.copy(path)) #recursion!
            if type(someValue) == type([]):
            #print("Found Array: " + str(someValue))
                runToTextInData(someValue, text, copy.copy(path))
            if type(someValue) == type("string"):
            #print("Found String: " + str(someValue))
                if str(someValue) == text:
                    print("Kind of Victory Array Path: " + path)
                    return path




# def runToTextInArray(data, text, path):

#     for someValue in data:
#         path += " -> "
#         path += str(data.index(someValue))

#         if type(someValue) == dict:
#             #print("Found Dictionary: " + str(someValue))
#             runToTextInDictionary(someValue, text, path) #recursion!
#         if type(someValue) == type([]):
#             #print("Found Array: " + str(someValue))
#             runToTextInArray(someValue, text, path)
#         if type(someValue) == type("string"):
#             #print("Found String: " + str(someValue))
#             if str(someValue) == text:
#                 print("Kind of Victory Array Path: " + path)
#                 return path


# def runToTextInDictionary(data, text, path):
#     for someKey in data:
#         #print("Testing " + str(someKey))
#         #path += str(someKey)
#         path += " -> "
#         path += str(someKey)
#         someValue = data[someKey]
#         if type(someValue) == dict:
#             #print("Found Dictionary: " + str(someValue))
#             runToTextInDictionary(someValue, text, path) #recursion!
#         if type(someValue) == type([]):
#             #print("Found Array: " + str(someValue))
#             runToTextInArray(someValue, text, path)
#         if type(someValue   ) == type("string"):
#             #print("Found String: " + str(someValue))
#             if str(someValue) == text:
#                 print("Successfully determined path to: " + text + " as: " + path)

globalPath = ""

serializedData = '{"itemList": {"items": [{"id": "item1"},{"id": "item2","label": "Item 2"},{"id": "item3"},{"id": "item4"},{"id": "item5"},{"id": "subItem1","subItems": [{"id": "subItem1Item1","label": "SubItem 1"},{"id": "subItem1Item2","label": "SubItem 2"},{"id": "subItem1Item3","label": "SubItem 3"}]},{"id": "item6"},{"id": "item7","label": "Item 7"},{"id": "subItem2","subItems": {"id": "item1","label": "SubItem 2 item1"}}]}}'

deserializedData = json.loads(serializedData)
print(runToTextInData(deserializedData, "item2", globalPath))




