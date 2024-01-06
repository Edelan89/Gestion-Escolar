def porcentajeAsistencia(diasCiclo,diasAsistidos):

    if diasCiclo==0:
        return 0
    porcentajeAsistenciaAlumno = (diasAsistidos/diasCiclo)*100
    return porcentajeAsistenciaAlumno

#----------------------- Prueba --------------------
#print(porcentajeAsistencia(50))   

#---------------------- pendientes -------------------

"""Tengo que cambiar la variable asistencia por otra que sume los dias
asistidos, dado que en la app el usuario solo deberia marcar si el alumno asistio
o no, en caso de marcar la casilla como si, deberia sumarse en una variable que
calcule el porcentaje de asistencia, en relacion a los dias estipulados
por el usuario, es decir, a los dias de clases.
"""
