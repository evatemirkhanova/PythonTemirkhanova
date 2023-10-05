i = input()
n = int(input())
s = 'abcdefghijklmnopqrstuvwxyz'
print( s[ ( s.find(i) + n ) % 26 ] )