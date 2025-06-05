%% DATOS DE ENTRADA (simulacion de sensores)
humedad_suelo(baja).          % valores posibles: baja, media, adecuada
temperatura(35).              % en grados Celsius
hora(20).                     % formato 24h
pronostico_lluvia(false).     % true/false

%% DEFINICION DE ZONAS DE RIEGO
% zona(Id, TipoVegetacion, ExposicionSolar)
zona(1, cesped, sol_pleno).
zona(2, arbustos, media_sombra).
zona(3, flores, sombra).
zona(4, huerto, sol_pleno).

%% NECESIDADES HIDRICAS POR TIPO DE VEGETACION
% necesidad_riego(TipoVegetacion, Necesidad)
necesidad_riego(cesped, media).
necesidad_riego(arbustos, baja).
necesidad_riego(flores, alta).
necesidad_riego(huerto, muy_alta).

%% REGLAS PRINCIPALES

% Hora adecuada para riego (evitar horas de mucho sol)
hora_adecuada :- 
    hora(H), 
    (H >= 21 ; H =< 8).

% Regla principal para activar riego en una zona especifica
activar_riego_zona(Zona) :-
    zona(Zona, TipoPlanta, _),
    humedad_suelo(Humedad),
    (Humedad = baja ; Humedad = media),
    pronostico_lluvia(false),
    hora_adecuada,
    necesita_riego(TipoPlanta, Humedad).

% Determina si el tipo de planta necesita riego segun humedad actual
necesita_riego(TipoPlanta, Humedad) :-
    necesidad_riego(TipoPlanta, Necesidad),
    ((Necesidad = alta, (Humedad = baja ; Humedad = media));
     (Necesidad = muy_alta, (Humedad = baja ; Humedad = media));
     (Necesidad = media, Humedad = baja)).

%% SISTEMA DE ALERTAS MEJORADO [Resto del código permanece igual...]

%% SISTEMA DE ALERTAS MEJORADO

% Alertas por temperatura
alerta_temperatura :-
    temperatura(T),
    (T >= 38 -> 
        write('ALERTA ROJA: Temperatura extremadamente alta (>38C). Posponer riego.'), nl,
        fail;
     T >= 32 -> 
        write('ALERTA AMARILLA: Temperatura alta (32-37C). Usar riego por goteo.'), nl;
     write('Temperatura dentro de rangos normales'), nl).

% Alertas por humedad
alerta_humedad :-
    humedad_suelo(H),
    (H = baja -> write('ALERTA: Humedad del suelo BAJA'), nl;
     H = media -> write('Precaucion: Humedad del suelo MEDIA'), nl;
     write('Humedad del suelo adecuada'), nl).

%% RECOMENDACIONES ESPECIFICAS POR ZONA

recomendacion_zona(Zona) :-
    zona(Zona, TipoPlanta, Exposicion),
    temperatura(T),
    humedad_suelo(Humedad),
    pronostico_lluvia(Lluvia),
    write('=== RECOMENDACION PARA ZONA '), write(Zona), write(' ==='), nl,
    write('Tipo: '), write(TipoPlanta), nl,
    write('Exposicion: '), write(Exposicion), nl, nl,
    alerta_temperatura,
    alerta_humedad, nl,
    generar_recomendacion(TipoPlanta, Exposicion, T, Humedad, Lluvia).

% Reglas de recomendacion especificas
generar_recomendacion(cesped, sol_pleno, T, baja, false) :-
    T >= 32,
    write('RECOMENDACION: Regar cesped 20 minutos entre 4-6am'), nl,
    write('Usar riego por aspersion en ciclos cortos'), nl.

generar_recomendacion(flores, sombra, _, baja, false) :-
    write('RECOMENDACION: Regar flores 15 minutos al anochecer'), nl,
    write('Evitar mojar las flores directamente'), nl.

generar_recomendacion(huerto, sol_pleno, T, Humedad, false) :-
    (T >= 30, Humedad = baja) ->
        write('RECOMENDACION: Riego por goteo 30 minutos al amanecer'), nl,
        write('Aplicar mulch para conservar humedad'), nl;
    write('RECOMENDACION: Riego estandar 20 minutos'), nl.

generar_recomendacion(_, _, _, _, true) :-
    write('RECOMENDACION: No regar - Se espera lluvia'), nl.

generar_recomendacion(_, _, _, adecuada, _) :-
    write('RECOMENDACION: No se necesita riego - Humedad adecuada'), nl.

%% PRIORIZACION DE RIEGO

% prioridad_riego(Zona, Prioridad)
prioridad_riego(Zona, alta) :-
    zona(Zona, TipoPlanta, _),
    necesidad_riego(TipoPlanta, muy_alta).

prioridad_riego(Zona, media) :-
    zona(Zona, TipoPlanta, _),
    necesidad_riego(TipoPlanta, alta).

prioridad_riego(Zona, baja) :-
    zona(Zona, TipoPlanta, _),
    necesidad_riego(TipoPlanta, media).

prioridad_riego(Zona, minima) :-
    zona(Zona, TipoPlanta, _),
    necesidad_riego(TipoPlanta, baja).

%% INTERFAZ DE CONSULTA PRINCIPAL

% Consulta el estado de todas las zonas
estado_riego :-
    write('=== ESTADO DEL SISTEMA DE RIEGO ==='), nl, nl,
    forall(zona(Z, _, _), (
        write('Zona '), write(Z), write(': '),
        (activar_riego_zona(Z) -> 
            write('RIEGO RECOMENDADO'), nl;
            write('No se recomienda riego'), nl),
        recomendacion_zona(Z), nl
    )).

% Consulta zonas con prioridad alta
zonas_prioritarias :-
    write('=== ZONAS CON PRIORIDAD ALTA DE RIEGO ==='), nl,
    findall(Z, prioridad_riego(Z, alta), Zonas),
    (Zonas = [] -> 
        write('No hay zonas con prioridad alta'), nl;
        write('Zonas prioritarias: '), write(Zonas), nl).