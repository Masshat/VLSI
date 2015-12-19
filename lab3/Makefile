ENV_YAGLE = MBK_IN_LO=al; export MBK_IN_LO

ENV_INIT = MBK_IN_LO=vst; export MBK_IN_LO

cougar:
	cougar -t nandlayout nand_al

yagle:
	$(ENV_YAGLE); ~encadr/yagle -s nand_al nand_yagle
	$(ENV_INIT)

proof:
	proof nand_yagle nand

druc:
	druc nandlayout

clean:
	rm -rf *.al *.rep *_yagle.vbe *.drc *.cif
