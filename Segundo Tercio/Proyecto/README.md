# Proyecto de Teoría Cuántica Clásica

**Este proyecto contiene un Jupyter Notebook en la carpeta que esta este README** que explora varios conceptos y ejercicios relacionados con la teoría cuántica clásica. A continuación se describen los contenidos del notebook.

## Contenido

### Simule el primer sistema cuántico descrito en la sección 4.1

El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea. El simulador debe permitir especificar el número de posiciones y un vector ket de estado asignando las amplitudes.

1. El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.

2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.

### Retos de programacion del capitulo 4

1. Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar del uno al otro después de hacer la observación.

2. Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.

3. El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.

4. Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a partir de un estado inicial.

### Exercice 4.3.1

Find all the possible state of a particle in initial spin up. Apply $S_x$ to it and determine the probability that the resulting state is still spin up.

Se deben tener claros los siguientes conceptos:

$$
|\uparrow \rangle = \begin{bmatrix}
1 \\
0 \\
\end{bmatrix}
$$

$$
S_x = \frac{\hbar}{2} \cdot \begin{bmatrix}
0 & 1\\
1 & 0\\
\end{bmatrix}
$$

### Ejercicio 4.4.1

Verifica que las siguientes matrices unitarias son correctas:

$$
U_1 = \begin{bmatrix}
    0 & 1\\
    1 & 0
\end{bmatrix}
$$

y

$$
U_2 = \begin{bmatrix}
    \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \\
    \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\
\end{bmatrix}
$$

### Exercise 4.4.1

Verify that

$$
U_1 = \begin{bmatrix}
    0 & 1\\
    1 & 0\\
\end{bmatrix}
$$

and
$$
U_2 = \begin{bmatrix}
\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2}\\
\frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2}\\
\end{bmatrix}
$$

are unitary matrices. Multiply them and verify that their product is also unitary.

Para realizar este ejercicio se debe tener en cuenta los conseptos de que es una matriz unitaria. Una matriz unitaria es aquella que al realizar el producto entre su adjunta y ella misma el resultado es la matriz identidad como se puede ver a continuación.

$$
U^{\dagger} \cdot U = I
$$


### Exercise 4.4.2

Go back to Example 3.3.2, keep the same initial state vector $\begin{bmatrix}1 & 0 & 0 & 0\end{bmatrix}^{T}$, but change the unitary map to

$$
A = \begin{bmatrix}
0 & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0\\
\frac{i}{\sqrt{2}} & 0 & 0 & \frac{1}{\sqrt{2}}\\
\frac{1}{\sqrt{2}} & 0 & 0 & \frac{i}{\sqrt{2}}\\
0 & \frac{1}{\sqrt{2}} & \frac{-1}{\sqrt{2}} & 0\\
\end{bmatrix}
$$

Determine the state of the system after three times steps. What is the change of the quantum ball to be found at point 3?

### Exercise 4.5.2

Write down the generic state vector for the system of two particles with spin. Generalize it to a system with $n$ particles

### Exercise 4.5.3

Assume the same scenario as in Example 4.5.2 an let 

$$
|\phi\rangle = |x_0\rangle \otimes |y_1 \rangle + |x_1\rangle \otimes |y_1\rangle
$$

Is this state separable?

## Como ejecutar los ejercicios y librerias

### Requisitos

- Jupyter Notebook
- Kernel de Python
- Bibliotecas Numpy de Python

Para poder revisar los ejercicios propuestos diríjase a el documento Jupyter que esta en la carpeta donde esta localizado este archivo README y siga las siguientes recomendaciones

### Parte 1

Para la primera parte de este proyecto se realizo un solo código el cual primeramente se tiene que dar el numero de elementos de o de los vectores, seguidamente se preguntara la parte real y parte imaginaria donde se tendrá que colocar los coeficientes correspondientes, después el programa preguntara en que posición deseas saber la probabilidad, el sistema te otorgara una respuesta. Posteriormente, el programa te pregunta si deseas añadir otro vector, donde se tiene que responder con un 's' o 'n', en el caso de 'n' el código terminara, en dado caso que 's' entonces el sistema te calculara la probabilidad de pasar de un ket a el otro ket.

### Parte 2

En esta parte se realizaron códigos por separado, los cuales te preguntara la dimensión del sistema o por los elementos del ket, después se tiene que llenar todos los datos solicitados del sistema para obtener un resultado, tenga en cuenta que para la parte del real e imaginario solo tiene que colocar los coeficientes correspondientes.

### Parte 3 (Problemas)

En esta sección solo es ejecutar el programa, es decir que el programa no te solicitara ningún dato y arrojara el resultado de lo pedido en el ejercicio. Se hizo el respectivo análisis para cada uno de los ejercicios.
