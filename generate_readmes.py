#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import urllib.parse
import json

# Mapeo de códigos exactos de materias (sigla-número) a exactamente 6 temas/subcarpetas de aprendizaje
COURSE_THEMES = {
    # 1º Semestre
    "INF-100": [
        "Tema 1 - Algoritmos y Pseudocodigo",
        "Tema 2 - Estructuras de Control y Secuenciales",
        "Tema 3 - Programacion Orientada a Objetos POO",
        "Tema 4 - Estructuras de Datos Lineales",
        "Tema 5 - Recursividad y Algoritmos de Busqueda",
        "Tema 6 - Archivos y Manejo de Excepciones"
    ],
    "ADM-100": [
        "Tema 1 - Introduccion a la Administracion",
        "Tema 2 - Planificacion",
        "Tema 3 - Organizacion",
        "Tema 4 - Direccion y Liderazgo",
        "Tema 5 - Control",
        "Tema 6 - Administracion Estrategica y FODA"
    ],
    "ISO-100": [
        "Tema 1 - Teoria de las Organizaciones y Enfoque de Sistemas",
        "Tema 2 - Estructuras Organizacionales y Diseno de Procesos",
        "Tema 3 - Sistemas de Informacion en la Empresa",
        "Tema 4 - Toma de Decisiones y Dinamica de Sistemas",
        "Tema 5 - Cultura y Cambio Organizacional",
        "Tema 6 - Modelos de Gestion de Calidad y Reingenieria"
    ],
    "ALF-100": [
        "Tema 1 - Logica Proposicional y Tablas de Verdad",
        "Tema 2 - Teoria de Conjuntos",
        "Tema 3 - Relaciones y Funciones Discretas",
        "Tema 4 - Algebra de Boole y Circuitos Lógicos",
        "Tema 5 - Teoria de Grafos e Induccion Matematica",
        "Tema 6 - Maquinas de Estado y Lenguajes Formales"
    ],
    "MAT-100": [
        "Tema 1 - Funciones y Graficos",
        "Tema 2 - Limites y Continuidad",
        "Tema 3 - La Derivada y Reglas",
        "Tema 4 - Aplicaciones de la Derivada",
        "Tema 5 - Introduccion a la Integral",
        "Tema 6 - Metodos de Integracion y Aplicaciones"
    ],
    "ING-100": [
        "Tema 1 - Gramatica y Estructuras Basicas",
        "Tema 2 - Vocabulario Tecnico de Computacion",
        "Tema 3 - Comprension Lectora de Manuales",
        "Tema 4 - Redaccion Tecnica y Documentacion",
        "Tema 5 - Presentaciones Tecnicas y Conversacion",
        "Tema 6 - Traduccion de Patentes y Articulos Cientificos"
    ],

    # 2º Semestre
    "INF-110": [
        "Tema 1 - Programacion Estructurada Avanzada",
        "Tema 2 - Punteros y Gestion de Memoria Dinamica",
        "Tema 3 - Estructuras de Datos Basicas",
        "Tema 4 - Programacion Orientada a Objetos en C++ y Java",
        "Tema 5 - Interfaces Graficas de Usuario GUI",
        "Tema 6 - Conectividad a Bases de Datos y CRUD"
    ],
    "ARC-110": [
        "Tema 1 - Logica Digital y Compuertas",
        "Tema 2 - Estructura de la CPU y Von Neumann",
        "Tema 3 - Organizacion y Jerarquia de Memoria",
        "Tema 4 - Set de Instrucciones y Ensamblador",
        "Tema 5 - Microarquitectura y Segmentacion Pipeline",
        "Tema 6 - Sistemas Multiprocesador y Paralelismo"
    ],
    "MAT-110": [
        "Tema 1 - Vectores y Geometria Analitica",
        "Tema 2 - Funciones de Varias Variables",
        "Tema 3 - Derivadas Parciales y Gradiente",
        "Tema 4 - Integrales Multiples",
        "Tema 5 - Integrales de Linea y Superficie",
        "Tema 6 - Teoremas de Green, Stokes y Divergencia"
    ],
    "MEC-110": [
        "Tema 1 - Vectores y Cinematica",
        "Tema 2 - Dinamica y Leyes de Newton",
        "Tema 3 - Trabajo y Energia",
        "Tema 4 - Estatica y Dinamica Rotacional",
        "Tema 5 - Movimiento Armonico Simple y Oscilaciones",
        "Tema 6 - Ley de Gravitacion Universal y Fluidos"
    ],
    "ALL-110": [
        "Tema 1 - Matrices y Operaciones",
        "Tema 2 - Determinantes y Matriz Inversa",
        "Tema 3 - Sistemas de Ecuaciones Lineales",
        "Tema 4 - Espacios Vectoriales",
        "Tema 5 - Valores y Vectores Propios",
        "Tema 6 - Transformaciones Lineales y Aplicaciones"
    ],
    "ING-110": [
        "Tema 1 - Gramatica Avanzada y Tiempos Compuestos",
        "Tema 2 - Redaccion de Reportes y Especificaciones de Software",
        "Tema 3 - Conversacion de Negocios y Entrevistas de Trabajo",
        "Tema 4 - Comprension de Ponencias y Conferencias de TI",
        "Tema 5 - Correspondencia Comercial y Emails Profesionales",
        "Tema 6 - Terminologia de Inteligencia Artificial y Cloud"
    ],

    # 3º Semestre
    "INF-120": [
        "Tema 1 - Analisis de Algoritmos y Complejidad Big-O",
        "Tema 2 - Listas Enlazadas Simples, Dobles y Circulares",
        "Tema 3 - Pilas y Colas Dinamicas",
        "Tema 4 - Arboles Binarios, AVL y Arboles de Busqueda",
        "Tema 5 - Grafos y Algoritmos de Recorrido BFS-DFS",
        "Tema 6 - Tablas Hash y Algoritmos de Dispersion"
    ],
    "ECD-120": [
        "Tema 1 - Introduccion y ED de Primer Orden",
        "Tema 2 - EDO de Orden Superior",
        "Tema 3 - Transformada de Laplace",
        "Tema 4 - Modelado con Ecuaciones Diferenciales",
        "Tema 5 - Sistemas de Ecuaciones Diferenciales Lineales",
        "Tema 6 - Soluciones en Series de Potencias"
    ],
    "ELM-120": [
        "Tema 1 - Electraceutica y Ley de Coulomb",
        "Tema 2 - Campo Electrico y Ley de Gauss",
        "Tema 3 - Circuitos de Corriente Continua DC",
        "Tema 4 - Campo Magnetico y Ley de Ampere",
        "Tema 5 - Induccion Electromagnetica y Ley de Faraday",
        "Tema 6 - Ecuaciones de Maxwell y Circuitos AC"
    ],
    "EST-120": [
        "Tema 1 - Estadistica Descriptiva y Datos",
        "Tema 2 - Teoria de Probabilidades",
        "Tema 3 - Variables Aleatorias y Distribuciones",
        "Tema 4 - Regresion Lineal y Correlacion",
        "Tema 5 - Inferencia Estadistica y Pruebas de Hipotesis",
        "Tema 6 - Estimacion de Parametros y Muestreo"
    ],
    "QUE-120": [
        "Tema 1 - Saludos y Gramatica Basica Quechua",
        "Tema 2 - Yupaykuna y Vocabulario Diario",
        "Tema 3 - Conversaciones Basicas y Cultura",
        "Tema 4 - Cuerpo Humano y Salud en la Comunidad",
        "Tema 5 - Flora, Fauna y Actividades Agricolas",
        "Tema 6 - Cuentos Tradicionales y Expresion Oral"
    ],
    "CBA-120": [
        "Tema 1 - Introduccion a la Contabilidad y Transacciones",
        "Tema 2 - Partida Doble y Asientos Contables",
        "Tema 3 - Libros Diario y Mayor",
        "Tema 4 - Balance de Comprobacion y Estados Financieros",
        "Tema 5 - Ajustes Contables y Hoja de Trabajo",
        "Tema 6 - Analisis e Interpretacion de Estados Financieros"
    ],

    # 4º Semestre
    "INF-130": [
        "Tema 1 - Paradigmas de Programacion y Sintaxis Comparada",
        "Tema 2 - Tipado de Datos y Expresiones",
        "Tema 3 - Programacion Funcional y Expresiones Lambda",
        "Tema 4 - Programacion Concurrente y Multihilo",
        "Tema 5 - Expresiones Regulares y Metaprogramacion",
        "Tema 6 - Compiladores e Interpretes Basicos"
    ],
    "INS-130": [
        "Tema 1 - Teoria General de Sistemas TGS",
        "Tema 2 - Modelado de Sistemas y Ciclo de Vida",
        "Tema 3 - Metodologia de Sistemas Blandos MSB",
        "Tema 4 - Ingenieria de Requerimientos",
        "Tema 5 - Modelos de Negocios y Arquitectura Enterprise",
        "Tema 6 - Calidad de Sistemas y Aseguramiento"
    ],
    "BDD-130": [
        "Tema 1 - Modelado Entidad-Relacion ER",
        "Tema 2 - Modelo Relacional y Normalizacion",
        "Tema 3 - Lenguaje SQL y Consultas DDL-DML",
        "Tema 4 - Transacciones y Control de Concurrencia",
        "Tema 5 - Seguridad, Roles y Privilegios en BDD",
        "Tema 6 - Bases de Datos NoSQL y Big Data"
    ],
    "EST-130": [
        "Tema 1 - Probabilidad Avanzada y Variables Aleatorias Bidimensionales",
        "Tema 2 - Estimacion Puntual y de Intervalo",
        "Tema 3 - Pruebas de Hipotesis Parametricas y No Parametricas",
        "Tema 4 - Analisis de Varianza ANOVA",
        "Tema 5 - Regresion Multiple y Series de Tiempo",
        "Tema 6 - Diseno de Experimentos y Estadistica Multivariada"
    ],
    "CEL-103": [
        "Tema 1 - Componentes Pasivos y Leyes de Kirchhoff",
        "Tema 2 - Diodos Semiconductores",
        "Tema 3 - Transistores BJT y FET",
        "Tema 4 - Amplificadores Operacionales",
        "Tema 5 - Electronica Digital y Compuertas",
        "Tema 6 - Osciladores, Temporizadores y Fuentes de Poder"
    ],
    "SIC-130": [
        "Tema 1 - Automatizacion y Sistemas Contables",
        "Tema 2 - Modulos de Facturacion e Inventarios",
        "Tema 3 - Planillas de Sueldos y Generacion de Reportes",
        "Tema 4 - Declaraciones Tributarias e Impuestos Automatizados",
        "Tema 5 - Auditoria de Sistemas Contables",
        "Tema 6 - Seguridad y Respaldo de Datos Financieros"
    ],

    # 5º Semestre
    "INO-140": [
        "Tema 1 - Programacion Lineal y Modelado",
        "Tema 2 - Metodo Simplex",
        "Tema 3 - Redes PERT-CPM",
        "Tema 4 - Teoria de Colas y Modelos de Inventarios",
        "Tema 5 - Programacion Dinamica e Entera",
        "Tema 6 - Modelos de Simulacion Montecarlo y Decisiones"
    ],
    "INS-140": [
        "Tema 1 - Enfoque de Sistemas Aplicado a Organizaciones",
        "Tema 2 - Dinamica de Sistemas Complejos y Bucles de Retorno",
        "Tema 3 - Modelos de Simulacion Organizacional (Vensim / Stella)",
        "Tema 4 - Ingenieria de Requerimientos Avanzada y UML",
        "Tema 5 - Arquitectura de Informacion y Diseno de Sistemas",
        "Tema 6 - Evaluacion de Usabilidad e Impacto Tecnologico"
    ],
    "DPW-140": [
        "Tema 1 - Maquetacion Estructurada HTML5",
        "Tema 2 - Diseno Responsivo y Adaptativo CSS3",
        "Tema 3 - Programacion Frontend JavaScript",
        "Tema 4 - Desarrollo Backend y Servidor PHP",
        "Tema 5 - Arquitectura MVC y Frameworks Modernos",
        "Tema 6 - APIs RESTful y Seguridad en Aplicaciones Web"
    ],
    "BDD-140": [
        "Tema 1 - SQL Avanzado y Funciones de Ventana",
        "Tema 2 - Triggers y Procedimientos Almacenados PL-pgSQL",
        "Tema 3 - Optimizacion de Consultas (Performance Tuning) y Planes de Ejecucion",
        "Tema 4 - Administracion de Bases de Datos (DBA), Indices y Particionamiento",
        "Tema 5 - Alta Disponibilidad, Replicacion y Respaldos Automatizados",
        "Tema 6 - Bases de Datos Distribuidas y NoSQL"
    ],
    "DGI-140": [
        "Tema 1 - Experiencia de Usuario UX y Usabilidad",
        "Tema 2 - Diseno Visual UI y Maquetacion",
        "Tema 3 - Prototipado Interactivo y Wireframes en Figma",
        "Tema 4 - Psicologia del Color y Tipografia UI",
        "Tema 5 - Diseno de Sistemas de Diseno (Design Systems)",
        "Tema 6 - Pruebas A-B y Evaluacion de Interfaces"
    ],
    "OPT-140": [
        "Tema 1 - Introduccion a IoT y Microcontroladores",
        "Tema 2 - Sensores y Actuadores",
        "Tema 3 - Protocolos de Comunicacion y Redes Inalambricas",
        "Tema 4 - Prototipado y Proyectos Arduino",
        "Tema 5 - Interfaces de Usuario para IoT y Dashboard Web",
        "Tema 6 - Seguridad en Redes IoT y Aplicaciones Industriales"
    ],

    # 6º Semestre
    "INO-150": [
        "Tema 1 - Programacion Multiobjetivo y Metodos de Optimizacion",
        "Tema 2 - Teoria de Juegos y Modelos de Decision Colectiva",
        "Tema 3 - Procesos de Decision de Markov",
        "Tema 4 - Teoria de Colas Avanzada y Redes de Colas",
        "Tema 5 - Modelado con Variables Estocasticas",
        "Tema 6 - Optimizacion Heuristica y Algoritmos Geneticos"
    ],
    "INS-150": [
        "Tema 1 - Viabilidad de Sistemas y Enfoque de Viabilidad Viable (VSM)",
        "Tema 2 - Ciberorganizaciones y Diseno Sistemico",
        "Tema 3 - Auditoria Sistemica de Procesos Organizacionales",
        "Tema 4 - Gestion del Conocimiento y Aprendizaje Organizacional",
        "Tema 5 - Ingenieria de Reingenieria de Negocios (BPR)",
        "Tema 6 - Liderazgo Sistemico y Gobernanza"
    ],
    "DPW-150": [
        "Tema 1 - Desarrollo Frontend Moderno con Frameworks (React/Vue)",
        "Tema 2 - Manejo de Estado Global y Enrutamiento Web",
        "Tema 3 - Desarrollo Backend con Node.js y Express",
        "Tema 4 - Bases de Datos NoSQL en la Web (MongoDB / Firebase)",
        "Tema 5 - Autenticacion JWT y Seguridad Web Avanzada",
        "Tema 6 - Despliegue en la Nube (Cloud Deployment) y Serverless"
    ],
    "BDD-150": [
        "Tema 1 - Arquitectura de Bodegas de Datos (Data Warehousing)",
        "Tema 2 - Modelado Dimensional: Hechos y Dimensiones (Estrella/Copo de Nieve)",
        "Tema 3 - Procesos ETL (Extraccion, Transformacion y Carga)",
        "Tema 4 - Mineria de Datos (Data Mining) y Algoritmos Asociativos",
        "Tema 5 - Analisis Multidimensional OLAP",
        "Tema 6 - Big Data e Integracion con Spark/Hadoop"
    ],
    "PED-150": [
        "Tema 1 - Identificacion del Proyecto y Ciclo de Vida",
        "Tema 2 - Estudio de Mercado y Aspectos Tecnicos",
        "Tema 3 - Evaluacion Economica y Financiera VAN-TIR",
        "Tema 4 - Analisis de Riesgo e Impacto Ambiental",
        "Tema 5 - Financiamiento del Proyecto y Estructura de Capital",
        "Tema 6 - Plan de Ejecucion, Seguimiento y Cierre"
    ],
    "SOP-150": [
        "Tema 1 - Introduccion e Historia de los SO",
        "Tema 2 - Gestion de Procesos e Hilos",
        "Tema 3 - Planificacion de CPU y Sincronizacion",
        "Tema 4 - Administracion de Memoria RAM y Virtual",
        "Tema 5 - Sistema de Archivos y Almacenamiento",
        "Tema 6 - Seguridad y Proteccion en Sistemas Operativos"
    ],

    # 7º Semestre
    "ING-160": [
        "Tema 1 - Introduccion a la Ingenieria de Software y Modelos de Proceso",
        "Tema 2 - Metodologias Agiles (Scrum, Kanban, XP)",
        "Tema 3 - Diseno de Arquitectura de Software y Patrones de Diseno",
        "Tema 4 - Ingenieria de Requerimientos y Casos de Uso",
        "Tema 5 - Pruebas de Software (Unitarias, Integracion, Sistema) y QA",
        "Tema 6 - Mantenimiento de Software, Refactorizacion y Gestion de Configuraciones"
    ],
    "TEE-160": [
        "Tema 1 - Cloud Computing y Servicios AWS-Azure",
        "Tema 2 - Virtualizacion y Contenedores Docker",
        "Tema 3 - Integracion Continua y Metodologias DevOps",
        "Tema 4 - Blockchain y Big Data",
        "Tema 5 - Arquitectura de Microservicios",
        "Tema 6 - Computacion en el Borde y Tendencias Futuras"
    ],
    "SIM-160": [
        "Tema 1 - Modelado y Metodologia de Simulacion",
        "Tema 2 - Simulacion de Eventos Discretos",
        "Tema 3 - Generacion de Numeros Pseudoaleatorios",
        "Tema 4 - Analisis de Resultados y Validacion",
        "Tema 5 - Simulacion Dinamica de Sistemas Continuos",
        "Tema 6 - Herramientas de Simulacion por Computadora"
    ],
    "LEI-160": [
        "Tema 1 - Derecho Informatico y Etica",
        "Tema 2 - Delitos Informaticos y Ciberseguridad",
        "Tema 3 - Propiedad Intelectual y Licencias de Software",
        "Tema 4 - Contratos y Comercio Electronico",
        "Tema 5 - Proteccion de Datos y Privacidad en la Red",
        "Tema 6 - Firma Digital y Regulaciones Nacionales"
    ],
    "RED-160": [
        "Tema 1 - Modelos OSI y TCP-IP",
        "Tema 2 - Capa Fisica y Medios de Transmision",
        "Tema 3 - Direccionamiento IP y Subneteo",
        "Tema 4 - Protocolos de Transporte y Ruteo",
        "Tema 5 - Redes de Area Local Inalambricas WLAN",
        "Tema 6 - Seguridad en Redes y Firewalls"
    ],
    "OPT-160": [
        "Tema 1 - Diseno Avanzado de Circuitos Impresos PCB",
        "Tema 2 - Comunicacion Inalambrica Industrial (LoraWAN/Zigbee)",
        "Tema 3 - Diseno de Firmware Robusto en C-C++",
        "Tema 4 - Procesamiento de Senales en Tiempo Real",
        "Tema 5 - Sistemas Embebidos Basados en Linux (Raspberry Pi)",
        "Tema 6 - Proyecto Integrador de Optativa II"
    ],

    # 8º Semestre
    "MET-170": [
        "Tema 1 - Investigacion Cientifica y Metodologia",
        "Tema 2 - Planteamiento del Problema y Objetivos",
        "Tema 3 - Marco Teorico y Diseno Metodologico",
        "Tema 4 - Redaccion del Perfil de Proyecto de Grado",
        "Tema 5 - Recoleccion y Analisis de Datos de Investigacion",
        "Tema 6 - Estilo de Redaccion APA e Informe Final de Tesis"
    ],
    "AUT-170": [
        "Tema 1 - Fundamentos de Auditoria de TI",
        "Tema 2 - Evaluacion de Riesgos y Controles Internos",
        "Tema 3 - Seguridad Fisica y Logica",
        "Tema 4 - Elaboracion de Informes y Recomendaciones",
        "Tema 5 - Auditoria de Redes y Comunicaciones",
        "Tema 6 - Auditoria de Continuidad del Negocio y Respaldo"
    ],
    "INT-170": [
        "Tema 1 - Algoritmos de Busqueda no Informada e Informada",
        "Tema 2 - Aprendizaje Automatico Machine Learning",
        "Tema 3 - Redes Neuronales Artificiales y Deep Learning",
        "Tema 4 - Sistemas Expertos y Procesamiento de Lenguaje",
        "Tema 5 - Vision Artificial e Inteligencia Robotica",
        "Tema 6 - Etica y Futuro de la Inteligencia Artificial"
    ],
    "RED-170": [
        "Tema 1 - Conmutacion de Etiquetas Multiprotocolo (MPLS)",
        "Tema 2 - Redes Privadas Virtuales VPN IPsec y SSL",
        "Tema 3 - Calidad de Servicio QoS en Redes Convergentes",
        "Tema 4 - Telefonia IP y Comunicaciones Unificadas VoIP",
        "Tema 5 - IPv6 e Integracion en Redes Existentes",
        "Tema 6 - Monitoreo y Diagnostico Avanzado de Redes"
    ],
    "ASI-170": [
        "Tema 1 - Planificacion Estrategica de TI",
        "Tema 2 - Marco de Trabajo COBIT e ITIL",
        "Tema 3 - Seguridad de la Informacion y Auditoria",
        "Tema 4 - Gestion de Servicios de TI",
        "Tema 5 - Gestion de Proyectos de Sistemas de Informacion",
        "Tema 6 - Etica e Impacto Social de los Sistemas"
    ],
    "OPT-170": [
        "Tema 1 - Introduccion a la Robotica Movil y Brazos Roboticos",
        "Tema 2 - Cinematica Directa e Inversa de Manipuladores",
        "Tema 3 - Sistemas de Control Retroalimentado y Servos",
        "Tema 4 - Programacion Robotica Basada en ROS",
        "Tema 5 - Sensores Roboticos de Alta Precision (LiDAR, Encoders)",
        "Tema 6 - Proyecto Completo de Robotica o Automatizacion Industrial"
    ],

    # Taller de Grado
    "TG-180": [
        "Tema 1 - Seleccion y Delimitacion del Tema de Grado",
        "Tema 2 - Estructuracion de la Introduccion y Justificacion",
        "Tema 3 - Desarrollo del Marco Teorico Referencial",
        "Tema 4 - Marco Metodologico e Ingenieria del Proyecto",
        "Tema 5 - Primer Borrador del Perfil y Diseno Inicial",
        "Tema 6 - Pre-defensa del Perfil de Tesis"
    ]
}


# Mapeo de códigos de materias a sus apuntes académicos con 6 temas estructurados
SYLLABUS_MAPPING = {
    # 1º Semestre
    "INF-100": {
        "emoji": "💻",
        "title": "Informática I",
        "prereq": "Ninguno",
        "description": "Fundamentos de la computación, algoritmos, programación lógica e introducciones prácticas.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Informática y Programación
Conceptos clave de diseño de software y estructuras que debes dominar:

#### 📂 Tema 1: Algoritmos y Pseudocódigo
* Lógica computacional y pseudocódigo. Representación mediante diagramas de flujo.
* Variables, constantes y tipos de datos primitivos (enteros, booleanos, flotantes, cadenas).

#### 📂 Tema 2: Estructuras de Control y Secuenciales
* Estructuras de decisión condicional (`if`, `else`, `switch`).
* Estructuras de repetición iterativa (bucles `for`, `while`, `do-while`).

#### 📂 Tema 3: Programación Orientada a Objetos POO
* Definición de clases y objetos. Constructores e instanciación.
* Los 4 pilares: encapsulamiento, herencia, polimorfismo y abstracción de datos.

#### 📂 Tema 4: Estructuras de Datos Lineales
* Manejo de arreglos unidimensionales y bidimensionales (matrices).
* Conceptos básicos de estructuras de datos dinámicas: listas, pilas (LIFO) y colas (FIFO).

#### 📂 Tema 5: Recursividad y Algoritmos de Búsqueda
* Concepto de llamadas recursivas y casos base.
* Algoritmos clásicos de ordenamiento (Burbuja, QuickSort) y búsqueda (Lineal y Binaria).

#### 📂 Tema 6: Archivos y Manejo de Excepciones
* Lectura y escritura de archivos planos de texto y binarios.
* Control de errores lógicos en tiempo de ejecución mediante bloques `try-catch`."""
    },
    "ADM-100": {
        "emoji": "📈",
        "title": "Administración I",
        "prereq": "Ninguno",
        "description": "Introducción a los conceptos y teorías de la administración, el diseño organizacional y la gestión de recursos.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Administración I
Esta es la guía completa de temas que debes estudiar y dominar en esta asignatura:

#### 📂 Tema 1: Introducción a la Teoría Administrativa y la Empresa

##### 1. Conceptos Básicos de Administración
La **administración** es el proceso de planificar, organizar, dirigir y controlar el uso de los recursos (humanos, financieros, materiales y tecnológicos) para alcanzar los objetivos organizacionales de manera eficiente y eficaz.

*   **Eficiencia:** Capacidad de obtener los mayores resultados con la mínima cantidad de recursos (insumos). Se enfoca en los "medios" y en minimizar costos ("hacer las cosas bien").
*   **Eficacia:** Grado en el que se alcanzan los objetivos y metas propuestas. Se enfoca en los "fines" y resultados logrados ("hacer las cosas correctas").
*   **Productividad:** Relación matemática entre los resultados obtenidos (salidas) y los recursos utilizados (entradas).
    $$\\text{Productividad} = \\frac{\\text{Resultados Obtenidos}}{\\text{Recursos Utilizados}}$$
    Ser productivo implica lograr la máxima eficiencia y eficacia conjuntamente.

| Concepto | Enfoque | Pregunta Clave |
| :--- | :--- | :--- |
| **Eficiencia** | Recursos y Medios | ¿Cómo se utilizaron los recursos? |
| **Eficacia** | Objetivos y Fines | ¿Se lograron las metas propuestas? |
| **Productividad** | Relación Insumo-Producto | ¿Cómo optimizamos la relación salidas/entradas? |

##### 2. Historia y Evolución de la Teoría Administrativa
La administración científica y clásica nació de la necesidad de estructurar y racionalizar el trabajo durante la Revolución Industrial:

*   **Escuela de la Administración Científica (Frederick W. Taylor):**
    *   **Énfasis:** En las tareas y el trabajo operativo.
    *   **Aportes:** Estudio de tiempos y movimientos, estandarización de herramientas, división del trabajo obrero y pago de incentivos salariales por producción.
    *   **Principios:** Planeación, preparación, control y ejecución.
*   **Escuela de la Teoría Clásica (Henri Fayol):**
    *   **Énfasis:** En la estructura organizacional y funciones administrativas globales.
    *   **Funciones Básicas de la Empresa:** Técnicas, comerciales, financieras, de seguridad, contables y administrativas (prever, organizar, dirigir, coordinar y controlar).
    *   **Principios Relevantes:** Unidad de mando, unidad de dirección, división del trabajo, jerarquía, equidad y disciplina (14 principios en total).
*   **Escuela de las Relaciones Humanas (Elton Mayo):**
    *   **Énfasis:** En las personas y la psicología industrial.
    *   **Experimento de Hawthorne:** Demostró que el nivel de producción depende de la integración social y las normas del grupo informal, no solo de los incentivos económicos.
*   **Enfoques Modernos:**
    *   **Enfoque de Sistemas:** Concibe a la empresa como un sistema abierto integrado por subsistemas que interactúan dinámicamente con su entorno (entradas -> proceso -> salidas -> retroalimentación).
    *   **Enfoque Contingencial (Teoría de las Decisiones):** Establece que no existe una única "mejor forma" de administrar; todo es relativo y depende de factores externos (tecnología, ambiente, tamaño).

##### 3. Definición, Clasificación y Rol Social de la Empresa
Una **empresa** es una entidad socioeconómica constituida por capital, trabajo y dirección, coordinada para producir bienes o prestar servicios que satisfacen necesidades de la sociedad con fines lucrativos o sociales.

*   **Clasificación de Empresas:**
    1.  **Por Actividad/Sector:**
        *   *Primario:* Extractivas (minería, petróleo, agricultura).
        *   *Secundario:* Manufactureras e industriales (construcción, fábricas).
        *   *Terciario:* Servicios y comercio (bancos, educación, TI).
    2.  **Por Tamaño (criterios de empleados y ventas):**
        *   *Microempresa* (1-10 empleados), *Pequeña* (11-50), *Mediana* (51-250), *Grande* (más de 250).
    3.  **Por Origen del Capital:**
        *   *Privada:* Capital de particulares.
        *   *Pública:* Capital aportado por el Estado.
        *   *Mixta:* Capital conjunto público-privado.
    4.  **Por Ámbito Geográfico:** Locales, provinciales, nacionales, multinacionales.
*   **Rol de la Empresa en la Sociedad:**
    *   **Económico:** Creación de empleo, dinamización del mercado y generación de riqueza/PIB.
    *   **Social:** Innovación, provisión de bienes de calidad y Responsabilidad Social Empresarial (RSE), buscando mitigar impactos ecológicos y contribuir activamente al bienestar comunitario.

#### 📂 Tema 2: Planificación (El rumbo de la empresa)
* Proceso de establecer metas y definir la visión y misión de la empresa.
* Objetivos SMART, políticas, reglas y presupuestos operativos.
* Técnicas de toma de decisiones y planeación bajo incertidumbre.

#### 📂 Tema 3: Organización (Diseño de la estructura)
* Diseño de organigramas y asignación de puestos de trabajo.
* Conceptos clave: división del trabajo, jerarquía, autoridad, responsabilidad y tramo de control.
* Tipos de departamentalización (funcional, por productos, geográfica o matricial).

#### 📂 Tema 4: Dirección y Liderazgo (El factor humano)
* Teorías de la motivación humana (Jerarquía de Maslow, Teoría de los dos factores de Herzberg).
* Estilos de liderazgo (autocrático, democrático, laissez-faire) y rejilla gerencial.
* Canales de comunicación en la empresa y resolución de conflictos interpersonales.

#### 📂 Tema 5: Control (Evaluación del desempeño)
* Establecimiento de estándares de desempeño y puntos clave de control.
* Medición del desempeño real frente a los objetivos planificados.
* Corrección de desviaciones mediante retroalimentación y mejora de procesos.

#### 📂 Tema 6: Administración Estratégica y FODA
* Análisis del entorno externo (oportunidades y amenazas) e interno (fortalezas y debilidades).
* Formulación de estrategias corporativas, competitivas y funcionales."""
    },
    "ISO-100": {
        "emoji": "🏢",
        "title": "Ingeniería de Sistemas en las Organizaciones",
        "prereq": "Ninguno",
        "description": "Estudio del rol sistémico de la tecnología dentro de las estructuras organizativas, modelos de negocio y flujo de información.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Ingeniería de Sistemas en las Organizaciones
Comprende la interacción de la ingeniería informática con el ecosistema empresarial:

#### 📂 Tema 1: Teoría de las Organizaciones y Enfoque de Sistemas
* Concepto de organización como sistema abierto y complejo.
* Entorno interno y externo: variables de influencia organizacional.

#### 📂 Tema 2: Estructuras Organizacionales y Diseño de Procesos
* Diseño y análisis de estructuras organizativas tradicionales y matriciales.
* Modelado y mapeo de procesos de negocio (BPMN básico).

#### 📂 Tema 3: Sistemas de Información en la Empresa
* El rol de los sistemas de información en los niveles operativo, táctico y estratégico.
* Integración de tecnologías empresariales (ERP, CRM, SCM).

#### 📂 Tema 4: Toma de Decisiones y Dinámica de Sistemas
* Modelos de toma de decisiones gerenciales bajo certidumbre y riesgo.
* Introducción a la dinámica y bucles de realimentación en organizaciones.

#### 📂 Tema 5: Cultura y Cambio Organizacional
* Clima organizacional, cultura corporativa e impacto de la transformación digital.
* Metodologías para la gestión de resistencia al cambio tecnológico.

#### 📂 Tema 6: Modelos de Gestión de Calidad y Reingeniería
* Introducción al Aseguramiento de Calidad y mejora continua.
* Reingeniería de procesos organizacionales mediante la informática."""
    },
    "ALF-100": {
        "emoji": "📐",
        "title": "Álgebra y Lógica Formal",
        "prereq": "Ninguno",
        "description": "Introducción a las matemáticas discretas, lógica proposicional, teoría de conjuntos y estructuras algebraicas.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Álgebra y Lógica Formal
Fundamentos de lógica y estructuras discretas matemáticas:

#### 📂 Tema 1: Lógica Proposicional y Tablas de Verdad
* Proposiciones atómicas y moleculares. Conectivas lógicas (negación, conjunción, disyunción, implicación).
* Construcción de tablas de verdad. Análisis de tautologías, contradicciones y contingencias.

#### 📂 Tema 2: Teoría de Conjuntos
* Definición de conjuntos por extensión y comprensión. Conjunto potencia.
* Operaciones entre conjuntos (unión, intersección, diferencia, complemento) y diagramas de Venn.

#### 📂 Tema 3: Relaciones y Funciones Discretas
* Producto cartesiano. Relaciones binarias, propiedades de reflexividad, simetría y transitividad.
* Funciones discretas e inyectividad, sobreyectividad y biyectividad.

#### 📂 Tema 4: Álgebra de Boole y Circuitos Lógicos
* Definición de variables y operaciones booleanas. Compuertas lógicas de hardware (AND, OR, NOT, XOR).
* Simplificación de expresiones booleanas algebraicamente y mediante Mapas de Karnaugh.

#### 📂 Tema 5: Teoría de Grafos e Inducción Matemática
* Grafos, dígrafos, caminos, ciclos, conectividad y representación matricial.
* Principio de inducción matemática y su aplicación en demostraciones formales.

#### 📂 Tema 6: Máquinas de Estado y Lenguajes Formales
* Autómatas finitos deterministas (DFA) y no deterministas (NFA).
* Gramáticas formales y expresiones regulares en computación."""
    },
    "MAT-100": {
        "emoji": "🔢",
        "title": "Cálculo I",
        "prereq": "Ninguno",
        "description": "Estudio del cálculo infinitesimal de una variable, límites, derivadas y sus aplicaciones.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Cálculo I
Esta es la guía de contenidos indispensables para aprobar la materia:

#### 📂 Tema 1: Funciones y Gráficos
* Dominio, codominio y rango de funciones reales.
* Funciones especiales: lineales, cuadráticas, exponenciales, logarítmicas y trigonométricas.

#### 📂 Tema 2: Límites y Continuidad
* Definición intuitiva y formal de límite. Resolución de indeterminaciones (0/0, infinito/infinito).
* Límites laterales, límites infinitos y definición de continuidad en un punto.

#### 📂 Tema 3: La Derivada y Reglas
* La derivada como la pendiente de la recta tangente. Definición mediante límite.
* Reglas de diferenciación: suma, producto, cociente y regla de la cadena para funciones compuestas.

#### 📂 Tema 4: Aplicaciones de la Derivada
* Análisis de funciones: máximos, mínimos, puntos de inflexión y concavidad.
* Regla de L'Hôpital para resolver límites indeterminados y problemas de optimización.

#### 📂 Tema 5: Introducción a la Integral
* Concepto de antiderivada y la integral indefinida.
* Teorema Fundamental del Cálculo e integrales definidas para cálculo de áreas bajo curvas.

#### 📂 Tema 6: Métodos de Integración y Aplicaciones
* Integración por partes, sustitución trigonométrica y fracciones parciales.
* Aplicaciones del cálculo integral al cálculo de volúmenes de sólidos de revolución."""
    },
    "ING-100": {
        "emoji": "🗣️",
        "title": "Inglés I",
        "prereq": "Ninguno",
        "description": "Desarrollo de competencias lingüísticas básicas aplicadas a la informática y lectura de documentación técnica.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Inglés Técnico I
Competencias de traducción y lectura comprensiva orientadas a tecnología:

#### 📂 Tema 1: Gramática y Estructuras Básicas
* Estructura de oraciones en presente simple, pasado simple y futuro en inglés.
* Modificadores y sustantivos compuestos muy comunes en TI (ej. *database server*).

#### 📂 Tema 2: Vocabulario Técnico de Computación
* Glosario de términos clave: *hardware, software, framework, API, repository, deployment*.
* Traducción de verbos de acción informática: *compile, debug, run, execute, fetch, push*.

#### 📂 Tema 3: Comprensión Lectora de Manuales
* Lectura y traducción comprensiva de hojas de datos (*datasheets*), manuales de API y especificaciones de código.
* Identificación de ideas principales y traducción precisa de instrucciones técnicas.

#### 📂 Tema 4: Redacción Técnica y Documentación
* Escritura de comentarios de código estructurados en inglés.
* Redacción básica de informes técnicos de errores y documentación técnica de proyectos.

#### 📂 Tema 5: Presentaciones Técnicas y Conversación
* Estructuras conversacionales para reuniones de desarrollo ágil (Daily standups).
* Explicar el funcionamiento de un sistema o arquitectura de software de forma oral en inglés.

#### 📂 Tema 6: Traducción de Patentes y Artículos Científicos
* Técnicas de lectura rápida (skimming y scanning) aplicadas a papers académicos.
* Traducción técnica avanzada y terminología de patentes tecnológicas."""
    },

    # 2º Semestre
    "INF-110": {
        "emoji": "🖥️",
        "title": "Informática II",
        "prereq": "Informática I (INF-100)",
        "description": "Programación avanzada estructurada, punteros, gestión dinámica de memoria y estructuras fundamentales de software.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Informática II
Desarrollo estructurado y manejo dinámico de memoria:

#### 📂 Tema 1: Programación Estructurada Avanzada
* Modularidad de software, funciones de biblioteca y paso de parámetros por valor y referencia.
* Ámbito de variables globales y locales.

#### 📂 Tema 2: Punteros y Gestión de Memoria Dinámica
* Direcciones de memoria y declaración de variables puntero.
* Asignación dinámica de memoria en C/C++ (`malloc`, `free`, `new`, `delete`).

#### 📂 Tema 3: Estructuras de Datos Básicas
* Declaración y manejo de registros estructurados (structs).
* Vectores y arreglos de registros aplicados a la persistencia en archivos.

#### 📂 Tema 4: Programación Orientada a Objetos en C++ y Java
* Transición de la programación estructurada a POO.
* Conceptos prácticos de encapsulamiento y polimorfismo en lenguajes modernos.

#### 📂 Tema 5: Interfaces Gráficas de Usuario GUI
* Programación guiada por eventos.
* Creación de ventanas, formularios y controles gráficos interactivos.

#### 📂 Tema 6: Conectividad a Bases de Datos y CRUD
* Conexión básica de la aplicación a bases de datos relacionales locales (JDBC / SQLite).
* Operaciones CRUD mediante sentencias directas."""
    },
    "ARC-110": {
        "emoji": "🔌",
        "title": "Arquitectura Computacional",
        "prereq": "Informática I (INF-100)",
        "description": "Comportamiento del hardware de computadoras a nivel de puertas lógicas, microarquitectura y lenguaje ensamblador.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Arquitectura Computacional
Comportamiento interno del procesador y hardware:

#### 📂 Tema 1: Lógica Digital y Compuertas
* Diseño de circuitos combinacionales y secuenciales básicos (flip-flops, multiplexores).
* Álgebra de circuitos lógicos aplicados a la Unidad Aritmético Lógica (ALU).

#### 📂 Tema 2: Estructura de la CPU y Von Neumann
* El modelo de Von Neumann: Unidad de Control, Unidad de Procesamiento, Memoria y E/S.
* Registros del procesador (acumulador, contador de programa, puntero de pila).

#### 📂 Tema 3: Organización y Jerarquía de Memoria
* Memorias RAM y ROM. Jerarquía: Registros -> Caché L1/L2/L3 -> Memoria RAM -> Almacenamiento Secundario.
* Concepto de dirección de memoria y bus de datos/direcciones.

#### 📂 Tema 4: Set de Instrucciones y Ensamblador
* Ciclo de instrucción: Fetch, Decode, Execute.
* Programación básica en lenguaje ensamblador (Assembly x86 o MIPS): instrucciones `MOV`, `ADD`, `SUB`, `JMP`, `CMP`.

#### 📂 Tema 5: Microarquitectura y Segmentación Pipeline
* Rutas de datos de ciclo único y multiciclo.
* Segmentación del procesador (pipelining) y resolución de riesgos estructurales y de datos.

#### 📂 Tema 6: Sistemas Multiprocesador y Paralelismo
* Arquitecturas paralelas y clasificación de Flynn (SISD, SIMD, MISD, MIMD).
* Coherencia de caché en arquitecturas multinúcleo modernas."""
    },
    "MAT-110": {
        "emoji": "🌀",
        "title": "Cálculo II",
        "prereq": "Cálculo I (MAT-100)",
        "description": "Análisis matemático en varias variables, cálculo vectorial e integración múltiple.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Cálculo II
Análisis matemático multivariable:

#### 📂 Tema 1: Vectores y Geometría Analítica
* Vectores en R2 y R3. Producto escalar, producto vectorial y producto mixto.
* Ecuaciones de la recta y el plano en el espacio tridimensional.

#### 📂 Tema 2: Funciones de Varias Variables
* Dominio, límites y continuidad de funciones multivariables.
* Gráficos tridimensionales elementales (paraboloides, elipsoides, planos).

#### 📂 Tema 3: Derivadas Parciales y Gradiente
* Concepto y cálculo de derivadas parciales de primer orden y orden superior.
* Regla de la cadena multivariable. Vector Gradiente (∇f) y derivadas direccionales.

#### 📂 Tema 4: Integrales Múltiples
* Integrales dobles sobre regiones rectangulares y generales. Cambio de variables (coordenadas polares).
* Integrales triples y cálculo de volúmenes de sólidos en R3.

#### 📂 Tema 5: Integrales de Línea y Superficie
* Integrales de línea de funciones escalares y campos vectoriales.
* Parametrización de superficies e integrales de superficie de flujo.

#### 📂 Tema 6: Teoremas de Green, Stokes y Divergencia
* Teorema de Green en el plano.
* Teorema de Stokes y Teorema de la Divergencia de Gauss aplicados a electromagnetismo y fluidos."""
    },
    "MEC-110": {
        "emoji": "⚙️",
        "title": "Mecánica Clásica",
        "prereq": "Cálculo I (MAT-100)",
        "description": "Fundamentos de física clásica sobre cinemática, dinámica de partículas y leyes de conservación.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Mecánica Clásica
Leyes físicas del movimiento y fuerzas:

#### 📂 Tema 1: Vectores y Cinemática
* Análisis vectorial aplicado a magnitudes físicas.
* Movimiento en una y dos dimensiones: MRU, MRUV, caída libre, movimiento parabólico y circular.

#### 📂 Tema 2: Dinámica y Leyes de Newton
* Concepto de fuerza, masa y peso. Diagramas de cuerpo libre (DCL).
* Aplicación de las 3 Leyes de Newton en sistemas mecánicos con y sin fricción.

#### 📂 Tema 3: Trabajo y Energía
* Trabajo realizado por fuerzas constantes y variables.
* Teorema del Trabajo y la Energía. Conservación de la energía mecánica (cinética, potencial y elástica).

#### 📂 Tema 4: Estática y Dinámica Rotacional
* Equilibrio de cuerpos rígidos (primera y segunda condición de equilibrio).
* Momento de torsión (torque) y momento de inercia.

#### 📂 Tema 5: Movimiento Armónico Simple y Oscilaciones
* Ecuaciones de movimiento del oscilador armónico simple.
* Péndulo simple y péndulo físico. Sistemas amortiguados y forzados.

#### 📂 Tema 6: Ley de Gravitación Universal y Fluidos
* Ley de gravitación de Newton y órbitas planetarias (Leyes de Kepler).
* Mecánica de fluidos: densidad, presión, principio de Pascal, principio de Arquímedes y ecuación de Bernoulli."""
    },
    "ALL-110": {
        "emoji": "🧮",
        "title": "Álgebra Lineal",
        "prereq": "Álgebra y Lógica Formal (ALF-100)",
        "description": "Estudio de sistemas de ecuaciones lineales, matrices, determinantes y espacios vectoriales.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Álgebra Lineal
Estructuras lineales y álgebra matricial:

#### 📂 Tema 1: Matrices y Operaciones
* Definición y tipos de matrices (transpuesta, simétrica, identidad).
* Operaciones: suma, multiplicación escalar y multiplicación de matrices.

#### 📂 Tema 2: Determinantes y Matriz Inversa
* Métodos para calcular determinantes (Sarrus, cofactores).
* Concepto de matriz invertible y cálculo de la inversa mediante Gauss-Jordan o adjunta.

#### 📂 Tema 3: Sistemas de Ecuaciones Lineales
* Clasificación de sistemas (compatibles determinados, indeterminados e incompatibles).
* Métodos de resolución de sistemas lineales: eliminación de Gauss, regla de Cramer e inversa.

#### 📂 Tema 4: Espacios Vectoriales
* Definición de espacio y subespacio vectorial. Combinación lineal e independencia lineal.
* Base y dimensión de un espacio vectorial.

#### 📂 Tema 5: Valores y Vectores Propios
* Ecuación característica para el cálculo de valores propios (eigenvalues).
* Cálculo de vectores propios (eigenvectors) asociados y diagonalización de matrices.

#### 📂 Tema 6: Transformaciones Lineales y Aplicaciones
* Definición y propiedades de las transformaciones lineales (núcleo e imagen).
* Aplicaciones de las transformaciones lineales en gráficos por computadora y modelado."""
    },
    "ING-110": {
        "emoji": "💬",
        "title": "Inglés II",
        "prereq": "Inglés I (ING-100)",
        "description": "Lectura avanzada de código, redacción de documentación y vocabulario de tecnologías modernas.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Inglés Técnico II
Habilidades comunicativas avanzadas para el ámbito profesional de TI:

#### 📂 Tema 1: Gramática Avanzada y Tiempos Compuestos
* Tiempos verbales perfectos y voz pasiva aplicados a reportes técnicos de TI.
* Oraciones condicionales para lógica de programación.

#### 📂 Tema 2: Redacción de Reportes y Especificaciones de Software
* Estilo de redacción técnica formal para especificaciones funcionales.
* Uso de vocabulario formal para guías de usuario.

#### 📂 Tema 3: Conversación de Negocios y Entrevistas de Trabajo
* Estructuras conversacionales para entrevistas de trabajo y dinámicas de proyectos ágiles.
* Presentaciones cortas de proyectos.

#### 📂 Tema 4: Comprensión de Ponencias y Conferencias de TI
* Escucha activa y toma de notas de expositores nativos de tecnología.
* Identificación de tendencias técnicas globales.

#### 📂 Tema 5: Correspondencia Comercial y Emails Profesionales
* Normas de escritura formal para correos de soporte técnico y contacto corporativo.
* Redacción de tickets de soporte técnico.

#### 📂 Tema 6: Terminología de Inteligencia Artificial y Cloud
* Glosario moderno de Machine Learning, computación cuántica y servicios Cloud."""
    },

    # 3º Semestre
    "INF-120": {
        "emoji": "🌳",
        "title": "Estructura de Datos",
        "prereq": "Informática II (INF-110)",
        "description": "Estructuras de datos lineales y no lineales, algoritmos de ordenamiento y optimización de memoria.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Estructuras de Datos
Optimización de memoria y almacenamiento de datos complejos:

#### 📂 Tema 1: Análisis de Algoritmos y Complejidad Big-O
* Notación asintótica para medir eficiencia temporal y espacial de algoritmos.
* Comparación de algoritmos iterativos frente a recursivos.

#### 📂 Tema 2: Listas Enlazadas Simples, Dobles y Circulares
* Manejo de nodos y punteros para la creación de listas de datos dinámicas.
* Implementación de operaciones básicas (insertar, buscar, eliminar).

#### 📂 Tema 3: Pilas y Colas Dinámicas
* Implementación LIFO (Pilas) y FIFO (Colas) con punteros.
* Aplicaciones en recorrido de grafos e interpretes de código.

#### 📂 Tema 4: Árboles Binarios, AVL y Árboles de Búsqueda
* Concepto de estructuras ramificadas jerárquicas y recorridos (Preorden, Inorden, Postorden).
* Árboles auto-balanceables AVL y operaciones.

#### 📂 Tema 5: Grafos y Algoritmos de Recorrido BFS-DFS
* Representación mediante listas y matrices de adyacencia.
* Búsqueda en amplitud (BFS) y profundidad (DFS).

#### 📂 Tema 6: Tablas Hash y Algoritmos de Dispersión
* Funciones hash, resolución de colisiones y optimización de búsquedas de tiempo constante O(1)."""
    },
    "ECD-120": {
        "emoji": "📉",
        "title": "Ecuaciones Diferenciales",
        "prereq": "Cálculo II (MAT-110)",
        "description": "Modelado matemático a través de ecuaciones diferenciales ordinarias de primer orden y orden superior.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Ecuaciones Diferenciales
Modelos de cambio y su resolución analítica:

#### 📂 Tema 1: Introducción y ED de Primer Orden
* Definición, orden y grado de una ecuación diferencial.
* Métodos de resolución: Variables separables, homogéneas, lineales de primer orden (factor integrante) y exactas.

#### 📂 Tema 2: EDO de Orden Superior
* Ecuaciones lineales homogéneas con coeficientes constantes (ecuación auxiliar característica).
* Métodos no homogéneos: coeficientes indeterminados y variación de parámetros.

#### 📂 Tema 3: Transformada de Laplace
* Definición y propiedades de la transformada lineal integral de Laplace.
* Resolución de problemas de valor inicial (PVI) mediante la transformada inversa de Laplace.

#### 📂 Tema 4: Modelado con Ecuaciones Diferenciales
* Modelos aplicados: crecimiento poblacional, enfriamiento de Newton, mezclas químicas y circuitos eléctricos RLC simples.

#### 📂 Tema 5: Sistemas de Ecuaciones Diferenciales Lineales
* Métodos de resolución de sistemas lineales de primer orden (operadores diferenciales).
* Uso de autovalores y autovectores para sistemas acoplados.

#### 📂 Tema 6: Soluciones en Series de Potencias
* Solución en puntos ordinarios mediante series de potencias de Taylor.
* Método de Frobenius para soluciones de singularidades regulares."""
    },
    "ELM-120": {
        "emoji": "⚡",
        "title": "Electricidad y Magnetismo",
        "prereq": "Mecánica Clásica (MEC-110)",
        "description": "Estudio de las leyes electromagnéticas fundamentales aplicadas a sistemas e ingeniería física.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Electricidad y Magnetismo
Leyes físicas de la electricidad y campos electromagnéticos:

#### 📂 Tema 1: Electrostática y Ley de Coulomb
* Carga eléctrica, aislantes y conductores. Ley de Coulomb para la fuerza entre cargas puntuales.
* Campo eléctrico de distribuciones continuas de carga.

#### 📂 Tema 2: Campo Eléctrico y Ley de Gauss
* Flujo eléctrico y formulación de la Ley de Gauss para calcular campos eléctricos en geometrías simétricas.
* Concepto de Potencial Eléctrico y capacitancia.

#### 📂 Tema 3: Circuitos de Corriente Continua DC
* Resistencia eléctrica, resistividad y Ley de Ohm.
* Análisis de circuitos eléctricos en serie, paralelo y mixto mediante Leyes de Kirchhoff.

#### 📂 Tema 4: Campo Magnético y Ley de Ampere
* Fuerza magnética sobre cargas en movimiento (Ley de Lorentz) y conductores con corriente.
* Fuentes de campo magnético: Ley de Biot-Savart y Ley de Ampere.

#### 📂 Tema 5: Inducción Electromagnética y Ley de Faraday
* Flujo magnético y formulación de la Ley de Inducción de Faraday y Ley de Lenz.
* Inductancia mutua y autoinductancia en bobinas.

#### 📂 Tema 6: Ecuaciones de Maxwell y Circuitos AC
* Corriente de desplazamiento y formulación unificada de las 4 Ecuaciones de Maxwell.
* Comportamiento de capacitores e inductores en circuitos de corriente alterna (impedancia)."""
    },
    "EST-120": {
        "emoji": "📈",
        "title": "Estadística I",
        "prereq": "Cálculo II (MAT-110)",
        "description": "Análisis estadístico descriptivo e inferencial con aplicaciones prácticas en modelado y sistemas.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Estadística I
Análisis de datos, probabilidades y toma de decisiones:

#### 📂 Tema 1: Estadística Descriptiva y Datos
* Recopilación de datos, tablas de distribución de frecuencias y gráficos estadísticos.
* Medidas de tendencia central (media, mediana, moda) y de dispersión (varianza, desviación estándar).

#### 📂 Tema 2: Teoría de Probabilidades
* Experimento aleatorio, espacio muestral y eventos. Definición clásica, axiomática y condicional de probabilidad.
* Teorema de Bayes e independencia de eventos.

#### 📂 Tema 3: Variables Aleatorias y Distribuciones
* Variables aleatorias discretas (Binomial, Poisson) y continuas (Normal, Normal estándar).
* Uso de tablas estadísticas para el cálculo de probabilidades.

#### 📂 Tema 4: Regresión Lineal y Correlación
* Diagrama de dispersión y cálculo de la recta de regresión de mínimos cuadrados.
* Coeficiente de correlación de Pearson y análisis de varianza.

#### 📂 Tema 5: Inferencia Estadística y Pruebas de Hipótesis
* Concepto de muestreo y teorema del límite central.
* Formulación y prueba de hipótesis para medias y proporciones (Prueba Z y T-Student).

#### 📂 Tema 6: Estimación de Parámetros y Muestreo
* Intervalos de confianza para la media de una población.
* Métodos cuantitativos de selección de tamaño de muestra óptimo."""
    },
    "QUE-120": {
        "emoji": "🦙",
        "title": "Quechua",
        "prereq": "Ninguno",
        "description": "Desarrollo de habilidades de comunicación básica en Quechua y contextualización sociocultural en la región.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Quechua (Idioma Originario)
Desarrollo de competencias lingüísticas en Quechua:

#### 📂 Tema 1: Saludos y Gramática Básica Quechua
* Saludos iniciales (Napaykuna) y pronombres personales (Ñoqa, Qan, Pay).
* Sufijos aglutinantes básicos para la conjugación verbal en tiempo presente.

#### 📂 Tema 2: Yupaykuna y Vocabulario Diario
* Los números en quechua (Yupaykuna) del 1 al 100 y operaciones simples.
* Vocabulario de la familia (Ayllu), la casa (Wasi) y la naturaleza (Pachamama).

#### 📂 Tema 3: Conversaciones Básicas y Cultura
* Diálogos de presentación personal (nombre, procedencia y ocupación).
* Costumbres y cosmovisión andina en el altiplano boliviano.

#### 📂 Tema 4: Cuerpo Humano y Salud en la Comunidad
* Vocabulario del cuerpo humano (Kurku) y terminología de salud andina.
* Diálogos simulados de atención y descripción de dolencias en Quechua.

#### 📂 Tema 5: Flora, Fauna y Actividades Agrícolas
* Terminología sobre animales (Juywakuna) y plantas típicas del altiplano.
* Expresiones referidas al cultivo de la tierra e interacción comunitaria.

#### 📂 Tema 6: Cuentos Tradicionales y Expresión Oral
* Lectura y entonación de canciones (Takiykuna) y cuentos cortos tradicionales.
* Conversación fluida final y expresión verbal de ideas complejas."""
    },
    "CBA-120": {
        "emoji": "📊",
        "title": "Contabilidad Básica",
        "prereq": "Administración I (ADM-100)",
        "description": "Principios contables fundamentales para el registro de transacciones comerciales y elaboración de estados financieros.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Contabilidad Básica
Procesos financieros y control contable en empresas:

#### 📂 Tema 1: Introducción a la Contabilidad y Transacciones
* Definición de contabilidad, objetivos y usuarios de la información contable.
* Clasificación de cuentas: Activos, Pasivos, Patrimonio, Ingresos y Egresos.

#### 📂 Tema 2: Partida Doble y Asientos Contables
* La ecuación contable: Activo = Pasivo + Patrimonio.
* Reglas del cargo y del abono (Debe y Haber). Registro contable de transacciones comerciales.

#### 📂 Tema 3: Libros Diario y Mayor
* Estructuración y llenado del Libro Diario (asientos contables cronológicos).
* Pase al Libro Mayor (centralización de saldos por cuenta contable).

#### 📂 Tema 4: Balance de Comprobación y Estados Financieros
* Elaboración del Balance de Comprobación de Sumas y Saldos.
* Preparación de Estados Financieros básicos: Estado de Resultados y Balance General.

#### 📂 Tema 5: Ajustes Contables y Hoja de Trabajo
* Asientos de ajuste (depreciaciones, acumulaciones, diferidos).
* Estructuración de la Hoja de Trabajo de 10 o 12 columnas.

#### 📂 Tema 6: Análisis e Interpretación de Estados Financieros
* Métodos de análisis vertical y horizontal.
* Cálculo de razones financieras básicas (liquidez, solvencia y rentabilidad)."""
    },

    # 4º Semestre
    "INF-130": {
        "emoji": "👾",
        "title": "Lenguajes de Programación",
        "prereq": "Informática II (INF-110)",
        "description": "Estudio comparativo de los paradigmas de programación, análisis semántico y compiladores.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Lenguajes de Programación
Comprensión profunda de la estructura y ejecución del código:

#### 📂 Tema 1: Paradigmas de Programación y Sintaxis Comparada
* Concepto de paradigma: imperativo, funcional, lógico y orientado a objetos.
* Análisis de sintaxis mediante gramáticas libres de contexto.

#### 📂 Tema 2: Tipado de Datos y Expresiones
* Tipado estático frente a dinámico; tipado fuerte frente a débil.
* Evaluación de expresiones de control y reglas de precedencia.

#### 📂 Tema 3: Programación Funcional y Expresiones Lambda
* Funciones de primera clase y de orden superior en lenguajes como Python y Haskell.
* Expresiones Lambda y clausuras (closures).

#### 📂 Tema 4: Programación Concurrente y Multihilo
* Procesos independientes e hilos ligeros de ejecución compartida.
* Sincronización mediante semáforos, monitores y exclusión mutua.

#### 📂 Tema 5: Expresiones Regulares y Metaprogramación
* Diseño de analizadores léxicos simples usando expresiones regulares.
* Metaprogramación y reflexión en tiempo de ejecución.

#### 📂 Tema 6: Compiladores e Intérpretes Básicos
* Fases de la traducción de lenguajes: análisis léxico, sintáctico, semántico y generación de código."""
    },
    "INS-130": {
        "emoji": "🌐",
        "title": "Ingeniería de Sistemas I",
        "prereq": "Administración I (ADM-100)",
        "description": "Teoría general de sistemas, modelado de cajas negras e ingeniería de requerimientos inicial.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Ingeniería de Sistemas I
Teoría general y modelado holístico de sistemas complejos:

#### 📂 Tema 1: Teoría General de Sistemas TGS
* Origen e introducción a la TGS de Ludwig von Bertalanffy.
* Definición, límites y clasificación de sistemas (abiertos, cerrados, conceptuales).

#### 📂 Tema 2: Modelado de Sistemas y Ciclo de Vida
* Representación sistémica usando diagramas causales y diagramas de caja negra.
* Dinámica de sistemas y ciclos de retroalimentación (positivos y negativos).

#### 📂 Tema 3: Metodología de Sistemas Blandos MSB
* Enfoque de Peter Checkland para la solución de problemas complejos con factores humanos.
* Las 7 etapas de la MSB y definición de sistemas raíz (CATWOE).

#### 📂 Tema 4: Ingeniería de Requerimientos
* Proceso de elicitación, análisis, especificación y validación de requerimientos de software.

#### 📂 Tema 5: Modelos de Negocios y Arquitectura Enterprise
* Estructuras de modelado organizacional (TOGAF / Zachman).
* Alineación de procesos empresariales y sistemas tecnológicos.

#### 📂 Tema 6: Calidad de Sistemas y Aseguramiento
* Estándares internacionales de calidad (ISO 9001 / ISO 25010).
* Pruebas de integración de sistemas y métricas de madurez organizativa."""
    },
    "BDD-130": {
        "emoji": "🗄️",
        "title": "Bases de Datos I",
        "prereq": "Estructura de Datos (INF-120)",
        "description": "Modelado de datos relacionales, lenguaje de consultas SQL y normalización de bases de datos.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Bases de Datos I
Diseño relacional y programación de bases de datos:

#### 📂 Tema 1: Modelado Entidad-Relación ER
* Entidades, atributos, claves primarias y relaciones de cardinalidad.
* Construcción de diagramas conceptuales de bases de datos basados en requerimientos.

#### 📂 Tema 2: Modelo Relacional y Normalización
* Paso del diagrama ER a tablas relacionales con llaves foráneas.
* Proceso de normalización de datos (1FN, 2FN y 3FN) para eliminar redundancias y anomalías.

#### 📂 Tema 3: Lenguaje SQL y Consultas DDL-DML
* Creación de estructuras (CREATE TABLE, ALTER TABLE).
* Consultas avanzadas (SELECT con JOINs, GROUP BY, HAVING, subconsultas).

#### 📂 Tema 4: Transacciones y Control de Concurrencia
* Propiedades ACID de las transacciones (Atomicidad, Consistencia, Isolation, Durabilidad).
* Control de accesos concurrentes y bloqueos.

#### 📂 Tema 5: Seguridad, Roles y Privilegios en BDD
* Creación de usuarios y asignación de permisos (GRANT y REVOKE).
* Cifrado de datos en tránsito y en reposo en el motor de base de datos.

#### 📂 Tema 6: Bases de Datos NoSQL y Big Data
* Diferencias entre bases de datos relacionales SQL y no relacionales NoSQL (MongoDB, Redis).
* Modelos de almacenamiento documental, clave-valor y de base gráfica."""
    },
    "EST-130": {
        "emoji": "📊",
        "title": "Estadística II",
        "prereq": "Estadística I (EST-120)",
        "description": "Análisis estadístico multivariado, pruebas de hipótesis, ANOVA y regresión lineal avanzada.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Estadística II
Técnicas estadísticas avanzadas de modelado e inferencia:

#### 📂 Tema 1: Probabilidad Avanzada y Variables Aleatorias Bidimensionales
* Distribuciones marginales y condicionales.
* Esperanza condicional, covarianza y coeficiente de correlación lineal.

#### 📂 Tema 2: Estimación Puntual y de Intervalo
* Propiedades de los estimadores (insesgadez, consistencia, eficiencia).
* Estimación por intervalos de confianza para la diferencia de medias y proporciones.

#### 📂 Tema 3: Pruebas de Hipótesis Paramétricas y No Paramétricas
* Errores de Tipo I y Tipo II. Pruebas de hipótesis para dos poblaciones independientes y pareadas.
* Pruebas de bondad de ajuste (Chi-cuadrada) y pruebas de independencia.

#### 📂 Tema 4: Análisis de Varianza ANOVA
* Diseño de un solo factor (One-way ANOVA) para comparar múltiples medias.
* Diseños de bloques aleatorizados y comparaciones múltiples (Tukey).

#### 📂 Tema 5: Regresión Múltiple y Series de Tiempo
* Modelo de regresión lineal múltiple: estimación de coeficientes y pruebas de significancia.
* Conceptos básicos de series de tiempo y descomposición.

#### 📂 Tema 6: Diseño de Experimentos y Estadística Multivariada
* Principios del diseño experimental y análisis factorial básico.
* Introducción al análisis de componentes principales y agrupamiento estadístico."""
    },
    "CEL-103": {
        "emoji": "🔋",
        "title": "Circuitos Electrónicos",
        "prereq": "Electricidad y Magnetismo (ELM-120)",
        "description": "Diseño y análisis de circuitos con semiconductores, transistores y amplificadores operacionales.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Circuitos Electrónicos
Diseño y comportamiento de circuitos con semiconductores:

#### 📂 Tema 1: Componentes Pasivos y Leyes de Kirchhoff
* Análisis de circuitos RC, RL y RLC en corriente alterna.
* Métodos de análisis de mallas y nodos (LKV y LKC).

#### 📂 Tema 2: Diodos Semiconductores
* Unión P-N y física de semiconductores. Diodo ideal y real.
* Circuitos aplicados: rectificadores de media onda, onda completa y regulador Zener.

#### 📂 Tema 3: Transistores BJT y FET
* Estructura y zonas de operación del transistor BJT (corte, saturación y activa).
* Transistores de efecto de campo (JFET y MOSFET). Aplicaciones en conmutación y amplificación.

#### 📂 Tema 4: Amplificadores Operacionales
* El amplificador operacional ideal.
* Configuraciones básicas: amplificador inversor, no inversor, sumador y comparador.

#### 📂 Tema 5: Electrónica Digital y Compuertas
* Sistemas numéricos digitales y álgebra de Boole.
* Diseño de circuitos lógicos combinacionales con puertas lógicas básicas.

#### 📂 Tema 6: Osciladores, Temporizadores y Fuentes de Poder
* Configuración y aplicaciones del temporizador integrado 555.
* Diseño básico de fuentes de alimentación reguladas lineales."""
    },
    "SIC-130": {
        "emoji": "💸",
        "title": "Sistemas Informáticos Contables",
        "prereq": "Contabilidad Básica (CBA-120)",
        "description": "Integración de la contabilidad empresarial con herramientas y software de automatización informática.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Sistemas Informáticos Contables
Integración contable mediante sistemas automatizados:

#### 📂 Tema 1: Automatización y Sistemas Contables
* Arquitectura y estructura de un sistema informático contable moderno.
* Configuración del Plan de Cuentas digital en software de contabilidad.

#### 📂 Tema 2: Módulos de Facturación e Inventarios
* Procesamiento digital de compras y ventas. Integración con inventarios (método PEPS, promedio ponderado).
* Emisión automática de facturas y notas de crédito.

#### 📂 Tema 3: Planillas de Sueldos y Generación de Reportes
* Automatización de planillas de sueldos y aportes de ley (AFP, Caja de Salud, retenciones).
* Generación del Libro Diario, Mayor y Estados Financieros automatizados.

#### 📂 Tema 4: Declaraciones Tributarias e Impuestos Automatizados
* Configuración del módulo de impuestos (IVA, IT, IUE en Bolivia).
* Exportación automatizada del Libro de Compras y Ventas (LCV) para envío estatal.

#### 📂 Tema 5: Auditoría de Sistemas Contables
* Controles de seguridad para evitar fraudes en el ingreso de registros contables.
* Pistas de auditoría interna en bases de datos contables (logs de transacciones).

#### 📂 Tema 6: Seguridad y Respaldo de Datos Financieros
* Políticas de copias de seguridad de los sistemas financieros en local y en la nube.
* Encriptación de datos contables confidenciales y restauración ante desastres."""
    },

    # 5º Semestre
    "INO-140": {
        "emoji": "🎯",
        "title": "Investigación Operativa I",
        "prereq": "Álgebra Lineal (ALL-110)",
        "description": "Optimización matemática de recursos mediante programación lineal y análisis de decisiones cuantitativas.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Investigación Operativa I
Optimización matemática para la toma de decisiones críticas:

#### 📂 Tema 1: Programación Lineal y Modelado
* Formulación matemática de problemas de optimización: variables de decisión, función objetivo y restricciones.
* Resolución gráfica de problemas de dos variables.

#### 📂 Tema 2: Método Simplex
* Algoritmo Simplex en formato tabular para problemas de múltiples variables.
* Método de la Gran M y método de las dos fases. Análisis de sensibilidad.

#### 📂 Tema 3: Redes PERT-CPM
* Modelado de proyectos mediante diagramas de red de actividades en nodos/flechas.
* Cálculo de tiempos tempranos, tardíos, holguras y determinación de la ruta crítica.

#### 📂 Tema 4: Teoría de Colas y Modelos de Inventarios
* Estructura básica de sistemas de líneas de espera. Modelos de colas exponenciales de un canal (M/M/1).
* Modelo clásico de cantidad económica de pedido (EOQ) para la gestión de inventarios.

#### 📂 Tema 5: Programación Dinámica e Entera
* Modelos de programación entera (métodos de ramificación y acotación).
* Principio de optimalidad de Bellman y programación dinámica determinista.

#### 📂 Tema 6: Modelos de Simulación Montecarlo y Decisiones
* Simulación Montecarlo para el análisis de riesgo e incertidumbre en decisiones.
* Estructuración de árboles de decisión y matrices de pago."""
    },
    "INS-140": {
        "emoji": "🗺️",
        "title": "Ingeniería de Sistemas II",
        "prereq": "Ingeniería de Sistemas I (INS-130)",
        "description": "Dinámica de sistemas, modelación organizacional por computadora y requerimientos de sistemas avanzados.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Ingeniería de Sistemas II
Modelado avanzado de dinámicas organizacionales complejas:

#### 📂 Tema 1: Enfoque de Sistemas Aplicado a Organizaciones
* El pensamiento sistémico en las estructuras administrativas modernas.
* Arquetipos organizacionales e intervenciones de ingeniería.

#### 📂 Tema 2: Dinámica de Sistemas Complejos y Bucles de Retorno
* Bucles de realimentación reforzadora y compensadora.
* Estructura de flujos, niveles y diagramas de Forrester.

#### 📂 Tema 3: Modelos de Simulación Organizacional (Vensim / Stella)
* Construcción informática de modelos de simulación dinámica organizacional.
* Análisis de escenarios e impacto del cambio de parámetros.

#### 📂 Tema 4: Ingeniería de Requerimientos Avanzada y UML
* Uso avanzado de Lenguaje de Modelado Unificado (UML).
* Diagramas de secuencia, actividades y estados aplicados a requerimientos de software.

#### 📂 Tema 5: Arquitectura de Información y Diseño de Sistemas
* Jerarquías de la información empresarial.
* Diseño conceptual de sistemas de información distribuidos.

#### 📂 Tema 6: Evaluación de Usabilidad e Impacto Tecnológico
* Auditorías de usabilidad e interfaz y diseño centrado en el usuario.
* Medición del impacto socio-técnico de los nuevos sistemas instalados."""
    },
    "DPW-140": {
        "emoji": "🌐",
        "title": "Diseño de Páginas Web I",
        "prereq": "Lenguajes de Programación (INF-130)",
        "description": "Desarrollo web Fullstack inicial, maquetación adaptativa y lógica de servidor en PHP.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Desarrollo Web I
Desarrollo web Fullstack moderno:

#### 📂 Tema 1: Maquetación Estructurada HTML5
* Etiquetas semánticas estándar de HTML5. Estructuración y jerarquía de un sitio web.
* Formularios, validación nativa y accesibilidad web.

#### 📂 Tema 2: Diseño Responsivo y Adaptativo CSS3
* Estilización con Flexbox y CSS Grid.
* Media Queries para diseño adaptativo en dispositivos móviles, tablets y desktops.

#### 📂 Tema 3: Programación Frontend JavaScript
* Sintaxis básica de JS, manipulación del DOM y manejo de eventos.
* Solicitudes asíncronas utilizando Fetch API y promesas.

#### 📂 Tema 4: Desarrollo Backend y Servidor PHP
* Configuración del entorno de servidor local (XAMPP / Apache).
* Programación estructurada en PHP, variables globales `$_POST` y `$_GET`, y conexiones seguras a MySQL para operaciones CRUD.

#### 📂 Tema 5: Arquitectura MVC y Frameworks Modernos
* Patrón de diseño Modelo-Vista-Controlador (MVC) en el desarrollo de aplicaciones.
* Conceptos básicos de librerías modernas de frontend y backend.

#### 📂 Tema 6: APIs RESTful y Seguridad en Aplicaciones Web
* Diseño y consumo de servicios API REST en formato JSON.
* Medidas de seguridad contra inyecciones SQL y ataques Cross-Site Scripting (XSS)."""
    },
    "BDD-140": {
        "emoji": "💾",
        "title": "Bases de Datos II",
        "prereq": "Bases de Datos I (BDD-130)",
        "description": "SQL avanzado, procedimientos almacenados, optimización de consultas y afinamiento de rendimiento.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Bases de Datos II
Desarrollo y administración avanzada de motores de bases de datos relacionales:

#### 📂 Tema 1: SQL Avanzado y Funciones de Ventana
* Consultas analíticas utilizando cláusulas `OVER`, `PARTITION BY` y `ORDER BY`.
* Expresiones de tabla comunes (CTEs) recursivas e integradas.

#### 📂 Tema 2: Triggers y Procedimientos Almacenados PL-pgSQL
* Creación de disparadores (Triggers) avanzados para integridad referencial compleja.
* Programación en lenguaje estructurado de servidor en PostgreSQL/Oracle.

#### 📂 Tema 3: Optimización de Consultas (Performance Tuning) y Planes de Ejecución
* Interpretación de planes de ejecución (`EXPLAIN ANALYZE`).
* Optimización de consultas complejas y subconsultas pesadas.

#### 📂 Tema 4: Administración de Bases de Datos (DBA), Índices y Particionamiento
* Creación y administración de índices (B-Tree, Hash, GIN).
* Estrategias de particionamiento de tablas y tablas distribuidas.

#### 📂 Tema 5: Alta Disponibilidad, Replicación y Respaldos Automatizados
* Configuración de servidores esclavos y replicación por flujo de datos.
* Políticas de seguridad y automatización de respaldos (Backups).

#### 📂 Tema 6: Bases de Datos Distribuidas y NoSQL
* Conceptos básicos de consistencia y teorema CAP en bases de datos distribuidas.
* Modelado en bases de datos documentales (MongoDB)."""
    },
    "DGI-140": {
        "emoji": "🎨",
        "title": "Diseño Gráfico de Interfaz",
        "prereq": "Bases de Datos I (BDD-130)",
        "description": "Diseño visual, prototipado interactivo UI/UX y creación de sistemas de diseño en Figma.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Diseño Gráfico de Interfaz (UI/UX)
Diseño de interfaces web y móviles profesionales:

#### 📂 Tema 1: Experiencia de Usuario UX y Usabilidad
* Principios de diseño centrado en el usuario (Heurísticas de Jakob Nielsen).
* Flujos de usuario (User Flows), wireframes y prototipado rápido de software.

#### 📂 Tema 2: Diseño Visual UI y Maquetación
* Teoría del color, tipografía, consistencia y cuadrículas (Grid systems).
* Herramientas modernas de diseño (Figma / Adobe XD) aplicadas a mockups interactivos.

#### 📂 Tema 3: Prototipado Interactivo y Wireframes en Figma
* Diseño de transiciones animadas y flujos de pantallas vinculadas.
* Creación de componentes inteligentes reutilizables y variantes.

#### 📂 Tema 4: Psicología del Color y Tipografía UI
* Teoría del color aplicada a la retención de usuarios.
* Jerarquías de texto y legibilidad en dispositivos digitales.

#### 📂 Tema 5: Diseño de Sistemas de Diseño (Design Systems)
* Creación de bibliotecas de componentes, iconos y variables tipográficas.
* Consistencia visual en sistemas multi-plataforma.

#### 📂 Tema 6: Pruebas A-B y Evaluación de Interfaces
* Métodos cuantitativos y cualitativos para evaluar el impacto de interfaces.
* Optimización de tasas de conversión basadas en diseño UI."""
    },
    "OPT-140": {
        "emoji": "🤖",
        "title": "Optativa I",
        "prereq": "Circuitos Electrónicos (CEL-103)",
        "description": "Internet de las Cosas (IoT), robótica básica, sensores y prototipado en hardware con Arduino.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Materia Optativa (Internet de las Cosas - IoT)
Introducción al hardware libre e IoT:

#### 📂 Tema 1: Introducción a IoT y Microcontroladores
* Arquitectura de plataformas de hardware abierto (Arduino, ESP8266/ESP32).
* Programación básica en C/C++ para hardware físico.

#### 📂 Tema 2: Sensores y Actuadores
* Conexión y lectura de sensores analógicos y digitales (temperatura, ultrasonido, luz).
* Control de actuadores físicos: servomotores, relés de potencia, zumbadores y pantallas LCD.

#### 📂 Tema 3: Protocolos de Comunicación y Redes Inalámbricas
* Envío de datos por protocolos serie (I2C, SPI, UART).
* Conectividad inalámbrica: Wi-Fi, Bluetooth e introducción al protocolo MQTT para IoT.

#### 📂 Tema 4: Prototipado y Proyectos Arduino
* Diseño y ensamblaje de proyectos prácticos orientados a la automatización del hogar (domótica) o monitorización remota.

#### 📂 Tema 5: Interfaces de Usuario para IoT y Dashboard Web
* Creación de interfaces gráficas para la monitorización de datos en tiempo real (Blynk / Node-RED).
* Conexión de sensores de hardware con bases de datos en la nube.

#### 📂 Tema 6: Seguridad en Redes IoT y Aplicaciones Industriales
* Principios de encriptación de datos inalámbricos y autenticación segura de sensores.
* IoT industrial (IIoT) y su rol en la manufactura automatizada moderna."""
    },

    # 6º Semestre
    "INO-150": {
        "emoji": "🔮",
        "title": "Investigación Operativa II",
        "prereq": "Investigación Operativa I (INO-140)",
        "description": "Programación dinámica, simulación Montecarlo, teoría de decisiones y optimización heurística.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Investigación Operativa II
Modelos matemáticos estocásticos avanzados para toma de decisiones:

#### 📂 Tema 1: Programación Multiobjetivo y Métodos de Optimización
* Optimización de problemas con múltiples criterios de evaluación concurrentes.
* Métodos de suma ponderada y restricciones de frontera.

#### 📂 Tema 2: Teoría de Juegos y Modelos de Decisión Colectiva
* Juegos cooperativos y no cooperativos en condiciones de conflicto.
* Equilibrio de Nash y estrategias mixtas.

#### 📂 Tema 3: Procesos de Decisión de Markov
* Modelado estocástico de transiciones de estado a través del tiempo.
* Ecuaciones de Bellman aplicadas al control óptimo de inventarios.

#### 📂 Tema 4: Teoría de Colas Avanzada y Redes de Colas
* Modelos de colas con distribuciones generales y múltiples servidores acoplados.
* Ecuación de Little y redes de Jackson.

#### 📂 Tema 5: Modelado con Variables Estocásticas
* Representación matemática del riesgo en la cadena de suministros.
* Simulación de procesos bajo incertidumbre estadística.

#### 📂 Tema 6: Optimización Heurística y Algoritmos Genéticos
* Métodos de búsqueda metaheurística para problemas NP-duros (Búsqueda Tabú, Recocido Simulado).
* Operadores genéticos: selección, cruce y mutación computacional."""
    },
    "INS-150": {
        "emoji": "🏛️",
        "title": "Ingeniería de Sistemas III",
        "prereq": "Ingeniería de Sistemas II (INS-140)",
        "description": "Viabilidad organizacional, modelo del sistema viable (VSM) y reingeniería sistémica de procesos.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Ingeniería de Sistemas III
Modelado y gobernanza sistémica de organizaciones complejas de alto desempeño:

#### 📂 Tema 1: Viabilidad de Sistemas y Enfoque de Viabilidad Viable (VSM)
* Introducción a la cibernética organizacional de Stafford Beer.
* Los 5 sistemas del VSM: Operaciones, Coordinación, Control, Inteligencia y Políticas.

#### 📂 Tema 2: Ciberorganizaciones y Diseño Sistémico
* Estructuras recursivas de viabilidad organizacional.
* El rol del flujo de información ciber-segura en la toma de decisiones distribuidas.

#### 📂 Tema 3: Auditoría Sistémica de Procesos Organizacionales
* Métodos de auditoría basados en el VSM para detectar cuellos de botella de información.
* Diagnóstico de patologías organizacionales complejas.

#### 📂 Tema 4: Gestión del Conocimiento y Aprendizaje Organizacional
* Modelos de transferencia de conocimiento tácito y explícito en la empresa (Nonaka-Takeuchi).
* Diseño de plataformas tecnológicas de soporte al aprendizaje.

#### 📂 Tema 5: Ingeniería de Reingeniería de Negocios (BPR)
* Rediseño radical de flujos de trabajo organizacionales soportados por la TI.
* Medición de eficiencia de la reingeniería aplicada.

#### 📂 Tema 6: Liderazgo Sistémico y Gobernanza
* Toma de decisiones éticas y de responsabilidad en sistemas socio-técnicos complejos.
* Mecanismos de gobernanza corporativa para la resiliencia organizativa."""
    },
    "DPW-150": {
        "emoji": "⚡",
        "title": "Diseño de Páginas Web II",
        "prereq": "Diseño de Páginas Web I (DPW-140)",
        "description": "Desarrollo frontend moderno con frameworks (React/Vue), backend en Node.js y APIs seguras.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Desarrollo Web II
Construcción de aplicaciones web distribuidas complejas (SPAs):

#### 📂 Tema 1: Desarrollo Frontend Moderno con Frameworks (React/Vue)
* Arquitectura orientada a componentes interactivos y ciclo de vida de componentes.
* Uso de estados locales y propiedades (`props`).

#### 📂 Tema 2: Manejo de Estado Global y Enrutamiento Web
* Soluciones de manejo de estado en aplicaciones complejas (Redux / Pinia).
* Configuración de rutas dinámicas del lado del cliente.

#### 📂 Tema 3: Desarrollo Backend con Node.js y Express
* Programación asíncrona de servidores web utilizando JavaScript moderno.
* Creación de middlewares para autenticación y validación de datos.

#### 📂 Tema 4: Bases de Datos NoSQL en la Web (MongoDB / Firebase)
* Modelado de bases de datos documentales para aplicaciones web en tiempo real.
* Integración del ORM (Mongoose) en servidores Express.

#### 📂 Tema 5: Autenticación JWT y Seguridad Web Avanzada
* Autenticación basada en JSON Web Tokens (JWT) y cookies seguras.
* Prevención de ataques mediante CORS y cabeceras Helmet.

#### 📂 Tema 6: Despliegue en la Nube (Cloud Deployment) y Serverless
* Despliegue de aplicaciones frontend y backend en servidores PaaS y VPS.
* Conceptos introductorios al despliegue serverless."""
    },
    "BDD-150": {
        "emoji": "🗃️",
        "title": "Bases de Datos III",
        "prereq": "Bases de Datos II (BDD-140)",
        "description": "Bodegas de datos (Data Warehouses), minería de datos, Big Data y modelado multidimensional.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Bases de Datos III
Almacenamiento analítico y análisis de datos masivos (Business Intelligence):

#### 📂 Tema 1: Arquitectura de Bodegas de Datos (Data Warehousing)
* Diferencias entre sistemas OLTP (operativo) y OLAP (analítico).
* Concepto de repositorio centralizado de datos e infraestructura asociada.

#### 📂 Tema 2: Modelado Dimensional: Hechos y Dimensiones (Estrella/Copo de Nieve)
* Diseño lógico de almacenes de datos: tablas de hechos y tablas de dimensiones.
* Jerarquías de dimensiones y dimensiones que cambian lentamente (SCD).

#### 📂 Tema 3: Procesos ETL (Extracción, Transformación y Carga)
* Diseño de flujos de extracción de datos de fuentes heterogéneas.
* Transformación de datos (limpieza, normalización) e inserción en la bodega.

#### 📂 Tema 4: Minería de Datos (Data Mining) y Algoritmos Asociativos
* Descubrimiento de patrones ocultos en grandes conjuntos de datos.
* Algoritmos de asociación (Apriori), clasificación y clustering de datos.

#### 📂 Tema 5: Análisis Multidimensional OLAP
* Consultas complejas utilizando cubos de datos y operaciones de agregación (Drill-down, Roll-up, Slice, Dice).
* Herramientas de visualización de inteligencia de negocios.

#### 📂 Tema 6: Big Data e Integración con Spark/Hadoop
* Introducción al ecosistema de procesamiento distribuido de datos masivos.
* Modelado básico MapReduce y consultas SQL masivas."""
    },
    "PED-150": {
        "emoji": "💼",
        "title": "Preparación y Evaluación de Proyectos",
        "prereq": "Sistemas Informáticos Contables (SIC-130)",
        "description": "Formulación de proyectos, estudios de viabilidad comercial y evaluación financiera (VAN/TIR).",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Preparación de Proyectos
Formulación y evaluación matemática de proyectos de inversión:

#### 📂 Tema 1: Identificación del Proyecto y Ciclo de Vida
* Definición de proyectos. Fases del ciclo de vida (preinversión, inversión, operación).
* Detección de necesidades y formulación de la idea del proyecto.

#### 📂 Tema 2: Estudio de Mercado y Aspectos Técnicos
* Análisis de demanda y oferta del servicio o producto. Estrategias de precios y canales.
* Tamaño y localización óptima del proyecto de ingeniería.

#### 📂 Tema 3: Evaluación Económica y Financiera VAN-TIR
* Estructuración del Flujo de Caja proyectado (ingresos, costos operativos, inversiones, financiamiento).
* Cálculo y análisis de métricas de rentabilidad financiera: Valor Actual Neto (VAN) y Tasa Interna de Retorno (TIR).

#### 📂 Tema 4: Análisis de Riesgo e Impacto Ambiental
* Análisis de sensibilidad ante cambios en variables críticas (costos, precios).
* Evaluación ética del impacto ambiental y social del proyecto en su entorno.

#### 📂 Tema 5: Financiamiento del Proyecto y Estructura de Capital
* Fuentes de financiamiento internas (capital propio) y externas (crédito bancario, bonos).
* Cálculo del Costo Promedio Ponderado de Capital (WACC / CPPC).

#### 📂 Tema 6: Plan de Ejecución, Seguimiento y Cierre
* Planificación de la ejecución física del proyecto utilizando diagramas de Gantt e hitos de control.
* Auditoría posterior al cierre de proyecto y lecciones aprendidas."""
    },
    "SOP-150": {
        "emoji": "🐧",
        "title": "Sistemas Operativos",
        "prereq": "Arquitectura Computacional (ARC-110)",
        "description": "Principios de diseño, gestión de procesos, concurrencia, administración de memoria RAM y sistemas de archivos.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Sistemas Operativos
Administración de hardware y recursos lógicos por el software del sistema:

#### 📂 Tema 1: Introducción e Historia de los SO
* Evolución histórica, funciones principales y arquitectura de un sistema operativo (monolítico, micronúcleo).
* Interfaz de llamadas al sistema (System Calls).

#### 📂 Tema 2: Gestión de Procesos e Hilos
* Concepto de proceso, estados de un proceso (listo, ejecutándose, bloqueado) y bloque de control de procesos (PCB).
* Diferencia entre procesos e hilos (threads).

#### 📂 Tema 3: Planificación de CPU y Sincronización
* Algoritmos de planificación del procesador (FCFS, Shortest Job First, Round Robin).
* Problemas de concurrencia y sincronización: exclusión mutua, semáforos y condiciones de carrera.

#### 📂 Tema 4: Administración de Memoria RAM y Virtual
* Métodos de asignación de memoria: paginación, segmentación y fragmentación (interna y externa).
* Algoritmos de reemplazo de páginas en memoria virtual (FIFO, LRU).

#### 📂 Tema 5: Sistema de Archivos y Almacenamiento
* Estructura de directorios y métodos de asignación de espacio en disco (FAT, NTFS, ext4).
* Gestión de dispositivos de almacenamiento secundario y algoritmos de planificación del brazo de disco.

#### 📂 Tema 6: Seguridad y Protección en Sistemas Operativos
* Mecanismos de protección de memoria y control de acceso a archivos.
* Seguridad contra malware y vulnerabilidades a nivel de núcleo (Kernel)."""
    },

    # 7º Semestre
    "ING-160": {
        "emoji": "🛠️",
        "title": "Ingeniería de Software",
        "prereq": "Ingeniería de Sistemas III (INS-150)",
        "description": "Ingeniería de requerimientos avanzada, metodologías de desarrollo de software ágiles y QA.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Ingeniería de Software
Procesos estructurados y ágiles para el desarrollo de software industrial de calidad:

#### 📂 Tema 1: Introducción a la Ingeniería de Software y Modelos de Proceso
* Evolución del desarrollo de software y crisis del software.
* Ciclo de vida clásico (Cascada, Espiral) frente al enfoque moderno iterativo.

#### 📂 Tema 2: Metodologías Ágiles (Scrum, Kanban, XP)
* Fundamentos y manifiesto ágil de desarrollo de software.
* Roles, artefactos y ceremonias del marco de trabajo Scrum.

#### 📂 Tema 3: Diseño de Arquitectura de Software y Patrones de Diseño
* Patrones estructurales y de comportamiento comunes (MVC, Factory, Singleton).
* Acoplamiento, cohesión y diseño orientado a componentes independientes.

#### 📂 Tema 4: Ingeniería de Requerimientos y Casos de Uso
* Modelado estructurado de requerimientos: historias de usuario y casos de uso en diagramas.
* Prototipado y validación ágil de especificaciones con el cliente.

#### 📂 Tema 5: Pruebas de Software (Unitarias, Integración, Sistema) y QA
* Estrategias de aseguramiento de calidad (QA) y pruebas de caja negra y caja blanca.
* Automatización de pruebas unitarias básicas y pruebas de rendimiento.

#### 📂 Tema 6: Mantenimiento de Software, Refactorización y Gestión de Configuraciones
* Deuda técnica del código y técnicas de refactorización limpia.
* Sistemas de control de versiones distribuidos y flujos de ramificación profesionales."""
    },
    "TEE-160": {
        "emoji": "🚀",
        "title": "Tecnologías Emergentes",
        "prereq": "Lenguajes de Programación (INF-130)",
        "description": "Virtualización, microservicios, DevOps, Blockchain, Big Data y cloud computing.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Tecnologías Emergentes
Estudio de las últimas tecnologías de la industria del software:

#### 📂 Tema 1: Cloud Computing y Servicios AWS-Azure
* Modelos de servicios en la nube: IaaS, PaaS y SaaS.
* Despliegue de instancias de computación (EC2) y bases de datos alojadas (RDS).

#### 📂 Tema 2: Virtualización y Contenedores Docker
* Diferencia entre máquinas virtuales tradicionales y contenedores ligeros de Docker.
* Creación de imágenes personalizadas mediante Dockerfiles e interconexión de servicios con Docker Compose.

#### 📂 Tema 3: Integración Continua y Metodologías DevOps
* Automatización de pruebas e integración continua (CI/CD) con plataformas de código (GitLab CI o GitHub Actions).
* Despliegue automatizado de software.

#### 📂 Tema 4: Blockchain y Big Data
* Concepto de cadena de bloques y contratos inteligentes descentralizados (Smart Contracts).
* Introducción al procesamiento y análisis de grandes volúmenes de datos (Big Data).

#### 📂 Tema 5: Arquitectura de Microservicios
* Diseño de sistemas divididos en pequeños servicios independientes comunicados por APIs.
* Descubrimiento de servicios y balanceo de carga en arquitecturas distribuidas.

#### 📂 Tema 6: Computación en el Borde y Tendencias Futuras
* Reducción de latencia mediante computación en el borde (Edge Computing).
* Introducción a la computación cuántica y tendencias futuras del desarrollo de software."""
    },
    "SIM-160": {
        "emoji": "🎲",
        "title": "Simulación de Sistemas",
        "prereq": "Estadística II (EST-130)",
        "description": "Simulación de eventos discretos, congruencias de números aleatorios y validación estadística.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Simulación de Sistemas
Imitación computacional del comportamiento de sistemas reales:

#### 📂 Tema 1: Modelado y Metodología de Simulación
* Introducción a los modelos de simulación: variables del sistema, estados y parámetros de diseño.
* Fases de un estudio formal de simulación: definición del problema, recolección de datos y programación.

#### 📂 Tema 2: Simulación de Eventos Discretos
* Estructura lógica de un simulador de eventos discretos. Planificador de eventos (event calendar).
* Modelos clásicos de simulación de líneas de espera en bancos o industrias.

#### 📂 Tema 3: Generación de Números Pseudoaleatorios
* Algoritmos aritméticos congruenciales para generar variables uniformes en [0,1].
* Pruebas de aleatoriedad (prueba de medias, varianza y uniformidad Chi-cuadrada).

#### 📂 Tema 4: Análisis de Resultados y Validación
* Métodos de inferencia estadística para validar que el modelo informático imita al sistema real.
* Análisis de escenarios simulados para la optimización de procesos.

#### 📂 Tema 5: Simulación Dinámica de Sistemas Continuos
* Modelado continuo utilizando ecuaciones diferenciales sencillas.
* Simulación dinámica de flujos y niveles de inventarios o poblaciones.

#### 📂 Tema 6: Herramientas de Simulación por Computadora
* Uso de software de simulación comercial o librerías científicas de software libre.
* Presentación y visualización gráfica de resultados de simulación."""
    },
    "LEI-160": {
        "emoji": "⚖️",
        "title": "Legislación Informática",
        "prereq": "Ninguno",
        "description": "Propiedad intelectual, delitos informáticos, comercio electrónico y legislación digital boliviana.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Legislación Informática
Aspectos legales y éticos del ejercicio informático en Bolivia:

#### 📂 Tema 1: Derecho Informático y Ética
* Introducción al derecho informático. Código de ética para ingenieros de sistemas.
* Regulación del uso de la tecnología de información.

#### 📂 Tema 2: Delitos Informáticos y Ciberseguridad
* Tipificación de delitos informáticos según el código penal boliviano (phishing, sabotaje informático, acceso no autorizado).
* Aspectos legales sobre seguridad de la información.

#### 📂 Tema 3: Propiedad Intelectual y Licencias de Software
* Derechos de autor aplicados al desarrollo de software y patentes comerciales.
* Tipos de licencias de software: Software Libre (GPL, MIT, Apache) y Licencias Propietarias.

#### 📂 Tema 4: Contratos y Comercio Electrónico
* Validez legal de firmas digitales y contratos informáticos.
* Leyes que regulan el comercio electrónico y protección de datos personales en línea.

#### 📂 Tema 5: Protección de Datos y Privacidad en la Red
* Derecho a la intimidad, privacidad digital y habeas data.
* Leyes de protección de datos personales y obligaciones corporativas en el manejo de información sensible.

#### 📂 Tema 6: Firma Digital y Regulaciones Nacionales
* Entidades certificadoras y validez del documento digital frente al documento físico en Bolivia.
* Infraestructura de firma digital nacional."""
    },
    "RED-160": {
        "emoji": "📡",
        "title": "Redes de Computadoras I",
        "prereq": "Sistemas Operativos (SOP-150)",
        "description": "Modelos OSI y TCP/IP, cableado estructurado, subneteo IP y protocolos de transporte.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Redes de Computadoras I
Interconexión y protocolos de comunicación de datos:

#### 📂 Tema 1: Modelos OSI y TCP-IP
* Comparativa detallada entre el modelo teórico OSI (7 capas) y el modelo práctico TCP/IP (4 capas).
* Proceso de encapsulamiento y desencapsulamiento de datos.

#### 📂 Tema 2: Capa Física y Medios de Transmisión
* Características de los medios guiados (cable coaxial, UTP Cat5e/6/6a, Fibra óptica monomodo y multimodo).
* Estructura física y conectores del estándar Ethernet.

#### 📂 Tema 3: Direccionamiento IP y Subneteo
* Direcciones IPv4 clases A, B y C. Concepto de máscara de red.
* Subneteo de redes mediante direccionamiento de máscara de longitud variable (VLSM).

#### 📂 Tema 4: Protocolos de Transporte y Ruteo
* Capa de transporte: diferencias fundamentales de control de flujo entre TCP (orientado a conexión) y UDP (no orientado).
* Ruteo estático y dinámico. Funcionamiento de switches de capa 2 y routers de capa 3.

#### 📂 Tema 5: Redes de Área Local Inalámbricas WLAN
* Estándares inalámbricos IEEE 802.11 (a, b, g, n, ac, ax).
* Seguridad inalámbrica: encriptación mediante WPA2 y WPA3.

#### 📂 Tema 6: Seguridad en Redes y Firewalls
* Conceptos básicos de seguridad perimetral de red.
* Configuración de listas de control de acceso (ACLs) y reglas de firewalls de hardware y software."""
    },
    "OPT-160": {
        "emoji": "🔬",
        "title": "Optativa II",
        "prereq": "Optativa I (OPT-140)",
        "description": "Diseño avanzado de circuitos impresos (PCB), microcontroladores industriales y firmware en C/C++.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Optativa II (Sistemas Embebidos Avanzados)
Diseño de hardware e integración a sistemas de automatización industrial:

#### 📂 Tema 1: Diseño Avanzado de Circuitos Impresos PCB
* Introducción al modelado asistido de placas de circuito impreso (EDA).
* Reglas de enrutamiento digital y reducción de ruido interferencial.

#### 📂 Tema 2: Comunicación Inalámbrica Industrial (LoraWAN/Zigbee)
* Conceptos físicos de la modulación RF industrial de largo alcance.
* Estructuración de tramas seguras de datos.

#### 📂 Tema 3: Diseño de Firmware Robusto en C-C++
* Arquitectura de interrupciones de baja latencia y máquinas de estado en firmware.
* Uso de sistemas operativos en tiempo real (RTOS).

#### 📂 Tema 4: Procesamiento de Señales en Tiempo Real
* Filtrado digital básico de sensores de ruido analógico en microcontroladores.
* Transformación rápida de Fourier elemental en sistemas embebidos.

#### 📂 Tema 5: Sistemas Embebidos Basados en Linux (Raspberry Pi)
* Configuración y control físico de periféricos GPIO bajo sistemas Linux.
* Ejecución automática de scripts e interfaces de hardware en paralelo.

#### 📂 Tema 6: Proyecto Integrador de Optativa II
* Diseño de un módulo electrónico de adquisición inalámbrica de datos industrial."""
    },

    # 8º Semestre
    "MET-170": {
        "emoji": "📝",
        "title": "Metodología de la Investigación",
        "prereq": "Estadística II (EST-130)",
        "description": "Estructura del método científico, planteamiento del problema, hipótesis y perfiles de tesis formales.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Metodología de la Investigación
Estructuración de trabajos de investigación y perfiles de tesis:

#### 📂 Tema 1: Investigación Científica y Metodología
* Enfoques cuantitativos, cualitativos y mixtos de investigación.
* Tipos de alcance de investigación: exploratorio, descriptivo, correlacional y explicativo.

#### 📂 Tema 2: Planteamiento del Problema y Objetivos
* Redacción y delimitación clara del problema de investigación científica.
* Formulación de la pregunta de investigación, Objetivo General y Objetivos Específicos.

#### 📂 Tema 3: Marco Teórico y Diseño Metodológico
* Búsqueda y revisión de literatura científica de fuentes confiables (bases de datos académicas).
* Definición del diseño metodológico: hipótesis, variables, población y muestra.

#### 📂 Tema 4: Redacción del Perfil de Proyecto de Grado
* Estructura oficial del Perfil de Grado exigida por el reglamento de la UNIOR.
* Cronograma de actividades (Diagrama de Gantt) y presupuesto estimado de recursos.

#### 📂 Tema 5: Recolección y Análisis de Datos de Investigación
* Técnicas e instrumentos de recolección de datos (cuestionarios, entrevistas, bitácoras).
* Procesamiento de datos cuantitativos mediante software estadístico.

#### 📂 Tema 6: Estilo de Redacción APA e Informe Final de Tesis
* Normas APA vigentes para citas bibliográficas y referencias académicas.
* Estructuración del documento final de tesis y técnicas de sustentación oral ante tribunal."""
    },
    "AUT-170": {
        "emoji": "🔍",
        "title": "Auditoría de Sistemas",
        "prereq": "Bases de Datos III (BDD-150)",
        "description": "Evaluación sistemática de los controles, seguridad, eficiencia y confiabilidad de los sistemas de información corporativos.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Auditoría de Sistemas
Evaluación estructurada del control y la seguridad informática:

#### 📂 Tema 1: Fundamentos de Auditoría de TI
* Definición de auditoría informática, objetivos y ética del auditor.
* Estándares y normas de auditoría de sistemas nacionales e internacionales (ISACA).

#### 📂 Tema 2: Evaluación de Riesgos y Controles Internos
* Identificación y matriz de riesgos en centros de procesamiento de datos.
* Diseño y ejecución de pruebas de cumplimiento y pruebas sustantivas.

#### 📂 Tema 3: Seguridad Física y Lógica
* Auditoría de controles de accesos físicos a salas de servidores y protección contra incendios.
* Auditoría de seguridad lógica: permisos de bases de datos, contraseñas y cifrado.

#### 📂 Tema 4: Elaboración de Informes y Recomendaciones
* Proceso de redacción del borrador de observaciones detectadas durante el trabajo de campo.
* Presentación del Informe de Auditoría oficial incluyendo el Dictamen y recomendaciones correctivas.

#### 📂 Tema 5: Auditoría de Redes y Comunicaciones
* Revisión de vulnerabilidades y seguridad en dispositivos de red (switches, routers, firewalls).
* Análisis de controles de acceso a redes inalámbricas y VPNs.

#### 📂 Tema 6: Auditoría de Continuidad del Negocio y Respaldo
* Evaluación del Plan de Continuidad del Negocio (BCP) y de Recuperación ante Desastres (DRP).
* Verificación física del almacenamiento seguro de copias de seguridad de datos."""
    },
    "INT-170": {
        "emoji": "🧠",
        "title": "Inteligencia Artificial",
        "prereq": "Simulación de Sistemas (SIM-160)",
        "description": "Agentes inteligentes, machine learning, redes neuronales y ética de la inteligencia artificial.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Inteligencia Artificial
Algoritmos inteligentes y modelos predictivos:

#### 📂 Tema 1: Algoritmos de Búsqueda no Informada e Informada
* Agentes inteligentes y entornos de software.
* Búsqueda ciega (anchura y profundidad) y búsqueda con heurísticas (Algoritmo A*).

#### 📂 Tema 2: Aprendizaje Automático Machine Learning
* Modelos supervisados: Regresión Lineal, Regresión Logística y Árboles de Decisión.
* Modelos no supervisados: Agrupamiento con K-Means.

#### 📂 Tema 3: Redes Neuronales Artificiales y Deep Learning
* Estructura de una neurona artificial (Perceptrón simple) y funciones de activación.
* Redes neuronales multicapa (MLP) y algoritmo de retropropagación (Backpropagation).

#### 📂 Tema 4: Sistemas Expertos y Procesamiento de Lenguaje
* Modelado de conocimiento mediante reglas de producción lógica (SI-ENTONCES).
* Fundamentos de Procesamiento de Lenguaje Natural (PLN).

#### 📂 Tema 5: Visión Artificial e Inteligencia Robótica
* Procesamiento digital de imágenes y detección de contornos.
* Redes neuronales convolucionales (CNN) para clasificación de imágenes y robótica básica.

#### 📂 Tema 6: Ética y Futuro de la Inteligencia Artificial
* Desafíos éticos de la IA: sesgo algorítmico, privacidad y automatización del trabajo.
* Futuro del desarrollo de la Inteligencia Artificial General (AGI)."""
    },
    "RED-170": {
        "emoji": "🕸️",
        "title": "Redes de Computadoras II",
        "prereq": "Redes de Computadoras I (RED-160)",
        "description": "Tecnología de conmutación MPLS, VPNs IPsec, calidad de servicio (QoS), telefonía IP e integración IPv6.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Redes de Computadoras II
Diseño avanzado de redes multiservicio robustas de escala metropolitana:

#### 📂 Tema 1: Conmutación de Etiquetas Multiprotocolo (MPLS)
* Principios de conmutación de etiquetas y comparación con el ruteo IP clásico.
* Configuración de túneles MPLS y distribución de etiquetas LDP.

#### 📂 Tema 2: Redes Privadas Virtuales VPN IPsec y SSL
* Protocolos de encriptación de datos de capa de red (ESP, AH) y túneles seguros.
* Configuración de VPN sitio a sitio e interfaces de acceso remoto SSL.

#### 📂 Tema 3: Calidad de Servicio QoS en Redes Convergentes
* Clasificación y marcado de tráfico de datos prioritario.
* Mecanismos de administración de colas en routers de frontera (WFQ, CBWFQ).

#### 📂 Tema 4: Telefonía IP y Comunicaciones Unificadas VoIP
* Protocolos de señalización de voz (SIP, H.323) e integración analógica-digital.
* Configuración de servidores de telefonía IP IP-PBX virtuales.

#### 📂 Tema 5: IPv6 e Integración en Redes Existentes
* Estructuración del direccionamiento y subneteo IPv6.
* Mecanismos de transición (Dual stack, túneles 6to4, NAT64).

#### 📂 Tema 6: Monitoreo y Diagnóstico Avanzado de Redes
* Protocolos de monitorización (SNMP, NetFlow) y análisis de rendimiento de red.
* Resolución de fallas de enlaces troncales redundantes."""
    },
    "ASI-170": {
        "emoji": "🏢",
        "title": "Administración de Sistemas de Información",
        "prereq": "Ingeniería de Software (ING-160)",
        "description": "Gobernanza corporativa de TI (COBIT/ITIL), seguridad de la información y gestión de proyectos informáticos.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Administración de Sistemas de Información
Gobernanza y gestión de recursos tecnológicos empresariales:

#### 📂 Tema 1: Planificación Estratégica de TI
* Alineamiento de la infraestructura tecnológica con la misión y metas corporativas de la empresa.
* Análisis de inversiones de TI y justificación de costos y beneficios de nuevos sistemas.

#### 📂 Tema 2: Marco de Trabajo COBIT e ITIL
* Estudio de COBIT para la gobernanza integral de las tecnologías de información empresariales.
* Fundamentos del estándar ITIL para la entrega eficiente de servicios de soporte de TI.

#### 📂 Tema 3: Seguridad de la Información y Auditoría
* Políticas corporativas de seguridad, controles de acceso lógicos y físicos.
* Planes de recuperación ante desastres (DRP) y continuidad del negocio.

#### 📂 Tema 4: Gestión de Servicios de TI
* Gestión de incidencias, problemas, cambios en la infraestructura de red y monitorización de niveles de servicio (SLA).

#### 📂 Tema 5: Gestión de Proyectos de Sistemas de Información
* Metodologías de gestión de proyectos tecnológicos (PMBOK / metodologías ágiles Scrum).
* Estimación de presupuestos y gestión de riesgos en proyectos de software.

#### 📂 Tema 6: Ética e Impacto Social de los Sistemas
* Impacto social de la automatización industrial y digitalización empresarial.
* Responsabilidad ética del ingeniero de sistemas en el manejo de información masiva y automatización."""
    },
    "OPT-170": {
        "emoji": "🤖",
        "title": "Optativa III",
        "prereq": "Optativa II (OPT-160)",
        "description": "Robótica móvil, control retroalimentado, sistemas operativos de robótica (ROS) y automatización industrial.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Optativa III (Robótica y Automatización)
Desarrollo físico y control de sistemas de robótica autónoma avanzada:

#### 📂 Tema 1: Introducción a la Robótica Móvil y Brazos Robóticos
* Clasificación de robots industriales y sistemas articulados cinemáticos.
* Ecuaciones vectoriales de rotación y traslación en coordenadas homogéneas.

#### 📂 Tema 2: Cinemática Directa e Inversa de Manipuladores
* Algoritmo de Denavit-Hartenberg para modelar brazos robóticos de múltiples eslabones.
* Resolución analítica e iterativa de la cinemática inversa.

#### 📂 Tema 3: Sistemas de Control Retroalimentado y Servos
* Diseño y calibración de controladores de lazo cerrado (PID) para motores.
* Sensores de retroalimentación de posición y encoders ópticos.

#### 📂 Tema 4: Programación Robótica Basada en ROS
* Conceptos lógicos de nodos, tópicos y mensajes en el middleware ROS.
* Simulación de robots en entornos virtuales interactivos (Gazebo / Rviz).

#### 📂 Tema 5: Sensores Robóticos de Alta Precisión (LiDAR, Encoders)
* Procesamiento de nubes de puntos de sensores de rango láser LiDAR.
* Algoritmos básicos de mapeo y localización simultánea (SLAM).

#### 📂 Tema 6: Proyecto Completo de Robótica o Automatización Industrial
* Diseño, construcción y control programado de un robot autónomo o brazo industrial de manufactura."""
    },

    # Taller de Grado
    "TG-180": {
        "emoji": "🎓",
        "title": "Taller de Grado",
        "prereq": "Metodología de la Investigación (MET-170)",
        "description": "Estructura formal del perfil de proyecto de grado y pre-defensa ante tribunal.",
        "apuntes": """### 🗺️ Ruta de Aprendizaje de Taller de Grado
Fórmate en la concepción y estructuración metodológica de tu proyecto de graduación:

#### 📂 Tema 1: Selección y Delimitación del Tema de Grado
* Identificación de problemas tecnológicos específicos de la industria.
* Formulación de hipótesis y planteamiento del alcance de la solución informática.

#### 📂 Tema 2: Estructuración de la Introducción y Justificación
* Redacción de antecedentes del problema investigado.
* Justificación técnica, social y económica del proyecto tecnológico propuesto.

#### 📂 Tema 3: Desarrollo del Marco Teórico Referencial
* Búsqueda analítica de referencias y soluciones tecnológicas similares a nivel mundial.
* Definición de fundamentos de hardware y software del desarrollo.

#### 📂 Tema 4: Marco Metodológico e Ingeniería del Proyecto
* Definición del tipo de investigación y diseño metodológico.
* Planificación de la arquitectura inicial del software o sistema propuesto.

#### 📂 Tema 5: Primer Borrador del Perfil y Diseño Inicial
* Estructuración del borrador del documento siguiendo las normas formales UNIOR.
* Estimación del presupuesto inicial y diagrama de Gantt de ejecución.

#### 📂 Tema 6: Pre-defensa del Perfil de Tesis
* Preparación de material audiovisual de exposición oral.
* Simulación de defensa final ante tribunales simulados y corrección de observaciones."""
    }
}


def clean_name(folder_name):
    # Remueve el check "√" y espacios extras
    name = folder_name.replace("√", "")
    return name.strip()

def generate_theme_readmes(item_path, course_title, course_code, apuntes):
    # Parsear los temas y sus contenidos
    pattern = r'####\s+📂\s+Tema\s+(\d+)(?:\s*[:\-]\s*|\s+)([^\n]+)\n(.*?)(?=####\s+📂\s+Tema|\Z)'
    theme_matches = re.findall(pattern, apuntes, re.DOTALL)
    
    for num, title, content in theme_matches:
        num = num.strip()
        title = title.strip()
        content = content.strip()
        
        # Buscar la subcarpeta correspondiente que inicie con "Tema {num}"
        theme_folder = None
        for folder in os.listdir(item_path):
            folder_path = os.path.join(item_path, folder)
            if os.path.isdir(folder_path) and folder.startswith(f"Tema {num}"):
                theme_folder = folder
                break
                
        if theme_folder:
            theme_folder_path = os.path.join(item_path, theme_folder)
            
            # Listar archivos en la subcarpeta del tema
            theme_files = []
            for file in os.listdir(theme_folder_path):
                file_path = os.path.join(theme_folder_path, file)
                if os.path.isfile(file_path) and file.lower() != "readme.md":
                    theme_files.append(file)
            
            theme_readme_lines = [
                f"# Tema {num}: {title}",
                f"## 🏫 Materia: {course_title} ({course_code})",
                "",
                "---",
                "",
                "### 📚 Apuntes y Conceptos Clave",
                content,
                "",
                "---",
                "",
                "### ✍️ Mis Resúmenes y Notas de Clase",
                "*Haz doble clic en este archivo para registrar tus notas, fórmulas o resúmenes de las clases del docente.*",
                "",
                "---",
                "",
                "### 📂 Archivos y Tareas de esta Unidad",
            ]
            
            if theme_files:
                for tf in sorted(theme_files):
                    encoded_tf = urllib.parse.quote(tf)
                    theme_readme_lines.append(f"- 📄 [{tf}](./{encoded_tf})")
            else:
                theme_readme_lines.append("*Arrastra tus prácticas, códigos o diapositivas a esta carpeta para organizarlas aquí.*")
                
            theme_readme_lines.append("")
            theme_readme_lines.append("---")
            theme_readme_lines.append(f"*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*")
            
            theme_readme_path = os.path.join(theme_folder_path, "README.md")
            with open(theme_readme_path, "w", encoding="utf-8") as f:
                f.write("\n".join(theme_readme_lines))

def build_readme_content(semester, code, subject_name, approved, existing_files, existing_dirs):
    details = SYLLABUS_MAPPING.get(code, None)
    
    if details:
        title = details["title"]
        emoji = details.get("emoji", "📚")
        prereq = details["prereq"]
        desc = details["description"]
        apuntes = details["apuntes"]
    else:
        title = subject_name
        emoji = "📚"
        prereq = "No Especificado"
        desc = "Asignatura perteneciente a la carrera de Ingeniería de Sistemas de la UNIOR."
        apuntes = "*   No hay apuntes teóricos cargados para esta materia especial.\n*   Puedes registrar en esta sección tus resúmenes y notas de estudio correspondientes a las clases del semestre."
    
    status_emoji = "🟢 Aprobada" if approved else "🟡 Cursando / Pendiente"
    
    markdown = []
    markdown.append(f"# {emoji} {title}")
    markdown.append("")
    markdown.append("## 🏫 Universidad Privada de Oruro (UNIOR)")
    markdown.append("### 💻 Carrera: Ingeniería de Sistemas")
    markdown.append("")
    markdown.append("---")
    markdown.append("")
    markdown.append("### 📊 Ficha Técnica de la Asignatura")
    markdown.append(f"- **Sigla:** {code if code else 'S/S'}")
    markdown.append(f"- **Semestre:** {semester if semester else 'No Especificado'}")
    markdown.append(f"- **Prerrequisitos:** {prereq}")
    markdown.append(f"- **Estado:** {status_emoji}")
    markdown.append("")
    markdown.append("### 📝 Descripción de la Materia")
    markdown.append(desc)
    markdown.append("")
    
    markdown.append("### 📚 Apuntes y Resumen de Contenidos")
    markdown.append(apuntes)
    markdown.append("")
    
    markdown.append("### 🗂️ Estructura de Carpetas de Aprendizaje")
    if existing_dirs:
        markdown.append("Temas y carpetas de estudio organizadas en este directorio:")
        for dirname in sorted(existing_dirs):
            encoded_dir = urllib.parse.quote(dirname)
            markdown.append(f"- 📁 [{dirname}](./{encoded_dir})")
    else:
        markdown.append("*No hay subcarpetas creadas aún. Puedes organizar tus archivos por unidades temáticas.*")
    markdown.append("")
    
    markdown.append("### 🎯 Ponderación y Control de Calificaciones")
    markdown.append("| Actividad Evaluativa | Ponderación | Nota Obtenida |")
    markdown.append("| --- | :---: | :---: |")
    markdown.append("| **Examen Primer Parcial** | 30% | `__ / 100` |")
    markdown.append("| **Examen Segundo Parcial** | 30% | `__ / 100` |")
    markdown.append("| **Examen Final / Proyecto** | 30% | `__ / 100` |")
    markdown.append("| **Tareas y Prácticas** | 10% | `__ / 100` |")
    markdown.append("| **Nota Final** | **100%** | **`__ / 100`** |")
    markdown.append("")
    
    markdown.append("### 📅 Cronograma de Fechas Importantes")
    markdown.append("- [ ] **Examen Primer Parcial:** _Fecha: ____/____/_________")
    markdown.append("- [ ] **Examen Segundo Parcial:** _Fecha: ____/____/_________")
    markdown.append("- [ ] **Entrega de Proyecto/Trabajo Final:** _Fecha: ____/____/_________")
    markdown.append("- [ ] **Examen Final:** _Fecha: ____/____/_________")
    markdown.append("")
    
    markdown.append("### 📂 Archivos en esta Carpeta")
    if existing_files:
        markdown.append("Aquí tienes un listado de los archivos almacenados en esta materia:")
        for filename in sorted(existing_files):
            if filename.lower() == "readme.md":
                continue
            encoded_name = urllib.parse.quote(filename)
            markdown.append(f"- 📄 [{filename}](./{encoded_name})")
    else:
        markdown.append("*Esta carpeta está vacía actualmente. Puedes añadir tus apuntes, códigos y documentos aquí.*")
    
    markdown.append("")
    markdown.append("---")
    markdown.append("*Documento autogenerado para el control de estudios del Ing. José Luis Choquevilca - UNIOR*")
    
    return "\n".join(markdown)


def build_html_dashboard(courses_data):
    std_courses = [c for c in courses_data if c["sem_num"] is not None]
    std_courses.sort(key=lambda x: (x["sem_num"], x["code"]))
    courses_json = json.dumps(courses_data, ensure_ascii=False)
    
    total_std = len(std_courses)
    approved_std = sum(1 for c in std_courses if c["approved"])
    pending_std = total_std - approved_std
    percentage = (approved_std / total_std * 100) if total_std > 0 else 0
    
    # Calculate semester completion counts
    semesters_count = {i: {"total": 0, "approved": 0} for i in range(1, 10)}
    for c in std_courses:
        sem = c["sem_num"]
        if 1 <= sem <= 9:
            semesters_count[sem]["total"] += 1
            if c["approved"]:
                semesters_count[sem]["approved"] += 1
                
    # Generate Roadmap Cards HTML for Dashboard
    roadmap_html = []
    for sem in range(1, 10):
        total = semesters_count[sem]["total"]
        approved = semesters_count[sem]["approved"]
        is_complete = approved == total and total > 0
        sem_label = f"{sem}º Semestre" if sem < 9 else "Taller de Grado"
        status_text = f"{approved}/{total} Aprobadas"
        status_class = "approved" if is_complete else "pending"
        icon_name = "check-circle-2" if is_complete else "clock"
        
        roadmap_html.append(f'''
        <div class="roadmap-card" data-target-sem="{sem}">
            <div class="roadmap-card-left">
                <span class="roadmap-sem">{sem_label}</span>
                <span class="roadmap-status {status_class}">
                    <i data-lucide="{icon_name}"></i> {status_text}
                </span>
            </div>
            <div class="roadmap-card-right">
                <i data-lucide="chevron-right"></i>
            </div>
        </div>
        ''')
    roadmap_joined = "\n".join(roadmap_html)
    
    lucide_map = {
        # 1º Semestre
        "ADM-100": "briefcase",
        "ALF-100": "binary",
        "INF-100": "code-2",
        "ING-100": "languages",
        "ISO-100": "network",
        "MAT-100": "calculator",
        # 2º Semestre
        "ALL-110": "grid",
        "ARC-110": "cpu",
        "INF-110": "terminal",
        "ING-110": "message-square",
        "MAT-110": "infinity",
        "MEC-110": "wrench",
        # 3º Semestre
        "CBA-120": "coins",
        "ECD-120": "line-chart",
        "ELM-120": "zap",
        "EST-120": "pie-chart",
        "INF-120": "git-fork",
        "QUE-120": "globe-2",
        # 4º Semestre
        "BDD-130": "database",
        "CEL-103": "circuit-board",
        "EST-130": "bar-chart-3",
        "INF-130": "braces",
        "INS-130": "layers",
        "SIC-130": "receipt",
        # 5º Semestre
        "BDD-140": "server",
        "DGI-140": "palette",
        "DPW-140": "layout",
        "INO-140": "target",
        "INS-140": "map",
        "OPT-140": "smartphone",
        # 6º Semestre
        "BDD-150": "hard-drive",
        "DPW-150": "chrome",
        "INO-150": "compass",
        "INS-150": "shield",
        "PED-150": "presentation",
        "SOP-150": "monitor",
        # 7º Semestre
        "ING-160": "git-merge",
        "LEI-160": "gavel",
        "OPT-160": "flask-conical",
        "RED-160": "wifi",
        "SIM-160": "dices",
        "TEE-160": "rocket",
        # 8º Semestre
        "ASI-170": "folder-git",
        "AUT-170": "eye",
        "INT-170": "brain",
        "MET-170": "book-open",
        "OPT-170": "bot",
        "RED-170": "split",
        # 9º Semestre
        "TG-180": "award"
    }
    
    cards_html = []
    for c in std_courses:
        lucide_icon = lucide_map.get(c["code"], "book")
        status_class = "approved" if c["approved"] else "pending"
        status_text = "Aprobada" if c["approved"] else "Cursando"
        
        cards_html.append(f'''
        <div class="course-card" data-semester="{c['sem_num']}" data-status="{status_text.lower()}" data-name="{c['name'].lower()}" data-code="{c['code'].lower()}">
            <div class="card-header">
                <span class="sem-badge">{c['sem_num']}º Semestre</span>
                <span class="status-badge {status_class}">{status_text}</span>
            </div>
            <div class="card-body">
                <div class="course-icon"><i data-lucide="{lucide_icon}"></i></div>
                <h3 class="course-title">{c['name']}</h3>
                <span class="course-code">{c['code']}</span>
            </div>
            <div class="card-footer">
                <a href="{c['link']}" class="btn-notes">Ver Apuntes y Temas ➔</a>
            </div>
        </div>
        ''')
        
    cards_joined = "\n".join(cards_html)
    
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal Académico - Ing. José Luis Choquevilca</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
    <style>
        :root {{
            --bg-color: #080c14;
            --sidebar-bg: #0c111d;
            --card-bg: rgba(255, 255, 255, 0.02);
            --card-border: rgba(255, 255, 255, 0.06);
            --primary: #e50000;
            --primary-hover: #ff1a1a;
            --primary-glow: rgba(229, 0, 0, 0.15);
            --success: #dfa010;
            --success-glow: rgba(223, 160, 16, 0.15);
            --warning: #f59e0b;
            --text-main: #f3f4f6;
            --text-muted: #9ca3af;
            --glass-bg: rgba(15, 23, 42, 0.45);
            --sidebar-width: 260px;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            background-image: 
                radial-gradient(at 0% 0%, rgba(229, 0, 0, 0.12) 0px, transparent 40%),
                radial-gradient(at 100% 100%, rgba(223, 160, 16, 0.08) 0px, transparent 40%);
            background-attachment: fixed;
            color: var(--text-main);
            min-height: 100vh;
            overflow-x: hidden;
        }}

        /* App Layout */
        .app-layout {{
            display: flex;
            min-height: 100vh;
        }}

        /* Sidebar */
        .sidebar {{
            width: var(--sidebar-width);
            background-color: var(--sidebar-bg);
            border-right: 1px solid var(--card-border);
            padding: 2rem 1.5rem;
            display: flex;
            flex-direction: column;
            position: fixed;
            height: 100vh;
            left: 0;
            top: 0;
            z-index: 100;
        }}

        .sidebar-header {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 2rem;
            padding-left: 0.5rem;
        }}

        .logo-icon {{
            font-size: 1.8rem;
        }}

        .logo-text {{
            font-size: 1.25rem;
            font-weight: 700;
            background: linear-gradient(to right, #ffe699, var(--success));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 0.5px;
        }}

        .nav-menu {{
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
            overflow-y: auto;
            flex: 1;
            padding-right: 0.25rem;
        }}

        /* Scrollbar for sidebar */
        .nav-menu::-webkit-scrollbar {{
            width: 4px;
        }}
        .nav-menu::-webkit-scrollbar-thumb {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 2px;
        }}

        .nav-section-title {{
            font-size: 0.7rem;
            text-transform: uppercase;
            color: var(--text-muted);
            font-weight: 700;
            letter-spacing: 1.5px;
            margin-top: 1.2rem;
            margin-bottom: 0.4rem;
            padding-left: 0.75rem;
        }}

        .nav-item {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            width: 100%;
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 0.65rem 0.85rem;
            border-radius: 10px;
            font-family: inherit;
            font-size: 0.88rem;
            font-weight: 500;
            cursor: pointer;
            text-align: left;
            transition: all 0.2s ease;
        }}

        .nav-item i {{
            width: 18px;
            height: 18px;
            stroke-width: 2;
        }}

        .nav-item:hover {{
            color: var(--text-main);
            background: rgba(255, 255, 255, 0.03);
        }}

        .nav-item.active {{
            color: #fff;
            background: var(--primary-glow);
            border-left: 3px solid var(--primary);
            box-shadow: inset 4px 0 10px rgba(229, 0, 0, 0.05);
        }}

        .sem-number {{
            display: flex;
            align-items: center;
            justify-content: center;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.08);
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--text-muted);
            transition: all 0.2s ease;
        }}

        .nav-item.active .sem-number {{
            background: var(--primary);
            color: #fff;
        }}

        /* Main Content Area */
        .main-content {{
            flex: 1;
            margin-left: var(--sidebar-width);
            padding: 2.5rem 3.5rem;
            min-height: 100vh;
        }}

        /* Top Header */
        .top-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--card-border);
            padding-bottom: 1.5rem;
            margin-bottom: 2.5rem;
        }}

        .top-header h2 {{
            font-size: 1.8rem;
            font-weight: 700;
            color: #fff;
            letter-spacing: -0.5px;
        }}

        .top-header .subtitle {{
            font-size: 0.9rem;
            color: var(--text-muted);
        }}

        .profile-card {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            padding: 0.5rem 1rem;
            border-radius: 30px;
            backdrop-filter: blur(8px);
        }}

        .profile-avatar {{
            width: 36px;
            height: 36px;
            background: linear-gradient(135deg, var(--primary), var(--success));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            color: #fff;
            font-size: 0.85rem;
            box-shadow: 0 0 10px rgba(229, 0, 0, 0.4);
        }}

        .profile-info {{
            display: flex;
            flex-direction: column;
        }}

        .profile-name {{
            font-size: 0.85rem;
            font-weight: 600;
            color: #fff;
        }}

        .profile-title {{
            font-size: 0.75rem;
            color: var(--text-muted);
        }}

        /* Tab Panes */
        .tab-pane {{
            display: none;
            animation: fadeUp 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        .tab-pane.active {{
            display: block;
        }}

        @keyframes fadeUp {{
            from {{
                opacity: 0;
                transform: translateY(10px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        /* Stats Grid */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}

        .stat-card {{
            background: var(--glass-bg);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            border: 1px solid var(--card-border);
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease, border-color 0.3s ease;
        }}

        .stat-card:hover {{
            transform: translateY(-5px);
            border-color: rgba(229, 0, 0, 0.4);
        }}

        .stat-num {{
            font-size: 2.2rem;
            font-weight: 700;
            color: #fff;
            margin-bottom: 0.25rem;
        }}

        .stat-num.pct {{
            color: var(--success);
        }}

        .stat-label {{
            font-size: 0.9rem;
            color: var(--text-muted);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        /* Progress Bar wrapper */
        .progress-section {{
            background: var(--glass-bg);
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 2.5rem;
            border: 1px solid var(--card-border);
            backdrop-filter: blur(10px);
        }}

        .progress-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.75rem;
            font-weight: 600;
        }}

        .progress-bar-bg {{
            background: rgba(255, 255, 255, 0.05);
            height: 16px;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}

        .progress-bar-fill {{
            background: linear-gradient(90deg, var(--primary), var(--success));
            height: 100%;
            width: {percentage}%;
            border-radius: 8px;
            transition: width 1s ease-out;
            box-shadow: 0 0 10px rgba(229, 0, 0, 0.5);
        }}

        /* Roadmap Grid */
        .roadmap-title {{
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 1.25rem;
            color: #fff;
        }}

        .roadmap-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1.25rem;
        }}

        .roadmap-card {{
            background: var(--glass-bg);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 1.25rem 1.5rem;
            backdrop-filter: blur(10px);
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .roadmap-card:hover {{
            transform: translateY(-4px);
            border-color: rgba(229, 0, 0, 0.4);
            background: rgba(15, 23, 42, 0.75);
            box-shadow: 0 8px 24px rgba(229, 0, 0, 0.12);
        }}

        .roadmap-card-left {{
            display: flex;
            flex-direction: column;
            gap: 0.35rem;
        }}

        .roadmap-sem {{
            font-size: 1.05rem;
            font-weight: 600;
            color: #fff;
        }}

        .roadmap-status {{
            font-size: 0.8rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 0.35rem;
        }}

        .roadmap-status.approved {{
            color: var(--success);
        }}

        .roadmap-status.pending {{
            color: var(--warning);
        }}

        .roadmap-status svg {{
            width: 14px;
            height: 14px;
        }}

        .roadmap-card-right svg {{
            width: 20px;
            height: 20px;
            color: var(--text-muted);
            transition: transform 0.2s ease, color 0.2s ease;
        }}

        .roadmap-card:hover .roadmap-card-right svg {{
            transform: translateX(4px);
            color: #fff;
        }}

        /* Courses View Pane Header */
        .section-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
            flex-wrap: wrap;
            gap: 1rem;
        }}

        .section-header h2 {{
            font-size: 1.5rem;
            font-weight: 700;
            color: #fff;
        }}

        /* Search Controls */
        .search-box {{
            position: relative;
            min-width: 300px;
        }}

        .search-input {{
            width: 100%;
            background: rgba(0, 0, 0, 0.2);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 0.7rem 1rem 0.7rem 2.5rem;
            color: #fff;
            font-family: inherit;
            font-size: 0.9rem;
            outline: none;
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
        }}

        .search-input:focus {{
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(229, 0, 0, 0.2);
        }}

        .search-box svg {{
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
            pointer-events: none;
            width: 16px;
            height: 16px;
        }}

        /* Courses Grid */
        .courses-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1.5rem;
        }}

        .course-card {{
            background: var(--glass-bg);
            border-radius: 16px;
            border: 1px solid var(--card-border);
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            backdrop-filter: blur(10px);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        }}

        .course-card:hover {{
            transform: translateY(-8px);
            border-color: rgba(229, 0, 0, 0.5);
            box-shadow: 0 10px 25px rgba(229, 0, 0, 0.15);
            background: rgba(15, 23, 42, 0.8);
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.25rem;
        }}

        .sem-badge {{
            font-size: 0.72rem;
            font-weight: 600;
            background: rgba(255, 255, 255, 0.05);
            padding: 0.25rem 0.55rem;
            border-radius: 6px;
            color: var(--text-muted);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }}

        .status-badge {{
            font-size: 0.72rem;
            font-weight: 700;
            padding: 0.25rem 0.55rem;
            border-radius: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .status-badge.approved {{
            background: rgba(16, 185, 129, 0.15);
            color: #34d399;
            border: 1px solid rgba(16, 185, 129, 0.2);
        }}

        .status-badge.pending {{
            background: rgba(245, 158, 11, 0.15);
            color: #fbbf24;
            border: 1px solid rgba(245, 158, 11, 0.2);
        }}

        .course-icon {{
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            height: 48px;
            color: var(--success);
        }}

        .course-icon svg {{
            width: 42px;
            height: 42px;
            stroke-width: 1.5;
            filter: drop-shadow(0 0 8px rgba(229, 0, 0, 0.4));
            transition: all 0.3s ease;
        }}

        .course-card:hover .course-icon svg {{
            stroke: var(--success);
            filter: drop-shadow(0 0 12px rgba(223, 160, 16, 0.6));
        }}

        .course-title {{
            font-size: 1.15rem;
            font-weight: 600;
            line-height: 1.4;
            color: #fff;
            margin-bottom: 0.25rem;
            min-height: 3.2rem;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}

        .course-code {{
            font-family: monospace;
            font-size: 0.85rem;
            color: var(--text-muted);
            font-weight: 600;
        }}

        .card-footer {{
            margin-top: 1.5rem;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            padding-top: 1rem;
        }}

        .btn-notes {{
            display: block;
            width: 100%;
            text-align: center;
            background: rgba(229, 0, 0, 0.1);
            color: #ffd99e;
            border: 1px solid rgba(229, 0, 0, 0.2);
            padding: 0.6rem;
            border-radius: 10px;
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            transition: all 0.2s ease;
        }}

        .btn-notes:hover {{
            background: var(--primary);
            color: #fff;
            border-color: var(--primary);
            box-shadow: 0 4px 12px rgba(229, 0, 0, 0.3);
        }}

        /* Empty State */
        .no-results {{
            grid-column: 1 / -1;
            text-align: center;
            padding: 4rem 2rem;
            color: var(--text-muted);
            font-size: 1.1rem;
            background: var(--glass-bg);
            border-radius: 16px;
            border: 1px solid var(--card-border);
        }}

        footer {{
            margin-top: 4rem;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.82rem;
            border-top: 1px solid var(--card-border);
            padding-top: 1.5rem;
        }}

        /* Responsive Layout adjustments */
        @media (max-width: 900px) {{
            .sidebar {{
                width: 80px;
                padding: 1.5rem 0.5rem;
                align-items: center;
            }}
            .logo-text, .nav-section-title, .nav-item span:not(.sem-number) {{
                display: none;
            }}
            .main-content {{
                margin-left: 80px;
                padding: 2rem;
            }}
            .nav-item {{
                justify-content: center;
                padding: 0.75rem;
            }}
        }}

        /* Notes Modal Styling */
        .notes-modal {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(4, 6, 10, 0.7);
            backdrop-filter: blur(15px);
            z-index: 1000;
            display: none;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.3s ease;
            padding: 1.5rem;
        }}

        .notes-modal.active {{
            display: flex;
            opacity: 1;
        }}

        .modal-content {{
            background: rgba(12, 17, 29, 0.95);
            border: 1px solid var(--card-border);
            width: 100%;
            max-width: 900px;
            max-height: 85vh;
            border-radius: 20px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), 0 0 30px rgba(229, 0, 0, 0.05);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            transform: scale(0.95) translateY(10px);
            transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        }}

        .notes-modal.active .modal-content {{
            transform: scale(1) translateY(0);
        }}

        .modal-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 2rem;
            border-bottom: 1px solid var(--card-border);
            background: rgba(255, 255, 255, 0.01);
        }}

        .modal-header-left {{
            display: flex;
            align-items: center;
            gap: 1rem;
        }}

        .modal-title-emoji {{
            font-size: 2rem;
            display: flex;
            align-items: center;
        }}

        .modal-title-emoji svg {{
            width: 36px;
            height: 36px;
            stroke-width: 1.5;
            color: var(--success);
            filter: drop-shadow(0 0 8px rgba(229, 0, 0, 0.4));
        }}

        .modal-title-text h3 {{
            font-size: 1.4rem;
            font-weight: 700;
            color: #fff;
        }}

        .modal-title-text span {{
            font-family: monospace;
            font-size: 0.85rem;
            color: var(--text-muted);
            font-weight: 600;
        }}

        .modal-close-btn {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--card-border);
            color: var(--text-muted);
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .modal-close-btn:hover {{
            background: var(--primary);
            color: #fff;
            transform: rotate(90deg);
        }}

        .modal-body {{
            padding: 2rem;
            overflow-y: auto;
            flex: 1;
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
        }}

        /* Scrollbar for modal */
        .modal-body::-webkit-scrollbar {{
            width: 6px;
        }}
        .modal-body::-webkit-scrollbar-thumb {{
            background: rgba(255, 255, 255, 0.15);
            border-radius: 3px;
        }}

        .modal-main-col {{
            display: flex;
            flex-direction: column;
            gap: 1.75rem;
        }}

        .modal-side-col {{
            display: flex;
            flex-direction: column;
            gap: 1.75rem;
            border-left: 1px solid var(--card-border);
            padding-left: 2rem;
        }}

        .modal-section-title {{
            font-size: 0.9rem;
            text-transform: uppercase;
            color: var(--success);
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .modal-section-title svg {{
            width: 16px;
            height: 16px;
        }}

        .modal-description {{
            font-size: 0.95rem;
            line-height: 1.6;
            color: var(--text-main);
        }}

        .modal-info-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 1rem;
        }}

        .info-item {{
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
        }}

        .info-label {{
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
            font-weight: 600;
        }}

        .info-val {{
            font-size: 0.9rem;
            color: #fff;
            font-weight: 500;
        }}

        /* Rendered Markdown Styling */
        .apuntes-content {{
            font-size: 0.95rem;
            line-height: 1.6;
            color: var(--text-main);
        }}

        .apuntes-content h4 {{
            color: #fff;
            font-size: 1.05rem;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            padding-bottom: 0.25rem;
        }}

        .apuntes-content ul {{
            margin-left: 1.25rem;
            margin-bottom: 1rem;
            list-style-type: none;
        }}

        .apuntes-content li {{
            position: relative;
            margin-bottom: 0.5rem;
            padding-left: 1rem;
        }}

        .apuntes-content li::before {{
            content: "•";
            color: var(--primary);
            position: absolute;
            left: 0;
            font-weight: bold;
        }}

        .apuntes-content strong {{
            color: #fff;
            font-weight: 600;
        }}

        code.inline-code {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 4px;
            padding: 0.15rem 0.4rem;
            font-family: monospace;
            font-size: 0.85rem;
            color: var(--success);
        }}

        .files-list, .dirs-list {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}

        .file-link, .dir-link {{
            display: flex;
            align-items: center;
            gap: 0.6rem;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--card-border);
            padding: 0.6rem 0.8rem;
            border-radius: 8px;
            color: var(--text-main);
            text-decoration: none;
            font-size: 0.85rem;
            transition: all 0.2s ease;
        }}

        .file-link:hover, .dir-link:hover {{
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(229, 0, 0, 0.3);
            color: #fff;
            transform: translateX(4px);
        }}

        .file-link svg, .dir-link svg {{
            width: 16px;
            height: 16px;
            color: var(--text-muted);
            flex-shrink: 0;
        }}

        .file-link:hover svg, .dir-link:hover svg {{
            color: var(--success);
        }}

        .empty-list-text {{
            font-size: 0.85rem;
            color: var(--text-muted);
            font-style: italic;
        }}

        .modal-footer {{
            padding: 1.25rem 2rem;
            border-top: 1px solid var(--card-border);
            background: rgba(0, 0, 0, 0.2);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .btn-modal-open-readme {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--primary-glow);
            color: #fff;
            border: 1px solid var(--primary);
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            text-decoration: none;
            font-size: 0.88rem;
            font-weight: 500;
            transition: all 0.2s ease;
        }}

        .btn-modal-open-readme:hover {{
            background: var(--primary);
            box-shadow: 0 0 15px rgba(229, 0, 0, 0.4);
        }}

        .btn-modal-open-readme svg {{
            width: 16px;
            height: 16px;
        }}

        /* Responsive Modal */
        @media (max-width: 800px) {{
            .modal-body {{
                grid-template-columns: 1fr;
                gap: 1.5rem;
            }}
            .modal-side-col {{
                border-left: none;
                padding-left: 0;
                border-top: 1px solid var(--card-border);
                padding-top: 1.5rem;
            }}
        }}

        /* Markdown Tables inside Modal */
        .apuntes-content .table-container {{
            width: 100%;
            overflow-x: auto;
            margin: 1.5rem 0;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        .apuntes-content table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 0.9rem;
        }}
        .apuntes-content th, .apuntes-content td {{
            padding: 0.75rem 1rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }}
        .apuntes-content th {{
            background: rgba(255, 255, 255, 0.05);
            color: #fff;
            font-weight: 600;
        }}
        .apuntes-content tr:last-child td {{
            border-bottom: none;
        }}
        .apuntes-content tr:hover td {{
            background: rgba(255, 255, 255, 0.02);
        }}
        
        /* KaTeX custom sizing in modal */
        .apuntes-content .katex-display {{
            margin: 1rem 0;
            overflow-x: auto;
            overflow-y: hidden;
        }}
    </style>
</head>
<body>
    <div class="app-layout">
        <!-- Sidebar Navigation -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <span class="logo-icon">🎓</span>
                <span class="logo-text">UNIOR Portal</span>
            </div>
            
            <nav class="nav-menu">
                <button class="nav-item active" data-tab="dashboard">
                    <i data-lucide="layout-dashboard"></i>
                    <span>Panel General</span>
                </button>
                
                <div class="nav-section-title">Semestres</div>
                
                <button class="nav-item" data-tab="sem-1">
                    <span class="sem-number">1</span>
                    <span>1º Semestre</span>
                </button>
                <button class="nav-item" data-tab="sem-2">
                    <span class="sem-number">2</span>
                    <span>2º Semestre</span>
                </button>
                <button class="nav-item" data-tab="sem-3">
                    <span class="sem-number">3</span>
                    <span>3º Semestre</span>
                </button>
                <button class="nav-item" data-tab="sem-4">
                    <span class="sem-number">4</span>
                    <span>4º Semestre</span>
                </button>
                <button class="nav-item" data-tab="sem-5">
                    <span class="sem-number">5</span>
                    <span>5º Semestre</span>
                </button>
                <button class="nav-item" data-tab="sem-6">
                    <span class="sem-number">6</span>
                    <span>6º Semestre</span>
                </button>
                <button class="nav-item" data-tab="sem-7">
                    <span class="sem-number">7</span>
                    <span>7º Semestre</span>
                </button>
                <button class="nav-item" data-tab="sem-8">
                    <span class="sem-number">8</span>
                    <span>8º Semestre</span>
                </button>
                <button class="nav-item" data-tab="sem-9">
                    <span class="sem-number">9</span>
                    <span>Taller de Grado</span>
                </button>
            </nav>
        </aside>

        <!-- Main Content Panel -->
        <main class="main-content">
            <!-- Header Bar -->
            <header class="top-header">
                <div>
                    <h2>Planificación Académica</h2>
                    <p class="subtitle">Universidad Privada de Oruro (UNIOR)</p>
                </div>
                
                <div class="profile-card">
                    <div class="profile-avatar">JC</div>
                    <div class="profile-info">
                        <span class="profile-name">Ing. José Luis Choquevilca</span>
                        <span class="profile-title">Ingeniero de Sistemas</span>
                    </div>
                </div>
            </header>

            <!-- Tab Pane: Panel General -->
            <section class="tab-pane active" id="pane-dashboard">
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-num">{total_std}</div>
                        <div class="stat-label">Total Asignaturas</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-num">{approved_std}</div>
                        <div class="stat-label">Materias Aprobadas</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-num">{pending_std}</div>
                        <div class="stat-label">Materias Pendientes</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-num pct">{percentage:.1f}%</div>
                        <div class="stat-label">Progreso de Carrera</div>
                    </div>
                </div>

                <!-- Progress Bar -->
                <div class="progress-section">
                    <div class="progress-header">
                        <span>Estado del Avance Académico</span>
                        <span>{percentage:.1f}% Completado</span>
                    </div>
                    <div class="progress-bar-bg">
                        <div class="progress-bar-fill"></div>
                    </div>
                </div>

                <!-- Roadmap -->
                <h3 class="roadmap-title">Mapa de Avance Curricular</h3>
                <div class="roadmap-grid">
                    {roadmap_joined}
                </div>
            </section>

            <!-- Tab Pane: Course Grid Filtered by Semester -->
            <section class="tab-pane" id="pane-courses">
                <div class="section-header">
                    <h3 id="currentSemesterTitle" style="font-size: 1.5rem; font-weight: 700; color: #fff;">1º Semestre</h3>
                    <div class="search-box">
                        <i data-lucide="search"></i>
                        <input type="text" id="searchInput" class="search-input" placeholder="Buscar materia por nombre o sigla...">
                    </div>
                </div>
                
                <div class="courses-grid" id="coursesGrid">
                    {cards_joined}
                </div>
            </section>

            <footer>
                Portal de control académico interactivo autogenerado para el Ing. José Luis Choquevilca - UNIOR
            </footer>
        </main>
    </div>

    <!-- Notes Modal -->
    <div id="notesModal" class="notes-modal">
        <div class="modal-content">
            <div class="modal-header">
                <div class="modal-header-left">
                    <span class="modal-title-emoji" id="modalEmoji">📚</span>
                    <div class="modal-title-text">
                        <h3 id="modalTitle">Nombre de Asignatura</h3>
                        <span id="modalCode">SIG-100</span>
                    </div>
                </div>
                <button class="modal-close-btn" id="modalCloseBtn" aria-label="Cerrar modal">
                    <i data-lucide="x"></i>
                </button>
            </div>
            <div class="modal-body">
                <div class="modal-main-col">
                    <div>
                        <div class="modal-section-title">
                            <i data-lucide="info"></i> Descripción
                        </div>
                        <p class="modal-description" id="modalDescription">Descripción de la materia...</p>
                    </div>
                    <div>
                        <div class="modal-section-title">
                            <i data-lucide="map"></i> Ruta de Aprendizaje (Temas)
                        </div>
                        <div class="apuntes-content" id="modalApuntes">
                            <!-- Apuntes formateados -->
                        </div>
                    </div>
                </div>
                <div class="modal-side-col">
                    <div class="modal-info-grid">
                        <div class="info-item">
                            <span class="info-label">Semestre</span>
                            <span class="info-val" id="modalSemestre">1º Semestre</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Estado</span>
                            <span class="info-val" id="modalEstado">Aprobada</span>
                        </div>
                        <div class="info-item" style="grid-column: span 2;">
                            <span class="info-label">Prerrequisitos</span>
                            <span class="info-val" id="modalPrereq">Ninguno</span>
                        </div>
                    </div>
                    <div>
                        <div class="modal-section-title">
                            <i data-lucide="folder"></i> Carpetas de Estudio
                        </div>
                        <div class="dirs-list" id="modalDirs">
                            <!-- Listado de directorios -->
                        </div>
                    </div>
                    <div>
                        <div class="modal-section-title">
                            <i data-lucide="file-text"></i> Archivos Adjuntos
                        </div>
                        <div class="files-list" id="modalFiles">
                            <!-- Listado de archivos -->
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <span style="font-size: 0.8rem; color: var(--text-muted);">
                    Ing. José Luis Choquevilca - UNIOR
                </span>
                <a href="#" id="modalReadmeLink" class="btn-modal-open-readme" target="_blank">
                    <i data-lucide="external-link"></i> Abrir README.md Original
                </a>
            </div>
        </div>
    </div>

    <script>
        const COURSES_DATA = {courses_json};

        const searchInput = document.getElementById('searchInput');
        const navItems = document.querySelectorAll('.nav-item');
        const roadmapCards = document.querySelectorAll('.roadmap-card');
        const courseCards = document.querySelectorAll('.course-card');
        const coursesGrid = document.getElementById('coursesGrid');
        
        const paneDashboard = document.getElementById('pane-dashboard');
        const paneCourses = document.getElementById('pane-courses');
        const currentSemesterTitle = document.getElementById('currentSemesterTitle');

        let currentSemester = '1';
        let searchQuery = '';

        const cleanString = (str) => str.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();

        // Handle tabs switching
        function switchTab(targetTab) {{
            navItems.forEach(item => item.classList.remove('active'));
            
            const activeBtn = Array.from(navItems).find(item => item.getAttribute('data-tab') === targetTab);
            if (activeBtn) activeBtn.classList.add('active');

            if (targetTab === 'dashboard') {{
                paneDashboard.classList.add('active');
                paneCourses.classList.remove('active');
            }} else {{
                paneDashboard.classList.remove('active');
                paneCourses.classList.add('active');
                
                // Extract semester number
                const semNum = targetTab.split('-')[1];
                currentSemester = semNum;
                
                // Update title
                const titles = {{
                    '1': '1º Semestre',
                    '2': '2º Semestre',
                    '3': '3º Semestre',
                    '4': '4º Semestre',
                    '5': '5º Semestre',
                    '6': '6º Semestre',
                    '7': '7º Semestre',
                    '8': '8º Semestre',
                    '9': 'Taller de Grado'
                }};
                currentSemesterTitle.textContent = titles[semNum] || (semNum + 'º Semestre');
                
                filterCourses();
            }}
        }}

        navItems.forEach(btn => {{
            btn.addEventListener('click', () => {{
                const tab = btn.getAttribute('data-tab');
                switchTab(tab);
            }});
        }});

        // Roadmap cards click triggers semester tab switch
        roadmapCards.forEach(card => {{
            card.addEventListener('click', () => {{
                const targetSem = card.getAttribute('data-target-sem');
                switchTab('sem-' + targetSem);
            }});
        }});

        function filterCourses() {{
            let visibleCount = 0;
            const cleanQuery = cleanString(searchQuery);
            
            courseCards.forEach(card => {{
                const semester = card.getAttribute('data-semester');
                const name = cleanString(card.getAttribute('data-name'));
                const code = cleanString(card.getAttribute('data-code'));

                const matchesSearch = name.includes(cleanQuery) || code.includes(cleanQuery);
                const matchesSemester = semester === currentSemester;

                if (matchesSearch && matchesSemester) {{
                    card.style.display = 'flex';
                    visibleCount++;
                }} else {{
                    card.style.display = 'none';
                }}
            }});

            const existingNoResults = document.querySelector('.no-results');
            if (visibleCount === 0) {{
                if (!existingNoResults) {{
                    const noResults = document.createElement('div');
                    noResults.className = 'no-results';
                    noResults.innerHTML = '🔍 No se encontraron asignaturas en este semestre.';
                    coursesGrid.appendChild(noResults);
                }}
            }} else {{
                if (existingNoResults) {{
                    existingNoResults.remove();
                }}
            }}
        }}

        // Intercept all "btn-notes" clicks
        document.addEventListener('click', (e) => {{
            const btnNotes = e.target.closest('.btn-notes');
            if (btnNotes) {{
                const card = btnNotes.closest('.course-card');
                if (card) {{
                    e.preventDefault();
                    const code = card.getAttribute('data-code').toUpperCase();
                    openNotesModal(code);
                }}
            }}
        }});

        const notesModal = document.getElementById('notesModal');
        const modalEmoji = document.getElementById('modalEmoji');
        const modalTitle = document.getElementById('modalTitle');
        const modalCode = document.getElementById('modalCode');
        const modalDescription = document.getElementById('modalDescription');
        const modalApuntes = document.getElementById('modalApuntes');
        const modalSemestre = document.getElementById('modalSemestre');
        const modalEstado = document.getElementById('modalEstado');
        const modalPrereq = document.getElementById('modalPrereq');
        const modalDirs = document.getElementById('modalDirs');
        const modalFiles = document.getElementById('modalFiles');
        const modalReadmeLink = document.getElementById('modalReadmeLink');
        const modalCloseBtn = document.getElementById('modalCloseBtn');

        function parseMarkdownToHTML(mdText) {{
            if (!mdText) return '';
            let html = mdText;
            
            // Clean headers
            html = html.replace(/^##### (.*$)/gim, '<h5>$1</h5>');
            html = html.replace(/^#### (.*$)/gim, '<h4>$1</h4>');
            html = html.replace(/^### (.*$)/gim, '<h4>$1</h4>');
            
            // Bold text
            html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            html = html.replace(/__(.*?)__/g, '<strong>$1</strong>');
            
            // Inline code
            html = html.replace(/`(.*?)`/g, '<code class="inline-code">$1</code>');
            
            // Handle markdown tables
            let lines = html.split('\\n');
            let resultLines = [];
            let inList = false;
            let inTable = false;
            let tableRows = [];
            
            for (let i = 0; i < lines.length; i++) {{
                let line = lines[i].trim();
                
                // Table parsing
                if (line.startsWith('|') && line.endsWith('|')) {{
                    if (inList) {{
                        resultLines.push('</ul>');
                        inList = false;
                    }}
                    if (!inTable) {{
                        inTable = true;
                        tableRows = [];
                    }}
                    tableRows.push(line);
                    continue;
                }} else {{
                    if (inTable) {{
                        resultLines.push(renderHTMLTable(tableRows));
                        inTable = false;
                        tableRows = [];
                    }}
                }}
                
                // List parsing
                if (line.startsWith('*') || line.startsWith('-')) {{
                    if (!inList) {{
                        resultLines.push('<ul>');
                        inList = true;
                    }}
                    let content = line.replace(/^[*+-]\s+/, '');
                    resultLines.push('<li>' + content + '</li>');
                }} else {{
                    if (inList) {{
                        resultLines.push('</ul>');
                        inList = false;
                    }}
                    resultLines.push(lines[i]);
                }}
            }}
            if (inTable) {{
                resultLines.push(renderHTMLTable(tableRows));
            }}
            if (inList) {{
                resultLines.push('</ul>');
            }}
            
            function renderHTMLTable(rows) {{
                if (rows.length < 1) return '';
                let tableHtml = '<div class="table-container"><table>';
                for (let r = 0; r < rows.length; r++) {{
                    let cols = rows[r].split('|').map(c => c.trim()).filter((c, idx, arr) => idx > 0 && idx < arr.length - 1);
                    if (rows[r].replace(/[\s|:\-]/g, '') === '') {{
                        continue;
                    }}
                    if (r === 0) {{
                        tableHtml += '<thead><tr>' + cols.map(c => '<th>' + c + '</th>').join('') + '</tr></thead><tbody>';
                    }} else {{
                        tableHtml += '<tr>' + cols.map(c => '<td>' + c + '</td>').join('') + '</tr>';
                    }}
                }}
                tableHtml += '</tbody></table></div>';
                return tableHtml;
            }}
            
            return resultLines.join('\\n');
        }}

        function openNotesModal(courseCode) {{
            const course = COURSES_DATA.find(c => c.code.toUpperCase() === courseCode);
            if (!course) return;

            modalTitle.textContent = course.name;
            modalCode.textContent = course.code;
            modalSemestre.textContent = course.sem_num ? `${{course.sem_num}}º Semestre` : 'Taller de Grado';
            modalEstado.textContent = course.approved ? 'Aprobada' : 'Cursando';
            
            if (course.approved) {{
                modalEstado.style.color = 'var(--success)';
            }} else {{
                modalEstado.style.color = 'var(--warning)';
            }}
            
            modalPrereq.textContent = course.prereq || 'Ninguno';
            modalDescription.textContent = course.description || '';
            modalReadmeLink.href = course.link;
            
            const card = document.querySelector(`.course-card[data-code="${{course.code.toLowerCase()}}"]`);
            if (card) {{
                const iconContainer = card.querySelector('.course-icon');
                if (iconContainer) {{
                    modalEmoji.innerHTML = iconContainer.innerHTML;
                }}
            }}
            
            modalApuntes.innerHTML = parseMarkdownToHTML(course.apuntes);
            if (typeof renderMathInElement === 'function') {{
                renderMathInElement(modalApuntes, {{
                    delimiters: [
                        {{left: '$$', right: '$$', display: true}},
                        {{left: '$', right: '$', display: false}}
                    ],
                    throwOnError: false
                }});
            }}

            // Populate Directories
            modalDirs.innerHTML = '';
            if (course.existing_dirs && course.existing_dirs.length > 0) {{
                course.existing_dirs.forEach(dir => {{
                    const encodedDir = encodeURIComponent(dir);
                    const link = document.createElement('a');
                    link.className = 'dir-link';
                    link.href = `${{course.folder_path}}/${{encodedDir}}`;
                    link.target = '_blank';
                    link.innerHTML = `<i data-lucide="folder"></i> <span>${{dir}}</span>`;
                    modalDirs.appendChild(link);
                }});
            }} else {{
                modalDirs.innerHTML = '<span class="empty-list-text">No hay subcarpetas de estudio.</span>';
            }}

            // Populate Files
            modalFiles.innerHTML = '';
            if (course.existing_files && course.existing_files.length > 0) {{
                course.existing_files.forEach(file => {{
                    const encodedFile = encodeURIComponent(file);
                    const link = document.createElement('a');
                    link.className = 'file-link';
                    link.href = `${{course.folder_path}}/${{encodedFile}}`;
                    link.target = '_blank';
                    
                    let icon = 'file-text';
                    const lowerFile = file.toLowerCase();
                    if (lowerFile.endsWith('.pdf')) {{
                        icon = 'file-digit';
                    }} else if (lowerFile.endsWith('.docx') || lowerFile.endsWith('.doc')) {{
                        icon = 'file-edit';
                    }} else if (lowerFile.endsWith('.xlsx') || lowerFile.endsWith('.xls')) {{
                        icon = 'file-spreadsheet';
                    }} else if (lowerFile.endsWith('.mwb')) {{
                        icon = 'database';
                    }} else if (lowerFile.endsWith('.mp4') || lowerFile.endsWith('.avi')) {{
                        icon = 'video';
                    }}
                    
                    link.innerHTML = `<i data-lucide="${{icon}}"></i> <span>${{file}}</span>`;
                    modalFiles.appendChild(link);
                }});
            }} else {{
                modalFiles.innerHTML = '<span class="empty-list-text">No hay archivos en este directorio.</span>';
            }}

            lucide.createIcons();

            notesModal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }}

        function closeNotesModal() {{
            notesModal.classList.remove('active');
            document.body.style.overflow = '';
        }}

        modalCloseBtn.addEventListener('click', closeNotesModal);
        
        notesModal.addEventListener('click', (e) => {{
            if (e.target === notesModal) {{
                closeNotesModal();
            }}
        }});

        window.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape' && notesModal.classList.contains('active')) {{
                closeNotesModal();
            }}
        }});
        
        // Initialize Lucide Icons
        lucide.createIcons();
    </script>
</body>
</html>
'''
    return html

def build_master_readme(courses_data):
    std_courses = [c for c in courses_data if c["sem_num"] is not None]
    special_courses = [c for c in courses_data if c["sem_num"] is None]
    
    std_courses.sort(key=lambda x: (x["sem_num"], x["code"]))
    
    total_std = len(std_courses)
    approved_std = sum(1 for c in std_courses if c["approved"])
    pending_std = total_std - approved_std
    percentage = (approved_std / total_std * 100) if total_std > 0 else 0
    
    markdown = []
    markdown.append("# 🎓 Portal de Estudios - Ingeniería de Sistemas")
    markdown.append("## 🏫 Universidad Privada de Oruro (UNIOR)")
    markdown.append("### 👤 Ingeniero de Sistemas: Ing. José Luis Choquevilca")

    markdown.append("")
    markdown.append("---")
    markdown.append("")
    markdown.append("## 📊 Panel de Control y Estadísticas de Carrera")
    markdown.append(f"- **Total de Asignaturas:** {total_std}")
    markdown.append(f"- **Materias Aprobadas:** 🟢 {approved_std} ({percentage:.1f}%)")
    markdown.append(f"- **Materias Pendientes:** 🟡 {pending_std} ({100 - percentage:.1f}%)")
    markdown.append("")
    
    bar_width = 30
    filled_width = int(round(percentage / 100 * bar_width))
    bar = "█" * filled_width + "░" * (bar_width - filled_width)
    markdown.append(f"**Progreso de la carrera:**\n`[{bar}] {percentage:.1f}%`")
    markdown.append("")
    markdown.append("---")
    markdown.append("")
    markdown.append("## 🗺️ Malla Curricular e Índice de Apuntes")
    markdown.append("")
    markdown.append("| Semestre | Código | Asignatura | Estado | Acceso a Apuntes |")
    markdown.append("| :---: | :---: | :--- | :---: | :--- |")
    
    for c in std_courses:
        status_badge = "🟢 Aprobada" if c["approved"] else "🟡 Cursando"
        details = SYLLABUS_MAPPING.get(c["code"], {})
        emoji = details.get("emoji", "📚")
        markdown.append(f"| {c['sem_num']}º Sem | {c['code']} | {emoji} {c['name']} | {status_badge} | [Ver Apuntes y Prácticas]({c['link']}) |")
        
    markdown.append("")
    
    if special_courses:
        markdown.append("---")
        markdown.append("")
        markdown.append("## 📁 Cursos y Evaluaciones Especiales")
        markdown.append("")
        for c in special_courses:
            markdown.append(f"- 📂 **[{c['name']}]({c['link']})** ({c['code']})")
        markdown.append("")
        
    markdown.append("---")
    markdown.append("*Portal de control académico autogenerado para el Ing. José Luis Choquevilca - UNIOR*")
    
    return "\n".join(markdown)

def generate_readmes(root_dir):
    unior_dir = os.path.join(root_dir, "👨‍🎓 Unior [Univercidad Privada, Oruro] 💹")
    if not os.path.exists(unior_dir):
        print(f"Error: No se encontró la carpeta '{unior_dir}'")
        return
    
    folder_pattern = re.compile(r"^(\d+)\s+([A-Z]+)\s*-\s*(\d+[A-Z]*)\s+(.+)$")
    courses_data = []
    created_count = 0
    
    unior_folder_name = "👨‍🎓 Unior [Univercidad Privada, Oruro] 💹"
    encoded_unior_folder = urllib.parse.quote(unior_folder_name)
    
    for item in os.listdir(unior_dir):
        item_path = os.path.join(unior_dir, item)
        if not os.path.isdir(item_path):
            continue
            
        semester = None
        code = None
        subject_name = None
        approved = "√" in item
        sem_num = None
        
        match = folder_pattern.match(item)
        if match:
            sem_num = int(match.group(1))
            semester = f"{sem_num}º Semestre" if sem_num <= 8 else f"Taller {sem_num - 8}"
            code = f"{match.group(2)}-{match.group(3)}"
            subject_name = clean_name(match.group(4))
        else:
            semester = "Especial"
            subject_name = clean_name(item)
            code = "CURSO" if "curso" in item.lower() else "EXAMEN"
            
        # Crear físicamente las subcarpetas de temas de estudio
        course_themes = COURSE_THEMES.get(code, [])
        for theme in course_themes:
            os.makedirs(os.path.join(item_path, theme), exist_ok=True)
            
        # Obtener listado de archivos y subcarpetas actualizados
        existing_files = []
        existing_dirs = []
        for file in os.listdir(item_path):
            file_path = os.path.join(item_path, file)
            if os.path.isfile(file_path):
                existing_files.append(file)
            elif os.path.isdir(file_path) and not file.startswith("."):
                existing_dirs.append(file)
                
        readme_content = build_readme_content(semester, code, subject_name, approved, existing_files, existing_dirs)
        
        readme_path = os.path.join(item_path, "README.md")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)
            
        # Generar los README.md individuales para cada subcarpeta de tema
        course_details = SYLLABUS_MAPPING.get(code, None)
        if course_details:
            generate_theme_readmes(item_path, course_details["title"], code, course_details["apuntes"])
            prereq = course_details["prereq"]
            desc = course_details["description"]
            apuntes = course_details["apuntes"]
        else:
            prereq = "No Especificado"
            desc = "Asignatura perteneciente a la carrera de Ingeniería de Sistemas de la UNIOR."
            apuntes = "*   No hay apuntes teóricos cargados para esta materia especial."
            
        print(f"README.md y carpetas creadas en: {item}")
        created_count += 1
        
        filtered_files = [f for f in existing_files if f.lower() != "readme.md" and not f.startswith(".")]
        filtered_dirs = [d for d in existing_dirs if not d.startswith(".")]
        
        encoded_item = urllib.parse.quote(item)
        relative_link = f"./{encoded_unior_folder}/{encoded_item}/README.md"
        courses_data.append({
            "sem_num": sem_num,
            "code": code,
            "name": subject_name,
            "approved": approved,
            "link": relative_link,
            "prereq": prereq,
            "description": desc,
            "apuntes": apuntes,
            "existing_files": filtered_files,
            "existing_dirs": filtered_dirs,
            "folder_path": f"./{encoded_unior_folder}/{encoded_item}"
        })
        
    master_readme_content = build_master_readme(courses_data)
    master_readme_path = os.path.join(root_dir, "README.md")
    with open(master_readme_path, "w", encoding="utf-8") as f:
        f.write(master_readme_content)
        
    html_dashboard_content = build_html_dashboard(courses_data)
    html_dashboard_path = os.path.join(root_dir, "index.html")
    with open(html_dashboard_path, "w", encoding="utf-8") as f:
        f.write(html_dashboard_content)
        
    print(f"\nREADME.md maestro y index.html interactivo creados en la raíz.")
    print(f"Proceso finalizado. Se actualizaron {created_count} archivos README.md, portal web e índice maestro.")

if __name__ == "__main__":
    current_workspace = os.path.dirname(os.path.abspath(__file__))
    generate_readmes(current_workspace)
