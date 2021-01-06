
#when only being able to move right and down
#x = 2
#y = 2
#in a 2x2 grid you can move in three basic lanes to the right *upper, middle, lower
#routes_count = 0
#x axis gives that way x+1 different basic routes (all the way top lane to right, middle lane to right, lower lane to right ..)


#each cell gives 4 paths
#2x2 = 4 cells = 16 paths
#2x2 there are always 4 paths to take to get to the end
#each cell can only be traversed on max. 2 paths = max. 8 paths without further narrowing down
#if one cells gets traversed 2 times, another cell can only be traversed one time


#other way to see it: 4,3,2 2,1,0 cells to outline
#so 20x20 would be 400,399,...,200 and  200,199,198... which means -> 200...0 = 402
#all to half, half to none = 
# outsider = 2
#    1  2  3
#  1 |--|--|    
#    |[]|[]| 
#  2 |--|--| 
#    |[]|[]|
#  3 |--|--| 

#1 is right, 0 is down

#0011 = 3
#0101 = 5
#0110 = 6
#1001 = 9
#1010 = 10
#1100 = 12

#0011
#0101
#1001

#0110
#1010
#1100

# 3x3 field

100011
010011
001011
000111

110001
011001
001101
000111

111000
011100
001110
000111


4 bit
2x0 2x1

1: wie viel Möglichkeiten, um 1 bit zu setzen?
1 bei 3 freien bit
1 xxx

1 100
1 010
1 001


0: wie viel Möglichkeiten, um 2 bit zu setzen?
2 bei 3 freien bit
0 xxx

0 110
0 101
0 011

0 1xx -> 2 (freie bit) hoch 1 (zu setzende option) 2

0 0xx -> 2 freie bit hoch 2 zu setzende bit = 4

wa


wie berechnen sich Möglichkeiten bei gegeben: zu setzende bit, mögliche stellen?
a: 
i) freie bit / zu setzende bit
ii) 

bei 4 bit = 4! / (2!*2!)


bsp
0 xxx (3 freie davon 2 zu setzen) -> 1,5

110
101
011

3x2 / 2


3x1 3x0
XX XXXX

32 16 8 4 2 1

64 Möglichkeiten

XX XXXX
6 freie bit
3 zu setzen - egal wo









3x3 = 6 token 
#2x2 = 4token
#20x20 = 40token = 40bit
#

#1y3x = 2y 1 x = 2

#starting from top line: 3x2x1 possibilities

fak = 1
for i in range(1,22):
	fak +=i	
print(fak)

# always use 4 tokens


#gives you 2 move right tokens, 2 move down tokens
#maybe its 2**2+2 


#go down at 1y and 4x: 1 possibility
#go down at 1y and 3x: 3y left * 1x = 3 possibilities
#go down at 1y and 2x: 3y left * 2x = 6 possibilities
#go down at 1y and 1x: 3y left * 3x = 9 possibilities

#go down at 2y and 4x: 1 possibility
#go down at 

#   1  2  3   4
# 1 |---------|
#   |[] [] [] |  
# 2 |---------|
#   |[] [] [] | 
# 3 |---------|
#   |[] [] [] |
# 4 |---------|
#base gives you 8 tokens : 
#(those are split in move right and move down tokens)
#4 move right tokens
#4 move down tokens


#you always have to use up all tokens in ordner to finish the maze


#lets write a parser:

