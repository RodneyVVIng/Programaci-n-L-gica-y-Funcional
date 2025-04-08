from functools import reduce
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, ttk, Text, END
from typing import List, Dict, Tuple, Optional
from collections import defaultdict

# Tipos de datos
Evaluacion = Dict[str, int]
AsignaturaEvaluada = Dict[str, List[Evaluacion]]


def promedio_recursivo(calificaciones: List[float], acum: float = 0.0, n: int = 0) -> float:
    """
    Versión recursiva para calcular promedio.
    Args:
        calificaciones: Lista de valores a promediar.
        acum: Acumulador (inicia en 0).
        n: Contador (inicia en 0).
    Returns:
        Promedio de las calificaciones.
    """
    if not calificaciones:
        return acum / n if n > 0 else 0.0
    return promedio_recursivo(calificaciones[1:], acum + calificaciones[0], n + 1)


def calcular_promedio_aspecto(evaluaciones: List[Evaluacion], aspecto: str) -> float:
    """Versión con recursividad."""
    calificaciones = [e.get(aspecto, 0) for e in evaluaciones]
    return promedio_recursivo(calificaciones)

def calcular_promedio_general(evaluaciones: List[Evaluacion], aspectos: List[str]) -> float:
    """Calcula el promedio general de todas las calificaciones."""
    if not evaluaciones:
        return 0.0
    calificaciones = [e[aspecto] for e in evaluaciones for aspecto in aspectos if aspecto in e]
    return sum(calificaciones) / len(calificaciones) if calificaciones else 0.0

def mejores_peores_aspectos(evaluaciones: List[Evaluacion], aspectos: List[str]) -> Tuple[List[Tuple[str, float]], List[Tuple[str, float]]]:
    """Identifica los 3 aspectos mejor y peor calificados."""
    aspectos_validos = [a for a in aspectos if all(a in e for e in evaluaciones)]
    promedios = [(a, calcular_promedio_aspecto(evaluaciones, a)) for a in aspectos_validos]
    mejores = sorted(promedios, key=lambda x: -x[1])[:3]
    peores = sorted(promedios, key=lambda x: x[1])[:3]
    return mejores, peores

class EncuestaApp:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Evaluación de Asignaturas")
        
        # Aspectos a evaluar
        self.aspectos = ["Contenido", "Actividades", "Herramientas", "Claridad", "Utilidad"]
        
        # Datos
        self.evaluaciones_por_asignatura = defaultdict(list)
        self.current_asignatura = None
        
        # Interfaz
        self.setup_ui()
    
    def setup_ui(self):
        """Configura la interfaz gráfica."""
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Campos de entrada
        ttk.Label(main_frame, text="Asignatura:").grid(row=0, column=0, sticky="e")
        self.entry_asignatura = ttk.Entry(main_frame)
        self.entry_asignatura.grid(row=0, column=1, sticky="ew")
        
        # Campos para calificaciones
        self.entries = {}
        for i, aspecto in enumerate(self.aspectos, 1):
            ttk.Label(main_frame, text=f"{aspecto} (1-5):").grid(row=i, column=0, sticky="e")
            self.entries[aspecto] = ttk.Entry(main_frame)
            self.entries[aspecto].grid(row=i, column=1, sticky="ew")
        
        # Botones
        ttk.Button(main_frame, text="Agregar Evaluación", command=self.agregar_evaluacion).grid(
            row=len(self.aspectos)+1, column=0, columnspan=2, pady=10)
        
        # Área de resultados
        self.text_resultados = Text(main_frame, height=15, width=50, wrap="word")
        self.text_resultados.grid(row=len(self.aspectos)+2, column=0, columnspan=2, sticky="ew")
        
        # Historial
        ttk.Label(main_frame, text="Historial por Asignatura:").grid(
            row=len(self.aspectos)+3, column=0, sticky="w")
        self.combo_asignaturas = ttk.Combobox(main_frame, state="readonly")
        self.combo_asignaturas.grid(row=len(self.aspectos)+3, column=1, sticky="ew")
        self.combo_asignaturas.bind("<<ComboboxSelected>>", self.mostrar_historial)
        
        # Métricas generales
        ttk.Button(main_frame, text="Mostrar Métricas Generales", 
                  command=self.mostrar_metricas_generales).grid(
                      row=len(self.aspectos)+4, column=0, columnspan=2, pady=10)
    
    def agregar_evaluacion(self):
        """Agrega una nueva evaluación."""
        asignatura = self.entry_asignatura.get().strip()
        if not asignatura:
            messagebox.showerror("Error", "Ingrese el nombre de la asignatura")
            return
        
        try:
            evaluacion = {}
            for aspecto in self.aspectos:
                valor = int(self.entries[aspecto].get())
                if not 1 <= valor <= 5:
                    raise ValueError("Las calificaciones deben ser entre 1 y 5")
                evaluacion[aspecto] = valor
            
            self.evaluaciones_por_asignatura[asignatura].append(evaluacion)
            self.current_asignatura = asignatura
            
            # Limpiar campos
            for entry in self.entries.values():
                entry.delete(0, END)
            
            self.actualizar_combobox()
            self.mostrar_resultados()
            messagebox.showinfo("Éxito", "Evaluación agregada correctamente")
        except ValueError as e:
            messagebox.showerror("Error", f"Dato inválido: {e}")
    
    def mostrar_resultados(self):
        """Muestra los resultados de la evaluación actual."""
        if not self.current_asignatura:
            return
        
        evaluaciones = self.evaluaciones_por_asignatura[self.current_asignatura]
        if not evaluaciones:
            return
        
        self.text_resultados.delete(1.0, END)
        
        # Promedio general
        promedio = calcular_promedio_general(evaluaciones, self.aspectos)
        self.text_resultados.insert(END, f"Resultados para: {self.current_asignatura}\n")
        self.text_resultados.insert(END, f"Promedio General: {promedio:.2f}\n\n")
        
        # Aspectos destacados
        mejores, peores = mejores_peores_aspectos(evaluaciones, self.aspectos)
        
        self.text_resultados.insert(END, "Aspectos mejor calificados:\n")
        for aspecto, promedio in mejores:
            self.text_resultados.insert(END, f"- {aspecto}: {promedio:.2f}\n")
        
        self.text_resultados.insert(END, "\nAspectos a mejorar:\n")
        for aspecto, promedio in peores:
            self.text_resultados.insert(END, f"- {aspecto}: {promedio:.2f}\n")
        
        self.text_resultados.insert(END, f"\nTotal evaluaciones: {len(evaluaciones)}\n")
    
    def mostrar_historial(self, event=None):
        """Muestra el historial de una asignatura seleccionada."""
        asignatura = self.combo_asignaturas.get()
        if asignatura:
            self.current_asignatura = asignatura
            self.mostrar_resultados()
    
    def mostrar_metricas_generales(self):
        """Muestra métricas de todas las asignaturas."""
        if not self.evaluaciones_por_asignatura:
            messagebox.showinfo("Info", "No hay evaluaciones registradas")
            return
        
        self.text_resultados.delete(1.0, END)
        self.text_resultados.insert(END, "Métricas Generales:\n\n")
        
        # Promedios por asignatura
        for asignatura, evaluaciones in self.evaluaciones_por_asignatura.items():
            promedio = calcular_promedio_general(evaluaciones, self.aspectos)
            self.text_resultados.insert(END, f"{asignatura}:\n")
            self.text_resultados.insert(END, f"  Promedio General: {promedio:.2f}\n")
            
            mejores, peores = mejores_peores_aspectos(evaluaciones, self.aspectos)
            self.text_resultados.insert(END, f"  Mejor Aspecto: {mejores[0][0]} ({mejores[0][1]:.2f})\n")
            self.text_resultados.insert(END, f"  Peor Aspecto: {peores[0][0]} ({peores[0][1]:.2f})\n")
            self.text_resultados.insert(END, f"  Total Evaluaciones: {len(evaluaciones)}\n\n")
    
    def actualizar_combobox(self):
        """Actualiza la lista de asignaturas en el combobox."""
        asignaturas = list(self.evaluaciones_por_asignatura.keys())
        self.combo_asignaturas["values"] = asignaturas
        if asignaturas:
            self.combo_asignaturas.set(asignaturas[-1])

def main():
    root = Tk()
    app = EncuestaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()