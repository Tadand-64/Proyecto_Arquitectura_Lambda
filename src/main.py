import os
import sys
import time
from batch_layer import BatchLayer
from speed_layer import SpeedLayer
from serving_layer import ServingLayer

def main():
    print("====================================================")
    print("      SIMULACIÓN DE ARQUITECTURA LAMBDA (PYTHON)     ")
    print("====================================================\n")

    # Determinar la ruta relativa al archivo CSV de forma dinámica
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "..", "data", "historical_sales.csv")

    # 1. BATCH LAYER: Procesar datos históricos masivos
    print("[1] Ejecutando Batch Layer (Procesando historial)...")
    if not os.path.exists(data_path):
        print(f"    [Error] No se encontró el archivo de datos en: {data_path}")
        sys.exit(1)

    batch_processor = BatchLayer(data_path)
    batch_view = batch_processor.process_historical_data()
    print(f"    -> Datos históricos procesados con éxito.")
    print(f"    -> Registros procesados: {batch_view['total_ventas_batch']}")
    print(f"    -> Total acumulado Batch: ${batch_view['total_monto_batch']:.2f}")

    # 2. SPEED LAYER: Procesar flujo de nuevos eventos en tiempo real
    print("\n[2] Inicializando Speed Layer (Iniciando receptor streaming)...")
    speed_processor = SpeedLayer()
    
    # Nuevas ventas simuladas llegando en streaming
    nuevas_ventas = [
        {"id": 61, "producto": "Teclado", "monto": 50.00, "fecha": "2026-09-28"},
        {"id": 62, "producto": "Monitor", "monto": 320.00, "fecha": "2026-09-28"},
        {"id": 63, "producto": "Silla Gamer", "monto": 200.00, "fecha": "2026-09-28"},
        {"id": 64, "producto": "Laptop", "monto": 1200.00, "fecha": "2026-09-29"},
        {"id": 65, "producto": "Mouse", "monto": 25.50, "fecha": "2026-09-29"},
        {"id": 66, "producto": "Webcam", "monto": 60.00, "fecha": "2026-09-29"},
        {"id": 67, "producto": "Audifonos", "monto": 80.00, "fecha": "2026-09-30"},
        {"id": 68, "producto": "Micrófono USB", "monto": 95.00, "fecha": "2026-09-30"},
        {"id": 69, "producto": "Disco Duro", "monto": 110.00, "fecha": "2026-09-30"},
        {"id": 70, "producto": "Impresora", "monto": 180.00, "fecha": "2026-09-30"}
    ]

    for venta in nuevas_ventas:
        time.sleep(0.4)  # Simula latencia en la llegada del evento
        speed_processor.process_event(venta)
        print(f"    -> [EVENTO RECIBIDO] ID: {venta['id']} | Producto: {venta['producto']:<15} | Monto: ${venta['monto']:.2f}")

    speed_view = speed_processor.get_realtime_view()

    # 3. SERVING LAYER: Unificar vistas estáticas e instantáneas
    print("\n[3] Consultando Serving Layer (Unificando Batch + Speed)...")
    final_result = ServingLayer.query_combined_view(batch_view, speed_view)

    # REPORTE FINAL CONSOLIDADOS
    print("\n====================================================")
    print("               RESULTADOS CONSOLIDADOS              ")
    print("====================================================")
    print(f" Métrica histórica (Batch Layer):  ${batch_view['total_monto_batch']:>10.2f}  ({batch_view['total_ventas_batch']} ventas)")
    print(f" Métrica tiempo real (Speed Layer): ${speed_view['total_monto_speed']:>10.2f}  ({speed_view['total_ventas_speed']} ventas)")
    print(f"----------------------------------------------------")
    print(f" TOTAL GENERAL COMBINADO:           ${final_result['monto_total_general']:>10.2f}  ({final_result['ventas_totales_general']} ventas)")
    print("\nDesglose de Ventas por Producto (Consolidado):")
    for prod, monto in sorted(final_result['monto_por_producto'].items(), key=lambda x: x[1], reverse=True):
        print(f"  - {prod:<15}: ${monto:>8.2f}")
    print("====================================================")

if __name__ == "__main__":
    main()