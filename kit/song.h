TEMPODELAY equ 3


soundTurnArray
	byte 8, 0, 5, 9
	byte 0, 6, 4, 0

soundTypeArray
	byte 4,6,7,8
	byte 15,12,1,14


hatPattern
	byte %00000000
	byte %00000000
	byte %00000000
	byte %00000000

HATSTART equ 0
HATVOLUME equ 7
HATPITCH equ 0
HATSOUND equ 8


song1

	byte 0, 2
	byte 4, 6

	byte 255
song2

	byte 1, 3
	byte 5, 7

	byte 255



patternArrayH

	word CI0, CI2, CI4, CI6 ;0
	word CII1, CII3, CII5, CII7 ;1
	word CI8, CI10, CI12, CI14 ;2
	word CII9, CII11, CII13, CII15 ;3
	word CI16, CI18, CI20, CI22 ;4
	word CII17, CII19, CII21, CII23 ;5
	word CI24, CI26, CI28, CI30 ;6
	word CII25, CII27, CII29, CII31 ;7


patternArrayL



CI0
	byte %00111110
	byte %00111000
	byte %00110100
	byte %00111000
	byte %00110100
	byte %11011111
	byte %00110100
	byte %11011111

	byte %11111111

CI2
	byte %11011000
	byte %11011111
	byte %11011000
	byte %11010100
	byte %11011000
	byte %11010100
	byte %11001111
	byte %11010100

	byte %11111111

CI4
	byte %11001111
	byte %10111111
	byte %11001111
	byte %10111111
	byte %10111010
	byte %10111111
	byte %10111010
	byte %10110011

	byte %11111111

CI6
	byte %10111010
	byte %10110011
	byte %10101111
	byte %10110011
	byte %10101111
	byte %10101100
	byte %10101111
	byte %10101100

	byte %11111111

CI8
	byte %00011101
	byte %10101100
	byte %00011101
	byte %00010111
	byte %00011101
	byte %00010111
	byte %00010011
	byte %00010111

	byte %11111111

CI10
	byte %00010011
	byte %00001110
	byte %00001110
	byte %00001110
	byte 255
	byte 255
	byte 255
	byte 255

	byte %11111111

CI12
	byte %00001110
	byte 255
	byte %00001110
	byte %00001110
	byte %00001110
	byte %00001110
	byte %00001110
	byte %00001110

	byte %11111111

CI14
	byte %00001110
	byte %00001110
	byte %00001110
	byte %00001110
	byte 255
	byte 255
	byte 255
	byte 255

	byte %11111111

CI16
	byte %00111000
	byte %00110011
	byte %00101111
	byte %00110011
	byte %00101111
	byte %11011000
	byte %00101111
	byte %11011000

	byte %11111111

CI18
	byte %11010011
	byte %11011000
	byte %11010011
	byte %11010000
	byte %11010011
	byte %11010000
	byte %10111111
	byte %11010000

	byte %11111111

CI20
	byte %10111111
	byte %10111000
	byte %10111111
	byte %10111000
	byte %10110100
	byte %10111000
	byte %10110100
	byte %10101111

	byte %11111111

CI22
	byte %10110100
	byte %10101111
	byte %11000100
	byte %10101111
	byte %11000100
	byte %00011111
	byte %11000100
	byte %00011111

	byte %11111111

CI24
	byte %00010111
	byte %00011111
	byte %00010111
	byte %00010010
	byte %00010111
	byte %00010010
	byte %00001111
	byte %00010010

	byte %11111111

CI26
	byte %00001111
	byte %00001011
	byte %00001011
	byte %00001011
	byte 255
	byte 255
	byte 255
	byte 255

	byte %11111111

CI28
	byte %00001011
	byte 255
	byte %00001011
	byte %00001011
	byte %00001011
	byte %00001011
	byte %00001011
	byte %00001011

	byte %11111111

CI30
	byte %00001011
	byte %00001011
	byte %00001011
	byte %00001011
	byte 255
	byte 255
	byte 255
	byte 255

	byte %11111111
CII1
	byte 255
	byte 255
	byte 255
	byte 255
	byte 255
	byte %00111110
	byte %00111000
	byte %00110100

	byte %11111000

CII3
	byte %00111000
	byte %00110100
	byte %11011111
	byte %00110100
	byte %11011111
	byte %11011000
	byte %11011111
	byte %11011000

	byte %00000000

CII5
	byte %11010100
	byte %11011000
	byte %11010100
	byte %11001111
	byte %11010100
	byte %11001111
	byte %10111111
	byte %11001111

	byte %00000000

CII7
	byte %10111111
	byte %10111010
	byte %10111111
	byte %10111010
	byte %10110011
	byte %10111010
	byte %10110011
	byte %10101111

	byte %00000000

CII9
	byte %10110011
	byte %10101111
	byte %10101100
	byte %10101111
	byte %10101100
	byte %00011101
	byte %10101100
	byte %00011101

	byte %00000000

CII11
	byte %00010111
	byte %00011101
	byte %00010111
	byte %00010011
	byte %00010111
	byte %00010011
	byte %00001110
	byte %00001110

	byte %00000001

CII13
	byte %00001110
	byte 255
	byte 255
	byte 255
	byte 255
	byte %00001110
	byte 255
	byte %00001110

	byte %11111010

CII15
	byte %00001110
	byte %00001110
	byte %00001110
	byte %00001110
	byte %00001110
	byte %00001110
	byte %00001110
	byte 255

	byte %11111111

CII17
	byte 255
	byte 255
	byte 255
	byte 255
	byte 255
	byte %00111000
	byte %00110011
	byte %00101111

	byte %11111000

CII19
	byte %00110011
	byte %00101111
	byte %11011000
	byte %00101111
	byte %11011000
	byte %11010011
	byte %11011000
	byte %11010011

	byte %00000000

CII21
	byte %11010000
	byte %11010011
	byte %11010000
	byte %10111111
	byte %11010000
	byte %10111111
	byte %10111000
	byte %10111111

	byte %00000000

CII23
	byte %10111000
	byte %10110100
	byte %10111000
	byte %10110100
	byte %10101111
	byte %10110100
	byte %10101111
	byte %11000100

	byte %00000000

CII25
	byte %10101111
	byte %11000100
	byte %00011111
	byte %11000100
	byte %00011111
	byte %00010111
	byte %00011111
	byte %00010111

	byte %00000000

CII27
	byte %00010010
	byte %00010111
	byte %00010010
	byte %00001111
	byte %00010010
	byte %00001111
	byte %00001011
	byte %00001011

	byte %00000001

CII29
	byte %00001011
	byte 255
	byte 255
	byte 255
	byte 255
	byte %00001011
	byte 255
	byte %00001011

	byte %11111010

CII31
	byte %00001011
	byte %00001011
	byte %00001011
	byte %00001011
	byte %00001011
	byte %00001011
	byte %00001011
	byte 255

	byte %11111111
