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
import random

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
    def __init__(self, x0=["A1", [["sucio", "sucio","sucio"], ["sucio", "sucio","sucio"], ["sucio", "sucio","sucio"]]]):
        """
        Por default inicialmente el robot está en A1 y todos los cuartos
        están sucios.

        """
        super().__init__(x0)
        self.costo = 0

    def accion_legal(self, accion):
        posicion, _ = self.x
        piso, cuarto = posicion[0], int(posicion[1])
        
        if accion == "subir":
            return piso in "BC" and cuarto == 3
        elif accion == "bajar":
            return piso in "AB"
        elif accion == "ir_Derecha":
            return cuarto < 3
        elif accion == "ir_Izquierda":
            return cuarto > 1
        elif accion in ("limpiar", "nada"):
            return True
        return False

    def transicion(self, accion):
        if not self.accion_legal(accion):
             print(f"Acción ilegal: {accion}")
             return "nada" # Si la acción no es legal, simplemente no hace nada
            #raise ValueError(f"Acción '{accion}' no es legal en el estado actual.")

        print(f"Estado actual: {self.x}, Acción: {accion}")
        posicion, cuartos = self.x
        piso, cuarto = posicion[0], int(posicion[1])

        if accion == "limpiar":
            cuartos["ABC".index(piso)][cuarto - 1] = "limpio"
            self.costo += 1
        elif accion == "ir_Derecha" and cuarto < 3:
            self.x[0] = f"{piso}{cuarto + 1}"
            self.costo += 2
        elif accion == "ir_Izquierda" and cuarto > 1:
            self.x[0] = f"{piso}{cuarto - 1}"
            self.costo += 2
        elif accion == "subir" and piso != "A":
            self.x[0] = f"{chr(ord(piso) + 1)}{cuarto}"
            self.costo += 3
        elif accion == "bajar" and piso != "C":
            self.x[0] = f"{chr(ord(piso) - 1)}{cuarto}"
            self.costo += 3
        elif accion == "nada":
            pass

    def percepcion(self):
        posicion, cuartos = self.x
        piso, cuarto = posicion[0], int(posicion[1])
        if piso not in "ABC" or cuarto < 1 or cuarto > 3:
            raise ValueError(f"Posición inválida: {posicion}. Estado: {self.x}")
        return posicion, cuartos["ABC".index(piso)][cuarto - 1]
    
class AgenteReactivoNueveCuartos(entornos_o.Agente):
    """
    Agente reactivo para el entorno NueveCuartos.
    """
    def programa(self, percepcion):
        posicion, estado_cuarto = percepcion
        piso, cuarto = posicion[0], int(posicion[1])  # Dividimos la posición en piso y cuarto

        if estado_cuarto == "sucio":
            return "limpiar"
        elif cuarto < 3:  # Si no estamos en el último cuarto, ir a la derecha
            #print(cuarto)
            return "ir_Derecha"
        elif cuarto == 1 and estado_cuarto == "limpio" and piso != "A":  # Subir si estamos en el último cuarto de un piso y no estamos en C
            return "subir"
        elif cuarto == 3 and estado_cuarto == "limpio" and piso != "C":  # Bajar si estamos en el primer cuarto de un piso y no estamos en A
            return "bajar"
        elif cuarto > 1:  # Si no estamos en el primer cuarto, ir a la izquierda
            return "ir_Izquierda"
        else:  # Si todo está limpio o no hay nada más que hacer, hacer nada
            return "nada"

    

    
class AgenteAleatorioNueveCuartos(entornos_o.Agente):
    """
    Agente Aleatorio para el entorno NueveCuartos.
    """
    def programa(self, percepcion):
        posicion = percepcion
        piso, cuarto = posicion[0], int(posicion[1])
        
        num = random.randrange(6)

        if num == 0:
            return "limpiar"
        elif num == 1 and cuarto < 3:
            return "ir_Derecha"
        elif num == 2 and piso != "A":
            return "subir"
        elif num == 3 and cuarto > 1:
            return "ir_Izquierda"
        elif num == 4 and piso != "C":
            return "bajar"
        elif num == 5:
            return "nada"
        else:
            return "nada"

if __name__ == "__main__":
    # Inicializa el entorno y el agente
    entorno = NueveCuartos()
    #agente = AgenteAleatorioNueveCuartos()
    agente = AgenteReactivoNueveCuartos()

    # Simula por 200 pasos
    entornos_o.simulador(entorno, agente, pasos=200, verbose=True)
