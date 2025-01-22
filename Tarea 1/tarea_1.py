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
        super().__init__(x0)
        self.costo = 0

    def accion_legal(self, accion):
        posicion, _ = self.x
        piso, cuarto = posicion[0], int(posicion[1])
        
        if accion == "subir":
            return piso in "BC" and cuarto == 3  # Subir solo desde cuartos derechos
        elif accion == "bajar":
            return piso in "AB" and cuarto == 1  # Bajar solo desde cuartos izquierdos
        elif accion == "ir_Derecha":
            return cuarto < 3
        elif accion == "ir_Izquierda":
            return cuarto > 1
        elif accion in ("limpiar", "nada"):
            return True
        return False

    def transicion(self, accion):
        if not self.accion_legal(accion):
            raise ValueError(f"Acción '{accion}' no es legal en el estado actual.")

        posicion, cuartos = self.x
        piso, cuarto = posicion[0], int(posicion[1])

        if accion == "limpiar":
            cuartos["ABC".index(piso)][cuarto - 1] = "limpio"
            self.costo += 1
        elif accion == "ir_Derecha":
            self.x[0] = f"{piso}{cuarto + 1}"
            self.costo += 2
        elif accion == "ir_Izquierda":
            self.x[0] = f"{piso}{cuarto - 1}"
            self.costo += 2
        elif accion == "subir":
            self.x[0] = f"{chr(ord(piso) + 1)}{cuarto}"
            self.costo += 3
        elif accion == "bajar":
            self.x[0] = f"{chr(ord(piso) - 1)}{cuarto}"
            self.costo += 3
        elif accion == "nada":
            pass

    def percepcion(self):
        posicion, cuartos = self.x
        piso, cuarto = posicion[0], int(posicion[1])
        return posicion, cuartos["ABC".index(piso)][cuarto - 1]
    
class AgenteReactivoNueveCuartos(entornos_o.Agente):
    """
    Agente reactivo para el entorno NueveCuartos.
    """
    def programa(self, percepcion):
        posicion, estado_cuarto = percepcion

        if estado_cuarto == "sucio":
            return "limpiar"
        elif posicion.endswith("1"):
            return "ir_Derecha"
        elif posicion.endswith("3") and posicion[0] != "C":
            return "subir"
        elif posicion.endswith("3") and posicion[0] == "C":
            return "ir_Izquierda"
        elif posicion.endswith("2"):
            return "ir_Izquierda"
        else:
            return "nada"
        
if __name__ == "__main__":
    # Inicializa el entorno y el agente
    entorno = NueveCuartos()
    agente = AgenteReactivoNueveCuartos()

    # Simula por 100 pasos
    entornos_o.simulador(entorno, agente, pasos=100, verbose=True)
