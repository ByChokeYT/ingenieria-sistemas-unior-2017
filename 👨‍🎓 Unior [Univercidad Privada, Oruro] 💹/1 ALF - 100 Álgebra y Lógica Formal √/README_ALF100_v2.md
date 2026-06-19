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

Introducción a las matemáticas discretas, lógica proposicional, teoría de conjuntos y estructuras algebraicas, base fundamental para el razonamiento computacional, el diseño de algoritmos, las bases de datos (álgebra relacional) y la arquitectura digital (circuitos lógicos).

---

## 🗺️ Ruta de Aprendizaje Completa

---

## 📂 TEMA 1: Lógica Proposicional y Tablas de Verdad

### 1.1 Proposiciones

Una **proposición** es un enunciado declarativo que puede calificarse como verdadero (V/1) o falso (F/0), pero nunca ambos a la vez, y nunca ninguno.

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Atómica (simple)** | No contiene conectivos lógicos | p: "La Paz es la sede de gobierno" |
| **Molecular (compuesta)** | Combina proposiciones con conectivos | p∧q: "Llueve y hace frío" |

**NO son proposiciones:**
- Preguntas: "¿Qué hora es?"
- Órdenes/exclamaciones: "¡Cierra la puerta!"
- Enunciados ambiguos o de opinión sin valor de verdad objetivo: "El helado de chocolate es el mejor"

### 1.2 Conectivos Lógicos (Operadores)

| Conectivo | Símbolo | Nombre | Se lee | Verdadero cuando... |
|---|---|---|---|---|
| Negación | ¬p | NOT | "no p" | p es falso |
| Conjunción | p ∧ q | AND | "p y q" | ambas son verdaderas |
| Disyunción inclusiva | p ∨ q | OR | "p o q" | al menos una es verdadera |
| Disyunción exclusiva | p ⊕ q | XOR | "p o q, no ambas" | exactamente una es verdadera |
| Implicación (condicional) | p → q | IF...THEN | "si p, entonces q" | excepto cuando p=V y q=F |
| Doble implicación | p ↔ q | IFF | "p si y solo si q" | ambas tienen el mismo valor de verdad |

### 1.3 Tabla de Verdad Completa

| p | q | ¬p | p∧q | p∨q | p⊕q | p→q | p↔q |
|---|---|---|---|---|---|---|---|
| V | V | F | V | V | F | V | V |
| V | F | F | F | V | V | F | F |
| F | V | V | F | V | V | V | F |
| F | F | V | F | F | F | V | V |

**Regla del número de filas:** con $n$ proposiciones simples distintas, la tabla tiene $2^n$ filas.
> Con 3 proposiciones (p, q, r) → $2^3 = 8$ filas.

### 1.4 Construyendo una Tabla de Verdad para una Proposición Compleja

> *Ejemplo resuelto:* Construir la tabla de $(p \to q) \land (\lnot p \lor r)$

| p | q | r | p→q | ¬p | ¬p∨r | (p→q)∧(¬p∨r) |
|---|---|---|---|---|---|---|
| V | V | V | V | F | V | V |
| V | V | F | V | F | F | F |
| V | F | V | F | F | V | F |
| V | F | F | F | F | F | F |
| F | V | V | V | V | V | V |
| F | V | F | V | V | V | V |
| F | F | V | V | V | V | V |
| F | F | F | V | V | V | V |

**Pasos para resolverlo:**
1. Listar todas las combinaciones posibles de p, q, r ($2^3=8$ filas).
2. Resolver primero los subexpresiones más simples (p→q, ¬p).
3. Combinar columnas intermedias hasta llegar a la expresión final.

### 1.5 Tautologías, Contradicciones y Contingencias

| Tipo | Definición | Ejemplo |
|---|---|---|
| **Tautología** | Siempre verdadera, sin importar los valores de verdad | p ∨ ¬p (Ley del tercio excluido) |
| **Contradicción** | Siempre falsa | p ∧ ¬p (Ley de no contradicción) |
| **Contingencia** | A veces verdadera, a veces falsa | p → q |

> *Comprobación de que p ∨ ¬p es tautología:*

| p | ¬p | p∨¬p |
|---|---|---|
| V | F | **V** |
| F | V | **V** |

Como la última columna es siempre V, es una **tautología**.

### 1.6 Leyes del Álgebra Proposicional

| Ley | Expresión |
|---|---|
| Doble negación | ¬(¬p) ≡ p |
| Idempotencia | p∧p ≡ p ; p∨p ≡ p |
| Conmutativa | p∧q ≡ q∧p ; p∨q ≡ q∨p |
| Asociativa | (p∧q)∧r ≡ p∧(q∧r) |
| Distributiva | p∧(q∨r) ≡ (p∧q)∨(p∧r) |
| **De Morgan** | ¬(p∧q) ≡ ¬p∨¬q ; ¬(p∨q) ≡ ¬p∧¬q |
| Implicación material | p→q ≡ ¬p∨q |
| Contrapositiva | p→q ≡ ¬q→¬p |
| Absorción | p∧(p∨q) ≡ p ; p∨(p∧q) ≡ p |

> *Ejemplo de simplificación aplicando leyes:*
> Simplificar: $\lnot(p \land q) \lor (p \land q)$
> Aplicando De Morgan: $(\lnot p \lor \lnot q) \lor (p \land q)$
> Esta expresión es en realidad una **tautología** de la forma $X \lor \lnot X$ donde $X = p\land q$, por lo tanto siempre es V.

### 1.7 Razonamiento Lógico — Reglas de Inferencia

| Regla | Estructura formal | Ejemplo en lenguaje natural |
|---|---|---|
| **Modus Ponens** | p→q, p ⊢ q | "Si llueve, me mojo. Llueve. ∴ Me mojo." |
| **Modus Tollens** | p→q, ¬q ⊢ ¬p | "Si llueve, me mojo. No me mojé. ∴ No llovió." |
| **Silogismo hipotético** | p→q, q→r ⊢ p→r | "Si estudio, apruebo. Si apruebo, me gradúo. ∴ Si estudio, me gradúo." |
| **Silogismo disyuntivo** | p∨q, ¬p ⊢ q | "Es de día o de noche. No es de día. ∴ Es de noche." |
| **Adición** | p ⊢ p∨q | De una verdad, se puede agregar cualquier disyunción |
| **Simplificación** | p∧q ⊢ p | De una conjunción, se puede extraer cualquiera de sus partes |

### 1.8 Falacias Lógicas Comunes (errores de razonamiento)

| Falacia | Error | Ejemplo |
|---|---|---|
| **Afirmación del consecuente** | De p→q y q, concluir p (inválido) | "Si llueve, hay nubes. Hay nubes. ∴ Llueve." (falso: podría estar nublado sin llover) |
| **Negación del antecedente** | De p→q y ¬p, concluir ¬q (inválido) | "Si llueve, hay nubes. No llueve. ∴ No hay nubes." (falso: puede haber nubes sin lluvia) |

---

## 📂 TEMA 2: Teoría de Conjuntos

### 2.1 Definición de Conjuntos

Un **conjunto** es una colección bien definida de objetos (elementos), sin importar el orden ni repeticiones.

| Forma de definir | Notación | Ejemplo |
|---|---|---|
| **Por extensión** | Se listan los elementos | A = {2, 4, 6, 8} |
| **Por comprensión** | Se describe una propiedad que cumplen los elementos | A = {x \| x es par, 0<x<10} |

**Notación:** $a \in A$ (a pertenece a A); $a \notin A$ (a no pertenece a A); $A \subseteq B$ (A es subconjunto de B); $|A|$ (cardinalidad: número de elementos de A).

### 2.2 Tipos de Conjuntos

| Tipo | Descripción | Ejemplo |
|---|---|---|
| Vacío | No tiene elementos | ∅ = {} |
| Unitario | Tiene un solo elemento | {5} |
| Finito | Número limitado de elementos | {1,2,3} |
| Infinito | Número ilimitado de elementos | ℕ = {1,2,3,...} |
| Universal | Contiene a todos los elementos del contexto en estudio | U |
| Disjuntos | Dos conjuntos sin elementos en común | A∩B = ∅ |

### 2.3 Conjunto Potencia

El **conjunto potencia** $P(A)$ es el conjunto formado por TODOS los subconjuntos posibles de A, incluyendo el conjunto vacío y A mismo.

$$|P(A)| = 2^n \text{, donde } n = |A|$$

> *Ejemplo resuelto:* Si A = {1, 2, 3}, entonces $n=3$ y $|P(A)| = 2^3 = 8$.
>
> $P(A) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\}\}$

### 2.4 Operaciones entre Conjuntos (con ejemplos resueltos)

Sea $U = \{1,2,3,4,5,6,7,8,9,10\}$, $A=\{1,2,3,4,5\}$, $B=\{4,5,6,7,8\}$

| Operación | Símbolo | Definición | Resultado del ejemplo |
|---|---|---|---|
| **Unión** | A ∪ B | Elementos en A o en B (o ambos) | {1,2,3,4,5,6,7,8} |
| **Intersección** | A ∩ B | Elementos en A y en B | {4,5} |
| **Diferencia** | A − B | Elementos en A pero no en B | {1,2,3} |
| **Diferencia** | B − A | Elementos en B pero no en A | {6,7,8} |
| **Complemento** | A' | Elementos del universo que no están en A | {6,7,8,9,10} |
| **Diferencia simétrica** | A △ B | (A∪B) − (A∩B) | {1,2,3,6,7,8} |

### 2.5 Leyes de De Morgan para Conjuntos

$$(A \cup B)' = A' \cap B'$$
$$(A \cap B)' = A' \cup B'$$

> *Verificación con el ejemplo anterior:*
> $A' = \{6,7,8,9,10\}$, $B' = \{1,2,3,9,10\}$
> $A' \cap B' = \{9,10\}$
> $(A\cup B)' = \{1,...,8\}' = \{9,10\}$ ✓ Coinciden, la ley se cumple.

### 2.6 Producto Cartesiano

$$A \times B = \{(a,b) \mid a \in A, b \in B\}$$

> *Ejemplo:* Si A={1,2} y B={x,y}, entonces:
> $A \times B = \{(1,x),(1,y),(2,x),(2,y)\}$ → tiene $|A| \times |B| = 2\times2=4$ pares ordenados.

### 2.7 Diagramas de Venn — Representación Gráfica

```
        U
   ┌─────────────────┐
   │   A        B     │
   │ ┌───┐    ┌───┐   │
   │ │ 1 │┌──┐│ 6 │   │
   │ │ 2 ││4,5││ 7 │   │
   │ │ 3 │└──┘│ 8 │   │
   │ └───┘    └───┘   │
   │      9, 10        │
   └─────────────────┘
```
La zona compartida entre los dos círculos representa $A \cap B = \{4,5\}$.

---

## 📂 TEMA 3: Relaciones y Funciones Discretas

### 3.1 Relaciones Binarias

Una **relación binaria** R de A en B es cualquier subconjunto del producto cartesiano $A \times B$: $R \subseteq A \times B$.

> *Ejemplo:* Sea A = {1,2,3} y la relación R = "es menor que" definida en A:
> $R = \{(1,2),(1,3),(2,3)\}$

### 3.2 Propiedades de las Relaciones (definidas en un conjunto A)

| Propiedad | Definición formal | Ejemplo cotidiano | ¿Se cumple en "≤" sobre ℕ? |
|---|---|---|---|
| **Reflexiva** | ∀a∈A: (a,a)∈R | "es igual a" | Sí (a≤a siempre) |
| **Simétrica** | Si (a,b)∈R entonces (b,a)∈R | "es hermano de" | No (si a≤b no implica b≤a) |
| **Antisimétrica** | Si (a,b)∈R y (b,a)∈R entonces a=b | "es menor o igual que" | Sí |
| **Transitiva** | Si (a,b)∈R y (b,c)∈R entonces (a,c)∈R | "es ancestro de" | Sí |

### 3.3 Relación de Equivalencia vs. Relación de Orden

| Tipo | Propiedades que cumple | Ejemplo |
|---|---|---|
| **Relación de equivalencia** | Reflexiva + Simétrica + Transitiva | "Tiene la misma edad que", "≡ (mod n)" |
| **Relación de orden** | Reflexiva + Antisimétrica + Transitiva | "≤", "es subconjunto de (⊆)" |

> *Ejemplo de clases de equivalencia:* La relación "tiene el mismo resto al dividir por 3" sobre los números enteros divide a todos los enteros en exactamente 3 clases: {...,-3,0,3,6,...}, {...,-2,1,4,7,...}, {...,-1,2,5,8,...}

### 3.4 Funciones

Una **función** $f: A \to B$ asigna a **cada** elemento de A **exactamente un** elemento de B (no puede faltar ninguno, ni tener dos imágenes).

| Tipo | Definición | Verificación visual | Ejemplo |
|---|---|---|---|
| **Inyectiva (1 a 1)** | Elementos distintos del dominio tienen imágenes distintas | Ningún elemento de B recibe dos flechas | $f(x)=x+1$ en ℝ |
| **Sobreyectiva (sobre)** | Todo elemento de B tiene al menos una preimagen | Todos los elementos de B son alcanzados | $f(x)=x^3$ en ℝ |
| **Biyectiva** | Es inyectiva y sobreyectiva a la vez | Correspondencia exacta uno a uno | $f(x)=2x$ en ℝ |

> *Ejemplo:* $f(x) = x^2$ definida de ℝ a ℝ **NO es inyectiva** porque $f(2)=f(-2)=4$ (dos elementos del dominio tienen la misma imagen), y **NO es sobreyectiva** porque ningún número negativo de B tiene preimagen real.

### 3.5 Composición de Funciones

$$(f \circ g)(x) = f(g(x))$$

> *Ejemplo resuelto:* Si $f(x) = x+1$ y $g(x) = x^2$, entonces:
> $(f \circ g)(3) = f(g(3)) = f(9) = 10$
> $(g \circ f)(3) = g(f(3)) = g(4) = 16$
>
> Nótese que $f \circ g \neq g \circ f$ en general — la composición **no es conmutativa**.

---

## 📂 TEMA 4: Álgebra de Boole y Circuitos Lógicos

### 4.1 Variables y Operaciones Booleanas

El **álgebra de Boole** trabaja con variables binarias (0 o 1) y es la base matemática del diseño de circuitos digitales y procesadores.

| Operación | Notación algebraica | Equivalente lógico |
|---|---|---|
| AND | A · B (o AB) | Conjunción ∧ |
| OR | A + B | Disyunción ∨ |
| NOT | A' (o Ā) | Negación ¬ |

### 4.2 Postulados y Teoremas de Boole (Tabla Completa)

| Ley | AND | OR |
|---|---|---|
| Identidad | A·1 = A | A+0 = A |
| Nulo | A·0 = 0 | A+1 = 1 |
| Idempotencia | A·A = A | A+A = A |
| Complemento | A·A' = 0 | A+A' = 1 |
| Conmutativa | A·B = B·A | A+B = B+A |
| Asociativa | (AB)C = A(BC) | (A+B)+C = A+(B+C) |
| Distributiva | A(B+C) = AB+AC | A+BC = (A+B)(A+C) |
| **De Morgan** | (AB)' = A'+B' | (A+B)' = A'B' |

### 4.3 Compuertas Lógicas (Hardware)

| Compuerta | Tabla de verdad (A,B → Salida) | Expresión |
|---|---|---|
| **AND** | 00→0, 01→0, 10→0, 11→1 | A·B |
| **OR** | 00→0, 01→1, 10→1, 11→1 | A+B |
| **NOT** | 0→1, 1→0 | A' |
| **NAND** | 00→1, 01→1, 10→1, 11→0 | (A·B)' |
| **NOR** | 00→1, 01→0, 10→0, 11→0 | (A+B)' |
| **XOR** | 00→0, 01→1, 10→1, 11→0 | A⊕B |
| **XNOR** | 00→1, 01→0, 10→0, 11→1 | (A⊕B)' |

> NAND y NOR son **compuertas universales**: con solo NAND (o solo NOR) repetidas se puede construir CUALQUIER circuito lógico, incluyendo AND, OR y NOT.
> Ejemplo: $A' = (A \cdot A)'$ → un NAND con ambas entradas iguales a A funciona como NOT.

### 4.4 Simplificación de Expresiones Booleanas

**Método algebraico — ejemplo resuelto paso a paso:**

Simplificar: $F = AB + AB' + A'B$

```
F = AB + AB' + A'B
F = A(B+B') + A'B          [factor común A]
F = A(1) + A'B               [B+B' = 1, complemento]
F = A + A'B                  [identidad]
F = A + B                    [ley de absorción: A + A'B = A + B]
```

**Otro ejemplo:** Simplificar $F = (A+B)(A+B')$

```
F = AA + AB' + BA + BB'
F = A + AB' + AB + 0        [AA=A, BB'=0]
F = A + A(B'+B)
F = A + A(1)
F = A + A = A
```

### 4.5 Mapas de Karnaugh

Método visual con tablas de $2^n$ casillas que agrupa términos adyacentes (en grupos de 1, 2, 4, 8...) para simplificar funciones booleanas sin necesidad de álgebra paso a paso.

**Ejemplo: simplificar F(A,B) con tabla de verdad: F=1 cuando AB=01, 10, 11**

| | B=0 | B=1 |
|---|---|---|
| **A=0** | 0 | 1 |
| **A=1** | 1 | 1 |

**Pasos:**
1. Ubicar los 1s en el mapa: posiciones (A=0,B=1), (A=1,B=0), (A=1,B=1).
2. Agrupar adyacentes: el grupo de la fila A=1 completa (ambas columnas) da el término **A**; el grupo de la columna B=1 completa da el término **B**.
3. Expresión simplificada: $F = A + B$

---

## 📂 TEMA 5: Teoría de Grafos e Inducción Matemática

### 5.1 Conceptos Básicos de Grafos

Un **grafo** $G=(V,E)$ está formado por un conjunto de **vértices** (V) y un conjunto de **aristas** (E) que conectan pares de vértices.

| Tipo de Grafo | Descripción |
|---|---|
| **No dirigido** | Las aristas no tienen dirección (A-B = B-A) |
| **Dirigido (dígrafo)** | Las aristas tienen dirección (A→B ≠ B→A) |
| **Ponderado** | Las aristas tienen un peso/costo asociado |
| **Simple** | Sin lazos ni aristas múltiples entre el mismo par de vértices |
| **Completo ($K_n$)** | Todos los vértices están conectados entre sí; tiene $\frac{n(n-1)}{2}$ aristas |
| **Bipartito** | Los vértices se dividen en dos grupos, y las aristas solo conectan vértices de grupos distintos |

### 5.2 Conceptos Clave y Fórmulas

- **Grado de un vértice** $\deg(v)$: número de aristas que llegan o salen de él.
- **Teorema de la suma de grados:** $\sum \deg(v) = 2|E|$ (la suma de todos los grados es el doble del número de aristas, porque cada arista se cuenta dos veces).
- **Camino:** secuencia de vértices conectados por aristas, sin repetir vértices.
- **Ciclo:** camino que empieza y termina en el mismo vértice.
- **Grafo conexo:** existe un camino entre cualquier par de vértices.

### 5.3 Representación Matricial de Grafos

**Matriz de adyacencia** para el grafo: A-B, A-C, B-C

| | A | B | C |
|---|---|---|---|
| **A** | 0 | 1 | 1 |
| **B** | 1 | 0 | 1 |
| **C** | 1 | 1 | 0 |

> Este es un grafo completo $K_3$ (triángulo): todos conectados entre sí. Grado de cada vértice = 2. Suma de grados = 6 = 2×3 aristas ✓ (cumple el teorema).

### 5.4 Inducción Matemática

**Los 3 pasos formales:**
1. **Caso base:** demostrar para $n=1$ (o el primer valor del dominio).
2. **Hipótesis inductiva:** suponer verdadero para $n=k$.
3. **Paso inductivo:** demostrar que, a partir de la hipótesis, también es verdadero para $n=k+1$.

> *Ejemplo resuelto completo:* Demostrar que $1+2+3+\dots+n = \frac{n(n+1)}{2}$ para todo $n\geq1$.
>
> **Caso base ($n=1$):** $1 = \frac{1(1+1)}{2} = \frac{2}{2} = 1$ ✓
>
> **Hipótesis inductiva:** suponemos que $1+2+\dots+k = \frac{k(k+1)}{2}$ es verdadero.
>
> **Paso inductivo:** demostrar para $n=k+1$:
> $$1+2+\dots+k+(k+1) = \frac{k(k+1)}{2}+(k+1)$$
> $$= \frac{k(k+1)+2(k+1)}{2} = \frac{(k+1)(k+2)}{2}$$
> Esto es exactamente la fórmula con $n=k+1$. ✓ Queda demostrado para todo $n$.

---

## 📂 TEMA 6: Máquinas de Estado y Lenguajes Formales

### 6.1 Autómatas Finitos

Un **autómata finito** es un modelo matemático con un número finito de estados, usado para reconocer patrones en cadenas (lenguajes formales).

**Definición formal:** $M = (Q, \Sigma, \delta, q_0, F)$
- $Q$: conjunto finito de estados
- $\Sigma$: alfabeto de entrada
- $\delta$: función de transición ($Q \times \Sigma \to Q$)
- $q_0$: estado inicial
- $F$: conjunto de estados de aceptación

| Tipo | Característica |
|---|---|
| **DFA** (Determinista) | Para cada estado y símbolo, exactamente una transición posible |
| **NFA** (No determinista) | Puede haber cero, una o varias transiciones posibles para el mismo símbolo |

> *Ejemplo:* Autómata que reconoce cadenas binarias que terminan en "1":
> - Estados: $\{q_0, q_1\}$, donde $q_0$ es inicial y $q_1$ es de aceptación.
> - Transiciones: desde $q_0$ con "0" se queda en $q_0$; con "1" va a $q_1$. Desde $q_1$ con "0" vuelve a $q_0$; con "1" se queda en $q_1$.
> - La cadena "1101" termina en $q_1$ (acepta), la cadena "1100" termina en $q_0$ (rechaza).

### 6.2 Gramáticas Formales y Jerarquía de Chomsky

Una **gramática** $G=(V,T,P,S)$ define las reglas de producción que generan las cadenas válidas de un lenguaje.

| Tipo | Nombre | Reconocida por |
|---|---|---|
| Tipo 0 | Sin restricciones | Máquina de Turing |
| Tipo 1 | Sensible al contexto | Autómata linealmente acotado |
| Tipo 2 | Libre de contexto | Autómata de pila |
| Tipo 3 | Regular | Autómata finito |

> *Ejemplo de gramática regular* que genera cadenas con cualquier número de "a" seguidas de una "b":
> $S \to aS \mid b$
> Genera: b, ab, aab, aaab, ...

### 6.3 Expresiones Regulares

| Símbolo | Significado | Ejemplo |
|---|---|---|
| `*` | Cero o más repeticiones | `a*` → "", "a", "aa", "aaa"... |
| `+` | Una o más repeticiones | `a+` → "a", "aa", "aaa"... |
| `?` | Cero o una repetición (opcional) | `a?` → "" o "a" |
| `\|` | Alternancia (o) | `a\|b` → "a" o "b" |
| `.` | Cualquier carácter | `a.c` → "abc", "axc"... |

> *Ejemplo práctico:* la expresión regular para validar un número de teléfono boliviano simple podría ser `[67][0-9]{7}` (empieza con 6 o 7, seguido de 7 dígitos).

> Las expresiones regulares son equivalentes en poder de reconocimiento a los autómatas finitos (Tipo 3): todo lo que reconoce un DFA puede expresarse como expresión regular, y viceversa.

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
