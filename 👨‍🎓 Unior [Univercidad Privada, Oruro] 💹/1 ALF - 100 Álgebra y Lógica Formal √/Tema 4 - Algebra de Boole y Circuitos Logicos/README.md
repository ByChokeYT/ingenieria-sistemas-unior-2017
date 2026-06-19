# Tema 4: Álgebra de Boole y Circuitos Lógicos
## 🏫 Materia: Álgebra y Lógica Formal (ALF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 4.1 Variables y Operaciones Booleanas

El **álgebra de Boole** trabaja con variables que solo pueden tomar dos valores: 0 (falso) o 1 (verdadero). Es la base matemática de los circuitos digitales.

| Operación | Notación algebraica | Equivalente lógico |
|---|---|---|
| AND | A · B (o AB) | Conjunción ∧ |
| OR | A + B | Disyunción ∨ |
| NOT | A' o Ā | Negación ¬ |

##### 4.2 Postulados y Teoremas de Boole

| Ley | AND | OR |
|---|---|---|
| Identidad | A · 1 = A | A + 0 = A |
| Nulo | A · 0 = 0 | A + 1 = 1 |
| Idempotencia | A · A = A | A + A = A |
| Complemento | A · A' = 0 | A + A' = 1 |
| Conmutativa | A·B = B·A | A+B = B+A |
| Asociativa | (AB)C = A(BC) | (A+B)+C = A+(B+C) |
| Distributiva | A(B+C) = AB+AC | A+BC = (A+B)(A+C) |
| **De Morgan** | (AB)' = A'+B' | (A+B)' = A'B' |

##### 4.3 Compuertas Lógicas (Hardware)

| Compuerta | Símbolo eléctrico | Tabla de verdad | Expresión |
|---|---|---|---|
| **AND** | Compuerta en forma de D | 1 solo si ambas entradas son 1 | A·B |
| **OR** | Compuerta curva | 1 si al menos una entrada es 1 | A+B |
| **NOT** | Triángulo con círculo | Invierte la entrada | A' |
| **NAND** | AND + círculo (burbuja) | Inverso de AND | (A·B)' |
| **NOR** | OR + círculo (burbuja) | Inverso de OR | (A+B)' |
| **XOR** | OR con línea curva doble | 1 si las entradas son diferentes | A⊕B |
| **XNOR** | XOR + círculo | 1 si las entradas son iguales | (A⊕B)' |

> NAND y NOR son **compuertas universales**: con solo NAND (o solo NOR) se puede construir cualquier circuito lógico.

##### 4.4 Simplificación de Expresiones Booleanas

**Método algebraico:** aplicar los teoremas de Boole para reducir términos.

> *Ejemplo:* $AB + AB' = A(B+B') = A \cdot 1 = A$

**Mapas de Karnaugh:** método visual con tablas de 2, 4, 8 o 16 casillas que agrupa términos adyacentes (en potencias de 2: grupos de 1, 2, 4, 8...) para simplificar funciones booleanas sin usar álgebra paso a paso.

**Pasos para usar un Mapa de Karnaugh:**
1. Construir la tabla de verdad de la función.
2. Ubicar los 1s en el mapa según las combinaciones de variables.
3. Agrupar los 1s adyacentes en bloques de tamaño potencia de 2.
4. Escribir la expresión simplificada a partir de los grupos formados.

---

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **¿Qué son las compuertas universales y cuáles son en el diseño de circuitos?**
   * *Respuesta:* Son compuertas con las cuales se puede construir cualquier circuito o función lógica. Son NAND y NOR.
2. **Simplifique algebraicamente la expresión booleana $Y = A \cdot B + A \cdot B\prime$.**
   * *Respuesta:* $Y = A \cdot (B + B\prime) = A \cdot 1 = A$.
3. **¿Cuál es el valor binario de la salida de una compuerta XOR si sus entradas son $A = 1$ y $B = 1$?**
   * A) 1
   * B) 0
   * C) Z (alta impedancia)
   * D) Indefinido
   * *Respuesta correcta:* B) 0 (XOR da 1 solo si las entradas son diferentes).
4. **¿Cuál es la función de un Mapa de Karnaugh?**
   * *Respuesta:* Es una herramienta gráfica para simplificar funciones booleanas, reduciendo la cantidad de términos de forma visual mediante adyacencias lógicas.

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*