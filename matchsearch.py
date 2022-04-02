import re
line = "Cats are smater than dogs"
matcher = re.match(r'dogs',line,re.M|re.I)
if matcher:
    print("matcher.group():",matcher.group())
else:
    print("No match!")
searcher = re.search(r'dogs',line,re.M|re.I)
if searcher:
    print("searcher.group():",searcher.group())
else:
    print("No match!")