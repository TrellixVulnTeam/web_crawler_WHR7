output = '{"sites": ['

i = 1

with open("../tranco_X79N_sites") as file:
    for line in file:
    	line = line.rstrip()
    	output += '{"site_url": "' + line + '", "links_count": 1, "links": ["' + line + '"], "tranco_rating": "' + str(i) + '"}, '
    	i += 1

output = output[:-2]
output += ']}'

with open('sites_to_be_visited.json', 'w') as f:
    f.write(output)
