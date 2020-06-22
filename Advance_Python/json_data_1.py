import json

with open('hello.json') as f:
    data = json.load(f)
    #print(data)
for state in data['states']:
    del state['area_codes']
    print(state)   

with open('new_state.json','w') as f:
    json.dump(data, f, indent=3)    