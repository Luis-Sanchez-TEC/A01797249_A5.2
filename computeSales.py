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


def main():
    """Función principal."""
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py catálogo.json ventas.json")
        return

    prices = load_json_data(sys.argv[1])
    sales = load_json_data(sys.argv[2])

    if prices is not None and sales is not None:
        print("Archivos cargados correctamente.")


if __name__ == "__main__":
    main()