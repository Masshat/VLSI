# +-----------------------------------------------------------------+
# |                      M a s t e r   S E S I                      |
# |                      V L S I   -   L A B 2                      |
# |                                                                 |
# |  Author  . . . . . . . . . . .  Andres Brand/Massine BITAM      |
# |  Version   . . . . . . . . . . . . . . . . . . . . . . .   1.0  |
# |  Date  . . . . . . . . . . . . . . . . . . . .  November  2015  |
# |                                                                 |
# +-----------------------------------------------------------------+

from stratus import *
import adder
import mux
import accu

class addaccu ( Model ) :

	def Interface ( self ):
   # Recuperation du parametre "nbit".
		self.n   = self._param['nbit']
    
		if self.n<2:
			print("parametre entre < 2 => n=2")
			self.n=2
		elif self.n>64:
			print("parametre entre > 64 => n=64")
			self.n=64	

		
				
   # Declaration des connecteurs.
		self.a  = SignalIn  ( "a"  , self.n )
		self.b  = SignalIn  ( "b"  , self.n )
		self.sel= SignalIn  ( "sel" , 1      )
		self.ck= SignalIn  ( "clk" , 1      )
		self.s   = SignalOut ( "s"   , self.n )
		self.vdd = VddIn     ( "vdd" )
		self.vss = VssIn     ( "vss" )
		return

	def Netlist ( self ) :
		
		s_out_mx    = Signal ( "out_mx"   ,self.n)
		s_out_alu   = Signal ( "out_alu"   ,self.n)
		s_out_reg   = Signal ( "out_reg"   ,self.n)
		unused  = Signal ("unused",1)
		
		   
		Inst ( "mux_%d"%self.n,
			map = { 'i0'  : self.a,
					'i1' : s_out_reg,
					'cmd'   : self.sel,
					's'   : s_out_mx,
					'vdd' : self.vdd,
					'vss' : self.vss
					}
			)
			
		Inst ( "adder_%d"%self.n,
			 map = { 'i0'  : s_out_mx,
					 'i1' : self.b,
					 'cin' : self.vss,	
					 'cout':unused ,
					 'q'   : s_out_alu,
					 'vdd' : self.vdd,
					 'vss' : self.vss
					}
			)
       
 		Inst ( "accu_%d"%self.n,
         	 map = { 'i'  : s_out_alu,
                         'ck' : self.ck,
        	         'q'   : s_out_reg,
        	         'vdd' : self.vdd,
        	         'vss' : self.vss
        	           }
       				
			)
			
		for i in range ( self.n ) :
			Inst ( "buf_x4"
				, map = { 'i'  : s_out_reg[i]
						, 'q' : self.s[i]
						, 'vdd' : self.vdd
						, 'vss' : self.vss
						}
				)	
          
		return
		
	def Pattern ( self ) :
   # Nom du fichier de pattern.
		pat = PatWrite(self._name+'.pat',self)
   
   # Declaration de l'interface. 
		pat.declar ( self.a , 'B' )
		pat.declar ( self.b, 'B' )
		pat.declar ( self.sel, 'B' )
		pat.declar ( self.ck, 'B' )
		pat.declar ( self.s  ,'B' )
    
		pat.declar ( self.vdd, 'B' )
		pat.declar ( self.vss, 'B' )

   # Debut de la description des patterns.
		pat.pattern_begin ()
    
   # Affectation des valeurs.
		pat.affect_int ( self.vdd, 1 )
		pat.affect_int ( self.vss, 0 )
	
		for value_a in  range (self.n) :
			for value_b in range ( self.n) :
				for value_sel in range (2) :
					for value_ck in range (2) :
						pat.affect_int ( self.a, value_a )
						pat.affect_int ( self.b, value_b )
						pat.affect_int ( self.sel, value_sel )
						pat.affect_int ( self.ck,value_ck)
						pat.addpat ()
		del pat
		return
	
		return
  
