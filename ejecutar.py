# -*- encoding: utf-8 -*-
#  MEMO-Huayra es un fork de Memorice desarrollado para Huayra-gnu/linux
#  2013
#  Desarrolladores:
#     Mercedes Elgarte
#     Héctor Sanchez
#     Diego Accorinti
#
# license: lgplv3 (see http://www.gnu.org/licenses/lgpl.html)

# For pilas engine - a video game framework.
#
# copyright 2011 - Pablo Garrido
# license: lgplv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# website - http://www.pilas-engine.com.ar

import pilas

pilas.iniciar(titulo = "MEMO-Huayra")




# ejecuta escena actual.
import escena_menu
pilas.cambiar_escena(escena_menu.EscenaMenu())



pilas.ejecutar()
