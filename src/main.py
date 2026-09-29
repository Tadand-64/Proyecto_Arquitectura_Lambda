import time
from batch_layer import BatchLayer
from speed_layer import SpeedLayer
from serving_layer import ServingLayer

def main():
    print("=== SIMULACIÓN DE ARQUITECTURA LAMBDA ===\n")

    # 1. BATCH LAYER
    print("[1] Ejecutando Batch Layer...")
    batch_processor = BatchLayer("data/historical_sales.csv")
    batch_view = batch_processor.process_historical_data()
    print(f"    -> Datos históricos procesados. Total Batch: ${batch_view['total_monto_batch']:.2f}")

    # 2. SPEED LAYER
    print("\n[2] Inicializando Speed Layer...")
    speed_processor = SpeedLayer()
    
    nuevas_ventas = [
        {"id": 8, "producto": "Teclado", "monto": 50.00, "fecha": "2026-09-28"},
        {"id": 9, "producto": "Monitor", "monto": 320.00, "fecha": "2026-09-28"},
        {"id": 10, "producto": "Silla Gamer", "monto": 200.00, "fecha": "2026-09-28"}
    ]

    for venta in nuevas_ventas:
        time.sleep(0.5)
        speed_processor.process_event(venta)
        print(f"    -> Nueva venta recibida en streaming: {venta['producto']} (${venta['monto']:.2f})")

    speed_view = speed_processor.get_realtime_view()

    # 3. SERVING LAYER
    print("\n[3] Consultando Serving Layer (Batch + Speed)...")
    final_result = ServingLayer.query_combined_view(batch_view, speed_view)

    print("\n================ RESULTADOS FINALES ================")
    print(f" Métrica histórica (Batch):   ${batch_view['total_monto_batch']:.2f} ({batch_view['total_ventas_batch']} ventas)")
    print(f" Métrica tiempo real (Speed):  ${speed_view['total_monto_speed']:.2f} ({speed_view['total_ventas_speed']} ventas)")
    print(f"----------------------------------------------------")
    print(f" TOTAL GENERAL CONSOLIDADO:   ${final_result['monto_total_general']:.2f} ({final_result['ventas_totales_general']} ventas)")
    print("\nVentas por Producto (Consolidado):")
    for prod, monto in final_result['monto_por_producto'].items():
        print(f"  - {prod}: ${monto:.2f}")
    print("====================================================")

if __name__ == "__main__":
    main()