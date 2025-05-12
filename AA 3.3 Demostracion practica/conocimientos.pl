:- encoding(utf8).
% Base de conocimientos sobre cultura maya en Felipe Carrillo Puerto, Quintana Roo
% Enfoque en platillos y danzas tradicionales

% --------------------------------------------
% ONTOLOGÍA (Estructura del conocimiento)
% --------------------------------------------

% Tipos de elementos culturales
categoria(platillo).
categoria(danza).

% Atributos de los platillos
sabor(dulce).
sabor(salado).
sabor(picante).
sabor(agridulce).

ingrediente_principal(maiz).
ingrediente_principal(cerdo).
ingrediente_principal(pollo).
ingrediente_principal(venado).
ingrediente_principal(frijol).
ingrediente_principal(calabaza).

ocasion(festivo).
ocasion(diario).
ocasion(ceremonial).

% Atributos de las danzas
ritmo(rapido).
ritmo(lento).
ritmo(moderado).

instrumento(tunkul).
instrumento(flauta).
instrumento(tambor).
instrumento(caracol).

vestimenta(huipil).
vestimenta(calzon).
vestimenta(penacho).

% --------------------------------------------
% HECHOS (Framework de hechos)
% --------------------------------------------

% Platillos tradicionales
elemento_cultural(panuchos, platillo, [
    sabor(salado),
    ingrediente_principal(maiz),
    ingrediente_principal(frijol),
    ocasion(diario),
    descripcion('Tortilla rellena de frijol frita con carne encima')
]).

elemento_cultural(salbutes, platillo, [
    sabor(salado),
    ingrediente_principal(maiz),
    ingrediente_principal(pollo),
    ocasion(diario),
    descripcion('Tortilla frita con pollo desmenuzado, lechuga y tomate')
]).

elemento_cultural(relleno_negro, platillo, [
    sabor(picante),
    ingrediente_principal(cerdo),
    ingrediente_principal(chile),
    ocasion(festivo),
    descripcion('Carne de cerdo en salsa de chile quemado')
]).

elemento_cultural(mukbil_pollo, platillo, [
    sabor(agridulce),
    ingrediente_principal(pollo),
    ingrediente_principal(maiz),
    ocasion(ceremonial),
    descripcion('Tamal grande ceremonial cocido bajo tierra')
]).

elemento_cultural(pozol, platillo, [
    sabor(dulce),
    ingrediente_principal(maiz),
    ingrediente_principal(cacao),
    ocasion(diario),
    descripcion('Bebida refrescante de maíz y cacao')
]).

% Danzas tradicionales
elemento_cultural(la_cabeza_de_cochino, danza, [
    ritmo(rapido),
    instrumento(tunkul),
    instrumento(tambor),
    vestimenta(huipil),
    vestimenta(calzon),
    descripcion('Danza satírica que representa la caza del cerdo')
]).

elemento_cultural(la_jarana, danza, [
    ritmo(moderado),
    instrumento(flauta),
    instrumento(tambor),
    vestimenta(huipil),
    descripcion('Baile tradicional mestizo con influencia maya')
]).

elemento_cultural(la_danza_de_los_venados, danza, [
    ritmo(lento),
    instrumento(caracol),
    vestimenta(penacho),
    descripcion('Danza ritual que representa la cacería del venado')
]).

elemento_cultural(la_danza_de_los_pájaros, danza, [
    ritmo(rapido),
    instrumento(flauta),
    vestimenta(penacho),
    descripcion('Danza que imita el vuelo y canto de los pájaros')
]).

% --------------------------------------------
% REGLAS DE PRODUCCIÓN (Lógica de inferencia)
% --------------------------------------------

% Regla para recomendar platillos basados en preferencias
recomendar_platillo(PrefSabor, PrefIngrediente, PrefOcasion, Platillo) :-
    elemento_cultural(Platillo, platillo, Atributos),
    member(sabor(PrefSabor), Atributos),
    member(ingrediente_principal(PrefIngrediente), Atributos),
    member(ocasion(PrefOcasion), Atributos).

% Regla para recomendar danzas basadas en preferencias
recomendar_danza(PrefRitmo, PrefInstrumento, PrefVestimenta, Danza) :-
    elemento_cultural(Danza, danza, Atributos),
    member(ritmo(PrefRitmo), Atributos),
    member(instrumento(PrefInstrumento), Atributos),
    member(vestimenta(PrefVestimenta), Atributos).

% Regla general para obtener información detallada
obtener_info(Elemento, Info) :-
    elemento_cultural(Elemento, _, Atributos),
    member(descripcion(Info), Atributos).

% Regla para listar todos los elementos de una categoría
listar_elementos(Categoria) :-
    categoria(Categoria),
    elemento_cultural(Elemento, Categoria, _),
    write(Elemento), nl,
    fail.
listar_elementos(_).

