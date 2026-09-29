import pandas as pd

class BatchLayer:
    def __init__(self, filepath):
        self.filepath = filepath

    def process_historical_data(self):
        """Procesa el dataset histórico completo."""
        df = pd.read_csv(self.filepath)
        
        total_historico = df['monto'].sum()
        conteo_historico = len(df)
        ventas_por_producto = df.groupby('producto')['monto'].sum().to_dict()
        
        batch_view = {
            "total_monto_batch": total_historico,
            "total_ventas_batch": conteo_historico,
            "ventas_por_producto_batch": ventas_por_producto
        }
        return batch_view