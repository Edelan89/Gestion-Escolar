def porcentajeAsistencia(diasCiclo,diasAsistidos):

    if diasCiclo==0:
        return 0
    porcentajeAsistenciaAlumno = (diasAsistidos/diasCiclo)*100
    return porcentajeAsistenciaAlumno

def asistenciasFaltantes():

    