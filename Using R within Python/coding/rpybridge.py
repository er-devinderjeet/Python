__author__ = 'Devinderjeet'
import pyRserve
import numpy

conn = pyRserve.connect()
print(conn.port)
print(conn.host)
print(conn.isClosed)
# conn.close()
# print(conn.isClosed)
# conn.voidEval("a <- '223' ")
# # print(conn.eval("a"))
# print(conn.eval('c(1,5)'))
my_Script = '''
   squareit <- function(x)
   {x**2}
   squareit(4)
'''

print(conn.eval(my_Script))