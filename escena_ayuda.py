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


class Ayuda(pilas.escena.Base):
    "Escena que entrega instrucciones de como jugar."

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Fondo('data/ayuda.png')
		
        self.volver = pilas.actores.Boton(x=0, y=-200)
        self.volver.imagen = 'data/volver.png'
        self.volver.conectar_presionado(self.cuando_se_presione_escape)
        self.pulsa_tecla_escape.conectar(self.cuando_se_presione_escape)

    def cuando_se_presione_escape(self, *k, **kv):
        "Regresa al menu principal"
        import escena_menu
        pilas.cambiar_escena(escena_menu.EscenaMenu())
