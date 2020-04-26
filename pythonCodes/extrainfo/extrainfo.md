# Variables
* `_var` - The underscore prefix is meant as a hint to tell another programmer that a variable
or a method starting with a single underscore is intended for internal use.
* `var_` - The trailing underscore postfix is used by convention to avoid naming conflicts within
python keywords.
* `__var` - A double underscore prefix causes the python interpreter to rewrite the attribute name
in order to avoid naming conflicts in sub classes. This is called `name mangling`.
* `__var__` - Remains untouched by python
