TT_AND = True and True
TF_AND = True and False
FT_AND = False and True
FF_AND = False and False

print("AND:",TT_AND,TF_AND,FT_AND,FF_AND)
#Both must be True for True result

TTT_AND = True and True and True
TTF_AND = True and True and False
TFT_AND = True and False and True
FTT_AND = False and True and True
FFT_AND = False and False and True
FTF_AND = False and True and False
TFF_AND = True and False and False
FFF_AND = False and False and False

print("2x AND:",TTT_AND,TTF_AND,TFF_AND,TFT_AND,FFT_AND,FTF_AND,FTT_AND,FFF_AND)
#ALL must be True for True result

T_NOT = not True
F_NOT = not False