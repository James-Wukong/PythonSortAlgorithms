## naming conventions of python files

### Modules and Packages

A Python **module** is simply a Python source file, which can expose classes, functions and global variables. Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. 

A Python **package** is simply a directory of Python module(s). Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

### Classes

Class names should normally use the **CapWords** convention. 

The file containing this classes should follow the **module** naming convention:

=> CamelCase should in the file camelcase.py (or camel_case.py if neccessary)

### Function and (local) Variable names

lowercase, with words separated by underscores as necessary to improve readability

1. variable names are not full descriptors;
1. put details in comments;
1. too specific name might mean too specific code;
1. keep short scopes for quick lookup;
1. spend time thinking about readability.

| Type	|  Public	|  Internal	|
|---	|---	|---	|
| Packages	| lower_with_under	|  |
| Modules	| lower_with_under	| _lower_with_under |
| Classes	C| apWords	_CapWords|  |
| Exceptions	| CapWords	|  |
| Functions	| lower_with_under()	| _lower_with_under() |
| Global/Class Constants	| CAPS_WITH_UNDER	| _CAPS_WITH_UNDER |
| Global/Class Variables	l| ower_with_under	| _lower_with_under |
| Instance Variables	| lower_with_under	| _lower_with_under (protected) |
| Method Names	| lower_with_under()	| _lower_with_under() (protected) |
| Function/Method Parameters	| lower_with_under	|  |
| Local Variables	| lower_with_under|  |

For more detailed overview of the naming conventions: [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#3164-guidelines-derived-from-guidos-recommendations).