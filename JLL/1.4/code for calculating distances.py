import json
import math

with open(f'Workpiece1.json') as workpiece:
        workpiece_data = json.load(workpiece)

xw = workpiece_data['ReferenceAsset']['absPlace']['position'][0]
yw = workpiece_data['ReferenceAsset']['absPlace']['position'][1]
zw = workpiece_data['ReferenceAsset']['absPlace']['position'][2]

for i in range(1,5,1):

    with open(f'Tool_t{i}.json') as tool:
        tool_data = json.load(tool)

    xt = tool_data['ReferenceAsset']['absPlace']['position'][0]
    yt = tool_data['ReferenceAsset']['absPlace']['position'][1]
    zt = tool_data['ReferenceAsset']['absPlace']['position'][2]

    distance = math.sqrt((xt - xw)**2 + (yt - yw)**2 + (zt - zw)**2) - 0.14

    print(f'The distance between the tool and workpiece 1 during trajectory {i} is: {distance}')




