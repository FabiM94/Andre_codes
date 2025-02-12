import customtkinter as ctk
from pandastable import Table
import pandas as pd

class PandasTableApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Tabla Personalizada")
        self.geometry("800x600")
        ctk.set_appearance_mode("dark")

        custom_color = "#FF5733"  # Cambia este color para modificar el azul

        frame = ctk.CTkFrame(self, fg_color=custom_color)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        df = pd.DataFrame({
            "Columna 1": [1, 2, 3, 4],
            "Columna 2": ["A", "B", "C", "D"],
            "Columna 3": [10.5, 20.3, 30.7, 40.2]
        })

        self.table = Table(frame, dataframe=df, showtoolbar=False, showstatusbar=False)
        self.table.show()

        options = {
        "rowselectedcolor": "#444444",  # Color de fila seleccionada
    "grid_color": "#666666",        # Color de la cuadrícula
    "cellbackgr": "#222222",        # Fondo de las celdas
    "textcolor": "white",           # Color del texto
    "fontsize": 12                  # Tamaño de la fuente
    }
        self.table.applyOptions(options)
        self.table.redraw()


if __name__ == "__main__":
    app = PandasTableApp()
    app.mainloop()
