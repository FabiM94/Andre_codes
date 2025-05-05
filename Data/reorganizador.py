import pandas as pd
import os
import glob
import sys
import pathlib

def get_script_directory():
    if '__file__' in globals():
        return os.path.dirname(os.path.abspath(__file__))
    try:
        return str(pathlib.Path(__file__).parent.absolute())
    except:
        return os.getcwd()

def reorganize_excel_data(input_file, output_file):
    """
    Reorganiza datos de Excel: transponer los datos correctamente
    """
    # Leer archivo Excel sin header
    df = pd.read_excel(input_file, header=None)
    
    print(f"\n{'='*50}")
    print(f"Procesando archivo: {input_file}")
    
    # Extraer la última columna (fechas)
    last_column = df.iloc[:, -1]
    
    # Extraer todo excepto la última columna
    data = df.iloc[:, :-1]
    
    # Transponer los datos
    data_transposed = data.T
    
    # Preparar la nueva estructura
    result = data_transposed.copy()
    
    # Agregar la columna Date como primera columna
    result.insert(0, 'Date', result.index)
    
    # Resetear el índice
    result.reset_index(drop=True, inplace=True)
    
    # Asignar los nombres de las columnas (fechas)
    columns = ['Date'] + last_column.tolist()[1:]  # El primer elemento es "Date"
    result.columns = columns
    
    # Guardar el resultado
    result.to_excel(output_file, index=False)
    
    print(f"✓ Archivo guardado como: {output_file}")
    print(f"✓ Dimensiones finales: {result.shape}")
    
    # Mostrar vista previa
    print("\nVista previa:")
    print(result.head(10))
    
    print(f"{'='*50}")

def batch_process_excel_files(directory_path, output_directory):
    """
    Procesa múltiples archivos Excel en un directorio.
    """
    os.makedirs(output_directory, exist_ok=True)
    
    excel_files = [f for f in glob.glob(os.path.join(directory_path, "*.xlsx")) 
                   if 'ICC_List' not in os.path.basename(f) 
                   and 'reorganized' not in os.path.basename(f)
                   and 'output' not in os.path.basename(f)]
    
    if not excel_files:
        print("No se encontraron archivos Excel para procesar.")
        return
    
    processed_count = 0
    error_count = 0
    
    for input_file in excel_files:
        filename = os.path.basename(input_file)
        output_file = os.path.join(output_directory, f"reorganized_{filename}")
        
        try:
            reorganize_excel_data(input_file, output_file)
            processed_count += 1
        except Exception as e:
            error_count += 1
            print(f"✗ Error procesando {filename}: {str(e)}")
    
    print(f"\n{'*'*20}")
    print(f"Resumen:")
    print(f"Procesados: {processed_count}")
    print(f"Errores: {error_count}")
    print(f"{'*'*20}")

# Ejecutar el script
if __name__ == "__main__":
    script_directory = get_script_directory()
    input_directory = script_directory
    output_directory = os.path.join(script_directory, "reorganized_files")
    
    print("="*50)
    print("REORGANIZADOR DE ARCHIVOS EXCEL")
    print("="*50)
    
    batch_process_excel_files(input_directory, output_directory)
    
    print("\n¡Proceso completado!")