from stratus import *
import addaccu_dpgen

def StratusScript ():
  if globals().has_key ( "__editor" ):
    setEditor ( __editor )

  n = Param ( "n" )
  dict = { 'nbit' : n }
  instance = addaccu_dpgen.addaccu_dpgen ( "addaccu_dpgen_%d" % n , dict )
  instance.Interface ()
  instance.Netlist   ()
  instance.Layout ()
    
  instance.Save (PHYSICAL)
  
  instance.Pattern ()
  instance.Simul   ()

  return
  
if __name__ == "__main__" :
	StratusScript ()

