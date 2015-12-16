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
# |  Author  . . . . . . . . . . . . . . . . . .   Sophie Belloeil  |
# |  Status  . . . . . . . . . . . . . . . . . . . . .  "./mux.py"  |
# |  Version   . . . . . . . . . . . . . . . . . . . . . . .   1.0  |
# |  Date  . . . . . . . . . . . . . . . . . . .   January 08 2010  |
# |                                                                 |
# +-----------------------------------------------------------------+


from stratus import *
import full_adder


class adder ( Model ) :

	def Interface ( self ):
   # Recuperation du parametre "nbit".
		self.n   = self._param['nbit']
		
		Generate ( "full_adder.full_adder", "full_adder")

   # Declaration des connecteurs.
		self.i0  = SignalIn  ( "i0"  , self.n )
		self.i1  = SignalIn  ( "i1"  , self.n )
		self.cin = SignalIn  ( "cin" , 1      )
		self.cout   = SignalOut ( "cout"   , 1 )
		self.q  = SignalOut ( "q"   , self.n )
		self.vdd = VddIn     ( "vdd" )
		self.vss = VssIn     ( "vss" )
		return


	def Netlist ( self ) :
		self.r   = Signal ( "r"   , self.n)	
		#Premier Fulladder
		Inst ( "full_adder"
			, map = { 'a'  : self.i0[0]
					, 'b'  : self.i1[0]
                    , 'c'  : self.cin[0]
                    , 's' : self.q[0]
                    , 'r'   : self.r[0] 
                    , 'vdd' : self.vdd
                    , 'vssi' : self.vss
                   }
           )
	#Full Adder Intermedieres
		for i in range (1, self.n -1) :          
			Inst ( "full_adder" ,
			map = { 'a'  : self.i0[i]
                   , 'b'  : self.i1[i]
                   , 'c'  : self.r[i-1]
                   , 's' : self.q[i]
                   , 'r'   : self.r[i] 
                   , 'vdd' : self.vdd
                   , 'vssi' : self.vss
                   }
				)
     #Last Full Adder
		Inst ( "full_adder" , 
			map = { 'a'  : self.i0[self.n-1]
                   , 'b'  : self.i1[self.n-1]
                   , 'c'  : self.r[self.n-2]
                   , 's' : self.q[self.n-1]
                   , 'r'   : self.cout 
                   , 'vdd' : self.vdd
                   , 'vssi' : self.vss
                   }
			)
		return
       
	def Pattern ( self ) :
   # Nom du fichier de pattern.
		pat = PatWrite(self._name+'.pat',self)
   
   # Declaration de l'interface. 
		pat.declar ( self.i0 , 'X' )
		pat.declar ( self.i1 , 'X' )
		pat.declar ( self.cin, 'B' )
		pat.declar ( self.q , 'X' )
		pat.declar ( self.cout  , 'B' )
    
		pat.declar ( self.vdd, 'B' )
		pat.declar ( self.vss, 'B' )

   # Debut de la description des patterns.
		pat.pattern_begin ()
    
   # Affectation des valeurs.
		pat.affect_int ( self.vdd, 1 )
		pat.affect_int ( self.vss, 0 )
    
   # double boucle: pour toutes les valeurs de d on teste
   # la valeur en sortie du registre suivant l'horloge.
	#	for value_i0 in  range ((2 **self.n)) :
	#		for value_i1 in range ( (2 **self.n)) :
	#			for value_cin in range (2) :
	#				pat.affect_int ( self.i0, value_i0 )
	#				pat.affect_int ( self.i1, value_i1 )
	#				pat.affect_int ( self.cin,value_cin )
	#				#somme=(value_i0+value_i1+value_cin)
	#		#if (somme>((2**self.n)-1)): pat.affect_int ( self.q, 0 )
	#		#else: pat.affect_int ( self.q, somme)
	#		#if (somme>((2**self.n)-1)): pat.affect_int ( self.cout, 1 )
	#		#else: pat.affect_int ( self.cout, 0)
	#				pat.addpat ()
	#	del pat
		return


