#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tarea_1.py
------------

Revisa el archivo README.md con las instrucciones de la tarea.

"""
__author__ = 'escribe_tu_nombre'

import entornos_f
import entornos_o

# Requiere el modulo entornos_f.py o entornos_o.py
# Usa el modulo doscuartos_f.py para reutilizar código
# Agrega los modulos que requieras de python

class NueveCuartos(entornos_o.Entorno):
    """
    Crea un entorno de nueve cuartos 3x3, osea:
    A1|A2|A3
    B1|B2|B3
    C1|C2|C3
    
    Metodo Orientado a Objetos
    """
    def __init__(self, x0=["C1", [["sucio", "sucio","sucio"], ["sucio", "sucio","sucio"], ["sucio", "sucio","sucio"]]]):
        """
        Por default inicialmente el robot está en C1 y todos los cuartos
        están sucios.

        """
        self.x = x0[:]
        self.costo = 0

    def accion_legal(self, accion):
        return accion in ("ir_Derecha", "ir_Izquierda", "subir", "bajar", "limpiar", "nada")
    #"ir_A", "ir_B", "limpiar", "nada"

    def transicion(self, accion):
        if not self.acción_legal(accion):
            raise ValueError("La acción no es legal para este estado")

        robot, a, b = self.x
        if accion != "nada" or a == "sucio" or b == "sucio":
            self.costo += 1
        if accion == "limpiar":
            
            self.x[" AB".find(self.x[0])] = "limpio"
        elif accion == "ir_A":
            self.x[0] = "A"
        elif accion == "ir_B":
            self.x[0] = "B"

    def percepcion(self):
        return self.x[0], self.x[" AB".find(self.x[0])]
