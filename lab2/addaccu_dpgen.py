
#
# +-----------------------------------------------------------------+
# |                                                                 |
# |                      M a s t e r   S E S I                      |
# |                  U E   T O O L S  -  T M E   2                  |
# |                                                                 |
# |  Author  . . . . . . . . . . . . . . . . . .   Andres Brand  |
# |  Status  . . . . . . . . . . . . . . . . . . . . .  "./mux.py"  |
# |  Version   . . . . . . . . . . . . . . . . . . . . . . .   1.0  |
# |  Date  . . . . . . . . . . . . . . . . . . .   October 30 2015  |
# |                                                                 |
# +-----------------------------------------------------------------+

#!/usr/bin/env python

from stratus import *

class addaccu_dpgen ( Model ) :

	def Interface ( self ):
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
			
		Generate ( 'DpgenMux2', 'muxdp',
                 param = { 'nbit'     : self.n
                         , 'physical' : True
                         }
               )       
		
		Generate ( 'DpgenSff', 'accudp',
                 param = { 'nbit'     : self.n
                         , 'physical' : True
                         }
               )  
               
		Generate ( 'DpgenAdsb2f', 'adderdp',
                 param = { 'nbit'     : self.n
                         , 'physical' : True
                         }
               )   
               
		Generate ( 'DpgenBuff', 'buffdp',
                 param = { 'nbit'     : self.n
                         , 'physical' : True
                         }
               )		
		
		s_out_mx    = Signal ( "out_mx"   ,self.n)
		s_out_alu   = Signal ( "out_alu"   ,self.n)
		s_out_reg   = Signal ( "out_reg"   ,self.n)
		unconnected0  = Signal ("unconnected0",1)
		unconnected1  = Signal ("unconnected1",1)   
		ck_ring       = Signal ("ck_ring",       1)
		   
		self.mux = Inst ( "muxdp",
			map = { 'i0'  : self.a,
					'i1'  : s_out_reg,
					'cmd' : self.sel,
					'q'   : s_out_mx,
					'vdd' : self.vdd,
					'vss' : self.vss
					}
			)
			
		       
 		self.accu= Inst ( "accudp",
         	 map = { 'wen' : self.vdd,
					 'i0'  : s_out_alu,
                     'ck' : self.ck,
        	         'q'   : s_out_reg,
        	         'vdd' : self.vdd,
        	         'vss' : self.vss
        	           }
       				
			)
			
		self.adder= Inst ( "adderdp",
			 map = { 'i0'  : s_out_mx,
					 'i1' : self.b,
					 'add_sub' : self.vss,	
					 'q'   : s_out_alu,
					 'c30'     : unconnected0,
					 'c31'     : unconnected1,
					 'vdd' : self.vdd,
					 'vss' : self.vss
					}
			)
						
		self.buff = Inst ( 'buffdp',
             		map = { 'i0'  : s_out_reg,
					 'q'   : self.s,
         		   	         'vdd' : self.vdd,
                     			 'vss' : self.vss,
                   }
           )
			          
		return
		
	def Layout (self):
		#Massine#
		Place ( self.mux, NOSYM, XY(0,0) )
		#PlaceLeft (self.mux, NOSYM)
		PlaceRight (self.accu, NOSYM)
		PlaceRight (self.adder, NOSYM)
		PlaceRight (self.buff, NOSYM)	
		self.View()
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
  
