#!/usr/bin/env python
#
#    LIP6
#    University Pierre & Marie Curie - UPMC
#    4, place Jussieu 75252 Paris Cedex 05
#    France
#
# +-----------------------------------------------------------------+
# |                                                                 |
# |                      M a s t e r   S E S I                      |
# |                  U E   T O O L S  -  T M E   3                  |
# |                                                                 |
# |  Author  . . . . . . . . . . . . . . . . . .   Andres Brand     |
# |  Status  . . . . . . . . . . . . . . . . . . . . .  "./add.py" |
# |  Version   . . . . . . . . . . . . . . . . . . . . . . .   1.0  |
# |  Date  . . . . . . . . . . . . . . . . . . .   October 30 2015  |
# |                                                                 |
# +-----------------------------------------------------------------+


from stratus import *


class full_adder ( Model ) :

	def Interface ( self ):
   # Recuperation du parametre "nbit".
	  
    # Declaration des connecteurs.
		self.a  = SignalIn  ( "a"  , 1 )
		self.b  = SignalIn  ( "b"  , 1 )
		self.c = SignalIn  ( "c"  , 1 )
		self.s   = SignalOut ( "s"   , 1 )
		self.r   = SignalOut ( "r"   , 1)
		self.vdd = VddIn     ( "vdd" )
		self.vss = VssIn     ( "vssi" )
		return
    
	def Netlist ( self ) :
		# Instanciation du vecteur de 'n' accu.
		self.ng   = Signal ( "ng"   ,1)
		self.p   = Signal ( "p"   ,1)
		self.np_c   = Signal ( "np_c"   , 1)
		Inst('na2_x1'
			, map={'i0':self.a,
				'i1':self.b,
				'nq':self.ng,
				'vdd':self.vdd,
				'vss':self.vss}
			) 
		Inst('xr2_x1'
			, map={'i0':self.a,
				'i1':self.b,
				'q':self.p,
				'vdd':self.vdd,
				'vss':self.vss}
			) 
		Inst('na2_x1'
			, map={'i0':self.ng,
				'i1':self.np_c,
				'nq':self.r,
				'vdd':self.vdd,
				'vss':self.vss}
			) 
		Inst('na2_x1'
			, map={'i0':self.p,
				'i1':self.c,
				'nq':self.np_c,
				'vdd':self.vdd,
				'vss':self.vss}
			)	
		Inst('xr2_x1'
			, map={'i0':self.p,
				'i1':self.c,
				'q':self.s,
				'vdd':self.vdd,
				'vss':self.vss}
			)
			
	def Pattern ( self ) :
   # Nom du fichier de pattern.
		pat = PatWrite(self._name+'.pat',self)
   
   # Declaration de l'interface. 
		pat.declar ( self.a , 'B' )
		pat.declar ( self.b, 'B' )
		pat.declar ( self.c, 'B' )
		pat.declar ( self.r, 'B' )
		pat.declar ( self.s  ,'B' )
    
		pat.declar ( self.vdd, 'B' )
		pat.declar ( self.vss, 'B' )

   # Debut de la description des patterns.
		pat.pattern_begin ()
    
   # Affectation des valeurs.
		pat.affect_int ( self.vdd, 1 )
		pat.affect_int ( self.vss, 0 )
    
		for value_a in range ( 2 ) :
			for value_b in range ( 2 ) :
				for value_c in range ( 2 ) :
					pat.affect_int ( self.a , value_a )
					pat.affect_int ( self.b , value_b )
					pat.affect_int ( self.c , value_c )
					pat.affect_int ( self.r, ((value_a & value_b) | (value_a & value_c) | (value_b & value_c)))
					pat.affect_int ( self.s, (value_a ^ value_b ^ value_c) )
					pat.addpat ()
		del pat
		return
