# 📐 Álgebra y Lógica Formal — ALF-100

## 🏫 Universidad Privada de Oruro (UNIOR)
### 💻 Carrera: Ingeniería de Sistemas

---

### 📊 Ficha Técnica de la Asignatura

| Campo | Detalle |
|---|---|
| **Sigla** | ALF-100 |
| **Semestre** | 1º Semestre |
| **Prerrequisitos** | Ninguno |
| **Estado** | 🟢 Aprobada |

### 📝 Descripción de la Materia

Introducción a las matemáticas discretas, lógica proposicional, teoría de conjuntos y estructuras algebraicas, base fundamental para el razonamiento computacional, el diseño de algoritmos y la arquitectura digital.

---

## 🗺️ Ruta de Aprendizaje Completa

---

## 📂 TEMA 1: Lógica Proposicional y Tablas de Verdad

### 1.1 Proposiciones

Una **proposición** es un enunciado que puede calificarse como verdadero (V) o falso (F), pero no ambos a la vez.

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Atómica (simple)** | No contiene conectivos lógicos | "La Paz es la sede de gobierno" |
| **Molecular (compuesta)** | Combina proposiciones con conectivos | "Llueve y hace frío" |

> No son proposiciones las preguntas, órdenes o exclamaciones: "¿Qué hora es?" no es una proposición.

### 1.2 Conectivos Lógicos

| Conectivo | Símbolo | Nombre | Se lee | Verdadero cuando... |
|---|---|---|---|---|
| Negación | ¬p | NOT | "no p" | p es falso |
| Conjunción | p ∧ q | AND | "p y q" | ambas son verdaderas |
| Disyunción | p ∨ q | OR | "p o q" | al menos una es verdadera |
| Disyunción exclusiva | p ⊕ q | XOR | "p o q, no ambas" | exactamente una es verdadera |
| Implicación (condicional) | p → q | IF...THEN | "si p, entonces q" | excepto cuando p=V y q=F |
| Doble implicación | p ↔ q | IFF | "p si y solo si q" | ambas tienen el mismo valor |

### 1.3 Tablas de Verdad

**Tabla de los conectivos básicos:**

| p | q | ¬p | p∧q | p∨q | p⊕q | p→q | p↔q |
|---|---|---|---|---|---|---|---|
| V | V | F | V | V | F | V | V |
| V | F | F | F | V | V | F | F |
| F | V | V | F | V | V | V | F |
| F | F | V | F | F | F | V | V |

**Número de filas:** con $n$ proposiciones simples, la tabla tiene $2^n$ filas.

### 1.4 Tautologías, Contradicciones y Contingencias

| Tipo | Definición | Ejemplo |
|---|---|---|
| **Tautología** | Siempre verdadera, sin importar los valores de verdad | p ∨ ¬p |
| **Contradicción** | Siempre falsa | p ∧ ¬p |
| **Contingencia** | A veces verdadera, a veces falsa | p → q |

### 1.5 Leyes del Álgebra Proposicional

| Ley | Expresión |
|---|---|
| Doble negación | ¬(¬p) ≡ p |
| Idempotencia | p ∧ p ≡ p ; p ∨ p ≡ p |
| Conmutativa | p ∧ q ≡ q ∧ p ; p ∨ q ≡ q ∨ p |
| Asociativa | (p∧q)∧r ≡ p∧(q∧r) |
| Distributiva | p∧(q∨r) ≡ (p∧q)∨(p∧r) |
| De Morgan | ¬(p∧q) ≡ ¬p∨¬q ; ¬(p∨q) ≡ ¬p∧¬q |
| Implicación material | p→q ≡ ¬p∨q |

### 1.6 Razonamiento Lógico — Reglas de Inferencia

| Regla | Estructura | Ejemplo |
|---|---|---|
| **Modus Ponens** | p→q, p ⊢ q | Si llueve, me mojo. Llueve. ∴ Me mojo. |
| **Modus Tollens** | p→q, ¬q ⊢ ¬p | Si llueve, me mojo. No me mojé. ∴ No llovió. |
| **Silogismo hipotético** | p→q, q→r ⊢ p→r | Cadena de implicaciones |
| **Silogismo disyuntivo** | p∨q, ¬p ⊢ q | Es A o B. No es A. ∴ Es B. |

---

## 📂 TEMA 2: Teoría de Conjuntos

### 2.1 Definición de Conjuntos

Un **conjunto** es una colección bien definida de objetos llamados elementos.

| Forma de definir | Notación | Ejemplo |
|---|---|---|
| **Por extensión** | Se listan los elementos | A = {2, 4, 6, 8} |
| **Por comprensión** | Se describe una propiedad | A = {x \| x es par, 0<x<10} |

**Notación de pertenencia:** $a \in A$ (a pertenece a A), $a \notin A$ (a no pertenece a A).

### 2.2 Tipos de Conjuntos

| Tipo | Descripción | Ejemplo |
|---|---|---|
| Vacío | No tiene elementos | ∅ o {} |
| Unitario | Tiene un solo elemento | {5} |
| Finito | Número limitado de elementos | {1,2,3} |
| Infinito | Número ilimitado de elementos | Números naturales ℕ |
| Universal | Contiene a todos los elementos del contexto | U |

### 2.3 Conjunto Potencia

El **conjunto potencia** P(A) es el conjunto de todos los subconjuntos posibles de A, incluyendo el vacío y A mismo.

$$|P(A)| = 2^n \text{, donde } n = |A|$$

> *Ejemplo:* Si A = {1, 2}, entonces P(A) = {∅, {1}, {2}, {1,2}} → tiene $2^2=4$ elementos.

### 2.4 Operaciones entre Conjuntos

| Operación | Símbolo | Definición | Diagrama de Venn |
|---|---|---|---|
| **Unión** | A ∪ B | Elementos en A o en B (o ambos) | Ambos círculos sombreados |
| **Intersección** | A ∩ B | Elementos en A y en B | Solo zona compartida |
| **Diferencia** | A − B | Elementos en A pero no en B | Solo A, sin la parte de B |
| **Complemento** | A' o Aᶜ | Elementos del universo que no están en A | Todo excepto A |
| **Diferencia simétrica** | A △ B | Elementos en A o B, pero no en ambos | (A∪B) − (A∩B) |

### 2.5 Propiedades de las Operaciones

- **Leyes de De Morgan:** $(A \cup B)' = A' \cap B'$ ; $(A \cap B)' = A' \cup B'$
- **Distributivas:** $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
- **Conmutativas:** $A \cup B = B \cup A$
- **Asociativas:** $(A \cup B) \cup C = A \cup (B \cup C)$

### 2.6 Producto Cartesiano

$$A \times B = \{(a,b) \mid a \in A, b \in B\}$$

> *Ejemplo:* Si A={1,2} y B={x,y}, entonces A×B = {(1,x),(1,y),(2,x),(2,y)}

---

## 📂 TEMA 3: Relaciones y Funciones Discretas

### 3.1 Relaciones Binarias

Una **relación binaria** R de A en B es cualquier subconjunto del producto cartesiano $A \times B$.

### 3.2 Propiedades de las Relaciones (en un conjunto A)

| Propiedad | Definición | Ejemplo |
|---|---|---|
| **Reflexiva** | ∀a∈A: (a,a)∈R | "es igual a" |
| **Simétrica** | Si (a,b)∈R entonces (b,a)∈R | "es hermano de" |
| **Antisimétrica** | Si (a,b)∈R y (b,a)∈R entonces a=b | "es menor o igual que" |
| **Transitiva** | Si (a,b)∈R y (b,c)∈R entonces (a,c)∈R | "es ancestro de" |

**Relación de equivalencia:** cumple reflexiva + simétrica + transitiva (ej: "tiene la misma edad que").
**Relación de orden:** cumple reflexiva + antisimétrica + transitiva (ej: "≤").

### 3.3 Funciones

Una **función** f: A → B asigna a cada elemento de A exactamente un elemento de B.

| Tipo | Definición | ¿Cómo verificarlo? |
|---|---|---|
| **Inyectiva (1 a 1)** | Elementos distintos del dominio tienen imágenes distintas | Ningún elemento de B recibe dos flechas |
| **Sobreyectiva (sobre)** | Todo elemento de B tiene al menos una preimagen | Todos los elementos de B son alcanzados |
| **Biyectiva** | Es inyectiva y sobreyectiva a la vez | Correspondencia uno a uno perfecta, admite función inversa |

### 3.4 Composición de Funciones

$$(f \circ g)(x) = f(g(x))$$

Primero se aplica $g$, luego $f$ al resultado.

---

## 📂 TEMA 4: Álgebra de Boole y Circuitos Lógicos

### 4.1 Variables y Operaciones Booleanas

El **álgebra de Boole** trabaja con variables que solo pueden tomar dos valores: 0 (falso) o 1 (verdadero). Es la base matemática de los circuitos digitales.

| Operación | Notación algebraica | Equivalente lógico |
|---|---|---|
| AND | A · B (o AB) | Conjunción ∧ |
| OR | A + B | Disyunción ∨ |
| NOT | A' o Ā | Negación ¬ |

### 4.2 Postulados y Teoremas de Boole

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

### 4.3 Compuertas Lógicas (Hardware)

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

### 4.4 Simplificación de Expresiones Booleanas

**Método algebraico:** aplicar los teoremas de Boole para reducir términos.

> *Ejemplo:* $AB + AB' = A(B+B') = A \cdot 1 = A$

**Mapas de Karnaugh:** método visual con tablas de 2, 4, 8 o 16 casillas que agrupa términos adyacentes (en potencias de 2: grupos de 1, 2, 4, 8...) para simplificar funciones booleanas sin usar álgebra paso a paso.

**Pasos para usar un Mapa de Karnaugh:**
1. Construir la tabla de verdad de la función.
2. Ubicar los 1s en el mapa según las combinaciones de variables.
3. Agrupar los 1s adyacentes en bloques de tamaño potencia de 2.
4. Escribir la expresión simplificada a partir de los grupos formados.

---

## 📂 TEMA 5: Teoría de Grafos e Inducción Matemática

### 5.1 Conceptos Básicos de Grafos

Un **grafo** G = (V, E) está formado por un conjunto de **vértices** (V) y un conjunto de **aristas** (E) que conectan pares de vértices.

| Tipo de Grafo | Descripción |
|---|---|
| **No dirigido** | Las aristas no tienen dirección (A-B = B-A) |
| **Dirigido (dígrafo)** | Las aristas tienen dirección (A→B ≠ B→A) |
| **Ponderado** | Las aristas tienen un peso o costo asociado |
| **Simple** | Sin lazos ni aristas múltiples entre el mismo par de vértices |
| **Completo** | Todos los vértices están conectados entre sí |

### 5.2 Conceptos Clave

- **Grado de un vértice:** número de aristas que llegan o salen de él.
- **Camino:** secuencia de vértices conectados por aristas, sin repetir vértices.
- **Ciclo:** camino que empieza y termina en el mismo vértice.
- **Conectividad:** un grafo es conexo si existe un camino entre cualquier par de vértices.

### 5.3 Representación Matricial de Grafos

**Matriz de adyacencia:** matriz $n \times n$ donde la celda $(i,j) = 1$ si existe arista entre el vértice $i$ y el vértice $j$, y $0$ si no.

| | A | B | C |
|---|---|---|---|
| **A** | 0 | 1 | 1 |
| **B** | 1 | 0 | 0 |
| **C** | 1 | 0 | 0 |

> Este grafo de ejemplo tiene a A conectado con B y con C, pero B y C no están conectados entre sí.

### 5.4 Inducción Matemática

La **inducción matemática** es un método de demostración para afirmaciones que dependen de un número natural $n$.

**Pasos del principio de inducción:**

1. **Caso base:** demostrar que la afirmación es verdadera para $n=1$ (o el primer valor del dominio).
2. **Paso inductivo:** suponer que es verdadera para $n=k$ (hipótesis inductiva) y demostrar que entonces también es verdadera para $n=k+1$.
3. **Conclusión:** si ambos pasos se cumplen, la afirmación es verdadera para todo $n$ natural.

> *Ejemplo clásico:* demostrar que $1+2+3+\dots+n = \frac{n(n+1)}{2}$ para todo $n \geq 1$, verificando el caso base $n=1$ y luego el paso inductivo de $k$ a $k+1$.

---

## 📂 TEMA 6: Máquinas de Estado y Lenguajes Formales

### 6.1 Autómatas Finitos

Un **autómata finito** es un modelo matemático que representa un sistema con un número finito de estados, usado para reconocer patrones y procesar lenguajes formales.

| Tipo | Característica |
|---|---|
| **DFA** (Determinista) | Para cada estado y símbolo de entrada, hay exactamente una transición posible |
| **NFA** (No determinista) | Puede haber cero, una o varias transiciones posibles para el mismo símbolo |

**Componentes de un autómata finito:** $M = (Q, \Sigma, \delta, q_0, F)$

- $Q$: conjunto finito de estados
- $\Sigma$: alfabeto de símbolos de entrada
- $\delta$: función de transición
- $q_0$: estado inicial
- $F$: conjunto de estados finales (de aceptación)

### 6.2 Gramáticas Formales

Una **gramática formal** $G = (V, T, P, S)$ define las reglas de producción que generan las cadenas válidas de un lenguaje:

- $V$: símbolos no terminales (variables)
- $T$: símbolos terminales (alfabeto)
- $P$: reglas de producción
- $S$: símbolo inicial

**Jerarquía de Chomsky (clasificación de gramáticas):**

| Tipo | Nombre | Reconocida por |
|---|---|---|
| Tipo 0 | Sin restricciones | Máquina de Turing |
| Tipo 1 | Sensible al contexto | Autómata linealmente acotado |
| Tipo 2 | Libre de contexto | Autómata de pila |
| Tipo 3 | Regular | Autómata finito |

### 6.3 Expresiones Regulares

Las **expresiones regulares** son patrones que describen conjuntos de cadenas de texto, ampliamente usadas en programación para validación y búsqueda de texto.

| Símbolo | Significado | Ejemplo |
|---|---|---|
| `*` | Cero o más repeticiones | `a*` → "", "a", "aa", "aaa"... |
| `+` | Una o más repeticiones | `a+` → "a", "aa", "aaa"... |
| `?` | Cero o una repetición (opcional) | `a?` → "" o "a" |
| `\|` | Alternancia (o) | `a\|b` → "a" o "b" |
| `.` | Cualquier carácter | `a.c` → "abc", "axc"... |

> Las expresiones regulares son equivalentes en poder de reconocimiento a los autómatas finitos: todo lo que reconoce un DFA puede expresarse como una expresión regular, y viceversa.

---

## 🎯 Ponderación y Control de Calificaciones

| Actividad Evaluativa | Ponderación | Nota Obtenida |
|---|---|---|
| **Examen Primer Parcial** | 30% | `__ / 100` |
| **Examen Segundo Parcial** | 30% | `__ / 100` |
| **Examen Final / Proyecto** | 30% | `__ / 100` |
| **Tareas y Prácticas** | 10% | `__ / 100` |
| **Nota Final** | **100%** | **`__ / 100`** |

---

## 📅 Cronograma de Fechas Importantes

- [ ] **Examen Primer Parcial:** *Fecha: **/**/*________
- [ ] **Examen Segundo Parcial:** *Fecha: **/**/*________
- [ ] **Entrega de Proyecto/Trabajo Final:** *Fecha: **/**/*________
- [ ] **Examen Final:** *Fecha: **/**/*________

---

## 📂 Archivos en esta Carpeta

- 📄 [TEMA N° 1 Algebla I.docx](./TEMA%20N%C2%B0%201%20Algebla%20I.docx)

---

*Documento enriquecido para el control de estudios del Ing. José Luis Choquevilca — UNIOR 2017*
