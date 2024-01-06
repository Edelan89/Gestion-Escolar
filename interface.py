from tkinter import * 
from Funciones.porcentajeAsistencia import porcentajeAsistencia
from Funciones.promedioNota import calculoPromedio
from tkinter import ttk

root = Tk()

#--------------- Frame promedio ----------------

frame_promedio = Frame(root)
frame_promedio.pack(side="left")

#----------------- Frame de la barra vertical -----------------

# frame_barra_vertical_separadora = Frame(root)
# frame_barra_vertical_separadora.pack(side= LEFT, expand= True, fill = BOTH)

#---------------- Frame Asistencias ----------------

frame_asistencia = Frame(root)
frame_asistencia.pack(side="left")

#---------------------- Estilo de la barra vertical -----------------------

# styl = ttk.Style()
# styl.configure('red.TSeparator', background='red')

#------------------ lista con las notas - promedio -------------

"""Me da un error al querer usar calculoPromedio, no me esta
reconociendo los float en la funcion
Solucion: usar text = calculoPromedio(listaDatos), dado que solo reconoce str para mostrar en la app"""

def recuperarDatosPromedio():
    
    try:
        num1 = float(nota1Entry.get())
        num2 = float(nota2Entry.get())
        num3 = float(nota3Entry.get())    
        listaDatos = [num1, num2, num3]

        if calculoPromedio(listaDatos)>70:

            notaPromedioShow.config(text=calculoPromedio(listaDatos), foreground="green")

        else: 

            notaPromedioShow.config(text=calculoPromedio(listaDatos), foreground="red")
            
    except ValueError:

        notaPromedioShow.config(text="Debe ingresar numeros en las casillas Nota 1, Nota 2 y Nota 3")
#------------------ lista con las notas - promedio -------------

def recuperarDatosAsistencia():

    try:

        diasCiclo = float(diasDelCicloLectivoEntry.get())
        diasAsistidos = float(diasAlumnoAsistenciaEntry.get())
        
        if porcentajeAsistencia(diasCiclo, diasAsistidos) >= 85:
            AsistenciaPorcentajeShow.config(text="{}%".format(porcentajeAsistencia(diasCiclo, diasAsistidos)), foreground="green")

        else:
            AsistenciaPorcentajeShow.config(text="{}%".format(porcentajeAsistencia(diasCiclo, diasAsistidos)), foreground="red")

    except ValueError:

        AsistenciaPorcentajeShow.config(text="Debe ingresar numeros en las casillas dias del ciclo lectivo y dias asistidos")
#--------------- Textos Promedio --------------------------

nombreAlumnoPromedio = Label(frame_promedio, text="Nombre del alumno: ")
nombreAlumnoPromedio.grid(row=0, column=0, padx=10, pady=10)

cursoPromedio = Label(frame_promedio, text="Curso: ")
cursoPromedio.grid(row=1, column=0, padx=10, pady=10)

nota1 = Label(frame_promedio, text="Nota 1: ")
nota1.grid(row=2, column=0, padx=10, pady=10)

nota2 = Label(frame_promedio, text="Nota 2: ")
nota2.grid(row=3, column=0, padx=10, pady=10)

nota3 = Label(frame_promedio, text="Nota 3: ")
nota3.grid(row=4, column=0, padx=10, pady=10)

notaPromedio = Label(frame_promedio, text="Promedio: ")
notaPromedio.grid(row=6, column=0, padx=10, pady=10)

#---------------------- Textos Asistencias ----------------------

nombreAlumnoAsistencia= Label(frame_asistencia, text="Nombre del alumno: ")
nombreAlumnoAsistencia.grid(row=0, column=0, padx=10, pady=10)

cursoAsistencia= Label(frame_asistencia, text="Curso: ")
cursoAsistencia.grid(row=1, column=0, padx=10, pady=10)

diasDelCicloLectivo= Label(frame_asistencia, text="Dias del ciclo lectivo: ")
diasDelCicloLectivo.grid(row=2, column=0, padx=10, pady=10)

diasAlumnoAsistencia= Label(frame_asistencia, text="Dias asistidos: ")
diasAlumnoAsistencia.grid(row=3, column=0, padx=10, pady=10)

showPorcentajeAsistencia= Label(frame_asistencia, text="Porcentaje de asistencia: ")
showPorcentajeAsistencia.grid(row=5, column=0, padx=10, pady=10)

#--------------------- Boxes Promedio -----------------------

nombreAlumnoPromedioEntry = Entry(frame_promedio)
nombreAlumnoPromedioEntry.grid(row=0, column=1)

cursoEntryPromedio = Entry(frame_promedio)
cursoEntryPromedio.grid(row=1, column=1)

nota1Entry = Entry(frame_promedio)
nota1Entry.grid(row=2, column=1)

nota2Entry = Entry(frame_promedio)
nota2Entry.grid(row=3, column=1)

nota3Entry = Entry(frame_promedio)
nota3Entry.grid(row=4, column=1)

notaPromedioShow = Label(frame_promedio, text="")
notaPromedioShow.grid(row=6, column=1, padx=10, pady=10)

#--------------------- Boxes Promedio -----------------------

nombreAlumnoAsistenciaEntry = Entry(frame_asistencia)
nombreAlumnoAsistenciaEntry.grid(row=0, column=1)

cursoAlumnoAsistenciaEntry = Entry(frame_asistencia)
cursoAlumnoAsistenciaEntry.grid(row=1, column=1)

diasDelCicloLectivoEntry = Entry(frame_asistencia)
diasDelCicloLectivoEntry.grid(row=2, column=1)

diasAlumnoAsistenciaEntry = Entry(frame_asistencia)
diasAlumnoAsistenciaEntry.grid(row=3, column=1)

#-------------- Show porcentaje de asistencia ---------------------

AsistenciaPorcentajeShow = Label(frame_asistencia, text="")
AsistenciaPorcentajeShow.grid(row=5, column=1, padx=10, pady=10)

#-------------- Boton para calcular el promedio ---------------------


calculoPromedioBoton = Button(frame_promedio, text= "Calcular Promedio", command = recuperarDatosPromedio)
calculoPromedioBoton.grid(row = 5, column= 1)

#-------------- Boton para calcular el porcentaje de asistencias ---------------------


AsistenciaPorcentajeBoton = Button(frame_asistencia, text= "Calcular Porcentaje", command = recuperarDatosAsistencia)
AsistenciaPorcentajeBoton.grid(row = 4, column= 1)

#-------------------- Barra separadora vertical posicionada en la app --------------------

# ttk.Separator(
#     frame_barra_vertical_separadora,
#     orient=VERTICAL,
#     style="red.TSeparator"
# ).grid(row=0, column=2, ipady=200)



root.mainloop()