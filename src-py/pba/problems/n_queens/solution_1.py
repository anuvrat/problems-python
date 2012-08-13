'''
Created on Aug 13, 2012

@author: anuvrat
'''

from itertools import permutations

'''
Solution using the itertools from python by http://code.activestate.com/recipes/576647/
'''

def board( vec ):
    print ( "\n".join( '.' * i + 'Q' + '.' * ( n - i - 1 ) for i in vec ) + "\n===\n" )

n = 8
cols = range( n )
for vec in permutations( cols ):
    if n == len( set( vec[i] + i for i in cols ) ) == len( set( vec[i] - i for i in cols ) ):
        board( vec )
