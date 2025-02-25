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

def ICC_trasnform(input_file, output_file):
    # Cargar el archivo Excel
    df = pd.read_excel(input_file, header=None)  # Cargar sin encabezado si no tiene

    # Transponer el DataFrame
    df_transpuesto = df.T[::-1].reset_index(drop=True)
    # Convertir la primera fila en encabezado
    df_transpuesto.columns = df_transpuesto.iloc[0]  # Asignar la primera fila como encabezado
    df_transpuesto = df_transpuesto[1:].reset_index(drop=True)  # Eliminar la fila usada como header
    df= df_transpuesto
     # Eliminar filas 2 y 3 (índices en pandas empiezan en 0)
    df = df.drop(index=[1, 2])

    # Tomar la fila 1 y repetirla 24 veces
    fila_1 = df.iloc[0]  # Seleccionar la fila 1
    df_repetida = pd.DataFrame([fila_1] * 23, columns=df.columns)  # Repetir 24 veces

    # Combinar la fila 0 original con la fila repetida
    df_final = pd.concat([df.iloc[[0]], df_repetida], ignore_index=True)
    
    # Renombrar la primera columna como "time"
    df_final.rename(columns={df_final.columns[0]: "time"}, inplace=True)

    # Reemplazar los valores de "time" con números del 1 al 24
    df_final["time"] = range(1, 25)

    return df_final
                  
input_file= 'Data/ICC_list.xlsx'
output_file="Param/Param_ICC.xlsx"
#process_excel(input_file, output_file)
print(ICC_trasnform(input_file,output_file))
