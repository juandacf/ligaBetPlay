def addMatch (Teams):
    switchaddMatch = True 
    while switchaddMatch:
        try:
            switchTeam1 = False 
            switchTeam2 = False 
            equipo1 = str(input("Por favor, ingrese el nombre del primer equipo: ")).lower()
            marcadorEquipo1 = int(input("Por favor, ingrese la cantidad de goles anotador por el primer equipo: "))
            equipo2 = str(input("Por favor, ingrese el nombre del segundo equipo: ")).lower()
            marcadorEquipo2 = int(input("Por favor, ingrese la cantidad de goles anotador por el segundo equipo: "))
            local = str(input("Por favor, ingrese el nombre del equipo que jugó de local: "))
        except:
            input('Los datos ingresados no son adecuados. presione una letra para volverlo a intentar: ')
            addMatch(Teams)

        for k,v in Teams.items():
            if equipo1 in v.get("nombre"):
                switchTeam1=True
                codigoTeam1 = k
            if equipo2 in v.get("nombre"):
                switchTeam2=True
                codigoTeam2 = k


        
        if (switchTeam1==True and switchTeam2==True) and (equipo1==local or equipo2==local):
            Teams[codigoTeam1]['estadisticas']['partidosJugados']+=1  
            Teams[codigoTeam2]['estadisticas']['partidosJugados']+=1
            Teams[codigoTeam1]['estadisticas']['golesAFavor']+=marcadorEquipo1
            Teams[codigoTeam2]['estadisticas']['golesAFavor']+=marcadorEquipo2
            Teams[codigoTeam1]['estadisticas']['golesEnContra']+=marcadorEquipo2
            Teams[codigoTeam2]['estadisticas']['golesEnContra']+=marcadorEquipo1
            if (equipo1==local):
                Teams[codigoTeam1]['estadisticas']['partidosLocal']+=1
                Teams[codigoTeam2]['estadisticas']['partidosVisitante']+=1
            elif (equipo2==local):
                Teams[codigoTeam2]['estadisticas']['partidosLocal']+=1
                Teams[codigoTeam1]['estadisticas']['partidosVisitante']+=1

            if (marcadorEquipo1>marcadorEquipo2):
                Teams[codigoTeam1]['estadisticas'][ 'partidosGanados']+=1
                Teams[codigoTeam1]['estadisticas'][ 'totalPuntos']+=3
                Teams[codigoTeam2]['estadisticas'][ 'partidosPerdidos']+=1
            elif (marcadorEquipo2>marcadorEquipo1):
                Teams[codigoTeam2]['estadisticas'][ 'partidosGanados']+=1
                Teams[codigoTeam2]['estadisticas'][ 'totalPuntos']+=3
                Teams[codigoTeam1]['estadisticas'][ 'partidosPerdidos']+=1
            else:
                Teams[codigoTeam1]['estadisticas'][ 'partidosEmpatados']+=1
                Teams[codigoTeam2]['estadisticas'][ 'partidosEmpatados']+=1
                Teams[codigoTeam1]['estadisticas'][ 'totalPuntos']+=1
                Teams[codigoTeam2]['estadisticas'][ 'totalPuntos']+=1

        else: 
            input("Los equipos ingresados no se pudieron encontrar en nuestros registros. Por favor, inténtelo nuevamente")
        switchaddMatch = bool(input("Si quiere agregar otra fecha, ingrese cualquier caracter. Si no, ingrese enter."))


def addPlayerStatistics(Teams):
    switchPlayerStatistics = True
    while switchPlayerStatistics:
        try:
            equipo= str(input("Por favor, ingrese el nombre del equipo al cual pertenece el jugador: ")).lower()
            nombreJugador= str(input("Por favor, ingrese el nombre del jugador:  ")).lower()
            golesAnotados= int(input("Por favor, ingrese el número de goles anotados: "))
            tarjetasAmarillas= int(input("Por favor, ingrese el número de tarjetas amarillas del jugador: "))
            tarjetasRojas= int(input("Por favor, ingrese el número de tarjetas rojas del jugador. "))
            totalFaltas= int(input("Por favor, ingrese el número total de faltas del jugador: "))
        except:
            input('Los datos ingresados no son aropiados. Por favor, oprima enter y vuélvalo a intentar.')
            addPlayerStatistics(Teams)


        for i in range(1,len(Teams)+1):
                for k,v in Teams.items():
                    if equipo in v.get('nombre'):
                        indiceEquipo= k
                    for a,b in v.get('jugadores').items():
                        if nombreJugador in b.get('nombre'):
                            indiceJugador = a
                            Teams[indiceEquipo]['jugadores'][indiceJugador]['estadisticas']['golesAnotados']+=golesAnotados
                            Teams[indiceEquipo]['jugadores'][indiceJugador]['estadisticas']['tarjetasAmarillas']+=tarjetasAmarillas
                            Teams[indiceEquipo]['jugadores'][indiceJugador]['estadisticas']['tarjetasRojas']+=tarjetasRojas
                            Teams[indiceEquipo]['jugadores'][indiceJugador]['estadisticas']['totalFaltas']+=totalFaltas
                            print("Los datos se han añadido correctamente.")
                        
        
        switchPlayerStatistics = bool(input("Si desea seguir añadiendo estadísticas, presione cualquier caracter. Si no, presione enter."))

                    
    





