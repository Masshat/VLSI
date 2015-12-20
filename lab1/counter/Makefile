SYF = syf -CEV
ASIMUT = asimut -b 
ENC ?= r

all : asimut

syf : cpt5.fsm
	$(SYF) -$(ENC) $<

asimut : syf 
	$(ASIMUT) cpt5$(ENC) cpt5_in cpt5_out

xpat :
	xpat -l  cpt5_out

xfsm :
	xfsm -l cpt5.fsm

clean :
	rm -rf *.vbe *.enc *out*
