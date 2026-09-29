class ServingLayer:
    @staticmethod
    def query_combined_view(batch_view, speed_view):
        """Combina los resultados de la capa Batch y la capa Speed."""
        monto_total = batch_view['total_monto_batch'] + speed_view['total_monto_speed']
        ventas_totales = batch_view['total_ventas_batch'] + speed_view['total_ventas_speed']
        
        productos_combinados = batch_view['ventas_por_producto_batch'].copy()
        for prod, monto in speed_view['ventas_por_producto_speed'].items():
            productos_combinados[prod] = productos_combinados.get(prod, 0) + monto
            
        return {
            "monto_total_general": monto_total,
            "ventas_totales_general": ventas_totales,
            "monto_por_producto": productos_combinados
        }