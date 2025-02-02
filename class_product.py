class Product:

    # Defining Class
    def __init__(self, name, quantity: float = 0, unit_of_measurement: str = 'unit', category: str = '', **kwargs):
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = unit_of_measurement
        self.category = category
        for key, value in kwargs.items():
            setattr(self, key, value)

    # Defininf str output
    def __str__(self) -> str:
        return f"{self.category}: {self.name}- {self.quantity} {self.unit_of_measurement}"

    # Defininf repr output
    def __repr__(self) -> str:
        return f"'{self.name}': ({self.quantity}, '{self.unit_of_measurement}', '{self.category}')"