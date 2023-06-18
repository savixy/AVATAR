import json

for i in range(1, 5, 1):
	
	with open(f'trajectory{i}.txt', 'w') as t:
		
		with open(f'TRAJECTORY_{i}.json', 'r') as trajectory:
			file_load = json.load(trajectory)
		
		t.write('{\n')
		t.write('	"context": {\n		"assetTrail": false,\n		"UnitOfMeasureScale": 1,\n		"Zup": false,\n		"RepoAnim": ""\n')
		t.write('	},\n')
		t.write('	"nodes": [\n')

		for j in range(1, 7, 1):

			timestamp = 0

			t.write('		{\n')
			t.write(f'			"id": "Robot_1.Link_{j}",\n')
			t.write('			"actions": [\n')

			for x in file_load:

				J = x[f'J{j}']	

				t.write('			{\n')
				t.write('					"trigger": {\n						"type": "timestamp",\n')
				t.write(f'						"data": "{timestamp}"\n')
				t.write('					},\n					"event": {\n						"type": "show",\n')
				t.write('						"rotation": [\n							0,\n')
				t.write(f'							{J},\n')
				t.write(f'							0\n						],\n						"placementRelTo": "Robot_1.Joint_{j}"\n')
				t.write('					}\n				},\n')

				timestamp = timestamp + 100

			t.write('			]\n		},\n')
		
		t.write('	],\n	"sequences": [],\n	"bookmarks": []\n	}')



				

