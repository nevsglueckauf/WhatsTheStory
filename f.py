import json

dta = json.load(open('44.json', 'r'))['results']

print(dta, len(dta))