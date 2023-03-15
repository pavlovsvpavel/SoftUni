import re

text = input()

regex = r"(^|\s)(?P<mail>[a-z0-9]+[\.\-\_]*[a-z0-9]*@[a-z]+[\-]*[a-z]*\.[\.a-z]*[a-z])"

result = re.findall(regex, text)
for idx in range(len(result)):
    if result[idx]:
        print(result[idx][1])

# result = re.finditer(regex, text)
# for match in result:
#     if match:
#         print(match["mail"])
