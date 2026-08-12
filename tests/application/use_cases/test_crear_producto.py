from app.application.use_cases.crear_producto import CrearProductoUseCase
from app.infrastructure.persistence.repositories.in_memory_producto_repository import InMemoryProductoRepository

def test_crear_producto():
    # Arrange
    repository = InMemoryProductoRepository()
    use_case = CrearProductoUseCase(repository)

    # Act
    producto = use_case.ejecutar(
        nombre="Laptop",
        descripcion="Laptop Lenovo",
        precio=5000,
        stock=10,
    )

    # Assert
    assert producto.id == 1
    assert producto.nombre == "Laptop"
    assert producto.descripcion == "Laptop Lenovo"
    assert producto.precio == 5000
    assert producto.stock == 10