import json
import re

pattern = re.compile(r'"name"\s*:\s*"((?:\\.|[^"\\])*)"')

examples = [
    r'{"name": "Alyssa P. Hacker", "college": "MIT"}',
    r'{"name": "Alyssa \"Ace\" Hacker", "college": "MIT"}',
]

for text in examples:
    match = pattern.search(text)
    captured = match.group(1)
    name = json.loads('"' + captured + '"')
    print(name)
