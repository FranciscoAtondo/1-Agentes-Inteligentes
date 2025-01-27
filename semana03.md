# 27/01/2025 - Continuacion de Arboles de Decision.
En Arboles Binarios se llega mas rapido a la profunidad.

En Arboles Binarios, el limite de divisiones se puede definir como el numero de particiones del atributo X en el valor t, donde:
- Una rama: X<t
- otras ramas: X>t

Ganancia de Informacion - Entropia? Es sobre separacion de datos. Ejemplo: se tienen dos grupos de (10|10|5) datos en grupos Xa y Xb,
si se divide Xa en (8|10|4) y (2|0|1) y Xb en (7|7|0), (1|0|4) y (2|3|1), por el calculo:

H(<10, 10, 5>) = - (10/25) ln_2 10/25 - (10/25) ln_2 10/25 - (5/25) ln_2 5/25

Entropia si se separa por A:

H(<10, 10, 5>|Xa) = 22/25[ -8/22 ln_2 8/22 - 10/22 ln_2 10/22 - 4/22 ln_2 4/22] + 3/25[ -2/3 ln_2 2/3 - 0 * ln_2 0 - 1/3 ln_2 1/3]

H(<10, 10, 5>|Xb) = 14/25[ -1/2 ln 1/2 - 1/2 ln_2 1/2 - 0] + 5/25[ -1/5 ln_2 1/5 - 0 - 4/5 ln_2 4/5] + 6/25[ -1/3 ln_2 1/3 - 1/2 ln_2 1/2 - 1/6 ln_2 1/6]

La mayor ganancia de informacion a escoger es como la menor (?)
