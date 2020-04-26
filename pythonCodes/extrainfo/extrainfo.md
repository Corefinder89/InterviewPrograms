# Variables
* `_var` - The underscore prefix is meant as a hint to tell another programmer that a variable
or a method starting with a single underscore is intended for internal use. Besides being used
as a temporary variable it can also be used to get the last interpreted value, or
can be used in any operation temporarily where we don not want to signify name to an object.
* `var_` - The trailing underscore postfix is used by convention to avoid naming conflicts within
python keywords.
* `__var` - A double underscore prefix causes the python interpreter to rewrite the attribute name.
This is also called name mangling.
in order to avoid naming conflicts in sub classes. This is called `name mangling`.
* `__var__` - Remains untouched by python

# Parameters
* `*args` and `**kwargs` are used take optional parameters as arguments.
* `*args` takes in additional positional arguments and stores them as tuples.
* `**kwargs` takes in additional keyword arguments and stores them as dictionary.
