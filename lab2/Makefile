N ?= 64


all : mux full_adder adder accu addacu

gen :
	python gen_addacu_gen.py -n $(N)
	
dpgen : 
	python gen_addacu_dpgen.py -n $(N)

mux :
	python gen_mux.py -n $(N)

full_adder : 
	python gen_fulladder.py

adder : 
	python gen_adder.py -n $(N)

accu : 
	python gen_accu.py -n $(N)

addacu : 
	python gen_addacu.py -n $(N)

view :
	xsch -l addaccu$(N).vst 

clean :
	rm -rf *.vst *.pyc *.pat *.ap
