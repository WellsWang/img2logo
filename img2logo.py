# -*- coding: utf-8 -*-
import sys
import numpy as np
from PIL import Image

def image2array(img):

    arr = np.array(Image.open(img), dtype='uint8')
    return arr

def output_array(arr):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            print("▓" if arr[row][col] else " ",end="")
        print("")

def gen_data(arr):
    data=''
    for row in range(len(arr)):   
        count = 0         
        length = 0
        for col in range(len(arr[row])):
            if col==0:
                last_pt = arr[row][col]
            length = length + 1
            if arr[row][col] != last_pt:
                if arr[row][col]:
                    data += f"-{length} "
                else:
                    data += f"{length} "
                count += length
                length = 0
                last_pt = arr[row][col]
  
        if last_pt:
            data += f"{length} "
            count += length
        data += f"0 {count} "
    return data

def build_LOGO(data):
    return f"""
TO DRAWPIC :X :Y :ANGLE
 HOME
 PU
 SETXY :X :Y
 RT :ANGLE
 SCANLINE [{data}]
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
END"""

if __name__ == '__main__':
    if len(sys.argv)>1:
        try:
            arr = image2array(sys.argv[1])
            output_array(arr)
            print(build_LOGO(gen_data(arr)))
        except:
            print("Error on open image file, please check the image file.")
    else:
        print("-= Image to LOGO =- \n Usage:\n img2arr.py <filename>")