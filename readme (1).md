# Fractales en el plano complejo
En este proyecto se debe generar los puntos de un fractal similar a los de la siguiente figura. 
![alt text](assets/image.png)

# Descripción
El conjunto $F_s \in \mathbb{C}$ está conformado por los puntos $c\in \mathbb{C}$ para los cuales la [ecuación (1)](#1)  no diverge. 
$$
z_{(n+1)}=z_n^2+c \tag{1}
$$
usando la condición inicial $z_0=0$. 
Itere hasta que:
$$
|z_n |≥2 \tag{2}
$$

Asigne un color a cada punto $c$ del plano complejo dependiendo del número de iteraciones requeridas para cumplir con la condición dada. 


# Ejemplo
## Caso 1 
$c_1 = -1.8 -0.09i$

| $n$ | $c$ | $z_{n-1}$ | $z_{n}$ | $\|z_{n}\|$ | 
|:---:|:---:|:---:|:---:|:---:|
| 1 |$-1.8 -0.09i$ | $0$| $-1.8 - 0.09i$ | $1.8022$ |
| 2| $-1.8 -0.09i$ | $-1.8 - 0.09i$	| $ 1.4319 + 0.2340i  $ 		| $1.4509$ |
| 3| $-1.8 -0.09i$ | $ 1.4319 + 0.2340i  $ 	| $  0.1956 + 0.5801i $ | $0.6122$ |
| 4 |$-1.8 -0.09i$ | $  0.1956 + 0.5801i $ 	| $ -2.0983 + 0.1369i $ | $2.1028 \ge 2$  |

El punto $c_1$ tuvo 4 iteraciones hasta diverger. 

## Caso 2
$c_2 = -1.8 - 0.03i$

| $n$ | $c$ | $z_{n-1}$ | $z_{n}$ | $\|z_{n}\|$ | 
|:---:|:---:|:---:|:---:|:---:|
| 1 | $-1.8 - 0.03i$ | $0$ 	| $-1.8 - 0.03i$ | $1.8002$ |
| 2| $-1.8 - 0.03i$ |  $-1.8 - 0.03i$	| $ 1.4391 + 0.0780i$ | $1.4412$ |
| 3| $-1.8 - 0.03i$ | $ 1.4391 + 0.0780i$ 	| $  0.2649 + 0.1945i$ | $0.3287$ |
| 4| $-1.8 - 0.03i$ | $  0.2649 + 0.1945i$ 	| $ -1.7676 + 0.0731i$ | $1.7692$ |
| 5| $-1.8 - 0.03i$ | $ -1.7676 + 0.0731i$ 	| $  1.3192 - 0.2883i$ | $1.3504$ |
| 6| $-1.8 - 0.03i$ | $  1.3192 - 0.2883i$ 	| $ -0.1427 - 0.7906i$ | $0.8034$ |
| 7 | $-1.8 - 0.03i$ | $ -0.1427 - 0.7906i$ 	| $ -2.4047 + 0.1957i$ | $2.4126 \ge 2$  |

## Caso 3
$c_3 = 0.1 + 0.01i$

| $n$ | $c$ | $z_{n-1}$ | $z_{n}$ | $\|z_{n}\|$ | 
|:---:|:---:|:---:|:---:|:---:|
| 1|$	0.1 + 0.01i $ | $0$ 						| $ 0.1 + 0.01i $ | $ 0.1005 $ |
| 2| $	0.1 + 0.01i $ | $ 0.1 + 0.01i $ | $ 0.1099 + 0.0120i $			| $ 0.1106 $ |
| 3| $	0.1 + 0.01i $ | $ 0.1099 + 0.0120i $ | $ 0.1119 + 0.0126i $ 	| $ 0.1126 $ |
| 4| $	0.1 + 0.01i $ | $ 0.1119 + 0.0126i $ | $ 0.1124 + 0.0128i $ 	| $ 0.1131 $ |
| 5| $	0.1 + 0.01i $ | $ 0.1124 + 0.0128i $ | $ 0.1125 + 0.0129i $ 	| $ 0.1132 $ |
| 6| $	0.1 + 0.01i $ | $ 0.1125 + 0.0129i $ | $ 0.1125 + 0.0129i $ 	| $ 0.1132 $ |
| 7| $	0.1 + 0.01i $ | $ 0.1125 + 0.0129i $ | $ 0.1125 + 0.0129i $ 	| $ 0.1132 $ |

Observe que a partir de la iteración 5 el término $z_n$ no se modifica, por lo que el punto $c_3$ no diverge. Este punto pertenece al conjunto $F_s$. 

* Tenga en cuenta que el conjunto $F_s$ es un conjunto fractal, por lo que la frontera entre los puntos que divergen y los que no divergen es fractal.


# Objetivos del Proyecto
+ Calcular los puntos de un fractal:
	* Realizar el cálculo del número de iteraciones para todos los puntos $c \in \mathbb{C}$. 
	* Colorear cada punto de acuerdo al número de iteraciones hasta diverger.
+ Dominar técnicas de los métodos numéricos para asegurar una alta exactitud.
+ Visualizar el fractal resultante.

# Requerimientos
+ Se debe poder hacer zoom interactivamente, y la figura debe redibujarse. 

## Consejos para la implementación
+ Cree una cuadrícula de puntos complejos en el plano.
+ Para cada punto $c$, itere la secuencia $z_n$ hasta que alcance un límite o diverja.
+ Cuente el número de iteraciones antes de la divergencia y asigne un color según este valor.
+ Cada píxel en la imagen corresponderá a un punto en la cuadrícula.
+ Asigne diferentes colores según el número de iteraciones (se recomienda usar la función $ln$).
# Experimentación
+ Ajuste los parámetros (resolución, límites, colores) para explorar diferentes regiones del fractal. 
+	Muestre el resultado en los rangos:
	
	1. $-2.25<x<1.25, -1.5<y<1.5 $

	1. $-1.943,<x<-1.94, -0.0012<y<0.0012 $



	1. $-1.764<x< -1.7527, -0.01925<y<-0.0109 $

	1. $-1.768562608<x<-1.7685626045, -0.000790008<y<-0.000790005 $

+ Realice una animación y hacer zoom en cada rango dado.

## Preguntas de análisis
* ¿Cómo afecta la resolución de la cuadrícula al resultado visual?
* ¿Cuál es la resolución máxima de su programa?



https://github.com/user-attachments/assets/205c150e-1e80-47cf-bc19-bac252de7ea4


<video controls  loop autoplay src="assets/video_fractal.mp4" title="Title"></video>
