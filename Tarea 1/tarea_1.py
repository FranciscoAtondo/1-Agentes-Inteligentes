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
    def __init__(self, x0=["A1", [["sucio", "sucio", "sucio"], ["sucio", "sucio", "sucio"], ["sucio", "sucio", "sucio"]]]):
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
            return piso in "BC"  # Subir solo es posible desde los pisos B y C
        elif accion == "bajar":
            return piso in "AB"  # Bajar solo es posible desde los pisos A y B
        elif accion == "ir_Derecha":
            return cuarto < 3  # Ir a la derecha es posible si no estás en el cuarto 3
        elif accion == "ir_Izquierda":
            return cuarto > 1  # Ir a la izquierda es posible si no estás en el cuarto 1
        elif accion in ("limpiar", "nada"):
            return True  # Siempre es posible limpiar o no hacer nada
        return False

    def transicion(self, accion):
        if not self.accion_legal(accion):
            raise ValueError(f"Acción '{accion}' no es legal en el estado actual.")

        posicion, cuartos = self.x
        piso, cuarto = posicion[0], int(posicion[1])  # Convertimos la posición

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
            self.x[0] = f"{chr(ord(piso) - 1)}{cuarto}"  # Baja un nivel manteniendo el cuarto actual
            self.costo += 3
        elif accion == "nada":
            pass

def percepcion(self):
    posicion, cuartos = self.x
    piso, cuarto = posicion[0], int(posicion[1])  # Convertimos la posición
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
        elif cuarto < 3 and piso in "ABC":  # Si no está en el último cuarto, moverse a la derecha
            return "ir_Derecha"
        elif cuarto == 3 and piso != "A":  # Si está en el último cuarto de un piso inferior, subir
            return "subir"
        elif cuarto == 3 and piso == "A":  # Si está en el último cuarto del piso A, moverse a la izquierda
            return "ir_Izquierda"
        elif cuarto == 1 and piso != "C":  # Si está en el primer cuarto y no está en el piso C, bajar
            return "bajar"
        elif cuarto > 1:  # Si puede moverse a la izquierda
            return "ir_Izquierda"
        else:
            return "nada"
        
class AgenteAleatorio(entornos_o.Agente):
    """
    Agente Aleatorio para el entorno NueveCuartos.
    """
    def programa(self, percepcion):
        posicion, estado_cuarto = percepcion
        piso, cuarto = posicion[0], int(posicion[1])
        
        num = random.randrange(7)

        if num == 0 and estado_cuarto == "sucio":
            return "limpiar"
        elif num == 1 and cuarto < 3 and piso in "ABC":  # Si no está en el último cuarto, moverse a la derecha
            return "ir_Derecha"
        elif num == 2 and cuarto == 3 and piso != "A":  # Si está en el último cuarto de un piso inferior, subir
            return "subir"
        elif num == 3 and cuarto == 3 and piso == "A":  # Si está en el último cuarto del piso A, moverse a la izquierda
            return "ir_Izquierda"
        elif num == 4 and cuarto == 1 and piso != "C":  # Si está en el primer cuarto y no está en el piso C, bajar
            return "bajar"
        elif num == 5 and cuarto > 1:  # Si puede moverse a la izquierda
            return "ir_Izquierda"
        elif num == 6:
            return "nada"
        else:
            return "nada"

if __name__ == "__main__":
    # Inicializa el entorno y el agente
    entorno = NueveCuartos()
    agente = AgenteAleatorio()

    # Simula por 100 pasos
    entornos_o.simulador(entorno, agente, pasos=100, verbose=True)
