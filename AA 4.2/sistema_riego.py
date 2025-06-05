# Sistema de Riego Inteligente (Conversión de Prolog a Python)

# ========== DATOS DE ENTRADA (simulación de sensores) ==========
humedad_suelo = "baja"       # Valores: "baja", "media", "adecuada"
temperatura = 35             # Grados Celsius
hora_actual = 20             # Formato 24h
pronostico_lluvia = False    # True/False

# ========== BASE DE CONOCIMIENTO ==========
ZONAS = {
    1: {"tipo": "cesped", "exposicion": "sol_pleno"},
    2: {"tipo": "arbustos", "exposicion": "media_sombra"},
    3: {"tipo": "flores", "exposicion": "sombra"},
    4: {"tipo": "huerto", "exposicion": "sol_pleno"}
}

NECESIDADES_HIDRICAS = {
    "cesped": "media",
    "arbustos": "baja",
    "flores": "alta",
    "huerto": "muy_alta"
}

# ========== FUNCIONES PRINCIPALES ==========
def hora_adecuada():
    """Verifica si es hora adecuada para regar (8h o 21h+)"""
    return hora_actual >= 21 or hora_actual <= 8

def necesita_riego(tipo_planta, humedad):
    """Determina si una planta necesita riego según su tipo y humedad"""
    necesidad = NECESIDADES_HIDRICAS[tipo_planta]
    return (
        (necesidad == "alta" and humedad in ["baja", "media"]) or
        (necesidad == "muy_alta" and humedad in ["baja", "media"]) or
        (necesidad == "media" and humedad == "baja")
    )

def activar_riego_zona(zona_id):
    """Evalúa si se debe activar el riego para una zona"""
    zona = ZONAS[zona_id]
    return (
        humedad_suelo in ["baja", "media"] and
        not pronostico_lluvia and
        hora_adecuada() and
        necesita_riego(zona["tipo"], humedad_suelo)
    )

# ========== SISTEMA DE ALERTAS ==========
def alerta_temperatura():
    """Genera alertas basadas en temperatura"""
    if temperatura >= 38:
        print("ALERTA ROJA: Temperatura >38°C - Posponer riego")
    elif temperatura >= 32:
        print("ALERTA AMARILLA: Temperatura 32-37°C - Usar riego por goteo")
    else:
        print("Temperatura normal")

def alerta_humedad():
    """Genera alertas basadas en humedad"""
    if humedad_suelo == "baja":
        print("ALERTA: Humedad BAJA")
    elif humedad_suelo == "media":
        print("Precaución: Humedad MEDIA")
    else:
        print("Humedad adecuada")

# ========== RECOMENDACIONES ==========
def generar_recomendacion(tipo, exposicion, temp, humedad, lluvia):
    """Genera recomendaciones personalizadas por zona"""
    if lluvia:
        print("RECOMENDACIÓN: No regar - Lluvia pronosticada")
    elif humedad == "adecuada":
        print("Humedad óptima - No se necesita riego")
    elif tipo == "cesped" and exposicion == "sol_pleno":
        print("Regar césped 20min entre 4-6am\n   Usar aspersión en ciclos cortos")
    elif tipo == "flores" and exposicion == "sombra":
        print("Regar flores 15min al anochecer\n   Evitar mojar flores directamente")
    elif tipo == "huerto":
        print("Riego por goteo 30min al amanecer\n   Aplicar mulch para conservar humedad" 
              if temp >= 30 and humedad == "baja" 
              else "Riego estándar 20min")

def recomendacion_zona(zona_id):
    """Genera reporte completo para una zona"""
    zona = ZONAS[zona_id]
    print(f"\n=== ZONA {zona_id} ===")
    print(f"Tipo: {zona['tipo'].upper()} | Exposición: {zona['exposicion'].replace('_', ' ')}")
    alerta_temperatura()
    alerta_humedad()
    generar_recomendacion(zona["tipo"], zona["exposicion"], temperatura, humedad_suelo, pronostico_lluvia)

# ========== PRIORIZACIÓN ==========
def prioridad_riego(zona_id):
    """Calcula la prioridad de riego (alta/media/baja/minima)"""
    necesidad = NECESIDADES_HIDRICAS[ZONAS[zona_id]["tipo"]]
    return {
        "muy_alta": "alta",
        "alta": "media",
        "media": "baja",
        "baja": "minima"
    }[necesidad]

def zonas_prioritarias():
    """Lista zonas con prioridad alta"""
    prioritarias = [z for z in ZONAS if prioridad_riego(z) == "alta"]
    print("\n ZONAS PRIORITARIAS:", prioritarias if prioritarias else "Ninguna")

# ========== INTERFAZ PRINCIPAL ==========
def estado_riego():
    """Muestra el estado completo del sistema"""
    print("\n" + "="*40)
    print(" SISTEMA DE RIEGO INTELIGENTE")
    print("="*40)
    
    for zona_id in ZONAS:
        print(f"\nZona {zona_id}: ", end="")
        print("RIEGO RECOMENDADO" if activar_riego_zona(zona_id) else "No se recomienda riego")
        recomendacion_zona(zona_id)
    
    zonas_prioritarias()

# ========== EJECUCIÓN AUTOMÁTICA AL ABRIR EN VS CODE ==========
if __name__ == "__main__":
    estado_riego()
