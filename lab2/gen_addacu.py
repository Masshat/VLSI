from stratus import *
import addaccu

def StratusScript ():
  if globals().has_key ( "__editor" ):
    setEditor ( __editor )

 
  n = Param ( "n" )
  dict = { 'nbit' : n }
  instance = addaccu.addaccu ( "addaccu%d" % n, dict )
  instance.Interface ()
  instance.Netlist   ()
  instance.Save ()

  #Simulation
  instance.Pattern ()
  instance.Simul   ()
  return

if __name__ == "__main__" :
  StratusScript ()
