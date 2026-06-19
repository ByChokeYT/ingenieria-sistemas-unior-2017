# Tema 1: Lógica Proposicional y Tablas de Verdad
## 🏫 Materia: Álgebra y Lógica Formal (ALF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 1.1 Proposiciones

Una **proposición** es un enunciado declarativo que puede calificarse como verdadero (V/1) o falso (F/0), pero nunca ambos a la vez, y nunca ninguno.

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Atómica (simple)** | No contiene conectivos lógicos | p: "La Paz es la sede de gobierno" |
| **Molecular (compuesta)** | Combina proposiciones con conectivos | p∧q: "Llueve y hace frío" |

**NO son proposiciones:**
- Preguntas: "¿Qué hora es?"
- Órdenes/exclamaciones: "¡Cierra la puerta!"
- Enunciados ambiguos o de opinión sin valor de verdad objetivo: "El helado de chocolate es el mejor"

##### 1.2 Conectivos Lógicos (Operadores)

| Conectivo | Símbolo | Nombre | Se lee | Verdadero cuando... |
|---|---|---|---|---|
| Negación | ¬p | NOT | "no p" | p es falso |
| Conjunción | p ∧ q | AND | "p y q" | ambas son verdaderas |
| Disyunción inclusiva | p ∨ q | OR | "p o q" | al menos una es verdadera |
| Disyunción exclusiva | p ⊕ q | XOR | "p o q, no ambas" | exactamente una es verdadera |
| Implicación (condicional) | p → q | IF...THEN | "si p, entonces q" | excepto cuando p=V y q=F |
| Doble implicación | p ↔ q | IFF | "p si y solo si q" | ambas tienen el mismo valor de verdad |

##### 1.3 Tabla de Verdad Completa

| p | q | ¬p | p∧q | p∨q | p⊕q | p→q | p↔q |
|---|---|---|---|---|---|---|---|
| V | V | F | V | V | F | V | V |
| V | F | F | F | V | V | F | F |
| F | V | V | F | V | V | V | F |
| F | F | V | F | F | F | V | V |

**Regla del número de filas:** con $n$ proposiciones simples distintas, la tabla tiene $2^n$ filas.
> Con 3 proposiciones (p, q, r) → $2^3 = 8$ filas.

##### 1.4 Construyendo una Tabla de Verdad para una Proposición Compleja

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

##### 1.5 Tautologías, Contradicciones y Contingencias

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

##### 1.6 Leyes del Álgebra Proposicional

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

##### 1.7 Razonamiento Lógico — Reglas de Inferencia

| Regla | Estructura formal | Ejemplo en lenguaje natural |
|---|---|---|
| **Modus Ponens** | p→q, p ⊢ q | "Si llueve, me mojo. Llueve. ∴ Me mojo." |
| **Modus Tollens** | p→q, ¬q ⊢ ¬p | "Si llueve, me mojo. No me mojé. ∴ No llovió." |
| **Silogismo hipotético** | p→q, q→r ⊢ p→r | "Si estudio, apruebo. Si apruebo, me gradúo. ∴ Si estudio, me gradúo." |
| **Silogismo disyuntivo** | p∨q, ¬p ⊢ q | "Es de día o de noche. No es de día. ∴ Es de noche." |
| **Adición** | p ⊢ p∨q | De una verdad, se puede agregar cualquier disyunción |
| **Simplificación** | p∧q ⊢ p | De una conjunción, se puede extraer cualquiera de sus partes |

##### 1.8 Falacias Lógicas Comunes (errores de razonamiento)

| Falacia | Error | Ejemplo |
|---|---|---|
| **Afirmación del consecuente** | De p→q y q, concluir p (inválido) | "Si llueve, hay nubes. Hay nubes. ∴ Llueve." (falso: podría estar nublado sin llover) |
| **Negación del antecedente** | De p→q y ¬p, concluir ¬q (inválido) | "Si llueve, hay nubes. No llueve. ∴ No hay nubes." (falso: puede haber nubes sin lluvia) |

---

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **Diferencie entre una proposición atómica y una molecular.**
   * *Respuesta:* Una proposición atómica es simple y no contiene conectivos lógicos (ej. "La Paz es la sede de gobierno"); una molecular combina dos o más proposiciones atómicas mediante conectivos lógicos (ej. "Llueve y hace frío").
2. **Defina qué son Tautología, Contradicción y Contingencia.**
   * *Respuesta:* Tautología: enunciado que es siempre verdadero bajo cualquier interpretación. Contradicción: enunciado siempre falso. Contingencia: enunciado que puede ser verdadero o falso dependiendo de sus componentes.
3. **¿Cuántas filas tiene una tabla de verdad para un enunciado que contiene 4 proposiciones simples distintas?**
   * A) 8 filas
   * B) 16 filas
   * C) 32 filas
   * D) 4 filas
   * *Respuesta correcta:* B) 16 filas ($2^4 = 16$).
4. **Aplique la Ley de De Morgan para negar la proposición $p \land q$.**
   * *Respuesta:* $\neg(p \land q) \equiv \neg p \lor \neg q$.

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*