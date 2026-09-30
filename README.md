# Proyecto: Simulación de Arquitectura Lambda en Python

Este repositorio contiene la implementación práctica y funcional de una **Arquitectura Lambda** desarrollada en Python. La solución aborda el procesamiento y consolidación de transacciones de ventas en tiempo real e históricas.

---

## 1. Problema
En los sistemas de comercio electrónico y analítica moderna, las organizaciones se enfrentan a un dilema técnico constante:
- El procesamiento en lotes (**Batch**) ofrece máxima precisión y consistencia sobre volúmenes masivos de información histórica, pero padece de alta latencia.
- El procesamiento en flujo (**Streaming / Speed**) entrega métricas instantáneas con baja latencia, pero puede ser propenso a pérdidas temporales o duplicidad en redes inestables.

Este proyecto resuelve la necesidad de calcular métricas transaccionales unificadas (ventas totales acumuladas y desglose por producto) combinando la precisión del análisis histórico con la inmediatez del análisis en tiempo real.

---

## 2. Datos
El proyecto trabaja con dos flujos de datos complementarios:

1. **Datos Históricos (Batch):** Un dataset estructurado guardado en el archivo CSV `data/historical_sales.csv`. Contiene registros con los campos: `id`, `producto`, `monto` y `fecha`.
2. **Datos en Tiempo Real (Speed):** Un flujo continuo de nuevos eventos de venta emitidos de forma simulada durante la ejecución de la aplicación.

Las instrucciones de uso y origen del dataset se encuentran documentadas en `data/README.md`.

---

## 3. Arquitectura

La solución está construida siguiendo el patrón de **Arquitectura Lambda**, dividida de forma modular en tres capas:

```
                      +-----------------------------+
                      |   Fuentes de Transacciones   |
                      +--------------+--------------+
                                     |
             +-----------------------+-----------------------+
             |                                               |
             v                                               v
  +--------------------+                           +--------------------+
  |    Batch Layer     |                           |    Speed Layer     |
  | (data/sales.csv)   |                           | (Event Stream)     |
  +----------+---------+                           +---------+----------+
             |                                               |
             v                                               v
    [Vista Batch]                                   [Vista Speed]
             |                                               |
             +-----------------------+-----------------------+
                                     |
                                     v
                          +---------------------+
                          |    Serving Layer    |
                          | (Vista Consolidada) |
                          +----------+----------+
                                     |
                                     v
                          [ Reporte Final / UI ]
```

* **Batch Layer (`src/batch_layer.py`):** Carga y procesa progresivamente el archivo histórico completo (`data/historical_sales.csv`), generando una vista agregada e inmutable de los datos pasados.
* **Speed Layer (`src/speed_layer.py`):** Ingesta los eventos de ventas entrantes en streaming, procesándolos de manera inmediata en memoria para calcular deltas recientes de baja latencia.
* **Serving Layer (`src/serving_layer.py`):** Recibe las vistas precalculadas de la capa Batch y las métricas de la capa Speed, unificando los resultados en un reporte final sin duplicidad de datos.

---

## 4. Instrucciones de Instalación

Siga estos pasos en su terminal para preparar el entorno de ejecución en cualquier equipo:

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/Tadand-64/Proyecto_Arquitectura_Lambda.git
cd Proyecto_Arquitectura_Lambda
```

### Paso 2: Crear y activar un entorno virtual (.venv)

* **En Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```

* **En Linux / macOS:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### Paso 3: Instalar dependencias
Con el entorno virtual activado, instale las librerías necesarias ejecutando:
```bash
pip install -r requirements.txt
```

---

## 5. Instrucciones de Ejecución

Para iniciar la simulación interactiva de las tres capas de la Arquitectura Lambda, ejecute el script principal desde la raíz del proyecto:

```bash
python src/main.py
```

---

## 6. Evidencias de Funcionamiento

Las capturas de pantalla de la ejecución y pruebas del programa están almacenadas dentro de la carpeta:

```text
docs/evidencias/
```

En esta sección se demuestra:
1. La correcta lectura y procesamiento del archivo CSV en la capa Batch.
2. La simulación y recepción de nuevos eventos transaccionales en la capa Speed.
3. La consolidación correcta y exacta de las métricas en la capa Serving.

---

## 7. Explicación de Resultados e Interpretación

Al ejecutar el programa, el sistema produce los siguientes resultados consolidando el flujo de datos:

1. **Capa Batch:** Procesa el dataset histórico (por ejemplo, 60 registros almacenados) calculando un gran total acumulado y desglosando la suma gastada en cada producto.
2. **Capa Speed:** Procesa un bloque de ventas entrantes con pausas simularas de tiempo real, agregando nuevos ítems como *"Silla Gamer"*, *"Monitor"*, etc.
3. **Capa Serving:** Realiza la consulta combinada. En lugar de re-leer y re-procesar todo el dataset masivo cada vez que llega una nueva venta, la Capa Serving simplemente suma la vista estática del Batch con la vista en memoria de Speed.

**Resultado práctico:** Se obtiene una latencia de respuesta prácticamente instantánea para consultas globales, reduciendo la carga computacional en bases de datos analíticas.

---

## 8. Conclusiones Individuales

### Conclusión - Integrante 1 (Tadeo)
> "La implementación práctica de este proyecto me permitió comprender el valor fundamental de la Arquitectura Lambda en entornos de Big Data. La separación clara entre la capa Batch para el histórico y la capa Speed para la inmediatez resuelve eficientemente el trade-off entre precisión y velocidad. Aprendí que la clave de esta arquitectura radica en la inmutabilidad de los datos históricos y en cómo la Serving Layer permite consultar ambos mundos sin comprometer el rendimiento del sistema."

### Conclusión - Integrante 2 (Said)
> "A través de esta práctica logré apreciar la importancia de abstraer el procesamiento de datos en capas independientes. La Capa Serving simplifica enormemente la complejidad del sistema hacia el usuario final, ocultando la lógica de combinación de flujos en tiempo real e histórico. Además, trabajar con este proyecto utilizando Git y entornos virtuales en Python reafirmó las buenas prácticas de desarrollo colaborativo exigidas en proyectos de analítica distribuida."

### Conclusión - Integrante 3 (Ari)
> "La arquitectura lambda tiene razones para ser/haber sido de las más populares por su utilidad en proyectos relacionados con el procesamiento y el flujo de datos, ya que permite tener una visión de un parámetro a través de los datos históricos, mismo es de utilidad para su uso en la interpretación de los datos en flujo (streaming), lo cual puede agilizar la toma de decisiones al tener en claro el comportamiento esperado o habitual de una población o entidad. Este es el principal fuerte de la arquitectura Lambda, que la vuelve confiable para su uso en la interpretación de datos nuevos y de flujo constante."

### Conclusión - Integrante 4 (Danae)
> "Lambda combina una capa batch (precisa, con todo el histórico) y una capa de streaming (rápida, con lo más reciente), así que logra equilibrio entre precisión y velocidad. Su desventaja es que es más compleja y difícil de mantener, porque hay que operar dos sistemas con la misma lógica. Por eso conviene cuando se necesita análisis histórico exacto junto con tiempo real."

---

## Estructura del Repositorio

```text
Proyecto_Arquitectura_Lambda/
│
├── README.md                   # Documentación general e instrucciones
├── requirements.txt            # Dependencias de Python
│
├── src/                        # Código fuente
│   ├── batch_layer.py          # Lógica de la Capa Batch
│   ├── speed_layer.py          # Lógica de la Capa Speed
│   ├── serving_layer.py        # Lógica de la Capa Serving
│   └── main.py                 # Punto de entrada de la aplicación
│
├── data/                       # Datasets
│   ├── historical_sales.csv    # Datos históricos
│   └── README.md               # Instrucciones del dataset
│
└── docs/                       # Documentación técnica
    ├── arquitectura.png        # Diagrama de arquitectura
    └── evidencias/             # Evidencias de ejecución
```