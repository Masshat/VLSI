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
# |  Status  . . . . . . . . . . . . . . . . . . . . .  "./accu.py" |
# |  Version   . . . . . . . . . . . . . . . . . . . . . . .   1.0  |
# |  Date  . . . . . . . . . . . . . . . . . . .   October 30 2015  |
# |                                                                 |
# +-----------------------------------------------------------------+


from stratus import *


class accu ( Model ) :

	def Interface ( self ):
   # Recuperation du parametre "nbit".
		self.n   = self._param['nbit']
  
    # Declaration des connecteurs.
		self.i  = SignalIn  ( "i"  , self.n )
		self.ck= SignalIn ( "ck" , 1)
		self.q   = SignalOut ( "q"   , self.n )
		self.vdd = VddIn     ( "vdd" )
		self.vss = VssIn     ( "vss" )
		return
    
	def Netlist ( self ) :
		# Instanciation du vecteur de 'n' accu.
		for i in range (self.n) :
			Inst ( "sff1_x4"
           , map = { 'i'  : self.i[i]
                   , 'ck'  : self.ck
                   , 'q'   : self.q[i]
                   , 'vdd' : self.vdd
                   , 'vss' : self.vss
                   }
          )
           
		return
    
	def Pattern ( self ) :
   # Nom du fichier de pattern.
		pat = PatWrite(self._name+'.pat',self)
   
   # Declaration de l'interface. 
		pat.declar ( self.i , 'X' )
		pat.declar ( self.ck, 'B' )
		pat.declar ( self.q  , 'X' )
    
		pat.declar ( self.vdd, 'B' )
		pat.declar ( self.vss, 'B' )

   # Debut de la description des patterns.
		pat.pattern_begin ()
    
   # Affectation des valeurs.
		pat.affect_int ( self.vdd, 1 )
		pat.affect_int ( self.vss, 0 )
		
		for value_i in range ( self.n ) :
			for value_ck in range ( 2 ) :
				pat.affect_int ( self.i , value_i)
				pat.affect_int ( self.ck , value_ck)
				if value_ck == 1 : pat.affect_int ( self.q, value_i )
				pat.addpat ()
		del pat
		return

  
 
