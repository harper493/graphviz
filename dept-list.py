import re
import os
import sys

result = []

for line in open(sys.argv[1]).readlines():
    line = line[:-1]
    m = re.match(r'^(\d\d)( \d\d[ \d]*)(\[.*\])?', line)
    if (m):
        my_dept, depts, attrs = m.groups()
        for d in depts.split():
            result.append(f'{my_dept} -- {d} {attrs or ""}')
    else:
        result.append(line)
print('\n'.join(result))        
    
