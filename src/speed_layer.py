class SpeedLayer:
    def __init__(self):
        self.realtime_events = []

    def process_event(self, sale_event):
        """Procesa una nueva venta recibida en tiempo real."""
        self.realtime_events.append(sale_event)

    def get_realtime_view(self):
        """Genera la vista rápida a partir de eventos en memoria."""
        total_monto_speed = sum(e['monto'] for e in self.realtime_events)
        total_ventas_speed = len(self.realtime_events)
        
        ventas_por_producto = {}
        for e in self.realtime_events:
            prod = e['producto']
            ventas_por_producto[prod] = ventas_por_producto.get(prod, 0) + e['monto']
            
        return {
            "total_monto_speed": total_monto_speed,
            "total_ventas_speed": total_ventas_speed,
            "ventas_por_producto_speed": ventas_por_producto
        }