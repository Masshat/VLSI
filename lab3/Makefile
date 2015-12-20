ENV_YAGLE  = MBK_IN_LO=al;  export MBK_IN_LO
ENV_COUGAR = MBK_IN_PH=ap;  export MBK_IN_LO; \
	     MBK_OUT_LO=al; export MBK_OUT_LO

ENV_INIT = MBK_IN_LO=vst; export MBK_IN_LO

all: cougar Yagle proof druc

cougar:
	$(ENV_COUGAR); cougar -t nandlayout nand_al

Yagle:
	$(ENV_YAGLE); ./yagle -s nand_al nand_yagle
	$(ENV_INIT)

proof:
	proof nand_yagle nand

druc:
	druc nandlayout

clean:
	rm -rf *.al *.rep *_yagle.vbe *.drc *.cif
