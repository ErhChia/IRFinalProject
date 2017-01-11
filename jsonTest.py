import json
data = [
	{
		"query":"aaa",
		"document":
		{
			"aaa":3,
			"bbb":1,
			"ddd":5
		}
	},
	{
		"query":"bbb",
		"document":
		{
			"ccc":2,
			"ddd":1
		}
	}
]
with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, sort_keys=True, separators=(',', ':'))