SYF = syf -CEV
ASIMUT = asimut -b 
COUGAR = cougar
ENC ?= o
L ?= 3
D ?= 0

ENV_COUGAR = MBK_IN_LO=al; export MBK_IN_LO; \
	     MBK_OUT_LO=al; export MBK_OUT_LO

ENV_INIT   = MBK_IN_LO=vst; export MBK_IN_LO; \
	     MBK_OUT_LO=vst; export MBK_OUT_LO

ENV_S2R  = RDS_IN=cif; export RDS_IN; \
           RDS_OUT=cif; export RDS_OUT


all : asimut loon root

check : lvx

tp: asimut loon

syf : digi.fsm
	$(SYF) -$(ENC) $<

asimut : syf 
	$(ASIMUT) digi$(ENC) digi_in digi_out

asimut_verif :  
	$(ASIMUT) digi_verif digi_in digi_out

boom : digi$(ENC).vbe
	boom -V -l $(L) -d $(D) $< digi$(ENC)bm

boog : boom
	boog digi$(ENC)bm digi$(ENC)bg

loon : boog
	loon digi$(ENC)bg digi$(ENC)ln -x 1 -m 0

flatbeh :
	flatbeh digi$(ENC)ln digi_verif

proof : flatbeh
	proof -d digi$(ENC) digi_verif

ocp :
	 ocp -v -gnuplot -ioc digi digi$(ENC)ln digi_ap

root : ocp
	nero -V -p digi_ap digi$(ENC)ln digi_f

cougar :
	$(ENV_COUGAR); $(COUGAR)  -v -ac  digi_f digi_extract
	$(ENV_INIT)

lvx : cougar 
	 lvx vst al digi$(ENC)ln digi_extract

xpat :
	xpat -l  digi_out -xor

xfsm :
	xfsm -l digi.fsm 

#xsch :
#	xsch -I vst -l digiobg &

druc :
	druc digi_f

s2r :
	s2r -v digi_f

dreal :
	$(ENV_S2R); dreal -l digi_f -install

clean :
	rm -rf *.vbe *.enc *out* *.vst *.xsc *.ap *.gpl *.dat *.al *.drc *.cif
