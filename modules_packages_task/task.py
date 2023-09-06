#1
# A Python module is a file with the '.py' file extension that contains valid Python code
#2
#To use a module in another module, you must import it using an 'import' statement.

#3
from adder import add
result=add(2,3)
# result=adder.add(2,3)-->We only imported add() not adder file
import adder
result=adder.add(2,3)
#import add from adder-->invalid

#4
# A package is a folder containing one or more Python modules. One of the modules in a package must be called '__init__.py'



