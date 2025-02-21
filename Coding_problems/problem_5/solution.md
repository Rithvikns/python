```python
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

```


# Explanation:

1. **Reading Input:**
   - The first input line contains an integer `N`, which indicates the number of subsequent lines.
   - The next `N` lines are read and joined into a single string, `HTML_file`.

2. **Removing Comments:**
   - Uses `re.sub(r'<!--.*?-->', '', HTML_file, flags=re.DOTALL)` to remove multi-line HTML comments.

3. **Tag Extraction:**
   - The regex `<(\w+)([^>/]*)\s*/?>` is used to find all HTML tags:
     - `<(\w+)>` captures the tag name.
     - `([^>/]*)` captures attributes inside the tag.
     - `\s*/?>` ensures self-closing tags (`<meta />`, `<img />`) are handled.

4. **Attribute Extraction:**
   - The regex `([a-zA-Z_:][-a-zA-Z0-9_:]*)\s*=\s*"([^"]*)"` is used to extract attributes:
     - `([a-zA-Z_:][-a-zA-Z0-9_:]*)` captures attribute names (allowing hyphens and colons).
     - `\s*=\s*` allows for spaces around `=`.
     - `"([^"]*)"` captures attribute values inside double quotes.

5. **Printing Results:**
   - Each tag name is printed.
   - Each attribute and its corresponding value are printed in the format: `-> attribute > value`.


