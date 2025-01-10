# Plodon

## Overview

Combinatorics for [Will](https://www.wmad.co.uk/about/)'s alien alphabet (which they called Plodon).

cf. Colin Beveridge's [alfabet](https://github.com/icecolbeveridge/alfabet/).

Q: How many "letters" can be made, where each letter is two non-crossing paths made by connecting three distinct adjacent points in a 3-by-3 grid?

i.e. we wish to count the ways to draw two distinct paths of length 2 which do not cross in the following graph.

![3 by 3 grid of vertices with adjacent vertices connected with an edge.](graph.png)

A: I agree with Colin's 552. 

## Files included

Python code for counting, listing and drawing the language, described below, also LaTeX code for drawing the graph above and some adjacency matrix notes.

## Drawing the letters - `drawing-plodon.py`

Plodon uses the same approach as `listing-plodon.py` described below, but outputs as TikZ code in `all-plodon-letters.tex`. The [result of running this through LaTeX is available as a PDF](all-plodon-letters.pdf). Letter are presented one per page in the order the program found them (which prioritises the paths starting and moving through lower numbered vertices).

## List of letters - `listing-plodon.py`

The approach here is to make the graph (in networkx), find the 80 possible single paths by removing vertices and their neighbours in turn and, for each, repeat the same process to find all the possible second paths for this first path. 

The output from running `listing-plodon.py`:

```
Letter 1: path 1 1-2-3; path 2 4-5-6
Letter 2: path 1 1-2-3; path 2 4-5-7
Letter 3: path 1 1-2-3; path 2 4-5-8
Letter 4: path 1 1-2-3; path 2 4-5-9
Letter 5: path 1 1-2-3; path 2 4-7-5
Letter 6: path 1 1-2-3; path 2 4-7-8
Letter 7: path 1 1-2-3; path 2 4-8-5
Letter 8: path 1 1-2-3; path 2 4-8-6
Letter 9: path 1 1-2-3; path 2 4-8-7
Letter 10: path 1 1-2-3; path 2 4-8-9
Letter 11: path 1 1-2-3; path 2 5-4-7
Letter 12: path 1 1-2-3; path 2 5-4-8
Letter 13: path 1 1-2-3; path 2 5-6-8
Letter 14: path 1 1-2-3; path 2 5-6-9
Letter 15: path 1 1-2-3; path 2 5-7-8
Letter 16: path 1 1-2-3; path 2 5-8-6
Letter 17: path 1 1-2-3; path 2 5-8-7
Letter 18: path 1 1-2-3; path 2 5-8-9
Letter 19: path 1 1-2-3; path 2 5-9-6
Letter 20: path 1 1-2-3; path 2 5-9-8
Letter 21: path 1 1-2-3; path 2 6-5-7
Letter 22: path 1 1-2-3; path 2 6-5-8
Letter 23: path 1 1-2-3; path 2 6-5-9
Letter 24: path 1 1-2-3; path 2 6-8-7
Letter 25: path 1 1-2-3; path 2 6-8-9
Letter 26: path 1 1-2-3; path 2 6-9-8
Letter 27: path 1 1-2-3; path 2 7-4-8
Letter 28: path 1 1-2-3; path 2 7-5-8
Letter 29: path 1 1-2-3; path 2 7-5-9
Letter 30: path 1 1-2-3; path 2 7-8-9
Letter 31: path 1 1-2-3; path 2 8-5-9
Letter 32: path 1 1-2-3; path 2 8-6-9
Letter 33: path 1 1-2-4; path 2 3-5-6
Letter 34: path 1 1-2-4; path 2 3-5-7
Letter 35: path 1 1-2-4; path 2 3-5-8
Letter 36: path 1 1-2-4; path 2 3-5-9
Letter 37: path 1 1-2-4; path 2 3-6-5
Letter 38: path 1 1-2-4; path 2 3-6-8
Letter 39: path 1 1-2-4; path 2 3-6-9
Letter 40: path 1 1-2-4; path 2 5-3-6
Letter 41: path 1 1-2-4; path 2 5-6-8
Letter 42: path 1 1-2-4; path 2 5-6-9
Letter 43: path 1 1-2-4; path 2 5-7-8
Letter 44: path 1 1-2-4; path 2 5-8-6
Letter 45: path 1 1-2-4; path 2 5-8-7
Letter 46: path 1 1-2-4; path 2 5-8-9
Letter 47: path 1 1-2-4; path 2 5-9-6
Letter 48: path 1 1-2-4; path 2 5-9-8
Letter 49: path 1 1-2-4; path 2 6-5-7
Letter 50: path 1 1-2-4; path 2 6-5-8
Letter 51: path 1 1-2-4; path 2 6-5-9
Letter 52: path 1 1-2-4; path 2 6-8-7
Letter 53: path 1 1-2-4; path 2 6-8-9
Letter 54: path 1 1-2-4; path 2 6-9-8
Letter 55: path 1 1-2-4; path 2 7-5-8
Letter 56: path 1 1-2-4; path 2 7-5-9
Letter 57: path 1 1-2-4; path 2 7-8-9
Letter 58: path 1 1-2-4; path 2 8-5-9
Letter 59: path 1 1-2-4; path 2 8-6-9
Letter 60: path 1 1-2-5; path 2 3-6-8
Letter 61: path 1 1-2-5; path 2 3-6-9
Letter 62: path 1 1-2-5; path 2 4-7-8
Letter 63: path 1 1-2-5; path 2 4-8-6
Letter 64: path 1 1-2-5; path 2 4-8-7
Letter 65: path 1 1-2-5; path 2 4-8-9
Letter 66: path 1 1-2-5; path 2 6-8-7
Letter 67: path 1 1-2-5; path 2 6-8-9
Letter 68: path 1 1-2-5; path 2 6-9-8
Letter 69: path 1 1-2-5; path 2 7-4-8
Letter 70: path 1 1-2-5; path 2 7-8-9
Letter 71: path 1 1-2-5; path 2 8-6-9
Letter 72: path 1 1-2-6; path 2 4-5-7
Letter 73: path 1 1-2-6; path 2 4-5-8
Letter 74: path 1 1-2-6; path 2 4-5-9
Letter 75: path 1 1-2-6; path 2 4-7-5
Letter 76: path 1 1-2-6; path 2 4-7-8
Letter 77: path 1 1-2-6; path 2 4-8-5
Letter 78: path 1 1-2-6; path 2 4-8-7
Letter 79: path 1 1-2-6; path 2 4-8-9
Letter 80: path 1 1-2-6; path 2 5-4-7
Letter 81: path 1 1-2-6; path 2 5-4-8
Letter 82: path 1 1-2-6; path 2 5-7-8
Letter 83: path 1 1-2-6; path 2 5-8-7
Letter 84: path 1 1-2-6; path 2 5-8-9
Letter 85: path 1 1-2-6; path 2 5-9-8
Letter 86: path 1 1-2-6; path 2 7-4-8
Letter 87: path 1 1-2-6; path 2 7-5-8
Letter 88: path 1 1-2-6; path 2 7-5-9
Letter 89: path 1 1-2-6; path 2 7-8-9
Letter 90: path 1 1-2-6; path 2 8-5-9
Letter 91: path 1 1-4-2; path 2 3-5-6
Letter 92: path 1 1-4-2; path 2 3-5-7
Letter 93: path 1 1-4-2; path 2 3-5-8
Letter 94: path 1 1-4-2; path 2 3-5-9
Letter 95: path 1 1-4-2; path 2 3-6-5
Letter 96: path 1 1-4-2; path 2 3-6-8
Letter 97: path 1 1-4-2; path 2 3-6-9
Letter 98: path 1 1-4-2; path 2 5-3-6
Letter 99: path 1 1-4-2; path 2 5-6-8
Letter 100: path 1 1-4-2; path 2 5-6-9
Letter 101: path 1 1-4-2; path 2 5-7-8
Letter 102: path 1 1-4-2; path 2 5-8-6
Letter 103: path 1 1-4-2; path 2 5-8-7
Letter 104: path 1 1-4-2; path 2 5-8-9
Letter 105: path 1 1-4-2; path 2 5-9-6
Letter 106: path 1 1-4-2; path 2 5-9-8
Letter 107: path 1 1-4-2; path 2 6-5-7
Letter 108: path 1 1-4-2; path 2 6-5-8
Letter 109: path 1 1-4-2; path 2 6-5-9
Letter 110: path 1 1-4-2; path 2 6-8-7
Letter 111: path 1 1-4-2; path 2 6-8-9
Letter 112: path 1 1-4-2; path 2 6-9-8
Letter 113: path 1 1-4-2; path 2 7-5-8
Letter 114: path 1 1-4-2; path 2 7-5-9
Letter 115: path 1 1-4-2; path 2 7-8-9
Letter 116: path 1 1-4-2; path 2 8-5-9
Letter 117: path 1 1-4-2; path 2 8-6-9
Letter 118: path 1 1-4-5; path 2 2-3-6
Letter 119: path 1 1-4-5; path 2 2-6-3
Letter 120: path 1 1-4-5; path 2 2-6-8
Letter 121: path 1 1-4-5; path 2 2-6-9
Letter 122: path 1 1-4-5; path 2 3-2-6
Letter 123: path 1 1-4-5; path 2 3-6-8
Letter 124: path 1 1-4-5; path 2 3-6-9
Letter 125: path 1 1-4-5; path 2 6-8-7
Letter 126: path 1 1-4-5; path 2 6-8-9
Letter 127: path 1 1-4-5; path 2 6-9-8
Letter 128: path 1 1-4-5; path 2 7-8-9
Letter 129: path 1 1-4-5; path 2 8-6-9
Letter 130: path 1 1-4-7; path 2 2-3-5
Letter 131: path 1 1-4-7; path 2 2-3-6
Letter 132: path 1 1-4-7; path 2 2-5-3
Letter 133: path 1 1-4-7; path 2 2-5-6
Letter 134: path 1 1-4-7; path 2 2-5-8
Letter 135: path 1 1-4-7; path 2 2-5-9
Letter 136: path 1 1-4-7; path 2 2-6-3
Letter 137: path 1 1-4-7; path 2 2-6-5
Letter 138: path 1 1-4-7; path 2 2-6-8
Letter 139: path 1 1-4-7; path 2 2-6-9
Letter 140: path 1 1-4-7; path 2 3-2-5
Letter 141: path 1 1-4-7; path 2 3-2-6
Letter 142: path 1 1-4-7; path 2 3-5-6
Letter 143: path 1 1-4-7; path 2 3-5-8
Letter 144: path 1 1-4-7; path 2 3-5-9
Letter 145: path 1 1-4-7; path 2 3-6-5
Letter 146: path 1 1-4-7; path 2 3-6-8
Letter 147: path 1 1-4-7; path 2 3-6-9
Letter 148: path 1 1-4-7; path 2 5-2-6
Letter 149: path 1 1-4-7; path 2 5-3-6
Letter 150: path 1 1-4-7; path 2 5-6-8
Letter 151: path 1 1-4-7; path 2 5-6-9
Letter 152: path 1 1-4-7; path 2 5-8-6
Letter 153: path 1 1-4-7; path 2 5-8-9
Letter 154: path 1 1-4-7; path 2 5-9-6
Letter 155: path 1 1-4-7; path 2 5-9-8
Letter 156: path 1 1-4-7; path 2 6-5-8
Letter 157: path 1 1-4-7; path 2 6-5-9
Letter 158: path 1 1-4-7; path 2 6-8-9
Letter 159: path 1 1-4-7; path 2 6-9-8
Letter 160: path 1 1-4-7; path 2 8-5-9
Letter 161: path 1 1-4-7; path 2 8-6-9
Letter 162: path 1 1-4-8; path 2 2-3-5
Letter 163: path 1 1-4-8; path 2 2-3-6
Letter 164: path 1 1-4-8; path 2 2-5-3
Letter 165: path 1 1-4-8; path 2 2-5-6
Letter 166: path 1 1-4-8; path 2 2-5-9
Letter 167: path 1 1-4-8; path 2 2-6-3
Letter 168: path 1 1-4-8; path 2 2-6-5
Letter 169: path 1 1-4-8; path 2 2-6-9
Letter 170: path 1 1-4-8; path 2 3-2-5
Letter 171: path 1 1-4-8; path 2 3-2-6
Letter 172: path 1 1-4-8; path 2 3-5-6
Letter 173: path 1 1-4-8; path 2 3-5-9
Letter 174: path 1 1-4-8; path 2 3-6-5
Letter 175: path 1 1-4-8; path 2 3-6-9
Letter 176: path 1 1-4-8; path 2 5-2-6
Letter 177: path 1 1-4-8; path 2 5-3-6
Letter 178: path 1 1-4-8; path 2 5-6-9
Letter 179: path 1 1-4-8; path 2 5-9-6
Letter 180: path 1 1-4-8; path 2 6-5-9
Letter 181: path 1 1-5-2; path 2 3-6-8
Letter 182: path 1 1-5-2; path 2 3-6-9
Letter 183: path 1 1-5-2; path 2 4-7-8
Letter 184: path 1 1-5-2; path 2 4-8-6
Letter 185: path 1 1-5-2; path 2 4-8-7
Letter 186: path 1 1-5-2; path 2 4-8-9
Letter 187: path 1 1-5-2; path 2 6-8-7
Letter 188: path 1 1-5-2; path 2 6-8-9
Letter 189: path 1 1-5-2; path 2 6-9-8
Letter 190: path 1 1-5-2; path 2 7-4-8
Letter 191: path 1 1-5-2; path 2 7-8-9
Letter 192: path 1 1-5-2; path 2 8-6-9
Letter 193: path 1 1-5-3; path 2 4-7-8
Letter 194: path 1 1-5-3; path 2 4-8-6
Letter 195: path 1 1-5-3; path 2 4-8-7
Letter 196: path 1 1-5-3; path 2 4-8-9
Letter 197: path 1 1-5-3; path 2 6-8-7
Letter 198: path 1 1-5-3; path 2 6-8-9
Letter 199: path 1 1-5-3; path 2 6-9-8
Letter 200: path 1 1-5-3; path 2 7-4-8
Letter 201: path 1 1-5-3; path 2 7-8-9
Letter 202: path 1 1-5-3; path 2 8-6-9
Letter 203: path 1 1-5-4; path 2 2-3-6
Letter 204: path 1 1-5-4; path 2 2-6-3
Letter 205: path 1 1-5-4; path 2 2-6-8
Letter 206: path 1 1-5-4; path 2 2-6-9
Letter 207: path 1 1-5-4; path 2 3-2-6
Letter 208: path 1 1-5-4; path 2 3-6-8
Letter 209: path 1 1-5-4; path 2 3-6-9
Letter 210: path 1 1-5-4; path 2 6-8-7
Letter 211: path 1 1-5-4; path 2 6-8-9
Letter 212: path 1 1-5-4; path 2 6-9-8
Letter 213: path 1 1-5-4; path 2 7-8-9
Letter 214: path 1 1-5-4; path 2 8-6-9
Letter 215: path 1 1-5-6; path 2 4-7-8
Letter 216: path 1 1-5-6; path 2 4-8-7
Letter 217: path 1 1-5-6; path 2 4-8-9
Letter 218: path 1 1-5-6; path 2 7-4-8
Letter 219: path 1 1-5-6; path 2 7-8-9
Letter 220: path 1 1-5-7; path 2 2-3-6
Letter 221: path 1 1-5-7; path 2 2-6-3
Letter 222: path 1 1-5-7; path 2 2-6-8
Letter 223: path 1 1-5-7; path 2 2-6-9
Letter 224: path 1 1-5-7; path 2 3-2-6
Letter 225: path 1 1-5-7; path 2 3-6-8
Letter 226: path 1 1-5-7; path 2 3-6-9
Letter 227: path 1 1-5-7; path 2 6-8-9
Letter 228: path 1 1-5-7; path 2 6-9-8
Letter 229: path 1 1-5-7; path 2 8-6-9
Letter 230: path 1 1-5-8; path 2 2-3-6
Letter 231: path 1 1-5-8; path 2 2-6-3
Letter 232: path 1 1-5-8; path 2 2-6-9
Letter 233: path 1 1-5-8; path 2 3-2-6
Letter 234: path 1 1-5-8; path 2 3-6-9
Letter 235: path 1 1-5-9; path 2 2-3-6
Letter 236: path 1 1-5-9; path 2 2-6-3
Letter 237: path 1 1-5-9; path 2 3-2-6
Letter 238: path 1 1-5-9; path 2 4-7-8
Letter 239: path 1 1-5-9; path 2 4-8-7
Letter 240: path 1 1-5-9; path 2 7-4-8
Letter 241: path 1 2-1-4; path 2 3-5-6
Letter 242: path 1 2-1-4; path 2 3-5-7
Letter 243: path 1 2-1-4; path 2 3-5-8
Letter 244: path 1 2-1-4; path 2 3-5-9
Letter 245: path 1 2-1-4; path 2 3-6-5
Letter 246: path 1 2-1-4; path 2 3-6-8
Letter 247: path 1 2-1-4; path 2 3-6-9
Letter 248: path 1 2-1-4; path 2 5-3-6
Letter 249: path 1 2-1-4; path 2 5-6-8
Letter 250: path 1 2-1-4; path 2 5-6-9
Letter 251: path 1 2-1-4; path 2 5-7-8
Letter 252: path 1 2-1-4; path 2 5-8-6
Letter 253: path 1 2-1-4; path 2 5-8-7
Letter 254: path 1 2-1-4; path 2 5-8-9
Letter 255: path 1 2-1-4; path 2 5-9-6
Letter 256: path 1 2-1-4; path 2 5-9-8
Letter 257: path 1 2-1-4; path 2 6-5-7
Letter 258: path 1 2-1-4; path 2 6-5-8
Letter 259: path 1 2-1-4; path 2 6-5-9
Letter 260: path 1 2-1-4; path 2 6-8-7
Letter 261: path 1 2-1-4; path 2 6-8-9
Letter 262: path 1 2-1-4; path 2 6-9-8
Letter 263: path 1 2-1-4; path 2 7-5-8
Letter 264: path 1 2-1-4; path 2 7-5-9
Letter 265: path 1 2-1-4; path 2 7-8-9
Letter 266: path 1 2-1-4; path 2 8-5-9
Letter 267: path 1 2-1-4; path 2 8-6-9
Letter 268: path 1 2-1-5; path 2 3-6-8
Letter 269: path 1 2-1-5; path 2 3-6-9
Letter 270: path 1 2-1-5; path 2 4-7-8
Letter 271: path 1 2-1-5; path 2 4-8-6
Letter 272: path 1 2-1-5; path 2 4-8-7
Letter 273: path 1 2-1-5; path 2 4-8-9
Letter 274: path 1 2-1-5; path 2 6-8-7
Letter 275: path 1 2-1-5; path 2 6-8-9
Letter 276: path 1 2-1-5; path 2 6-9-8
Letter 277: path 1 2-1-5; path 2 7-4-8
Letter 278: path 1 2-1-5; path 2 7-8-9
Letter 279: path 1 2-1-5; path 2 8-6-9
Letter 280: path 1 2-3-5; path 2 4-7-8
Letter 281: path 1 2-3-5; path 2 4-8-6
Letter 282: path 1 2-3-5; path 2 4-8-7
Letter 283: path 1 2-3-5; path 2 4-8-9
Letter 284: path 1 2-3-5; path 2 6-8-7
Letter 285: path 1 2-3-5; path 2 6-8-9
Letter 286: path 1 2-3-5; path 2 6-9-8
Letter 287: path 1 2-3-5; path 2 7-4-8
Letter 288: path 1 2-3-5; path 2 7-8-9
Letter 289: path 1 2-3-5; path 2 8-6-9
Letter 290: path 1 2-3-6; path 2 4-1-5
Letter 291: path 1 2-3-6; path 2 4-5-7
Letter 292: path 1 2-3-6; path 2 4-5-8
Letter 293: path 1 2-3-6; path 2 4-5-9
Letter 294: path 1 2-3-6; path 2 4-7-5
Letter 295: path 1 2-3-6; path 2 4-7-8
Letter 296: path 1 2-3-6; path 2 4-8-5
Letter 297: path 1 2-3-6; path 2 4-8-7
Letter 298: path 1 2-3-6; path 2 4-8-9
Letter 299: path 1 2-3-6; path 2 5-4-7
Letter 300: path 1 2-3-6; path 2 5-4-8
Letter 301: path 1 2-3-6; path 2 5-7-8
Letter 302: path 1 2-3-6; path 2 5-8-7
Letter 303: path 1 2-3-6; path 2 5-8-9
Letter 304: path 1 2-3-6; path 2 5-9-8
Letter 305: path 1 2-3-6; path 2 7-4-8
Letter 306: path 1 2-3-6; path 2 7-5-8
Letter 307: path 1 2-3-6; path 2 7-5-9
Letter 308: path 1 2-3-6; path 2 7-8-9
Letter 309: path 1 2-3-6; path 2 8-5-9
Letter 310: path 1 2-4-5; path 2 3-6-8
Letter 311: path 1 2-4-5; path 2 3-6-9
Letter 312: path 1 2-4-5; path 2 6-8-7
Letter 313: path 1 2-4-5; path 2 6-8-9
Letter 314: path 1 2-4-5; path 2 6-9-8
Letter 315: path 1 2-4-5; path 2 7-8-9
Letter 316: path 1 2-4-5; path 2 8-6-9
Letter 317: path 1 2-4-7; path 2 3-5-6
Letter 318: path 1 2-4-7; path 2 3-5-8
Letter 319: path 1 2-4-7; path 2 3-5-9
Letter 320: path 1 2-4-7; path 2 3-6-5
Letter 321: path 1 2-4-7; path 2 3-6-8
Letter 322: path 1 2-4-7; path 2 3-6-9
Letter 323: path 1 2-4-7; path 2 5-3-6
Letter 324: path 1 2-4-7; path 2 5-6-8
Letter 325: path 1 2-4-7; path 2 5-6-9
Letter 326: path 1 2-4-7; path 2 5-8-6
Letter 327: path 1 2-4-7; path 2 5-8-9
Letter 328: path 1 2-4-7; path 2 5-9-6
Letter 329: path 1 2-4-7; path 2 5-9-8
Letter 330: path 1 2-4-7; path 2 6-5-8
Letter 331: path 1 2-4-7; path 2 6-5-9
Letter 332: path 1 2-4-7; path 2 6-8-9
Letter 333: path 1 2-4-7; path 2 6-9-8
Letter 334: path 1 2-4-7; path 2 8-5-9
Letter 335: path 1 2-4-7; path 2 8-6-9
Letter 336: path 1 2-4-8; path 2 3-5-6
Letter 337: path 1 2-4-8; path 2 3-5-9
Letter 338: path 1 2-4-8; path 2 3-6-5
Letter 339: path 1 2-4-8; path 2 3-6-9
Letter 340: path 1 2-4-8; path 2 5-3-6
Letter 341: path 1 2-4-8; path 2 5-6-9
Letter 342: path 1 2-4-8; path 2 5-9-6
Letter 343: path 1 2-4-8; path 2 6-5-9
Letter 344: path 1 2-5-3; path 2 4-7-8
Letter 345: path 1 2-5-3; path 2 4-8-6
Letter 346: path 1 2-5-3; path 2 4-8-7
Letter 347: path 1 2-5-3; path 2 4-8-9
Letter 348: path 1 2-5-3; path 2 6-8-7
Letter 349: path 1 2-5-3; path 2 6-8-9
Letter 350: path 1 2-5-3; path 2 6-9-8
Letter 351: path 1 2-5-3; path 2 7-4-8
Letter 352: path 1 2-5-3; path 2 7-8-9
Letter 353: path 1 2-5-3; path 2 8-6-9
Letter 354: path 1 2-5-4; path 2 3-6-8
Letter 355: path 1 2-5-4; path 2 3-6-9
Letter 356: path 1 2-5-4; path 2 6-8-7
Letter 357: path 1 2-5-4; path 2 6-8-9
Letter 358: path 1 2-5-4; path 2 6-9-8
Letter 359: path 1 2-5-4; path 2 7-8-9
Letter 360: path 1 2-5-4; path 2 8-6-9
Letter 361: path 1 2-5-6; path 2 4-7-8
Letter 362: path 1 2-5-6; path 2 4-8-7
Letter 363: path 1 2-5-6; path 2 4-8-9
Letter 364: path 1 2-5-6; path 2 7-4-8
Letter 365: path 1 2-5-6; path 2 7-8-9
Letter 366: path 1 2-5-7; path 2 3-6-8
Letter 367: path 1 2-5-7; path 2 3-6-9
Letter 368: path 1 2-5-7; path 2 6-8-9
Letter 369: path 1 2-5-7; path 2 6-9-8
Letter 370: path 1 2-5-7; path 2 8-6-9
Letter 371: path 1 2-5-8; path 2 3-6-9
Letter 372: path 1 2-5-9; path 2 4-7-8
Letter 373: path 1 2-5-9; path 2 4-8-7
Letter 374: path 1 2-5-9; path 2 7-4-8
Letter 375: path 1 2-6-3; path 2 4-1-5
Letter 376: path 1 2-6-3; path 2 4-5-7
Letter 377: path 1 2-6-3; path 2 4-5-8
Letter 378: path 1 2-6-3; path 2 4-5-9
Letter 379: path 1 2-6-3; path 2 4-7-5
Letter 380: path 1 2-6-3; path 2 4-7-8
Letter 381: path 1 2-6-3; path 2 4-8-5
Letter 382: path 1 2-6-3; path 2 4-8-7
Letter 383: path 1 2-6-3; path 2 4-8-9
Letter 384: path 1 2-6-3; path 2 5-4-7
Letter 385: path 1 2-6-3; path 2 5-4-8
Letter 386: path 1 2-6-3; path 2 5-7-8
Letter 387: path 1 2-6-3; path 2 5-8-7
Letter 388: path 1 2-6-3; path 2 5-8-9
Letter 389: path 1 2-6-3; path 2 5-9-8
Letter 390: path 1 2-6-3; path 2 7-4-8
Letter 391: path 1 2-6-3; path 2 7-5-8
Letter 392: path 1 2-6-3; path 2 7-5-9
Letter 393: path 1 2-6-3; path 2 7-8-9
Letter 394: path 1 2-6-3; path 2 8-5-9
Letter 395: path 1 2-6-5; path 2 4-7-8
Letter 396: path 1 2-6-5; path 2 4-8-7
Letter 397: path 1 2-6-5; path 2 4-8-9
Letter 398: path 1 2-6-5; path 2 7-4-8
Letter 399: path 1 2-6-5; path 2 7-8-9
Letter 400: path 1 2-6-8; path 2 4-1-5
Letter 401: path 1 2-6-8; path 2 4-5-7
Letter 402: path 1 2-6-8; path 2 4-7-5
Letter 403: path 1 2-6-8; path 2 5-4-7
Letter 404: path 1 2-6-9; path 2 4-1-5
Letter 405: path 1 2-6-9; path 2 4-5-7
Letter 406: path 1 2-6-9; path 2 4-5-8
Letter 407: path 1 2-6-9; path 2 4-7-5
Letter 408: path 1 2-6-9; path 2 4-7-8
Letter 409: path 1 2-6-9; path 2 4-8-5
Letter 410: path 1 2-6-9; path 2 4-8-7
Letter 411: path 1 2-6-9; path 2 5-4-7
Letter 412: path 1 2-6-9; path 2 5-4-8
Letter 413: path 1 2-6-9; path 2 5-7-8
Letter 414: path 1 2-6-9; path 2 5-8-7
Letter 415: path 1 2-6-9; path 2 7-4-8
Letter 416: path 1 2-6-9; path 2 7-5-8
Letter 417: path 1 3-2-4; path 2 5-6-8
Letter 418: path 1 3-2-4; path 2 5-6-9
Letter 419: path 1 3-2-4; path 2 5-7-8
Letter 420: path 1 3-2-4; path 2 5-8-6
Letter 421: path 1 3-2-4; path 2 5-8-7
Letter 422: path 1 3-2-4; path 2 5-8-9
Letter 423: path 1 3-2-4; path 2 5-9-6
Letter 424: path 1 3-2-4; path 2 5-9-8
Letter 425: path 1 3-2-4; path 2 6-5-7
Letter 426: path 1 3-2-4; path 2 6-5-8
Letter 427: path 1 3-2-4; path 2 6-5-9
Letter 428: path 1 3-2-4; path 2 6-8-7
Letter 429: path 1 3-2-4; path 2 6-8-9
Letter 430: path 1 3-2-4; path 2 6-9-8
Letter 431: path 1 3-2-4; path 2 7-5-8
Letter 432: path 1 3-2-4; path 2 7-5-9
Letter 433: path 1 3-2-4; path 2 7-8-9
Letter 434: path 1 3-2-4; path 2 8-5-9
Letter 435: path 1 3-2-4; path 2 8-6-9
Letter 436: path 1 3-2-5; path 2 4-7-8
Letter 437: path 1 3-2-5; path 2 4-8-6
Letter 438: path 1 3-2-5; path 2 4-8-7
Letter 439: path 1 3-2-5; path 2 4-8-9
Letter 440: path 1 3-2-5; path 2 6-8-7
Letter 441: path 1 3-2-5; path 2 6-8-9
Letter 442: path 1 3-2-5; path 2 6-9-8
Letter 443: path 1 3-2-5; path 2 7-4-8
Letter 444: path 1 3-2-5; path 2 7-8-9
Letter 445: path 1 3-2-5; path 2 8-6-9
Letter 446: path 1 3-2-6; path 2 4-1-5
Letter 447: path 1 3-2-6; path 2 4-5-7
Letter 448: path 1 3-2-6; path 2 4-5-8
Letter 449: path 1 3-2-6; path 2 4-5-9
Letter 450: path 1 3-2-6; path 2 4-7-5
Letter 451: path 1 3-2-6; path 2 4-7-8
Letter 452: path 1 3-2-6; path 2 4-8-5
Letter 453: path 1 3-2-6; path 2 4-8-7
Letter 454: path 1 3-2-6; path 2 4-8-9
Letter 455: path 1 3-2-6; path 2 5-4-7
Letter 456: path 1 3-2-6; path 2 5-4-8
Letter 457: path 1 3-2-6; path 2 5-7-8
Letter 458: path 1 3-2-6; path 2 5-8-7
Letter 459: path 1 3-2-6; path 2 5-8-9
Letter 460: path 1 3-2-6; path 2 5-9-8
Letter 461: path 1 3-2-6; path 2 7-4-8
Letter 462: path 1 3-2-6; path 2 7-5-8
Letter 463: path 1 3-2-6; path 2 7-5-9
Letter 464: path 1 3-2-6; path 2 7-8-9
Letter 465: path 1 3-2-6; path 2 8-5-9
Letter 466: path 1 3-5-4; path 2 6-8-7
Letter 467: path 1 3-5-4; path 2 6-8-9
Letter 468: path 1 3-5-4; path 2 6-9-8
Letter 469: path 1 3-5-4; path 2 7-8-9
Letter 470: path 1 3-5-4; path 2 8-6-9
Letter 471: path 1 3-5-6; path 2 4-7-8
Letter 472: path 1 3-5-6; path 2 4-8-7
Letter 473: path 1 3-5-6; path 2 4-8-9
Letter 474: path 1 3-5-6; path 2 7-4-8
Letter 475: path 1 3-5-6; path 2 7-8-9
Letter 476: path 1 3-5-7; path 2 6-8-9
Letter 477: path 1 3-5-7; path 2 6-9-8
Letter 478: path 1 3-5-7; path 2 8-6-9
Letter 479: path 1 3-5-9; path 2 4-7-8
Letter 480: path 1 3-5-9; path 2 4-8-7
Letter 481: path 1 3-5-9; path 2 7-4-8
Letter 482: path 1 3-6-5; path 2 4-7-8
Letter 483: path 1 3-6-5; path 2 4-8-7
Letter 484: path 1 3-6-5; path 2 4-8-9
Letter 485: path 1 3-6-5; path 2 7-4-8
Letter 486: path 1 3-6-5; path 2 7-8-9
Letter 487: path 1 3-6-8; path 2 4-1-5
Letter 488: path 1 3-6-8; path 2 4-2-5
Letter 489: path 1 3-6-8; path 2 4-5-7
Letter 490: path 1 3-6-8; path 2 4-7-5
Letter 491: path 1 3-6-8; path 2 5-4-7
Letter 492: path 1 3-6-9; path 2 4-1-5
Letter 493: path 1 3-6-9; path 2 4-2-5
Letter 494: path 1 3-6-9; path 2 4-5-7
Letter 495: path 1 3-6-9; path 2 4-5-8
Letter 496: path 1 3-6-9; path 2 4-7-5
Letter 497: path 1 3-6-9; path 2 4-7-8
Letter 498: path 1 3-6-9; path 2 4-8-5
Letter 499: path 1 3-6-9; path 2 4-8-7
Letter 500: path 1 3-6-9; path 2 5-4-7
Letter 501: path 1 3-6-9; path 2 5-4-8
Letter 502: path 1 3-6-9; path 2 5-7-8
Letter 503: path 1 3-6-9; path 2 5-8-7
Letter 504: path 1 3-6-9; path 2 7-4-8
Letter 505: path 1 3-6-9; path 2 7-5-8
Letter 506: path 1 4-1-5; path 2 6-8-7
Letter 507: path 1 4-1-5; path 2 6-8-9
Letter 508: path 1 4-1-5; path 2 6-9-8
Letter 509: path 1 4-1-5; path 2 7-8-9
Letter 510: path 1 4-1-5; path 2 8-6-9
Letter 511: path 1 4-2-5; path 2 6-8-7
Letter 512: path 1 4-2-5; path 2 6-8-9
Letter 513: path 1 4-2-5; path 2 6-9-8
Letter 514: path 1 4-2-5; path 2 7-8-9
Letter 515: path 1 4-2-5; path 2 8-6-9
Letter 516: path 1 4-2-6; path 2 5-7-8
Letter 517: path 1 4-2-6; path 2 5-8-7
Letter 518: path 1 4-2-6; path 2 5-8-9
Letter 519: path 1 4-2-6; path 2 5-9-8
Letter 520: path 1 4-2-6; path 2 7-5-8
Letter 521: path 1 4-2-6; path 2 7-5-9
Letter 522: path 1 4-2-6; path 2 7-8-9
Letter 523: path 1 4-2-6; path 2 8-5-9
Letter 524: path 1 4-5-6; path 2 7-8-9
Letter 525: path 1 4-5-7; path 2 6-8-9
Letter 526: path 1 4-5-7; path 2 6-9-8
Letter 527: path 1 4-5-7; path 2 8-6-9
Letter 528: path 1 4-7-5; path 2 6-8-9
Letter 529: path 1 4-7-5; path 2 6-9-8
Letter 530: path 1 4-7-5; path 2 8-6-9
Letter 531: path 1 4-7-8; path 2 5-2-6
Letter 532: path 1 4-7-8; path 2 5-3-6
Letter 533: path 1 4-7-8; path 2 5-6-9
Letter 534: path 1 4-7-8; path 2 5-9-6
Letter 535: path 1 4-7-8; path 2 6-5-9
Letter 536: path 1 4-8-7; path 2 5-2-6
Letter 537: path 1 4-8-7; path 2 5-3-6
Letter 538: path 1 4-8-7; path 2 5-6-9
Letter 539: path 1 4-8-7; path 2 5-9-6
Letter 540: path 1 4-8-7; path 2 6-5-9
Letter 541: path 1 4-8-9; path 2 5-2-6
Letter 542: path 1 4-8-9; path 2 5-3-6
Letter 543: path 1 5-2-6; path 2 7-4-8
Letter 544: path 1 5-2-6; path 2 7-8-9
Letter 545: path 1 5-3-6; path 2 7-4-8
Letter 546: path 1 5-3-6; path 2 7-8-9
Letter 547: path 1 5-4-7; path 2 6-8-9
Letter 548: path 1 5-4-7; path 2 6-9-8
Letter 549: path 1 5-4-7; path 2 8-6-9
Letter 550: path 1 5-6-9; path 2 7-4-8
Letter 551: path 1 5-9-6; path 2 7-4-8
Letter 552: path 1 6-5-9; path 2 7-4-8
```

## Program `plodon.py`

The approach here is to make the graph (in networkx), find the 80 possible single paths by removing vertices and their neighbours in turn and, for each, make the graph of remaining vertices and edges that don't lead to crossings and count the number of 2-paths within this. 

This counts all possible pairs of paths twice, i.e. each pair (path1, path2) is also counted the other way around. 

The output from running `plodon.py`:

```
1. path 1 is 1-2-3; 32 options for path 2
2. path 1 is 1-2-4; 27 options for path 2
3. path 1 is 1-2-5; 12 options for path 2
4. path 1 is 1-2-6; 19 options for path 2
5. path 1 is 1-4-2; 27 options for path 2
6. path 1 is 1-4-5; 12 options for path 2
7. path 1 is 1-4-7; 32 options for path 2
8. path 1 is 1-4-8; 19 options for path 2
9. path 1 is 1-5-2; 12 options for path 2
10. path 1 is 1-5-3; 10 options for path 2
11. path 1 is 1-5-4; 12 options for path 2
12. path 1 is 1-5-6; 5 options for path 2
13. path 1 is 1-5-7; 10 options for path 2
14. path 1 is 1-5-8; 5 options for path 2
15. path 1 is 1-5-9; 6 options for path 2
16. path 1 is 2-1-4; 27 options for path 2
17. path 1 is 2-1-5; 12 options for path 2
18. path 1 is 2-3-5; 12 options for path 2
19. path 1 is 2-3-6; 27 options for path 2
20. path 1 is 2-4-5; 7 options for path 2
21. path 1 is 2-4-7; 19 options for path 2
22. path 1 is 2-4-8; 8 options for path 2
23. path 1 is 2-5-3; 12 options for path 2
24. path 1 is 2-5-4; 7 options for path 2
25. path 1 is 2-5-6; 7 options for path 2
26. path 1 is 2-5-7; 5 options for path 2
27. path 1 is 2-5-8; 2 options for path 2
28. path 1 is 2-5-9; 5 options for path 2
29. path 1 is 2-6-3; 27 options for path 2
30. path 1 is 2-6-5; 7 options for path 2
31. path 1 is 2-6-8; 8 options for path 2
32. path 1 is 2-6-9; 19 options for path 2
33. path 1 is 3-2-4; 19 options for path 2
34. path 1 is 3-2-5; 12 options for path 2
35. path 1 is 3-2-6; 27 options for path 2
36. path 1 is 3-5-4; 5 options for path 2
37. path 1 is 3-5-6; 12 options for path 2
38. path 1 is 3-5-7; 6 options for path 2
39. path 1 is 3-5-8; 5 options for path 2
40. path 1 is 3-5-9; 10 options for path 2
41. path 1 is 3-6-5; 12 options for path 2
42. path 1 is 3-6-8; 19 options for path 2
43. path 1 is 3-6-9; 32 options for path 2
44. path 1 is 4-1-5; 12 options for path 2
45. path 1 is 4-2-5; 7 options for path 2
46. path 1 is 4-2-6; 8 options for path 2
47. path 1 is 4-5-6; 2 options for path 2
48. path 1 is 4-5-7; 12 options for path 2
49. path 1 is 4-5-8; 7 options for path 2
50. path 1 is 4-5-9; 5 options for path 2
51. path 1 is 4-7-5; 12 options for path 2
52. path 1 is 4-7-8; 27 options for path 2
53. path 1 is 4-8-5; 7 options for path 2
54. path 1 is 4-8-6; 8 options for path 2
55. path 1 is 4-8-7; 27 options for path 2
56. path 1 is 4-8-9; 19 options for path 2
57. path 1 is 5-2-6; 7 options for path 2
58. path 1 is 5-3-6; 12 options for path 2
59. path 1 is 5-4-7; 12 options for path 2
60. path 1 is 5-4-8; 7 options for path 2
61. path 1 is 5-6-8; 7 options for path 2
62. path 1 is 5-6-9; 12 options for path 2
63. path 1 is 5-7-8; 12 options for path 2
64. path 1 is 5-8-6; 7 options for path 2
65. path 1 is 5-8-7; 12 options for path 2
66. path 1 is 5-8-9; 12 options for path 2
67. path 1 is 5-9-6; 12 options for path 2
68. path 1 is 5-9-8; 12 options for path 2
69. path 1 is 6-5-7; 5 options for path 2
70. path 1 is 6-5-8; 7 options for path 2
71. path 1 is 6-5-9; 12 options for path 2
72. path 1 is 6-8-7; 19 options for path 2
73. path 1 is 6-8-9; 27 options for path 2
74. path 1 is 6-9-8; 27 options for path 2
75. path 1 is 7-4-8; 27 options for path 2
76. path 1 is 7-5-8; 12 options for path 2
77. path 1 is 7-5-9; 10 options for path 2
78. path 1 is 7-8-9; 32 options for path 2
79. path 1 is 8-5-9; 12 options for path 2
80. path 1 is 8-6-9; 27 options for path 2
Total: 1104
```