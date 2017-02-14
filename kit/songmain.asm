;---------------------------------------------------------------------------
;
; Song Player by Paul Slocum
;
;---------------------------------------------------------------------------

	processor 6502	
	include vcs.h	




;TODO
;---------------------------

; Replace song player with newer version

; Add play/pause/measure/beat display

; Add joystick support

; Add advanced transport controls
; Add light show

; Add support for multiple songs

; Increase tempo resolution
; Add tempo display



;---------------------------------------------------------------------------
; Constants
;---------------------------------------------------------------------------
SETUPDELAY equ #255


;---------------------------------------------------------------------------
; RAM Variables 
;---------------------------------------------------------------------------
frame equ $80

; Text engine variables
grfxBuffer equ frame + 1 ; 48 bytes

scanSec equ grfxBuffer + 48
EOTflag equ scanSec + 1


;---------------------------------------------------------------------------
; Song player variables

temp equ EOTflag + 1

; 16 bit temp
temp16L equ temp + 1
temp16H equ temp16L + 1


note1 equ temp16H + 1
note2 equ note1 + 1

vol1 equ note2 + 1
vol2 equ vol1 + 1

sound1 equ vol2 + 1
sound2 equ sound1 + 1



; Metrenome stuff
beat equ sound2 + 1
tempoCount equ beat + 1
measure equ tempoCount + 1

; Special attenuation
atten equ measure + 1

;--------------------------------------
; Visual Display variables
;
; visual display can use $C0-$FF

visualPointer equ $C0

visualBuffer equ $C1







;---------------------------------------------------------------------------
; Text Macros
;---------------------------------------------------------------------------
; a few macros for storing text in a reasonably easy to read format
; Thanks to Greg Troutman for this!
;---------------------------------------------------------------------------

	mac off
	dc.b <#{0}
	endm

	mac wordOff
	dc.b #<{1}
	dc.b #>{1}
	endm
	
	mac mapRow
	wordOff {1}
	wordOff {2}	
	wordOff {3}
	wordOff {4}
	wordOff {5}
	endm

	mac EOL
	dc.b #$FF
	endm

	mac EOT
	dc.b #$FE
	endm

	mac line
	;must supply 12 characters, though 0's will not be assembled
	;------------------------------------------------------------
	if {1} != 0
	 off {1}
	endif
	if {2} != 0
	 off {2}
	endif
	if {3} != 0
	 off {3}
	endif
	if {4} != 0
	 off {4}
	endif
	if {5} != 0
	 off {5}
	endif
	if {6} != 0
	 off {6}
	endif
	if {7} != 0
	 off {7}
	endif
	if {8} != 0
	 off {8}
	endif
	if {9} != 0
	 off {9}
	endif
	if {10} != 0
	 off {10}
	endif
	if {11} != 0
	 off {11}
	endif
	if {12} != 0
	 off {12}
	endif
	EOL
	endm
	
	mac blank
	 line #0,#0,#0,#0,#0,#0,#0,#0,#0,#0,#0,#0
	endm



;---------------------------------------------------------------------------
;---------------------------------------------------------------------------
	org $F000
;---------------------------------------------------------------------------
;---------------------------------------------------------------------------


	include song.h

	include songplay.h

	org $FA00

;***************************************************************************
;***************************************************************************
;***************************************************************************
;***************************************************************************
;***************************************************************************
;***************************************************************************
;***************************************************************************
;***************************************************************************
;***************************************************************************
;***************************************************************************
;***************************************************************************
;***************************************************************************


;---------------------------------------------------------------------------
; Font Data
;---------------------------------------------------------------------------
; Include the font data here so it is aligned on a page
; boundary without wasting any space
;---------------------------------------------------------------------------
	include songfont.h		

;--------------------------------------------------------------------------
; Println
;--------------------------------------------------------------------------
; Greg Troutman:
; Most of this subroutine is ripped from Stellar Trak.  Feel free to add
; your own comments--it's pretty straightforward ;)  and very touchy.  Won't
; work if a page boundary appears at certain places, due to excruciating
; cycle dependency, so if modifying the source, you might need an ALIGN
; pseudo-op to correct flubbery text displays.  ALIGN 256 will always work,
; but maybe ALIGN 128, ALIGN 64, etc. will also work, and not waste as many
; bytes.
;--------------------------------------------------------------------------
	align 256
println
	ldx #4
	sta WSYNC
pause
	nop
	dex	
	bne pause
	lda temp
	lda temp	
		
	sta HMCLR
	ldx #$90
	ldy #6	;FONTHEIGHT
	lda frame
	and #$01
	beq oddFrame
	jmp evenFrame

print1	
	sta GRP1
	lda (grfxBuffer + $8),y
	sta GRP0
	lda (grfxBuffer + $C),y
	stx HMP0
	stx HMP1
	sta GRP1
	lda (grfxBuffer + $10),y
	sta GRP0
	lda (grfxBuffer + $14),y
	sta GRP1
	sta GRP0
evenFrame	
	dey
	bmi wrapEven
	lda (grfxBuffer + $2),y
	lsr
	sta GRP0
	lda (grfxBuffer +6),y
	lsr
	sta.w $001C
	sta HMOVE
	lda (grfxBuffer + $A),y
	lsr
	sta GRP0
	lda (grfxBuffer + $12),y
	lsr
	sta temp
	lda (grfxBuffer + $E),y
	lsr
	sta GRP1
	lda temp
	sta GRP0
	lda (grfxBuffer + $16),y
	lsr
	sta GRP1

oddFrame
	sta GRP0
	lda #$70
	sta HMP0
	sta HMP1
	dey
	bmi wrapOdd
	lda (grfxBuffer),y
	sta GRP0
	lda (grfxBuffer + $4),y
	sta HMOVE
	jmp print1

wrapEven
	stx HMP0
	stx HMP1
	sta WSYNC
	sta HMOVE
	jmp print2

wrapOdd
	sta WSYNC
	sta temp
	sta temp

print2
	lda #$00
	sta GRP0
	sta GRP1
	sta GRP0

	rts ; println


				
;---------------------------------------------------------------------------
; Start of Program
;---------------------------------------------------------------------------
; Clear memory, locate character graphics positions and such,
; initialize key memory values, start GameLoop.
;-------------------------------------------------------------
Start
	sei  	
	cld  		
	ldx #$FF
	txs  		
	lda #0
clear   
	sta 0,x
	dex
	bne clear	


;---------------------------------------------------------------------------
; Font Setup
;---------------------------------------------------------------------------
;the entire font is limited to one page, so we can hard code that page
;value into the MSB position of our graphics buffer
;-----------------------------------------------------
	ldx #47		;graphics buffer is 48 bytes
	lda #>_space	;load up the page value for the font
grOff
	sta grfxBuffer,x	;stuff it, won't ever change
	dex		;back up two bytes
	dex
	bpl grOff	;and loop


;---------------------------------------------------------------------------
; Initialize variables
;---------------------------------------------------------------------------

	; Set initialization flag.
	; This stays set until the first frame is drawn.
	lda #$0f	;set text color to white
	sta COLUP0
	sta COLUP1	

;	lda #113
;	sta measure

	lda #<_play
	sta grfxBuffer+0
	lda #<_space
	sta grfxBuffer+2
	lda #<_space
	sta grfxBuffer+4
	lda #<_space
	sta grfxBuffer+6
	lda #<_space
	sta grfxBuffer+8
	lda #<_space
	sta grfxBuffer+10
	lda #<_space
	sta grfxBuffer+12
	lda #<M
	sta grfxBuffer+14
	lda #<_eq
	sta grfxBuffer+16
	lda #<_0
	sta grfxBuffer+18
	lda #<_0
	sta grfxBuffer+20
	lda #<_0
	sta grfxBuffer+22




;--------------------------------------------------------------------------
; GameLoop
;--------------------------------------------------------------------------
GameLoop
	jsr VSync 	;start vertical retrace

	inc frame	;we count frames for alternating graphics displays

	jsr VBlank    	; spare time during screen blank
	jsr Picture		; draw one screen
	jsr overscan	; do overscan

	jmp GameLoop    ;back to top


;---------------------------------------------------------------------------
; Text Engine Graphics Setup
;---------------------------------------------------------------------------
; use cycle counting to get the GRP registers configured and located
; in exactly the right spot
;---------------------------------------------------------------------------
textSetup
	sta WSYNC	;newline
	lda #54		;triple copy sprites, spaced wide
	sta NUSIZ0	;for both player graphic registers
	sta NUSIZ1	
	lda #$31	;draw leftmost and rightmost 2 playfield bits: reflect
	sta PF0		;this turns left/right edges black
	sta CTRLPF	;this makes playfield reflective
	nop		;wait 2 cycles, we need them get our RESP0/1 right
	sta VDELP0	;turn on vertical delay for both players
	sta VDELP1
	sta RESP0	;mark our left margin here in P0
	lda #$D0	;setup to shift over 3 pixels to the right
	sta RESP1	;set P1
	sta HMP0	;prep P0 for his HMOVE
	lda #$C0	;setup to shift P1 4 pixels to the right
	sta HMP1	;prep P1 for his HMOVE

	sta WSYNC	;newline
	sta HMOVE	;anchor them down

	rts




;--------------------------------------------------------------------------
; VSync
;--------------------------------------------------------------------------
VSync
	lda #2		;bit 1 needs to be 1 to start retrace
	sta VSYNC	;start retrace
	sta WSYNC 	;wait a few lines
	sta WSYNC 
	lda #44		;prepare timer to exit blank period (44)
	sta TIM64T	;turn it on
	sta WSYNC 	;wait one more
	sta VSYNC 	;done with retrace, write 0 to bit 1

	rts ; VSync


digitsOffsets
	byte <_0,<_1
	byte <_2,<_3
	byte <_4,<_5
	byte <_6,<_7
	byte <_8,<_9


;--------------------------------------------------------------------------
; VBlank
;--------------------------------------------------------------------------
; Handle user input and display setup during the VBLANK period
;--------------------------------------------------------------------------
VBlank

	; Clear any visual mode stuff
	jsr textSetup

	lda #0
	sta PF0
	sta PF1
	sta PF2
	sta COLUBK
	sta ENAM0
	sta ENAM1
	sta ENABL

	; Display beat progresser
	lda #<_space
	sta grfxBuffer+4
	lda #<_space
	sta grfxBuffer+6
	lda #<_space
	sta grfxBuffer+8 
	lda #<_space
	sta grfxBuffer+10

	lda beat
	and #%00001100
	lsr
	tax
	lda #<_dot
	sta grfxBuffer+4,x
	


	;Display current measure
	lda #<_0
	sta grfxBuffer+18
	lda #<_0
	sta grfxBuffer+20

	lda measure
	cmp #100
	bmi no100s
	
	sbc #100	

	ldx #<_1
	stx grfxBuffer+18

	cmp #100
	bmi no100s
	
	sbc #100

	ldx #<_2
	stx grfxBuffer+18

no100s


	ldx #0

tensLoop

	cmp #10
	bmi endTens
	
	sbc #10

	inx
	jmp tensLoop

endTens
	
	tay
	
	lda digitsOffsets,x
	sta grfxBuffer+20

	lda digitsOffsets,y
	sta grfxBuffer+22


	; default to play icon
	lda #<_play
	sta grfxBuffer+0
	lda #<_sp
	sta grfxBuffer+2
	

	lda SWCHB
	and #1
	bne noFF

	; default to play icon
	lda #<_ff
	sta grfxBuffer+0
	lda #<_ff
	sta grfxBuffer+2
	
	lda frame
	and #%00000011
	bne noFF 

	inc measure

noFF

	lda SWCHB
	and #2
	bne noRW

	; default to play icon
	lda #<_rew
	sta grfxBuffer+0
	lda #<_rew
	sta grfxBuffer+2
	
	lda frame
	and #%00000011
	bne noRW 

	lda measure
	beq noRW

	dec measure

noRW



	lda SWCHB
	and #8
	bne playMode

	; pause icon
	lda #<_pause
	sta grfxBuffer+0

	
	lda #0
	sta AUDV0
	sta AUDV1

	jmp skipPlay

playMode
	jsr songPlayer

skipPlay

	

	rts ; VBlank

;--------------------------------------------------------------------------
; Overscan
;--------------------------------------------------------------------------
; I ran out of time in VBlank, so I'm doing some things during overscan
;--------------------------------------------------------------------------
overscan

	sta WSYNC	
	lda #33		; Use the timer to make sure overscan takes (34)
	sta TIM64T	; 30 scan lines.  29 scan lines * 76 = 2204 / 64 = 34.4

endOS	
	lda INTIM	; We finished, but wait for timer
	bne endOS	; by looping till zero
	
	sta WSYNC	; End last scanline

	lda #$82
	sta VBLANK
	lda #$02
	sta VBLANK

	rts	; overscan






;--------------------------------------------------------------------------
; Draw TV Pictures
;--------------------------------------------------------------------------
; Here is where we step down the screen drawing everything.
;
; Note that temp16 is used in here as a text pointer, so don't use
; it for anything else during the loop.
;--------------------------------------------------------------------------
;	align 256
Picture

;	lda beat
;	ora #%00010110
	lda #$0F
	sta COLUP0
	sta COLUP1

	lda #1		;setup counter for rows of text
	sta scanSec	;store in zero page memory variable

	ldy #0		;Y is used to track progress through this screen's text
	sty EOTflag
	sty GRP0
	sty GRP1


pictureLoop
	lda INTIM	;check timer for end of VBLANK period
	bne pictureLoop	;loop until it reaches 0

	;sta WSYNC	;newline (1)
	lda #$80
	sta VBLANK  	;end screen blank

ScanLoop	
;---------------------------------------------------------------------------


	lda #64		; A variable amount of text will be processed, so stay....

	sta WSYNC	
	jmp timer	

; Timer
;--------------------------------------------------------------------------

	align 256
timer

	sta  TIM8T	;....in sync by timing out after finished (7 scanlines)

eol	
	lda INTIM	; We finished, but wait for timer
	bne eol		; by looping till zero
	sta WSYNC	; end current line

	tya			; Need to save Y by putting into accumulator
	pha			; then onto stack.
	jsr println	; Print this row via subroutine. (6 scanlines)
	pla			; Pull Y off stack
	tay			; and put back.

	dec scanSec	; next row to print
	beq quitScanLoop; loop until all 11 rows of text have been displayed

	jmp ScanLoop

quitScanLoop

;--------------------------------------------------------------------------
; ShowVisuals2
;--------------------------------------------------------------------------

showVisuals2

	lda #0
	sta COLUBK

	lda #$80
	sta VBLANK  	;end screen blank

; Setup Color buffer pointer
;--------------------------------------------------------------------------
	ldx visualPointer
	inx
	cpx #46
	bmi notResetVis
	ldx #0
notResetVis
	stx visualPointer

	sta WSYNC

; Put current note color into buffer
;--------------------------------------------------------------------------

	; Put the next color in the scrolling buffer
	; based on the current note1.

	lda frame
	and #%00001111
	sta temp

	lda note1
	cmp #255
	bne calcColor

	;lda #$44
	;lda frame
	lda #0
	jmp setColor

calcColor
	asl
	asl
	asl
	asl
	asl
	;ora #%00000100

setColor
	and #%11110000
	ora temp	
	
	;ora #%00000100



	sta visualBuffer,x

	sta WSYNC

	; Set the missile colors based on the current note2.

	lda note2

	cmp #255
	bne getColor2

	lda #0
	jmp setColor2

getColor2

	asl
	asl
	asl
	asl
	asl
	ora #%00001000

setColor2

	sta WSYNC

	; draw white line
	lda #$0F
	sta COLUBK

	sta temp16L
	sta COLUP0
	sta COLUP1

	; Enable missiles
	lda #255
	sta ENAM0
	sta ENAM1
;	sta GRP0
;	sta GRP1

	sta WSYNC
	lda visualBuffer+1,x
	sta COLUBK
	sta GRP1
	sta GRP0
	asl
	sta COLUP0
	lsr

	eor #$0F
	and #$0F
	ora temp16L
	sta COLUP1

	

; Draw screen loop
;--------------------------------------------------------------------------
	ldy #42
visualLoop

	sta WSYNC
	
	; Move the missles around every few scanlines
	; based on notes pressed.  This creates some
	; neat patterns.
	lda note1
	asl
	asl
	sta HMP0
	eor #255
	ora #16
	sta HMM0
	lda note2
	asl
	asl
	sta HMP1
	eor #255
	ora #16
	sta HMM1

	sta WSYNC
	sta HMOVE

	sta WSYNC

	; Display the scrolling note-color buffer	
	inx
	cpx #46
	bmi notResetVis2
	ldx #0
notResetVis2
	sta WSYNC
	lda visualBuffer,x
	sta COLUBK
	sta GRP1
	sta GRP0

;	eor #$0F
	asl
	sta COLUP0
	lsr

	eor #$0F
	and #$0F
	ora temp16L
	sta COLUP1

;	lda note1
;	eor #255
;	bne noBlack

;	sta COLUP0
	
noBlack	
	

	dey
	bne visualLoop

; Done drawing screen.  Finish up.
;--------------------------------------------------------------------------
	ldx #7
extraLines
	sta WSYNC
	dex
	bne extraLines

	stx GRP0
	stx GRP1
	
	
	lda #$82
	sta VBLANK	; Finished a screen, blank the beam.

	rts ; showVisuals






	org $F800



;---------------------------------------------------------------------------
; Program Startup
;---------------------------------------------------------------------------
	org $FFFC
	.word Start
	.word Start

