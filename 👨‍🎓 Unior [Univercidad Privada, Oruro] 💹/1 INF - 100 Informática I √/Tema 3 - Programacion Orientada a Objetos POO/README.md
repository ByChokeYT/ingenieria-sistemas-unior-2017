# Tema 3: Programación Orientada a Objetos (POO)
## 🏫 Materia: Informática I (INF-100)

---

### 📚 Apuntes y Conceptos Clave
##### 3.1 Clases y Objetos

| Concepto | Definición |
|---|---|
| **Clase** | Plantilla/molde que define atributos (datos) y métodos (comportamientos) comunes |
| **Objeto** | Instancia concreta de una clase, con valores propios en sus atributos |
| **Atributo** | Variable que pertenece a la clase, representa una característica |
| **Método** | Función que pertenece a la clase, representa un comportamiento |
| **Constructor** | Método especial ejecutado automáticamente al crear (instanciar) un objeto |

**Ejemplo completo en Python:**

```python
class Auto:
    def __init__(self, color, velocidad_max):  # Constructor
        self.color = color
        self.velocidad_max = velocidad_max
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        self.velocidad_actual = min(
            self.velocidad_actual + incremento,
            self.velocidad_max
        )

    def frenar(self):
        self.velocidad_actual = 0

# Creación de objetos (instancias)
mi_auto = Auto("rojo", 180)
mi_auto.acelerar(50)
print(f"El auto {mi_auto.color} va a {mi_auto.velocidad_actual} km/h")
```

##### 3.2 Los 4 Pilares de la POO

**1. Encapsulamiento** — ocultar los datos internos, exponiendo solo lo necesario mediante métodos públicos (`get`/`set`):

```python
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # atributo privado (doble guion bajo)

    def get_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
```

**2. Herencia** — una clase hija reutiliza atributos y métodos de una clase padre:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hacer_sonido(self):
        pass

class Perro(Animal):       # Perro hereda de Animal
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):         # Gato hereda de Animal
    def hacer_sonido(self):
        return "Miau!"
```

**3. Polimorfismo** — un mismo método se comporta diferente según el objeto que lo invoque:

```python
animales = [Perro("Rex"), Gato("Michi")]
for a in animales:
    print(f"{a.nombre} dice: {a.hacer_sonido()}")
# Rex dice: Guau!
# Michi dice: Miau!
```

**4. Abstracción** — modelar solo lo relevante de un objeto del mundo real, ocultando la complejidad interna (ej: una clase `Vehiculo` general no necesita saber cómo funciona internamente el motor, solo expone `arrancar()`, `frenar()`, etc.)

##### 3.3 Relaciones entre Clases

| Relación | Descripción | Ejemplo | ¿Puede existir independientemente? |
|---|---|---|---|
| **Asociación** | Una clase usa/conoce a otra | `Profesor` conoce a `Estudiante` | Sí, ambas existen aparte |
| **Agregación** | Una clase "tiene" otra, relación más fuerte | `Equipo` tiene `Jugadores` | Sí, el jugador existe sin el equipo |
| **Composición** | Una clase "es dueña" de otra, dependencia total | `Casa` tiene `Habitaciones` | No, la habitación no existe sin la casa |

---

##### 📑 Banco de Preguntas (Auto-Evaluación)
1. **Explique la diferencia entre una Clase y un Objeto en POO.**
   * *Respuesta:* Una Clase es la plantilla o molde que define los atributos y métodos comunes; un Objeto es la instancia concreta de esa clase, con datos reales en memoria.
2. **Defina brevemente el pilar de la "Herencia" en POO.**
   * *Respuesta:* Permite que una nueva clase (subclase o clase hija) adquiera las propiedades y métodos de una clase existente (superclase o clase padre), promoviendo la reutilización del código.
3. **El ocultamiento de los datos internos de un objeto mediante el uso de modificadores de acceso (`private`) se conoce como:**
   * A) Polimorfismo
   * B) Herencia
   * C) Encapsulamiento
   * D) Abstracción
   * *Respuesta correcta:* C) Encapsulamiento.
4. **¿Qué es un constructor en una clase?**
   * *Respuesta:* Es un método especial que se ejecuta automáticamente al instanciar un objeto de la clase, utilizado principalmente para inicializar sus atributos.

---

### ✍️ Mis Resúmenes y Notas de Clase
*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*

---

### 📂 Archivos y Tareas de esta Unidad
*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*

---
*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*