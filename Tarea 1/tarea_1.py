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
    def __init__(self, x0=["C1", [["sucio", "sucio","sucio"], ["sucio", "sucio","sucio"], ["sucio", "sucio","sucio"]]]):
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
        try:
            return posicion, cuartos["ABC".index(piso)][cuarto - 1]
        except (IndexError, TypeError) as e:
            raise ValueError(f"Error al acceder al estado: {self.x}. Detalles: {e}")


    
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
            return "ir_Derecha"
        elif cuarto == 3 and estado_cuarto == "limpio" and piso != "C":  # Subir si estamos en el último cuarto de un piso y no estamos en C
            return "subir"
        elif cuarto == 1 and estado_cuarto == "limpio" and piso != "A":  # Bajar si estamos en el primer cuarto de un piso y no estamos en A
            return "bajar"
        elif cuarto > 1:  # Si no estamos en el primer cuarto, ir a la izquierda
            return "ir_Izquierda"
        else:  # Si todo está limpio o no hay nada más que hacer, hacer nada
            return "nada"
        
class AgenteAleatorioNueveCuartos(entornos_o.Agente):
    """
    Agente Aleatorio para el entorno NueveCuartos.
    Selecciona una acción al azar entre las legales.
    """

    def programa(self, percepcion):
        posicion, estado_cuarto = percepcion  # Recibe la posición actual y el estado del cuarto
        acciones_posibles = ["limpiar", "ir_Derecha", "ir_Izquierda", "subir", "bajar", "nada"]

        # Filtra las acciones legales
        acciones_legales = [accion for accion in acciones_posibles if entorno.accion_legal(accion)]

        print(f"Estado actual: {self.x}")
        # Selecciona una acción aleatoria de entre las legales
        return random.choice(acciones_legales)

if __name__ == "__main__":
    # Inicializa el entorno y el agente
    entorno = NueveCuartos()
    #agente = AgenteAleatorioNueveCuartos()
    agente = AgenteReactivoNueveCuartos()

    # Simula por 100 pasos
    entornos_o.simulador(entorno, agente, pasos=100, verbose=True)
