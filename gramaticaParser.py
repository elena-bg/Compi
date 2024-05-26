# Generated from ./gramatica.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from cochinero import SymbolTable
symbol_table = SymbolTable()
current_scope=0
vacia = []

def serializedATN():
    return [
<<<<<<< Updated upstream
        4,1,33,335,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
=======
        4,1,33,341,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
>>>>>>> Stashed changes
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
<<<<<<< Updated upstream
        7,33,2,34,7,34,2,35,7,35,1,0,1,0,1,0,1,0,1,0,5,0,78,8,0,10,0,12,
        0,81,9,0,1,0,5,0,84,8,0,10,0,12,0,87,9,0,1,0,1,0,1,0,1,0,1,1,1,1,
        1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,
        1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,
        1,15,1,15,1,15,5,15,127,8,15,10,15,12,15,130,9,15,1,16,1,16,1,16,
        1,16,1,16,1,16,3,16,138,8,16,1,16,1,16,1,16,5,16,143,8,16,10,16,
        12,16,146,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,156,
        8,17,1,17,1,17,1,17,5,17,161,8,17,10,17,12,17,164,9,17,1,18,3,18,
        167,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,
        179,8,18,1,19,1,19,5,19,183,8,19,10,19,12,19,186,9,19,1,19,1,19,
        1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,3,22,208,8,22,1,22,1,22,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,25,1,25,3,25,234,8,25,1,25,1,25,1,25,1,25,
        1,25,1,25,3,25,242,8,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,250,8,
        25,5,25,252,8,25,10,25,12,25,255,9,25,1,25,1,25,1,25,1,25,1,26,1,
        26,1,26,1,26,1,26,5,26,266,8,26,10,26,12,26,269,9,26,3,26,271,8,
        26,1,26,1,26,1,26,1,27,1,27,3,27,278,8,27,1,28,1,28,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,
        29,1,29,3,29,299,8,29,1,30,5,30,302,8,30,10,30,12,30,305,9,30,1,
        31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,33,1,33,5,33,317,8,33,10,
        33,12,33,320,9,33,1,34,1,34,1,34,5,34,325,8,34,10,34,12,34,328,9,
        34,1,35,1,35,1,35,1,35,1,35,1,35,0,0,36,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        64,66,68,70,0,1,1,0,17,18,327,0,72,1,0,0,0,2,92,1,0,0,0,4,94,1,0,
        0,0,6,96,1,0,0,0,8,98,1,0,0,0,10,100,1,0,0,0,12,102,1,0,0,0,14,104,
        1,0,0,0,16,106,1,0,0,0,18,108,1,0,0,0,20,110,1,0,0,0,22,112,1,0,
        0,0,24,114,1,0,0,0,26,116,1,0,0,0,28,118,1,0,0,0,30,120,1,0,0,0,
        32,131,1,0,0,0,34,147,1,0,0,0,36,166,1,0,0,0,38,180,1,0,0,0,40,189,
        1,0,0,0,42,195,1,0,0,0,44,197,1,0,0,0,46,211,1,0,0,0,48,220,1,0,
        0,0,50,233,1,0,0,0,52,260,1,0,0,0,54,277,1,0,0,0,56,279,1,0,0,0,
        58,298,1,0,0,0,60,303,1,0,0,0,62,306,1,0,0,0,64,311,1,0,0,0,66,318,
        1,0,0,0,68,321,1,0,0,0,70,329,1,0,0,0,72,73,3,2,1,0,73,74,3,6,3,
        0,74,75,5,1,0,0,75,79,3,60,30,0,76,78,3,56,28,0,77,76,1,0,0,0,78,
        81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,85,1,0,0,0,81,79,1,0,0,
        0,82,84,3,58,29,0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,
        1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,89,5,2,0,0,89,90,5,0,0,1,
        90,91,6,0,-1,0,91,1,1,0,0,0,92,93,5,3,0,0,93,3,1,0,0,0,94,95,5,4,
        0,0,95,5,1,0,0,0,96,97,5,5,0,0,97,7,1,0,0,0,98,99,5,6,0,0,99,9,1,
        0,0,0,100,101,5,7,0,0,101,11,1,0,0,0,102,103,5,8,0,0,103,13,1,0,
        0,0,104,105,5,9,0,0,105,15,1,0,0,0,106,107,5,10,0,0,107,17,1,0,0,
        0,108,109,5,11,0,0,109,19,1,0,0,0,110,111,5,12,0,0,111,21,1,0,0,
        0,112,113,5,13,0,0,113,23,1,0,0,0,114,115,5,14,0,0,115,25,1,0,0,
        0,116,117,5,15,0,0,117,27,1,0,0,0,118,119,5,16,0,0,119,29,1,0,0,
        0,120,128,3,32,16,0,121,122,5,33,0,0,122,123,6,15,-1,0,123,124,3,
        32,16,0,124,125,6,15,-1,0,125,127,1,0,0,0,126,121,1,0,0,0,127,130,
        1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,31,1,0,0,0,130,128,1,
        0,0,0,131,132,3,34,17,0,132,144,6,16,-1,0,133,134,5,17,0,0,134,138,
        6,16,-1,0,135,136,5,18,0,0,136,138,6,16,-1,0,137,133,1,0,0,0,137,
        135,1,0,0,0,138,139,1,0,0,0,139,140,3,34,17,0,140,141,6,16,-1,0,
        141,143,1,0,0,0,142,137,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,
        144,145,1,0,0,0,145,33,1,0,0,0,146,144,1,0,0,0,147,148,3,36,18,0,
        148,162,6,17,-1,0,149,150,5,19,0,0,150,156,6,17,-1,0,151,152,5,20,
        0,0,152,156,6,17,-1,0,153,154,5,21,0,0,154,156,6,17,-1,0,155,149,
        1,0,0,0,155,151,1,0,0,0,155,153,1,0,0,0,156,157,1,0,0,0,157,158,
        3,36,18,0,158,159,6,17,-1,0,159,161,1,0,0,0,160,155,1,0,0,0,161,
        164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,35,1,0,0,0,164,162,
        1,0,0,0,165,167,7,0,0,0,166,165,1,0,0,0,166,167,1,0,0,0,167,178,
        1,0,0,0,168,169,5,28,0,0,169,179,6,18,-1,0,170,171,5,30,0,0,171,
        179,6,18,-1,0,172,173,5,31,0,0,173,179,6,18,-1,0,174,175,5,22,0,
        0,175,176,3,30,15,0,176,177,5,23,0,0,177,179,1,0,0,0,178,168,1,0,
        0,0,178,170,1,0,0,0,178,172,1,0,0,0,178,174,1,0,0,0,179,37,1,0,0,
        0,180,184,5,1,0,0,181,183,3,58,29,0,182,181,1,0,0,0,183,186,1,0,
        0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,187,1,0,0,0,186,184,1,0,
        0,0,187,188,5,2,0,0,188,39,1,0,0,0,189,190,5,28,0,0,190,191,5,24,
        0,0,191,192,3,30,15,0,192,193,6,20,-1,0,193,194,5,25,0,0,194,41,
        1,0,0,0,195,196,3,40,20,0,196,43,1,0,0,0,197,198,3,20,10,0,198,199,
        5,22,0,0,199,200,3,30,15,0,200,201,5,23,0,0,201,202,6,22,-1,0,202,
        207,3,38,19,0,203,204,3,18,9,0,204,205,6,22,-1,0,205,206,3,38,19,
        0,206,208,1,0,0,0,207,203,1,0,0,0,207,208,1,0,0,0,208,209,1,0,0,
        0,209,210,6,22,-1,0,210,45,1,0,0,0,211,212,3,22,11,0,212,213,6,23,
        -1,0,213,214,5,22,0,0,214,215,3,30,15,0,215,216,5,23,0,0,216,217,
        6,23,-1,0,217,218,3,38,19,0,218,219,6,23,-1,0,219,47,1,0,0,0,220,
        221,3,26,13,0,221,222,5,22,0,0,222,223,3,40,20,0,223,224,5,25,0,
        0,224,225,3,30,15,0,225,226,6,24,-1,0,226,227,5,25,0,0,227,228,3,
        40,20,0,228,229,5,23,0,0,229,230,3,38,19,0,230,49,1,0,0,0,231,234,
        3,28,14,0,232,234,3,4,2,0,233,231,1,0,0,0,233,232,1,0,0,0,234,235,
        1,0,0,0,235,241,5,22,0,0,236,237,3,30,15,0,237,238,6,25,-1,0,238,
        242,1,0,0,0,239,240,5,29,0,0,240,242,6,25,-1,0,241,236,1,0,0,0,241,
        239,1,0,0,0,242,253,1,0,0,0,243,249,5,26,0,0,244,245,3,30,15,0,245,
        246,6,25,-1,0,246,250,1,0,0,0,247,248,5,29,0,0,248,250,6,25,-1,0,
        249,244,1,0,0,0,249,247,1,0,0,0,250,252,1,0,0,0,251,243,1,0,0,0,
        252,255,1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,0,254,256,1,0,0,0,
        255,253,1,0,0,0,256,257,5,23,0,0,257,258,5,25,0,0,258,259,6,25,-1,
        0,259,51,1,0,0,0,260,261,5,28,0,0,261,270,5,22,0,0,262,267,3,30,
        15,0,263,264,5,26,0,0,264,266,3,30,15,0,265,263,1,0,0,0,266,269,
        1,0,0,0,267,265,1,0,0,0,267,268,1,0,0,0,268,271,1,0,0,0,269,267,
        1,0,0,0,270,262,1,0,0,0,270,271,1,0,0,0,271,272,1,0,0,0,272,273,
        5,23,0,0,273,274,5,25,0,0,274,53,1,0,0,0,275,278,3,14,7,0,276,278,
        3,16,8,0,277,275,1,0,0,0,277,276,1,0,0,0,278,55,1,0,0,0,279,280,
        3,12,6,0,280,281,5,28,0,0,281,282,5,22,0,0,282,283,3,68,34,0,283,
        284,5,23,0,0,284,285,5,1,0,0,285,286,3,60,30,0,286,287,3,38,19,0,
        287,288,5,2,0,0,288,289,5,25,0,0,289,290,6,28,-1,0,290,291,6,28,
        -1,0,291,57,1,0,0,0,292,299,3,40,20,0,293,299,3,48,24,0,294,299,
        3,44,22,0,295,299,3,46,23,0,296,299,3,50,25,0,297,299,3,52,26,0,
        298,292,1,0,0,0,298,293,1,0,0,0,298,294,1,0,0,0,298,295,1,0,0,0,
        298,296,1,0,0,0,298,297,1,0,0,0,299,59,1,0,0,0,300,302,3,62,31,0,
        301,300,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,304,1,0,0,0,
        304,61,1,0,0,0,305,303,1,0,0,0,306,307,3,54,27,0,307,308,3,64,32,
        0,308,309,5,25,0,0,309,310,6,31,-1,0,310,63,1,0,0,0,311,312,5,28,
        0,0,312,313,3,66,33,0,313,65,1,0,0,0,314,315,5,26,0,0,315,317,3,
        64,32,0,316,314,1,0,0,0,317,320,1,0,0,0,318,316,1,0,0,0,318,319,
        1,0,0,0,319,67,1,0,0,0,320,318,1,0,0,0,321,326,3,70,35,0,322,323,
        5,26,0,0,323,325,3,70,35,0,324,322,1,0,0,0,325,328,1,0,0,0,326,324,
        1,0,0,0,326,327,1,0,0,0,327,69,1,0,0,0,328,326,1,0,0,0,329,330,5,
        28,0,0,330,331,5,27,0,0,331,332,3,54,27,0,332,333,6,35,-1,0,333,
        71,1,0,0,0,22,79,85,128,137,144,155,162,166,178,184,207,233,241,
        249,253,267,270,277,298,303,318,326
=======
        7,33,2,34,7,34,2,35,7,35,1,0,1,0,1,0,1,0,5,0,77,8,0,10,0,12,0,80,
        9,0,1,0,1,0,1,0,1,0,5,0,86,8,0,10,0,12,0,89,9,0,1,0,1,0,1,0,1,0,
        1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,
        1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,
        15,1,15,1,15,1,15,1,15,5,15,129,8,15,10,15,12,15,132,9,15,1,16,1,
        16,1,16,1,16,1,16,1,16,3,16,140,8,16,1,16,1,16,1,16,5,16,145,8,16,
        10,16,12,16,148,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,
        158,8,17,1,17,1,17,1,17,5,17,163,8,17,10,17,12,17,166,9,17,1,18,
        3,18,169,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,3,18,183,8,18,1,19,1,19,5,19,187,8,19,10,19,12,19,190,
        9,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,212,8,22,1,22,1,22,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,3,25,238,8,25,1,25,
        1,25,1,25,1,25,1,25,1,25,3,25,246,8,25,1,25,1,25,1,25,3,25,251,8,
        25,5,25,253,8,25,10,25,12,25,256,9,25,1,25,1,25,1,25,1,26,1,26,1,
        26,1,26,1,26,5,26,266,8,26,10,26,12,26,269,9,26,3,26,271,8,26,1,
        26,1,26,1,26,1,26,1,27,1,27,3,27,279,8,27,1,28,1,28,1,28,1,28,1,
        28,1,28,1,28,1,28,5,28,289,8,28,10,28,12,28,292,9,28,1,28,1,28,1,
        28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,3,29,305,8,29,1,30,5,
        30,308,8,30,10,30,12,30,311,9,30,1,31,1,31,1,31,1,31,1,31,1,32,1,
        32,1,32,1,33,1,33,5,33,323,8,33,10,33,12,33,326,9,33,1,34,1,34,1,
        34,5,34,331,8,34,10,34,12,34,334,9,34,1,35,1,35,1,35,1,35,1,35,1,
        35,0,0,36,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,0,1,1,0,18,19,334,
        0,72,1,0,0,0,2,94,1,0,0,0,4,96,1,0,0,0,6,98,1,0,0,0,8,100,1,0,0,
        0,10,102,1,0,0,0,12,104,1,0,0,0,14,106,1,0,0,0,16,108,1,0,0,0,18,
        110,1,0,0,0,20,112,1,0,0,0,22,114,1,0,0,0,24,116,1,0,0,0,26,118,
        1,0,0,0,28,120,1,0,0,0,30,122,1,0,0,0,32,133,1,0,0,0,34,149,1,0,
        0,0,36,168,1,0,0,0,38,184,1,0,0,0,40,193,1,0,0,0,42,199,1,0,0,0,
        44,201,1,0,0,0,46,215,1,0,0,0,48,224,1,0,0,0,50,237,1,0,0,0,52,260,
        1,0,0,0,54,278,1,0,0,0,56,280,1,0,0,0,58,304,1,0,0,0,60,309,1,0,
        0,0,62,312,1,0,0,0,64,317,1,0,0,0,66,324,1,0,0,0,68,327,1,0,0,0,
        70,335,1,0,0,0,72,73,3,2,1,0,73,74,5,28,0,0,74,78,5,1,0,0,75,77,
        3,56,28,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,
        0,79,81,1,0,0,0,80,78,1,0,0,0,81,82,3,6,3,0,82,83,5,2,0,0,83,87,
        3,60,30,0,84,86,3,58,29,0,85,84,1,0,0,0,86,89,1,0,0,0,87,85,1,0,
        0,0,87,88,1,0,0,0,88,90,1,0,0,0,89,87,1,0,0,0,90,91,5,3,0,0,91,92,
        5,0,0,1,92,93,6,0,-1,0,93,1,1,0,0,0,94,95,5,4,0,0,95,3,1,0,0,0,96,
        97,5,5,0,0,97,5,1,0,0,0,98,99,5,6,0,0,99,7,1,0,0,0,100,101,5,7,0,
        0,101,9,1,0,0,0,102,103,5,8,0,0,103,11,1,0,0,0,104,105,5,9,0,0,105,
        13,1,0,0,0,106,107,5,10,0,0,107,15,1,0,0,0,108,109,5,11,0,0,109,
        17,1,0,0,0,110,111,5,12,0,0,111,19,1,0,0,0,112,113,5,13,0,0,113,
        21,1,0,0,0,114,115,5,14,0,0,115,23,1,0,0,0,116,117,5,15,0,0,117,
        25,1,0,0,0,118,119,5,16,0,0,119,27,1,0,0,0,120,121,5,17,0,0,121,
        29,1,0,0,0,122,130,3,32,16,0,123,124,5,33,0,0,124,125,6,15,-1,0,
        125,126,3,32,16,0,126,127,6,15,-1,0,127,129,1,0,0,0,128,123,1,0,
        0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,31,1,0,0,
        0,132,130,1,0,0,0,133,134,3,34,17,0,134,146,6,16,-1,0,135,136,5,
        18,0,0,136,140,6,16,-1,0,137,138,5,19,0,0,138,140,6,16,-1,0,139,
        135,1,0,0,0,139,137,1,0,0,0,140,141,1,0,0,0,141,142,3,34,17,0,142,
        143,6,16,-1,0,143,145,1,0,0,0,144,139,1,0,0,0,145,148,1,0,0,0,146,
        144,1,0,0,0,146,147,1,0,0,0,147,33,1,0,0,0,148,146,1,0,0,0,149,150,
        3,36,18,0,150,164,6,17,-1,0,151,152,5,20,0,0,152,158,6,17,-1,0,153,
        154,5,21,0,0,154,158,6,17,-1,0,155,156,5,22,0,0,156,158,6,17,-1,
        0,157,151,1,0,0,0,157,153,1,0,0,0,157,155,1,0,0,0,158,159,1,0,0,
        0,159,160,3,36,18,0,160,161,6,17,-1,0,161,163,1,0,0,0,162,157,1,
        0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,35,1,0,
        0,0,166,164,1,0,0,0,167,169,7,0,0,0,168,167,1,0,0,0,168,169,1,0,
        0,0,169,182,1,0,0,0,170,171,5,28,0,0,171,183,6,18,-1,0,172,173,5,
        30,0,0,173,183,6,18,-1,0,174,175,5,31,0,0,175,183,6,18,-1,0,176,
        177,5,23,0,0,177,178,6,18,-1,0,178,179,3,30,15,0,179,180,5,24,0,
        0,180,181,6,18,-1,0,181,183,1,0,0,0,182,170,1,0,0,0,182,172,1,0,
        0,0,182,174,1,0,0,0,182,176,1,0,0,0,183,37,1,0,0,0,184,188,5,2,0,
        0,185,187,3,58,29,0,186,185,1,0,0,0,187,190,1,0,0,0,188,186,1,0,
        0,0,188,189,1,0,0,0,189,191,1,0,0,0,190,188,1,0,0,0,191,192,5,3,
        0,0,192,39,1,0,0,0,193,194,5,28,0,0,194,195,5,25,0,0,195,196,3,30,
        15,0,196,197,6,20,-1,0,197,198,5,1,0,0,198,41,1,0,0,0,199,200,3,
        40,20,0,200,43,1,0,0,0,201,202,3,20,10,0,202,203,5,23,0,0,203,204,
        3,30,15,0,204,205,5,24,0,0,205,206,6,22,-1,0,206,211,3,38,19,0,207,
        208,3,18,9,0,208,209,6,22,-1,0,209,210,3,38,19,0,210,212,1,0,0,0,
        211,207,1,0,0,0,211,212,1,0,0,0,212,213,1,0,0,0,213,214,6,22,-1,
        0,214,45,1,0,0,0,215,216,3,22,11,0,216,217,6,23,-1,0,217,218,5,23,
        0,0,218,219,3,30,15,0,219,220,5,24,0,0,220,221,6,23,-1,0,221,222,
        3,38,19,0,222,223,6,23,-1,0,223,47,1,0,0,0,224,225,3,26,13,0,225,
        226,5,23,0,0,226,227,3,40,20,0,227,228,5,1,0,0,228,229,3,30,15,0,
        229,230,6,24,-1,0,230,231,5,1,0,0,231,232,3,40,20,0,232,233,5,24,
        0,0,233,234,3,38,19,0,234,49,1,0,0,0,235,238,3,28,14,0,236,238,3,
        4,2,0,237,235,1,0,0,0,237,236,1,0,0,0,238,239,1,0,0,0,239,245,5,
        23,0,0,240,241,3,30,15,0,241,242,6,25,-1,0,242,246,1,0,0,0,243,244,
        5,29,0,0,244,246,6,25,-1,0,245,240,1,0,0,0,245,243,1,0,0,0,246,254,
        1,0,0,0,247,250,5,26,0,0,248,251,3,30,15,0,249,251,5,29,0,0,250,
        248,1,0,0,0,250,249,1,0,0,0,251,253,1,0,0,0,252,247,1,0,0,0,253,
        256,1,0,0,0,254,252,1,0,0,0,254,255,1,0,0,0,255,257,1,0,0,0,256,
        254,1,0,0,0,257,258,5,24,0,0,258,259,5,1,0,0,259,51,1,0,0,0,260,
        261,5,28,0,0,261,270,5,23,0,0,262,267,3,30,15,0,263,264,5,26,0,0,
        264,266,3,30,15,0,265,263,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,
        0,267,268,1,0,0,0,268,271,1,0,0,0,269,267,1,0,0,0,270,262,1,0,0,
        0,270,271,1,0,0,0,271,272,1,0,0,0,272,273,5,24,0,0,273,274,5,1,0,
        0,274,275,6,26,-1,0,275,53,1,0,0,0,276,279,3,14,7,0,277,279,3,16,
        8,0,278,276,1,0,0,0,278,277,1,0,0,0,279,55,1,0,0,0,280,281,3,12,
        6,0,281,282,5,28,0,0,282,283,5,23,0,0,283,284,3,68,34,0,284,285,
        5,24,0,0,285,286,5,2,0,0,286,290,3,60,30,0,287,289,3,58,29,0,288,
        287,1,0,0,0,289,292,1,0,0,0,290,288,1,0,0,0,290,291,1,0,0,0,291,
        293,1,0,0,0,292,290,1,0,0,0,293,294,5,3,0,0,294,295,6,28,-1,0,295,
        296,6,28,-1,0,296,297,6,28,-1,0,297,57,1,0,0,0,298,305,3,40,20,0,
        299,305,3,48,24,0,300,305,3,44,22,0,301,305,3,46,23,0,302,305,3,
        50,25,0,303,305,3,52,26,0,304,298,1,0,0,0,304,299,1,0,0,0,304,300,
        1,0,0,0,304,301,1,0,0,0,304,302,1,0,0,0,304,303,1,0,0,0,305,59,1,
        0,0,0,306,308,3,62,31,0,307,306,1,0,0,0,308,311,1,0,0,0,309,307,
        1,0,0,0,309,310,1,0,0,0,310,61,1,0,0,0,311,309,1,0,0,0,312,313,3,
        54,27,0,313,314,3,64,32,0,314,315,5,1,0,0,315,316,6,31,-1,0,316,
        63,1,0,0,0,317,318,5,28,0,0,318,319,3,66,33,0,319,65,1,0,0,0,320,
        321,5,26,0,0,321,323,3,64,32,0,322,320,1,0,0,0,323,326,1,0,0,0,324,
        322,1,0,0,0,324,325,1,0,0,0,325,67,1,0,0,0,326,324,1,0,0,0,327,332,
        3,70,35,0,328,329,5,26,0,0,329,331,3,70,35,0,330,328,1,0,0,0,331,
        334,1,0,0,0,332,330,1,0,0,0,332,333,1,0,0,0,333,69,1,0,0,0,334,332,
        1,0,0,0,335,336,5,28,0,0,336,337,5,27,0,0,337,338,3,54,27,0,338,
        339,6,35,-1,0,339,71,1,0,0,0,23,78,87,130,139,146,157,164,168,182,
        188,211,237,245,250,254,267,270,278,290,304,309,324,332
>>>>>>> Stashed changes
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "'}'", "'program'", "'writeln'", 
                     "'main'", "'end'", "'var'", "'void'", "'int'", "'float'", 
                     "'else'", "'if'", "'while'", "'do'", "'for'", "'write'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'='", 
                     "','", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Id", "CTE_STRING", "CTE_INT", "CTE_FLOAT", "WS", 
                      "OP_REL" ]

    RULE_programRule = 0
    RULE_program = 1
    RULE_writeln = 2
    RULE_main = 3
    RULE_end = 4
    RULE_var = 5
    RULE_void = 6
    RULE_int = 7
    RULE_float = 8
    RULE_else = 9
    RULE_if = 10
    RULE_while = 11
    RULE_do = 12
    RULE_for = 13
    RULE_write = 14
    RULE_expression = 15
    RULE_exp = 16
    RULE_term = 17
    RULE_factor = 18
    RULE_body = 19
    RULE_assign = 20
    RULE_initialization = 21
    RULE_condition = 22
    RULE_cycle = 23
    RULE_forSt = 24
    RULE_print = 25
    RULE_functionCall = 26
    RULE_type = 27
    RULE_function = 28
    RULE_statement = 29
    RULE_variables = 30
    RULE_listvars = 31
    RULE_listaId = 32
    RULE_idExtra = 33
    RULE_parameters = 34
    RULE_parameter = 35

    ruleNames =  [ "programRule", "program", "writeln", "main", "end", "var", 
                   "void", "int", "float", "else", "if", "while", "do", 
                   "for", "write", "expression", "exp", "term", "factor", 
                   "body", "assign", "initialization", "condition", "cycle", 
                   "forSt", "print", "functionCall", "type", "function", 
                   "statement", "variables", "listvars", "listaId", "idExtra", 
                   "parameters", "parameter" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    Id=28
    CTE_STRING=29
    CTE_INT=30
    CTE_FLOAT=31
    WS=32
    OP_REL=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(gramaticaParser.ProgramContext,0)


        def Id(self):
            return self.getToken(gramaticaParser.Id, 0)

        def main(self):
            return self.getTypedRuleContext(gramaticaParser.MainContext,0)


        def variables(self):
            return self.getTypedRuleContext(gramaticaParser.VariablesContext,0)


        def EOF(self):
            return self.getToken(gramaticaParser.EOF, 0)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.FunctionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.FunctionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_programRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramRule" ):
                listener.enterProgramRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramRule" ):
                listener.exitProgramRule(self)




    def programRule(self):

        localctx = gramaticaParser.ProgramRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.program()
            self.state = 73
            self.match(gramaticaParser.Id)
            self.state = 74
            self.match(gramaticaParser.T__0)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 75
                self.function()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.main()
            self.state = 82
            self.match(gramaticaParser.T__1)
            self.state = 83
            self.variables()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268656672) != 0):
                self.state = 84
                self.statement()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(gramaticaParser.T__2)
            self.state = 91
            self.match(gramaticaParser.EOF)
            symbol_table.maquina(symbol_table.cuadruplo)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = gramaticaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(gramaticaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WritelnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_writeln

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteln" ):
                listener.enterWriteln(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteln" ):
                listener.exitWriteln(self)




    def writeln(self):

        localctx = gramaticaParser.WritelnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_writeln)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(gramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = gramaticaParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(gramaticaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd" ):
                listener.enterEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd" ):
                listener.exitEnd(self)




    def end(self):

        localctx = gramaticaParser.EndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(gramaticaParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = gramaticaParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(gramaticaParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_void

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoid" ):
                listener.enterVoid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoid" ):
                listener.exitVoid(self)




    def void(self):

        localctx = gramaticaParser.VoidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_void)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(gramaticaParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)




    def int_(self):

        localctx = gramaticaParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(gramaticaParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)




    def float_(self):

        localctx = gramaticaParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(gramaticaParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)




    def else_(self):

        localctx = gramaticaParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(gramaticaParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)




    def if_(self):

        localctx = gramaticaParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(gramaticaParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)




    def while_(self):

        localctx = gramaticaParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(gramaticaParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_do

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo" ):
                listener.enterDo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo" ):
                listener.exitDo(self)




    def do(self):

        localctx = gramaticaParser.DoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_do)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(gramaticaParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)




    def for_(self):

        localctx = gramaticaParser.ForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(gramaticaParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)




    def write(self):

        localctx = gramaticaParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(gramaticaParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._OP_REL = None # Token

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpContext,i)


        def OP_REL(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.OP_REL)
            else:
                return self.getToken(gramaticaParser.OP_REL, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = gramaticaParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.exp()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 123
                localctx._OP_REL = self.match(gramaticaParser.OP_REL)
                symbol_table.push_operador((None if localctx._OP_REL is None else localctx._OP_REL.text))
                self.state = 125
                self.exp()
                symbol_table.push_mayor_menor()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.TermContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.TermContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = gramaticaParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.term()
            symbol_table.push_sumas()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 139
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [18]:
                    self.state = 135
                    self.match(gramaticaParser.T__17)
                    symbol_table.push_operador('+')
                    pass
                elif token in [19]:
                    self.state = 137
                    self.match(gramaticaParser.T__18)
                    symbol_table.push_operador('-')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 141
                self.term()
                symbol_table.push_sumas()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.FactorContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.FactorContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = gramaticaParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.factor()
            symbol_table.push_multi()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0):
                self.state = 157
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [20]:
                    self.state = 151
                    self.match(gramaticaParser.T__19)
                    symbol_table.push_operador('*')
                    pass
                elif token in [21]:
                    self.state = 153
                    self.match(gramaticaParser.T__20)
                    symbol_table.push_operador('/')
                    pass
                elif token in [22]:
                    self.state = 155
                    self.match(gramaticaParser.T__21)
                    symbol_table.push_operador('%')
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 159
                self.factor()
                symbol_table.push_multi()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token
            self._CTE_INT = None # Token
            self._CTE_FLOAT = None # Token

        def Id(self):
            return self.getToken(gramaticaParser.Id, 0)

        def CTE_INT(self):
            return self.getToken(gramaticaParser.CTE_INT, 0)

        def CTE_FLOAT(self):
            return self.getToken(gramaticaParser.CTE_FLOAT, 0)

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = gramaticaParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18 or _la==19:
                self.state = 167
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


<<<<<<< Updated upstream
            self.state = 178
=======
            self.state = 182
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 170
                localctx._Id = self.match(gramaticaParser.Id)
                symbol_table.push_factor((None if localctx._Id is None else localctx._Id.text), None, False)
                pass
            elif token in [30]:
                self.state = 172
                localctx._CTE_INT = self.match(gramaticaParser.CTE_INT)
                symbol_table.push_factor((None if localctx._CTE_INT is None else localctx._CTE_INT.text), 'int', True)
                pass
            elif token in [31]:
                self.state = 174
                localctx._CTE_FLOAT = self.match(gramaticaParser.CTE_FLOAT)
                symbol_table.push_factor((None if localctx._CTE_FLOAT is None else localctx._CTE_FLOAT.text), 'float', True)
                pass
<<<<<<< Updated upstream
            elif token in [22]:
                self.state = 174
                self.match(gramaticaParser.T__21)
                self.state = 175
                self.expression()
                self.state = 176
                self.match(gramaticaParser.T__22)
=======
            elif token in [23]:
                self.state = 176
                self.match(gramaticaParser.T__22)
                symbol_table.push_parentesis('(')
                self.state = 178
                self.expression()
                self.state = 179
                self.match(gramaticaParser.T__23)
                symbol_table.pop_parentesis()
>>>>>>> Stashed changes
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = gramaticaParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 180
            self.match(gramaticaParser.T__0)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268546064) != 0):
                self.state = 181
                self.statement()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self.match(gramaticaParser.T__1)
=======
            self.state = 184
            self.match(gramaticaParser.T__1)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268656672) != 0):
                self.state = 185
                self.statement()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
            self.match(gramaticaParser.T__2)
>>>>>>> Stashed changes
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token

        def Id(self):
            return self.getToken(gramaticaParser.Id, 0)

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = gramaticaParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 189
            localctx._Id = self.match(gramaticaParser.Id)
            self.state = 190
            self.match(gramaticaParser.T__23)
            self.state = 191
            self.expression()
            symbol_table.assign((None if localctx._Id is None else localctx._Id.text), '=')
            self.state = 193
            self.match(gramaticaParser.T__24)
=======
            self.state = 193
            localctx._Id = self.match(gramaticaParser.Id)
            self.state = 194
            self.match(gramaticaParser.T__24)
            self.state = 195
            self.expression()
            symbol_table.assign((None if localctx._Id is None else localctx._Id.text), '=')
            self.state = 197
            self.match(gramaticaParser.T__0)
>>>>>>> Stashed changes
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(gramaticaParser.AssignContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_initialization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitialization" ):
                listener.enterInitialization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitialization" ):
                listener.exitInitialization(self)




    def initialization(self):

        localctx = gramaticaParser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 195
=======
            self.state = 199
>>>>>>> Stashed changes
            self.assign()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(gramaticaParser.IfContext,0)


        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.BodyContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.BodyContext,i)


        def else_(self):
            return self.getTypedRuleContext(gramaticaParser.ElseContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = gramaticaParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 197
            self.if_()
            self.state = 198
            self.match(gramaticaParser.T__21)
            self.state = 199
            self.expression()
            self.state = 200
            self.match(gramaticaParser.T__22)
            symbol_table.ifSt()
            self.state = 202
            self.body()
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 203
                self.else_()
                symbol_table.elseSt()
                self.state = 205
=======
            self.state = 201
            self.if_()
            self.state = 202
            self.match(gramaticaParser.T__22)
            self.state = 203
            self.expression()
            self.state = 204
            self.match(gramaticaParser.T__23)
            symbol_table.ifSt()
            self.state = 206
            self.body()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 207
                self.else_()
                symbol_table.elseSt()
                self.state = 209
>>>>>>> Stashed changes
                self.body()


            symbol_table.endIf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def while_(self):
            return self.getTypedRuleContext(gramaticaParser.WhileContext,0)


        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def body(self):
            return self.getTypedRuleContext(gramaticaParser.BodyContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)




    def cycle(self):

        localctx = gramaticaParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 211
            self.while_()
            symbol_table.whileSt()
            self.state = 213
            self.match(gramaticaParser.T__21)
            self.state = 214
            self.expression()
            self.state = 215
            self.match(gramaticaParser.T__22)
            symbol_table.whileIf()
            self.state = 217
=======
            self.state = 215
            self.while_()
            symbol_table.whileSt()
            self.state = 217
            self.match(gramaticaParser.T__22)
            self.state = 218
            self.expression()
            self.state = 219
            self.match(gramaticaParser.T__23)
            symbol_table.ifSt()
            self.state = 221
>>>>>>> Stashed changes
            self.body()
            symbol_table.end_while()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_(self):
            return self.getTypedRuleContext(gramaticaParser.ForContext,0)


        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.AssignContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.AssignContext,i)


        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def body(self):
            return self.getTypedRuleContext(gramaticaParser.BodyContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_forSt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForSt" ):
                listener.enterForSt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForSt" ):
                listener.exitForSt(self)




    def forSt(self):

        localctx = gramaticaParser.ForStContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forSt)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 220
            self.for_()
            self.state = 221
            self.match(gramaticaParser.T__21)
            self.state = 222
            self.assign()
            self.state = 223
            self.match(gramaticaParser.T__24)
            self.state = 224
            self.expression()
            symbol_table.ifSt()
            self.state = 226
            self.match(gramaticaParser.T__24)
            self.state = 227
            self.assign()
            self.state = 228
            self.match(gramaticaParser.T__22)
            self.state = 229
=======
            self.state = 224
            self.for_()
            self.state = 225
            self.match(gramaticaParser.T__22)
            self.state = 226
            self.assign()
            self.state = 227
            self.match(gramaticaParser.T__0)
            self.state = 228
            self.expression()
            symbol_table.ifSt()
            self.state = 230
            self.match(gramaticaParser.T__0)
            self.state = 231
            self.assign()
            self.state = 232
            self.match(gramaticaParser.T__23)
            self.state = 233
>>>>>>> Stashed changes
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._CTE_STRING = None # Token

        def write(self):
            return self.getTypedRuleContext(gramaticaParser.WriteContext,0)


        def writeln(self):
            return self.getTypedRuleContext(gramaticaParser.WritelnContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def CTE_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.CTE_STRING)
            else:
                return self.getToken(gramaticaParser.CTE_STRING, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)




    def print_(self):

        localctx = gramaticaParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 231
                self.write()
                pass
            elif token in [4]:
                self.state = 232
=======
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 235
                self.write()
                pass
            elif token in [5]:
                self.state = 236
>>>>>>> Stashed changes
                self.writeln()
                pass
            else:
                raise NoViableAltException(self)

<<<<<<< Updated upstream
            self.state = 235
            self.match(gramaticaParser.T__21)
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 22, 28, 30, 31]:
                self.state = 236
=======
            self.state = 239
            self.match(gramaticaParser.T__22)
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 23, 28, 30, 31]:
                self.state = 240
>>>>>>> Stashed changes
                self.expression()
                symbol_table.print_function()
                pass
            elif token in [29]:
<<<<<<< Updated upstream
                self.state = 239
=======
                self.state = 243
>>>>>>> Stashed changes
                localctx._CTE_STRING = self.match(gramaticaParser.CTE_STRING)
                symbol_table.push_factor((None if localctx._CTE_STRING is None else localctx._CTE_STRING.text), 'string', True)
                pass
            else:
                raise NoViableAltException(self)

<<<<<<< Updated upstream
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 243
                self.match(gramaticaParser.T__25)
                self.state = 249
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [17, 18, 22, 28, 30, 31]:
                    self.state = 244
=======
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 247
                self.match(gramaticaParser.T__25)
                self.state = 250
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [18, 19, 23, 28, 30, 31]:
                    self.state = 248
>>>>>>> Stashed changes
                    self.expression()
                    symbol_table.print_function()
                    pass
                elif token in [29]:
                    self.state = 249
                    localctx._CTE_STRING = self.match(gramaticaParser.CTE_STRING)
                    symbol_table.push_factor((None if localctx._CTE_STRING is None else localctx._CTE_STRING.text), 'string', True)
                    pass
                else:
                    raise NoViableAltException(self)

<<<<<<< Updated upstream
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 256
            self.match(gramaticaParser.T__22)
            self.state = 257
            self.match(gramaticaParser.T__24)
            symbol_table.print_function()
=======
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 257
            self.match(gramaticaParser.T__23)
            self.state = 258
            self.match(gramaticaParser.T__0)
>>>>>>> Stashed changes
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token

        def Id(self):
            return self.getToken(gramaticaParser.Id, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = gramaticaParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
<<<<<<< Updated upstream
            self.match(gramaticaParser.Id)
            self.state = 261
            self.match(gramaticaParser.T__21)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3494248448) != 0):
=======
            localctx._Id = self.match(gramaticaParser.Id)
            self.state = 261
            self.match(gramaticaParser.T__22)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3498835968) != 0):
>>>>>>> Stashed changes
                self.state = 262
                self.expression()
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26:
                    self.state = 263
                    self.match(gramaticaParser.T__25)
                    self.state = 264
                    self.expression()
                    self.state = 269
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 272
<<<<<<< Updated upstream
            self.match(gramaticaParser.T__22)
            self.state = 273
            self.match(gramaticaParser.T__24)
=======
            self.match(gramaticaParser.T__23)
            self.state = 273
            self.match(gramaticaParser.T__0)
            symbol_table.fCall((None if localctx._Id is None else localctx._Id.text))
>>>>>>> Stashed changes
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_(self):
            return self.getTypedRuleContext(gramaticaParser.IntContext,0)


        def float_(self):
            return self.getTypedRuleContext(gramaticaParser.FloatContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = gramaticaParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_type)
        try:
<<<<<<< Updated upstream
            self.state = 277
=======
            self.state = 278
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
                self.state = 275
=======
                self.state = 276
>>>>>>> Stashed changes
                self.int_()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
<<<<<<< Updated upstream
                self.state = 276
=======
                self.state = 277
>>>>>>> Stashed changes
                self.float_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token
            self._parameters = None # ParametersContext
            self._variables = None # VariablesContext

        def void(self):
            return self.getTypedRuleContext(gramaticaParser.VoidContext,0)


        def Id(self):
            return self.getToken(gramaticaParser.Id, 0)

        def parameters(self):
            return self.getTypedRuleContext(gramaticaParser.ParametersContext,0)


        def variables(self):
            return self.getTypedRuleContext(gramaticaParser.VariablesContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = gramaticaParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 279
            self.void()
            self.state = 280
            localctx._Id = self.match(gramaticaParser.Id)
            self.state = 281
            self.match(gramaticaParser.T__21)
            self.state = 282
            localctx._parameters = self.parameters()
            self.state = 283
            self.match(gramaticaParser.T__22)
            self.state = 284
            self.match(gramaticaParser.T__0)
=======
            self.state = 280
            self.void()
            self.state = 281
            localctx._Id = self.match(gramaticaParser.Id)
            self.state = 282
            self.match(gramaticaParser.T__22)
            self.state = 283
            localctx._parameters = self.parameters()
            self.state = 284
            self.match(gramaticaParser.T__23)
>>>>>>> Stashed changes
            self.state = 285
            localctx._variables = self.variables()
            self.state = 286
<<<<<<< Updated upstream
            self.body()
            self.state = 287
            self.match(gramaticaParser.T__1)
            self.state = 288
            self.match(gramaticaParser.T__24)
=======
            localctx._variables = self.variables()
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268656672) != 0):
                self.state = 287
                self.statement()
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 293
            self.match(gramaticaParser.T__2)
>>>>>>> Stashed changes
            symbol_table.add_func((None if localctx._Id is None else localctx._Id.text), (None if localctx._parameters is None else self._input.getText(localctx._parameters.start,localctx._parameters.stop)), (None if localctx._variables is None else self._input.getText(localctx._variables.start,localctx._variables.stop)), current_scope)
            symbol_table.getQuads((None if localctx._Id is None else localctx._Id.text))
            symbol_table.pop_func((None if localctx._Id is None else localctx._Id.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(gramaticaParser.AssignContext,0)


        def forSt(self):
            return self.getTypedRuleContext(gramaticaParser.ForStContext,0)


        def condition(self):
            return self.getTypedRuleContext(gramaticaParser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(gramaticaParser.CycleContext,0)


        def print_(self):
            return self.getTypedRuleContext(gramaticaParser.PrintContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(gramaticaParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = gramaticaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_statement)
        try:
<<<<<<< Updated upstream
            self.state = 298
=======
            self.state = 304
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
                self.state = 292
=======
                self.state = 298
>>>>>>> Stashed changes
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
<<<<<<< Updated upstream
                self.state = 293
=======
                self.state = 299
>>>>>>> Stashed changes
                self.forSt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
<<<<<<< Updated upstream
                self.state = 294
=======
                self.state = 300
>>>>>>> Stashed changes
                self.condition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
<<<<<<< Updated upstream
                self.state = 295
=======
                self.state = 301
>>>>>>> Stashed changes
                self.cycle()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
<<<<<<< Updated upstream
                self.state = 296
=======
                self.state = 302
>>>>>>> Stashed changes
                self.print_()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
<<<<<<< Updated upstream
                self.state = 297
=======
                self.state = 303
>>>>>>> Stashed changes
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listvars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ListvarsContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ListvarsContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_variables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariables" ):
                listener.enterVariables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariables" ):
                listener.exitVariables(self)




    def variables(self):

        localctx = gramaticaParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_variables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 300
                self.listvars()
                self.state = 305
=======
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==11:
                self.state = 306
                self.listvars()
                self.state = 311
>>>>>>> Stashed changes
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListvarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._type = None # TypeContext
            self._listaId = None # ListaIdContext

        def type_(self):
            return self.getTypedRuleContext(gramaticaParser.TypeContext,0)


        def listaId(self):
            return self.getTypedRuleContext(gramaticaParser.ListaIdContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_listvars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListvars" ):
                listener.enterListvars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListvars" ):
                listener.exitListvars(self)




    def listvars(self):

        localctx = gramaticaParser.ListvarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_listvars)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 306
            localctx._type = self.type_()
            self.state = 307
            localctx._listaId = self.listaId()
            self.state = 308
            self.match(gramaticaParser.T__24)
=======
            self.state = 312
            localctx._type = self.type_()
            self.state = 313
            localctx._listaId = self.listaId()
            self.state = 314
            self.match(gramaticaParser.T__0)
>>>>>>> Stashed changes
            symbol_table.add_symbol((None if localctx._listaId is None else self._input.getText(localctx._listaId.start,localctx._listaId.stop)), (None if localctx._type is None else self._input.getText(localctx._type.start,localctx._type.stop)), current_scope)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(gramaticaParser.Id, 0)

        def idExtra(self):
            return self.getTypedRuleContext(gramaticaParser.IdExtraContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_listaId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaId" ):
                listener.enterListaId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaId" ):
                listener.exitListaId(self)




    def listaId(self):

        localctx = gramaticaParser.ListaIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_listaId)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 311
            self.match(gramaticaParser.Id)
            self.state = 312
=======
            self.state = 317
            self.match(gramaticaParser.Id)
            self.state = 318
>>>>>>> Stashed changes
            self.idExtra()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdExtraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaId(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ListaIdContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ListaIdContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_idExtra

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExtra" ):
                listener.enterIdExtra(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExtra" ):
                listener.exitIdExtra(self)




    def idExtra(self):

        localctx = gramaticaParser.IdExtraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_idExtra)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 318
=======
            self.state = 324
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
<<<<<<< Updated upstream
                    self.state = 314
                    self.match(gramaticaParser.T__25)
                    self.state = 315
                    self.listaId() 
                self.state = 320
=======
                    self.state = 320
                    self.match(gramaticaParser.T__25)
                    self.state = 321
                    self.listaId() 
                self.state = 326
>>>>>>> Stashed changes
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ParameterContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ParameterContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = gramaticaParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 321
            self.parameter()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 322
                self.match(gramaticaParser.T__25)
                self.state = 323
                self.parameter()
                self.state = 328
=======
            self.state = 327
            self.parameter()
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 328
                self.match(gramaticaParser.T__25)
                self.state = 329
                self.parameter()
                self.state = 334
>>>>>>> Stashed changes
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token
            self._type = None # TypeContext

        def Id(self):
            return self.getToken(gramaticaParser.Id, 0)

        def type_(self):
            return self.getTypedRuleContext(gramaticaParser.TypeContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = gramaticaParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 329
            localctx._Id = self.match(gramaticaParser.Id)
            self.state = 330
            self.match(gramaticaParser.T__26)
            self.state = 331
=======
            self.state = 335
            localctx._Id = self.match(gramaticaParser.Id)
            self.state = 336
            self.match(gramaticaParser.T__26)
            self.state = 337
>>>>>>> Stashed changes
            localctx._type = self.type_()
            symbol_table.add_symbol((None if localctx._Id is None else localctx._Id.text), (None if localctx._type is None else self._input.getText(localctx._type.start,localctx._type.stop)), current_scope)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





