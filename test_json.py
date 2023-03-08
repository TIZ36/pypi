import json

nums = [2, 3, 4, 5]

file_name="number.json"
with open(file_name, 'w') as f:
    json.dump(nums, f)