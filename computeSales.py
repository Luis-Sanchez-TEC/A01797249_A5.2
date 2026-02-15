"""
Módulo para el cálculo de ventas a partir de archivos JSON.
"""
import sys
import json
import time


def load_json_data(file_path):
    """Carga datos desde un archivo JSON con diagnóstico."""
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
        if not isinstance(sale, dict):
            continue

        product_name = sale.get('Product')
        quantity = sale.get('Quantity', 0)
        price = price_map.get(product_name)

        if price is not None:
            total += price * quantity
        else:
            if product_name is not None:
                print(f"Error: Producto '{product_name}' no en catálogo.")
    return total


def main():
    """Función principal para coordinar la ejecución del programa."""
    start_time = time.time()

    if len(sys.argv) != 3:
        print("Uso: python3 computeSales.py catálogo.json ventas.json")
        return

    prices_data = load_json_data(sys.argv[1])
    sales_data = load_json_data(sys.argv[2])

    if prices_data is not None and sales_data is not None:
        total = calculate_total(prices_data, sales_data)
        elapsed_time = time.time() - start_time

        results = (
            f"TOTAL DE VENTAS: ${total:,.2f}\n"
            f"TIEMPO DE EJECUCIÓN: {elapsed_time:.4f} segundos"
        )

        print(results)

        with open("SalesResults.txt", "w", encoding='utf-8') as f:
            f.write(results)
    else:
        print("Error: No se pudieron procesar los archivos.")


if __name__ == "__main__":
    main()
