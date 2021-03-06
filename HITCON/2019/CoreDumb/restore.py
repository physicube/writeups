from pwn import*

data = '''37 29 98 CC 2A 50 D1 61  A5 A1 26 3A 62 61 81 74 
A1 00 00 00 00 00 00 00'''.replace(' ', '').replace('\n', '').decode('hex')

code1 = list('''1F 4B 3C 6B 02 80 59 EE  02 8A C8 26 C3 76 11 EA
02 88 B1 AB 62 03 B5 8E  02 8A F0 76 7B C3 72 CB
8A 47 C0 C3 28 C5 F0 4A  4A 4B 72 CB 9A 03 B5 8E
4A 4B 72 CB 92 03 B5 8E  4A 4B 72 CB AA 03 B5 8E
4A C4 F0 66 4A 03 B5 8E  2C C4 F0 62 4A 03 FD 36
03 25 C7 BB 3C 32 A6 8A  02 8A F0 4B 2C C4 F0 43
04 5D 73 CB 85 03 72 CB  F2 03 B5 8E 4A C4 F0 32
4B 03 B5 8E 8D 46 0D 8E  4A 03 B5 65 73 88 F0 36
02 60 65 C6 C1 46 1D C6  4B D3 BA 38 42 88 F0 36
D3 C2 5F 90 4B D3 36 6E  49 2A 65 C6 D2 0C 03 CA
4F C3 36 66 4D 32 74 07  80 88 F0 36 02 9B 3D DA
4F D3 36 CB F2 02 3E CB  F2 38 F0 2A 36 BC 72 CB
F2 03 B5 8E 4A E8 96 05  0F BB FD 16 45 B5 E1 8B
9A 88 F0 36 02 9B BA 38  0E 06 70 B6 88 77 B2 49
0F BF B5 8E 4A 03 36 CB  F2 02 3E CB F2 38 F0 2A
36 D6 3E CB F6 4B 3E FB  B2 67 FD BD 7E 26 9D 8E
4A 03 C1 8B A2 B7 49 71  B5 CA 76'''.replace(' ', '').replace('\n','').decode('hex'))

code2 = list('''11 92 76 23 0C 59 13 B6  0C 53 82 5E 20 92 74 C2
61 F2 FF C6 44 92 76 83  BC EB 3F 01 01 7E FF C6
44 DA 38 83 EC DA FF C6  44 1D BA 6A 44 DA FF C6
83 9F 4F C7 44 DA FF 01  01 0A 42 4B 8F 4F 38 83
90 A3 33 42 4B 1D BA 1E  32 72 66 7E 83 9F 23 93
EF 87 F5 01 01 3A 45 FD  CF 40 38 83 A0 7D C7 74
34 1D BA 2E B5 E6 4A B4  83 9F 13 CF 46 A6 2B 01
01 76 FF C6 44 DA 16 D5  45 DA FF 4D 01 76 B7 A5
94 92 74 83 DC 92 FE 16  4B 6C FF C9 FA 1A DA 39
44 DA FF 4F 01 7E 74 83  E8 92 67 8E C9 8A FB 8E
CF 9F 67 8E 45 0A F0 70  44 D5 41 06 61 25 FF C6
44 53 BA 6E 83 9F 4B C6  44 DA FF 01 01 66 52 18
73 C9 38 83 84 99 FF C6  44 1D BA 02 74 DA FF C6
83 9F 37 94 44 DA FF 01  01 16 CC C6 44 DA 38 83
FC DA FF C6 44 1D BA 7E  44 DA FF C6 AF BF 74 83
EC 1B 1F C2 CD 18 74 83  EC 1B 17 C3 75 18 74 83
EC 57 F3 C4 CF 9F 4B 45  A4 D9 76 06 CF 8E 7A 06
CF 9F 4B C7 94 EB 37 C7  01 7E 74 83 F8 DB BA 72
CF 9F 5B 07 A4 DE 76 04  CF 9F 5B 07 AC DF CE 04
CF 9F 5B 4B 48 D8 74 83  F0 1B 17 CD C7 3A FC 4F
84 51 AB 43 84 51 BA 72  45 0A CE 0E 45 9F 57 45
01 62 FE 45 39 62 E0 B8  D1 51 BA 6A 45 1A B7 5E
CF 9E 7A 16 7D 9F 5B B2  43 1D BA 76 44 DA FF C6
CF 9F 53 C7 84 59 3F C7  0C 42 74 82 C1 0A C6 83
EC AE F8 01 01 6A FF C6  44 DA 7C 83 E8 DB 7C BB
E8 D9 F0 48 A7 24 00 39  CF 9F 4F 8E CF AF 07 A2
0C E9 CB E3 6C DA FF C6  30 DF 17 3B BE 25 00 0F
87'''.replace(' ', '').replace('\n','').decode('hex'))

code3 = list('''B4 77 63 60 A9 BE 06 65  E1 3F EA CD 68 82 C2 7A
1E C0 63 30 C5 C0 15 7A  85 77 61 81 C4 17 EA 85
E1 77 63 C0 19 0E 2A CD  26 BA 9A 7A 1E C0 EA 85
E1 3F A2 42 64 47 15 7A  1E 3F EA 85 E1 77 2D C0
61 3F EA 85 E1 77 2D C0  69 3F EA 85 E1 77 2D C0
71 3F EA 85 E1 77 2D C0  79 3F EA 85 E1 59 2D C0
41 3F EA CD 59 15 96 A8  A8 59 84 F4 D3 77 50 B5
C0 1F E0 C4 BB 5B CE CD  68 7A 5A CD 68 6A 52 CD
59 4D D6 DD 8E 63 AE AA  9A 77 50 CE A2 41 8B B1
B5 45 DD CD 68 7A 2A CD  68 6A 22 CD 59 16 B3 DB
DB 47 8A 8E 9C 77 50 D6  92 0E 93 CA 8C 56 9C CD
68 7A 3A CD 68 6A 32 CD  59 1C E7 A0 BC 7F B1 DA
AF 77 50 AD A9 55 C6 D3  B0 4A 8D CD 68 7A 0A CD
68 6A 02 43 A4 CF EA CD  59 0B 8A D4 C4 7E B5 C4
C2 77 50 D1 DB 65 CF C4  CE 77 97 CD 68 BA BA 7A
1E C0 A2 0C 74 67 15 7A  1E 77 52 FE C4 52 B9 C4
BA 6E E1 CD 68 BA 8A 7A  1E C0 2C 00 89 C0 15 7A
E1 F8 6F B5 1E C0 15 84  E1 3F EA 0E 64 1B 15 7A
1E 77 89 55 A9 B4 6F AD  1E C0 15 CD E0 EF A2 0C
64 77 15 7A 1E 77 61 00  C9 C0 15 7A A9 B6 6F C5
1E C0 15 CD 6C BA 9A 7A  1E C0 A2 0C 64 07 15 7A
1E D6 10 85 E1 3F A2 0E  64 7F 15 7A 1E 30 5C 85
21 D7 E8 8A 57 FF A2 1D  EE 89 A6 80 51 77 61 00
D9 C0 15 7A A9 B2 BA 84  A9 B6 7F BD 1E C0 15 0C
2B B7 FA CD 6A BA AA 7A  1E C0 E5 33 E1 30 5C 45
20 DF EE 06 01 0F 63 47  A9 B4 6F C5 1E C0 15 CD
62 FF EB 8A 57 3F 2A 6D  E5 30 5C 45 E8 EF A2 1D
EE 89 A6 80 51 77 61 00  D9 C0 15 7A A9 B2 BA 84
A9 B6 7F BD 1E C0 15 0C  2B B7 FA CD 6A BA AA 7A
1E C0 A2 06 21 3E E5 33  E1 30 5C 45 20 DF E8 06
01 03 63 47 A9 B4 6F C5  1E C0 15 CD 62 FF E8 8A
57 3F 2A 6D E7 30 5C 45  E8 EF A2 1D EE 89 A6 80
51 77 61 00 D9 C0 15 7A  A9 B2 BA 84 A9 B6 7F BD
1E C0 15 0C 2B B7 FA CD  6A BA AA 7A 1E C0 A2 06
21 3D E5 33 E1 30 5C 45  62 DF D5 CD 79 30 5C C9
E4 8F A2 0E 64 07 15 7A  1E 77 67 D5 E0 77 63 10
D9 C0 15 7A 68 F5 62 95  A9 BC 6F C5 1E C0 15 86
A9 B4 7F CD 1E C0 15 CD  6A BA AA 7A 1E C0 A2 AC
23 77 63 55 A9 BC 12 87  EE B0 02 7B 1E C0 2D 00
D5 C0 15 7A E1 3F EA 85  26 BA DE 7A 1E C0 EA 85
E1 3F 01 BE 6A BA DE 7A  1E C0 A2 1D EE 89 6E 80
91 C0 15 7A EE 89 3A 0E  64 0B 15 7A 1E 77 72 8A
57 BB EF D5 1E C0 15 8A  5F FF D3 47 95 35 2D 00
D1 C0 15 7A E1 3F EA 85  62 BA DE 7A 1E C0 EB 06
5C 0B 15 7A 1E 28 94 39  6A BA DA 7A 1E C0 A2 0E
94 C7 8E CD D2 0B CF AD  E1 3F EA F1 E4 D7 F3 7D
1E C0 23 46'''.replace(' ', '').replace('\n','').decode('hex'))

code4 = list('''A7 D6 24 A7 BA 1F 41 E2  F6 9E AD 0A 7B 23 C5 B9
0D 61 24 F7 96 65 52 BD  96 D6 26 46 D7 B6 AD 42
F2 D6 24 07 0A AF 6D 0A  7F 0B 3D B9 0D 61 15 42
F2 9E AD FB 8F 9E AD 42  BA 17 7A B1 BA 35 E5 FA
A2 F2 9E 23 81 C1 C9 72  BA 24 C3 65 86 C1 CE 10
C6 AB E5 CB B7 0E E5 CB  A7 06 E5 FA 9A C1 9C 2C
AD B5 C5 63 BA 24 DE 1D  94 CB C3 01 D9 AF E5 CB
B7 3E E5 CB A7 36 CB 85  B7 2E 9D 2C 34 DB 1F 42
BA 59 E8 82 F2 9E AD 42  BA 59 E8 8A F2 9E AD 42
BA 59 E8 92 F2 9E AD 42  BA 59 E8 9A F2 9E AD 42
BA 59 E8 A2 F2 9E AD 42  BA 59 E8 AA F2 9E AD 42
94 59 E8 B2 F2 9E E5 FA  D9 CB F0 D1 52 DD 70 56
BA 17 E8 C1 35 DB 26 01  A0 E3 48 84 B7 11 AD 85
77 1E 56 BD 0D BC AD 42  F2 59 28 32 09 61 52 42
F2 9E AD 85 77 EA 56 BD  0D 9E AD 42 F2 59 28 3A
09 61 52 43 F2 9E AD 85  77 EE 56 BD 0D 9E AD 42
F2 75 B1 C9 77 EE 56 BD  0D D6 35 C9 67 EE 56 BD
0D 17 39 C7 62 65 52 BD  71 1B DD B9 0D 61 AC C3
4F EE 56 BD 0D 6B AD 42  F2 E0 75 85 77 EE 56 BD
0D 9E AD 42 F2 77 1E 42  F2 9E 26 C7 82 65 52 BD
BA 06 26 D6 77 0E 56 BD  0D 15 28 36 09 61 52 CF
FE 9C 26 C7 82 65 52 BD  6B 69 10 C2 09 61 52 CB
22 D6 35 4D 44 DA A8 D2  FD 28 6D 43 33 24 B8 40
BF BF 24 8A 05 74 6C B8  F7 17 65 83 0A 81 84 80
7B 4E 24 C7 86 65 52 BD  79 1B D9 B9 0D 61 C4 82
04 9E AD 42 DB 5F 24 8A  7B 1B D9 B9 0D 61 26 C7
82 65 52 BD BA 06 26 C6  77 0E 56 BD 0D 17 28 CE
09 61 52 C9 77 EA 56 BD  0D D6 35 C9 66 1B 3D B9
0D 61 26 C7 82 65 52 BD  BA 06 24 D6 77 0E 56 BD
0D 15 28 36 09 61 52 0A  6A 15 38 CE 09 61 52 CB
66 1B 3D B9 0D 61 2E C7  82 65 52 BD F3 1F 10 32
09 61 52 B7 F2 9E AD 4D  7C A3 52 BD 0D 59 28 3E
09 61 52 42 F2 9E AD 85  77 EE 56 BD 0D 9E AD 42
F2 59 28 36 09 61 52 42  F2 9E AD AB BD 9F AD 42
79 1B DD B9 0D 61 20 0A  F3 24 B8 40 BF BF 24 8A
05 74 6C B8 F7 17 65 83  0A 81 84 80 7B 4E 24 C7
82 65 52 BD 79 1B DD B9  0D 61 C4 82 04 9E AD 42
DB 5F 24 8A 7B 1B DD B9  0D 61 26 C7 82 65 52 BD
BA 06 26 D6 77 0E 56 BD  0D 15 28 36 09 61 52 CF
FE 9C 17 57 F0 D3 8C CB  3A 69 47 83 08 9B 24 8A
33 66 B2 6B 30 17 7D CB  77 EA 56 BD 0D 15 28 36
09 61 52 2B 32 68 AD 42  F2 B7 6C CB 3A 17 28 36
09 61 52 C9 77 EE 56 BD  0D D6 35 C9 76 1B 3D B9
0D 61 24 C7 76 65 52 BD  79 1B D9 B9 0D 61 E5 DA
79 0A 28 D2 09 61 52 C9  77 EE 56 BD 0D D6 35 CB
66 1B 3D B9 0D 61 26 C7  86 65 52 BD BA 06 26 D7
76 65 52 BD 7B 0A 28 D2  09 61 52 C9 77 EE 56 BD
0D D6 35 C9 66 1B 3D B9  0D 61 26 C7 86 65 52 BD
BA 06 26 C6 77 0E 56 BD  0D 13 A1 40 48 8B AF 0F
D3 17 65 B5 18 5F 57 47  7B 56 6C BA ED B7 6F CB
22 F7 6D B4 F2 9E AD 6B  33 17 65 0A 6A 15 29 C7
62 65 52 BD 7B 1B 25 B9  0D 61 26 C7 7A 65 52 BD
7B 5F 26 C7 8E 65 52 BD  BA FD 7D 0A 79 1B C5 B9
0D 61 E5 43 22 91 1B 42  C3 56 24 80 79 1B D1 B9
0D 61 E5 DA 7A CA A8 82  71 1B D1 B9 0D 61 AC C9
77 E2 56 BD 0D A5 28 26  09 61 52 4D 7E 01 53 BD
0D 59 28 32 09 61 52 42  F2 9E AD A9 DD 15 28 32
09 61 52 0A 6A 91 1B 16  F7 5E 26 C7 82 65 52 BD
BA 06 A2 F4 B6 9B 2E 7A  30 EA A7 85 77 E6 56 BD
0D 9E AD 42 F2 1D 28 32  09 61 52 43 79 1B DD B9
0D 61 96 C7 96 65 52 BD  8E 5D 26 C7 8A 65 52 BD
BA 15 D8 BA 96 D6 9E 76  D7 B6 AD 42 F2 EA A8 AA
C1 6A 52 BD 3B 5D'''.replace(' ', '').replace('\n','').decode('hex'))

code5 = list('''09 1B 6B 92 14 DA 9F AF  9B 16 06 77 5C 53 E2 B0
19 BB E2 77 5C 53 25 32  A8 53 E2 77 5C 94 A7 9B
5D 53 E2 77 9B 16 1A 77  5C 53 E2 B0 19 A3 E2 77
5C 53 25 32 A0 53 E2 77  5C 94 A7 87 A3 AC 1D 88
B7 07 69 32 B8 DE B2 76  D5 06 06 3F 3F 83 AA FC
19 8B AA 76 8C 5C 54 77  53 ED 22 FE 19 AB 69 32
A4 62 A7 87 9B 16 0A 70  5C 53 E2 9C 7F D8 A7 87
DF B3 E3 80 84 DA A7 8B  D7 16 12 A6 B4 DA 20 FC
19 AF C7 57 DF EB 0F 46  8C DA A7 87 DF 3E 0A 76
DF 2E 0A 77 25 84 69 32  B8 1B 81 A7 14 D8 A7 AF
14 52 32 78 EA 53 66 B7  29 CB 63 0A AC 7A E3 EE
75 27 E5 B0 19 BF E2 77  5C 53 69 32 B0 0E 21'''.replace(' ', '').replace('\n','').decode('hex'))
codes = [code1, code2, code3, code4, code5]
keys = map(p32, [0x8EB5034A, 0x0C6FFDA44, 0x85EA3FE1, 0x42AD9EF2, 0x77E2535C])
sizes  = [0x10B, 0x1B1, 0x2E4, 0x3E6, 0x0B]

context.arch = 'amd64'
restored = ''
for i, code in enumerate(codes):
    for j, byte in enumerate(code):
        restored += chr(ord(byte) ^ ord(keys[i][j % 4]))

print disasm(restored, arch='amd64')

data = make_elf(restored)
with open('funcs', 'wb') as f:
    f.write(data)
