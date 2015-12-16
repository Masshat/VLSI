#!/usr/bin/env python


from stratus import *
import full_adder


def StratusScript ():
  if globals().has_key ( "__editor" ):
    setEditor ( __editor )
  
  instance = full_adder.full_adder ( "full_adder" )
 # Generation effective du full_adder
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
