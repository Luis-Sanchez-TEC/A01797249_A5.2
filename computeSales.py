"""
Módulo para el cálculo de ventas a partir de archivos JSON.
"""
import sys
import json
import time


def load_json_data(file_path):
    """Carga datos desde un archivo JSON con manejo de errores."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Error al procesar {file_path}: {error}")
    return None

def calculate_total(prices_list, sales_list):
    """Calcula el costo total usando las llaves exactas del JSON."""
    total = 0
    # Diccionario de precios: llave 'title' del catálogo
    price_map = {item.get('title'): item.get('price') for item in prices_list}

    for sale in sales_list:
        # Usamos 'Product' y 'Quantity' con MAYÚSCULA como en tu archivo
        product_name = sale.get('Product')
        quantity = sale.get('Quantity', 0)

        # Obtenemos el precio del mapa usando el nombre del producto
        price = price_map.get(product_name)

        if price is not None:
            total += price * quantity
        else:
            # Req 3: Manejo de errores para datos no encontrados
            if product_name is not None:
                print(f"Error: El producto '{product_name}' no está en el catálogo.")
            else:
                print("Error: Registro de venta con formato inválido encontrado.")

    return total

def main():
    """Función principal."""
    start_time = time.time()

    if len(sys.argv) != 3:
        print("Uso: python computeSales.py catálogo.json ventas.json")
        return

    prices = load_json_data(sys.argv[1])
    sales = load_json_data(sys.argv[2])

    if prices is not None and sales is not None:
        total = calculate_total(prices, sales)
        print(f"Cálculo completado. Total: {total:2f}")

        elapsed_time = time.time() - start_time
        print(f"Tiempo: {elapsed_time} segundos")


if __name__ == "__main__":
    main()