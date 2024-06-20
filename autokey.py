# -*- coding: utf-8 -*-

### pip install PyUserInput

from pykeyboard import *
import time


k = PyKeyboard() #建立键盘对象

prog = """
TO DRAWPIC :X :Y :ANGLE
 HOME
 PU
 SETXY :X :Y
 RT :ANGLE
 SCANLINE [-84 3 0 87 -83 5 0 88 -83 2 -1 3 -39 3 0 131 -84 6 -37 5 0 132 -3 15 -3 47 -3 8 -6 6 -36 2 -1 2 0 132 -3 16 -1 49 -2 8 -8 4 -36 5 0 132 -2 79 -6 5 -36 3 0 131 6 -10 7 -15 5 -14 5 -4 7 -4 5 -6 4 0 92 5 -12 6 -15 5 -14 5 -4 6 -4 6 -6 4 0 92 3 -5 6 -4 5 -4 16 -4 15 -4 5 -4 7 -6 4 0 92 3 -5 6 -4 5 -4 16 -4 15 -4 4 -4 8 -6 4 0 92 3 -5 15 -4 16 -4 15 -4 3 -4 9 -6 4 -6 8 -8 7 -7 3 -11 8 0 150 3 -5 15 -4 16 -4 15 -4 2 -4 9 -7 4 -5 10 -5 10 -5 5 -8 10 0 150 3 -5 4 -6 5 -13 7 -12 7 -9 9 -8 4 -5 11 -4 11 -4 2 -1 2 -7 9 -1 1 0 150 3 -5 4 -6 5 -13 7 -12 7 -9 8 -9 4 -5 12 -3 12 -3 5 -6 12 0 150 3 -5 6 -4 5 -4 16 -4 15 -4 2 -4 6 -10 4 -5 4 -4 5 -2 4 -4 5 -3 3 -6 5 0 142 3 -5 6 -4 5 -4 16 -4 15 -4 3 -4 4 -11 4 -5 4 -5 5 -1 4 -5 5 -2 3 -6 4 0 141 3 -5 6 -4 5 -4 16 -4 15 -4 4 -4 5 -9 4 -5 4 -6 4 -1 4 -6 5 -1 3 -5 4 0 140 3 -5 6 -4 5 -4 16 -4 15 -4 5 -4 4 -9 4 -5 4 -7 3 -1 4 -7 4 -1 3 -5 4 0 140 4 -4 6 -4 5 -4 16 -4 15 -4 5 -5 4 -8 4 -5 4 -7 3 -1 4 -7 4 -1 3 -5 4 0 140 5 -13 5 -15 5 -14 5 -4 6 -5 5 -6 4 -5 4 -7 3 -1 4 -7 4 -1 3 -5 4 0 140 6 -8 1 -3 5 -15 5 -14 5 -4 7 -4 5 -6 4 -5 4 -7 3 -1 4 -7 4 -1 3 -5 4 0 140 -3 79 -7 4 -4 5 -6 3 -1 5 -6 4 -1 4 -4 4 0 140 -3 79 -7 5 -4 5 -5 3 -2 5 -5 4 -1 5 -3 4 0 140 -5 66 -2 9 -8 6 -3 12 -3 6 -3 4 -2 6 -1 14 0 150 -5 66 -2 9 -9 6 -3 11 -4 6 -2 4 -3 20 0 150 -92 2 -1 2 -4 10 -5 2 -1 2 -2 4 -4 2 -1 14 -1 1 0 150 -93 3 -6 9 -6 3 -3 4 -5 3 -2 13 0 150 -123 4 0 127 -123 4 0 127 -122 5 0 127 -121 5 0 126 -120 5 0 125 -112 12 0 124 -111 2 -1 9 0 123 -111 11 0 122 -112 9 0 121 0 0 0 0 0 0 -9 2 -14 2 -33 3 -46 2 -31 3 0 145 4 -5 2 -8 1 -5 2 -34 2 -4 2 -31 2 -2 3 -3 3 -23 2 -4 7 0 149 -2 2 -1 2 -3 6 -4 2 -3 2 -1 5 -22 15 -30 2 -2 3 -1 5 -13 3 -7 2 -1 11 0 150 -3 1 -2 10 -4 3 -2 8 -22 6 -6 2 -31 4 -2 1 -3 1 -1 2 -5 11 -7 1 -4 2 0 144 -6 4 -2 1 -8 2 -2 1 -2 1 -2 2 -21 3 -8 1 -1 1 -32 1 -4 2 -1 6 -6 10 -12 1 -1 3 0 147 -4 1 -2 1 -3 2 -12 1 -1 2 -2 1 -23 2 -5 5 -32 1 -5 1 -4 1 -1 1 -25 1 -2 2 -1 5 0 149 5 -3 2 -1 2 -11 1 -2 2 -28 9 -33 5 -1 2 -1 5 -22 4 -1 10 0 150 5 -4 3 -15 2 -8 15 -5 3 -1 2 -18 15 -5 2 -3 1 -3 1 -26 2 -2 1 -2 2 0 146 -3 2 -4 4 -9 1 -4 2 -8 15 -9 2 -1 2 -15 15 -5 2 -3 1 -1 5 -9 7 -8 2 -3 7 0 149 -2 2 -4 7 -7 1 -4 2 -9 4 -15 1 -3 6 -15 5 -14 6 -3 1 -9 10 -7 2 -1 10 0 150 -2 2 -3 2 -3 4 -5 2 -3 4 -27 2 -2 2 -36 4 -1 2 -2 5 -24 2 -5 2 0 146 -3 2 -1 2 -5 3 -5 1 -4 2 -1 2 -26 6 -38 2 -2 1 -2 3 -27 1 -5 2 0 146 -3 3 -12 4 -3 2 -2 3 -25 6 -38 2 -2 2 -3 1 -17 3 -6 3 -5 1 -2 2 0 150 -2 15 -2 3 -3 2 -2 5 -22 2 -3 10 -30 4 -1 9 -4 13 -4 14 0 150 2 -4 9 -5 2 -2 1 -5 3 -22 2 -5 8 -31 2 -1 1 -2 7 -4 14 -3 1 -4 9 0 149 -64 5 -32 1 -6 6 0 114 ]
 HT
END

TO SCANLINE :PDATA
 TEST :PDATA = []
 IFTRUE STOP
 MAKE "D FIRST :PDATA
 MAKE "FOLLOW BUTFIRST :PDATA
 IF :D = 0 NEXTLINE FIRST :FOLLOW MAKE "FOLLOW BUTFIRST :FOLLOW
 IF :D > 0 PD FD :D
 IF :D < 0 PU FD 0 - :D
 SCANLINE :FOLLOW
END

TO NEXTLINE :B
 IF :B > 0 PU BK :B RT 90 FD 1 LT 90
 IF :B < 0 PU BK 0 - :B RT 90 FD 2 LT 90
END
"""

time.sleep(5)
for c in prog:
    if c == "\n":
        k.tap_key(k.return_key)
    else:
        k.type_string(c)
    time.sleep(0.1)
