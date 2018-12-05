%%% Hechos de los Recibos

es_un_recibo("123").

es_cliente_de_recibo("5719493","123").

es_nombre_de_cliente("Matias","123").

es_apellido_de_cliente("Fare","123").

es_fecha_de_recibo("2018/11/23","123").

es_observacion_de_recibo("no prende","123").

es_presupuesto_de_recibo("120.000","123").

es_validez_de_recibo("15 Dias","123").


%%% HECHOS DE UN CLIENTE

es_cliente("5719493").

es_nombre_de_cliente("Matias","5719493").
es_apellido_de_cliente("Fare","5719493").
es_contacto_de_cliente("0984908298","5719493")

%%% REGLA DE RECIBO

son_atributos_de_Recibo(Cedula, Nombre, Apellido,Observacion,Presupuesto,Validez):-
es_cliente_de_recibo(Cedula,Recibo),
es_fecha_de_recibo(Fecha,Recibo),
es_observacion_de_recibo(Observacion, Recibo),
es_presupuesto_de_recibo(Presupuesto, Recibo),
es_validez_de_recibo(Validez,Recibo).

# % HECHOS:
# es_un_pais(paraguay).
# es_un_pais(brasil).
# es_un_pais(argentina).
# es_un_pais(uruguay).
# es_un_pais(bolivia).
# limita_con(paraguay, argentina).
# limita_con(paraguay, brasil).
# limita_con(paraguay, bolivia).
# superficie_pais(paraguay, 406752).
# superficie_pais(brasil, 8547404).

# % REGLAS:
# limitrofes(X,Y):- limita_con(X,Y);

# %OR
# limita_con(Y,X).
# pais_pequeño(X) :- superficie_pai