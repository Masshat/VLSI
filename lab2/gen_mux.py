from stratus import *
import mux


def StratusScript ():
  if globals().has_key ( "__editor" ):
    setEditor ( __editor )

 # Recuperation du parametre depuis la ligne de commande
  n = Param ( "n" )
 # Fabrication du dictionnaire des parametres
  dict = { 'nbit' : n }
  
 # Creation de l'instance mux avec les parametres definis par le dictionnaire dict
  instance = mux.mux ( "mux_%d" % n, dict )
 # Generation effective du mux
  instance.Interface ()
  instance.Netlist   ()
 # Ecriture sur le disque de l'instance produite
  instance.Save ()
  
 # Simulation
  instance.Pattern ()
  instance.Simul   ()
  return


if __name__ == "__main__" :
  StratusScript ()
