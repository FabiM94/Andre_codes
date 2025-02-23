import pandas as pd

def process_excel(input_file, output_file):
    """Procesa un archivo Excel, calcula el promedio cada 4 filas y guarda el resultado."""
    
    # 1. Cargar el archivo Excel
    df = pd.read_excel(input_file, header=None, skiprows=1)  # Leer datos sin encabezado, omitiendo la primera fila

    # 2. Extraer la última columna (suponiendo que contiene fechas o identificadores)
    last_column = df.iloc[:, -1]  # Selecciona la última columna
    last_column_transposed = pd.DataFrame(last_column).T  # Convertir en fila (transposición)

    # 3. Eliminar la última columna del DataFrame, ya que no se incluirá en los cálculos
    df = df.iloc[:, :-1]  

    # 4. Convertir todos los valores a números, reemplazando errores con NaN
    df = df.apply(pd.to_numeric, errors='coerce')  

    # 5. Transponer el DataFrame para que las columnas se conviertan en filas
    df_transposed = df.T  

    # 6. Agrupar cada 4 filas (correspondientes a columnas en el archivo original) y calcular la media
    df_grouped = df_transposed.groupby(df_transposed.index // 4).mean()

    # 7. Agregar la fila de fechas nuevamente al DataFrame procesado
    df_grouped_full = pd.concat([last_column_transposed, df_grouped])

    # 8. Resetear los índices para evitar inconsistencias
    df_grouped_full.reset_index(drop=True, inplace=True)


    df = df_grouped_full
    # Tomar la primera fila como encabezado y eliminarla del DataFrame
    df.columns = df.iloc[0].infer_objects()  # Asignar la primera fila como nombres de columna
    df = df[1:].reset_index(drop=True)  # Eliminar la primera fila y resetear el índice

    horas = pd.DataFrame({'Horas': range(1, 25)})
    df.insert(0, "Horas", horas)
    # 9. Guardar el DataFrame procesado en un nuevo archivo Excel
    df.to_excel(output_file, index=False, header=True)


input_file= 'Data/Heat_Demand.xlsx'
output_file="output.xlsx"
process_excel(input_file, output_file)