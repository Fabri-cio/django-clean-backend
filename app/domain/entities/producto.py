from dataclasses import dataclass

@dataclass
class Producto:
    id: int | None
    nombre: str
    descripcion: str
    precio: float
    stock: int