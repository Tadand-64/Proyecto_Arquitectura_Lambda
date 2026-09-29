# Proyecto: Simulación de Arquitectura Lambda

Este proyecto implementa una simulación en Python de una Arquitectura Lambda para un sistema de ventas.

## Componentes

- **Batch Layer (`src/batch_layer.py`):** Procesa datos históricos desde un CSV.
- **Speed Layer (`src/speed_layer.py`):** Procesa eventos de ventas entrantes en tiempo real.
- **Serving Layer (`src/serving_layer.py`):** Combina ambas vistas para mostrar métricas consolidadas.

## Ejecución

1. Activar el entorno virtual:
   ```bash
   source .venv/bin/activate   # En Linux/macOS
   .\.venv\Scripts\Activate.ps1 # En Windows