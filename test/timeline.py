import re
k = "[ 00:00:01.290 -->  00:00:20.595] E SPEAKER_01"
pattern = r"\[ (\d\d:\d\d:\d\d\.\d\d\d) -->  (\d\d:\d\d:\d\d\.\d\d\d)\] ([A-Z]) (\w+)"
match = re.search(pattern, k)
if match:
    j = [match.group(1), match.group(2), match.group(3), match.group(4)]
    print(j)
else:
    print("No match found")