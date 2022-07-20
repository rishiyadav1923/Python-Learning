# Python compile() Function

# Example
# Compile text as code, and the execute it:

x = compile('print(55)', 'test', 'eval')
exec(x)

# Definition and Usage
# The compile() function returns the specified source as a code object, ready to be executed.

# Syntax
# compile(source, filename, mode, flag, dont_inherit, optimize)

# Parameter Values
# Parameter	                        Description
# source	                        Required. The source to compile, can be a String, a Bytes object, or an AST object
# filename	                        Required. The name of the file that the source comes from. If the source does not come from a file, you can write whatever you like
# mode	                            Required. Legal values:
#                                   eval - if the source is a single expression
#                                   exec - if the source is a block of statements
#                                   single - if the source is a single interactive statement
# flags	                            Optional. How to compile the source. Default 0
# dont-inherit	                    Optional. How to compile the source. Default False
# optimize	                        Optional. Defines the optimization level of the compiler. Default -1

# More Examples
# Example
# Compile more than one statement, and the execute it:

x = compile('print(55)\nprint(88)', 'test', 'exec')
exec(x)

# Related Pages
# The eval() Function
# The exec() Function


