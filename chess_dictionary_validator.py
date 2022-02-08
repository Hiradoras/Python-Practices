board =  {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

#Boards to test
#more than 2 kings
test_1  = {'1a':'bking', '8f':'wking', '2a': 'bking', '5d':'wking'}

#more than 8 pawns for one side
test_2 = {'2a':'bpawn', '2b': 'bpawn', '2c':'bpawn', '2d': 'bpawn', '2e': 'bpawn',\
         '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',\
         '7a': 'bpawn', '7b': 'wpawn', '8e': 'wking', '1e': 'bking'}

#more than 16 pieces for one player
test_3 = {'2a':'bpawn', '2b': 'bpawn', '2c':'bpawn', '2d': 'bpawn', '2e': 'bpawn',\
         '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',\
         '1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bqueen', \
         '1e':'bking', '1f': 'brook', '1g': 'bknight', '1h': 'bbishop', \
         '3a': 'bpawn', '7b': 'wking', '7c': 'wqueen'}

#invalid space 9d
test_4 = {'1a':'bking', '8f':'wking', '1b':'bqueen', '9d': 'wqueen'}

#names don't begin with 'w' or 'b'
test_5 = {'1a':'bking', '8f':'wking', '1b':'zqueen', '6d': 'wqueen'}

#pieces names 
test_6 = {'1a':'bking', '8f':'wking', '1b':'bqueen', '6d': 'wqueen', '7b':'wknightt'}

#too many white rooks
test_7 = {'1a':'bking', '8f':'wking', '1b':'bqueen', '6d': 'wqueen', '5c': 'wrook', '8c':'wrook', '7d': 'wrook'}

#this board should be valid
test_8 = {'1a':'bking', '8f':'wking', '1b':'bqueen', '6d': 'wqueen', '5c': 'wrook'}

def isValidChessBoard(dic):
    pieces = list(dic.values())
    cords = list(dic.keys())
    valid_cords = ('a','b','c','d','e','f','g','h')

    #piece counts and valid names
    valid_pieces = ['wking', 'bking', 'wqueen','bqueen',  'wbishop','wbishop'  ,'bbishop','bbihsop'  ,'wknight','wknight'  ,'bknight','bknight',  'wrook','wrook', 'brook','brook', 
    'wpawn','wpawn','wpawn','wpawn','wpawn','wpawn','wpawn','wpawn',
    'bpawn','bpawn','bpawn','bpawn','bpawn','bpawn','bpawn','bpawn']
    
    #Check if both sides have king
    if pieces.count('bking') != 1:
        return False
    if pieces.count('wking') != 1:
        return False

    #If both sides have king, then iterate through cords to check if all of them valid. And then check for pieces' counts.
    else:
        #Check cords
        for c in cords:
            if int(c[:1])>8:
                return False
            elif c[1:] not in valid_cords:
                return False
        #And finally check pieces for validation.
        for p in pieces:
            #Check if piece name is correct or not more than valid piece count.
            if p not in valid_pieces:
                return False
            else:
                #Remove the piece from list. So we can see if number of piece is not more than valid
                valid_pieces.remove(p)
    return True
            
print('Default board test:' , isValidChessBoard(board))
print('test_1 test:' , isValidChessBoard(test_1))
print('test_2 test:' , isValidChessBoard(test_2))
print('test_3 test:' , isValidChessBoard(test_3))
print('test_4 test:' , isValidChessBoard(test_4))
print('test_5 test:' , isValidChessBoard(test_5))
print('test_6 test:' , isValidChessBoard(test_6))
print('test_7 test:' , isValidChessBoard(test_7))
print('test_8 test:' , isValidChessBoard(test_8))
