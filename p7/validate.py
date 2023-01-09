import re
import sys

name = sys.argv[1].strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

'''
r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`
{|}~-]+@[a-zA-Z0-9](?:[a-zA-
Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a
-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
'''