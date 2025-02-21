# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

N = int(input())
HTML_file = "\n".join(input() for _ in range(N)) 

HTML_file = re.sub(r'<!--.*?-->','',HTML_file,flags=re.DOTALL)
HTML_file = re.sub(r'</.*?>','',HTML_file,flags=re.DOTALL)
tag_pattern = re.compile(r'<(\w+)(.*?)>',re.DOTALL)
attribute_pattern = re.compile(r'([a-zA-Z_:][-a-zA-Z0-9_:]*)\s*=\s*"([^"]*)"')

for tag_match in tag_pattern.finditer(HTML_file):
    tag = tag_match.group(1)
    attribute = tag_match.group(2)
    print(tag)
    for attribute_match in attribute_pattern.finditer(attribute):
        attribute_name = attribute_match.group(1)
        attribute_value = attribute_match.group(2)
        print(f"-> {attribute_name} > {attribute_value}")
        
        
