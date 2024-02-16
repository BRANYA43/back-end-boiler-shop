### Template Structure Data 

```json
{
    "<category>": [
        {
            "type": ["mixed", "equal"],
            "price": ["int", "float", "str"],
            "title": "str",
            "template_title": "{title}",
            "template_description": ["text", "file-path", ""],
            "template_specifications": [{"key":  "specification-name"}, {}],
            "specifications": {
                "<specification>": [["int", "float", "str", "bool"], "list"],
                "<sort_specification>": "list",
                "<sort_specification:specification>": {
                  "<sort_specification>":  [["int", "float", "str", "bool"], "list"]
                }
            }
        }
    ]
}
```
***
# Documentation

**Type** - a variable that says to script how it must process data. Values:
- "mixed" - need to mix all specifications in all variation.
- "equal" - need to combine all specification. Specification list must be equal 
by length.
```
# Mixed Example
specification_1 = [1, 2]
specification_2 = ["a", "b", "c"]
mixed_specifications = [[1, "a"], [1, "b"], [1, "c"],
                       [2, "a"], [2, "b"], [2, "c"]]

# Equal Example
specification_1 = [1, 2, 3]
specification_1 = ["a", "b", "c"]
combined_specification = [1, "a"], [2, "b"], [3, "c"]
```

if you don't have some specification value you use null:
```
# Equal Example if some specification is null

specification_1 = [1, 2, 3]
specification_1 = ["a", null, "c"]
combined_specification = [1, "a"], [2, null], [3, "c"]
```

**Price** - a variable of product price.

**Title** - a variable of product title.

**Template Title** - a variable that is needed to create a title of product 
flexibly by keywords from _"template_specifications"_. It's "{title}" by default.
```
# Example
template_title = "Some Title Text {title}-{specification}"
```
When _"Some Title Text"_ is any text; _"{title}"_ and _"{specification}"_ are 
keyword;

**Template Description** - a variable that is needed to create a description of product
flexibly by keywords from _"template_specifications"_. It can contain text or file path.
It's empty string by default.
```
# Example
template_description = "Some Description Text {title}-{specification}."
```
When _"Some Description Text"_ is any text; _"{title}"_ and _"{specification}"_ are 
keyword;

**Template Specifications** - a variable that contains _"keywords"_ and _"specification 
names"_ to fill content of _"template_title"_ and _"template_description"_. 

**Specifications** - a variable that contains specifications dictionary.

***