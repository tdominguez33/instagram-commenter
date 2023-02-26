from os.path import exists
from scripts.cls import cls
import json

def start():
    if not exists("datos.json"):

        salir = False
        arrobas = []

        repetir = True

        datos = {
            "navegador": 0,
            "link": "link",
            "comentario": "comentario",
            "arrobas": [],
            "arrobasReutilizables": 0
        }

        while repetir == True:
            rta = input("Que navegador quieres usar (Tiene que estar instalado) Firefox [0] / Chrome [1] ")
            if rta == '0':
                NAVEGADOR = 0
                repetir = False
            elif rta == '1':
                NAVEGADOR = 1
                repetir = False
            else:
                print("Ingrese un valor válido")

        while repetir == True:
            cls()
            LINK = input("Ingresar link de la publicación a comentar: ")
            rta = input("'" + LINK + "' este es la página ingresada, ¿Es correcta? S/N: ")
            if rta == 'S' or 's':
                repetir = False
        
        repetir = True

        while repetir == True:
            cls()
            rta = input("Seleccione el tipo de comentario a hacer: Comentario Simple [1] / Comentario con usuarios [2]: ")
            if rta == '1':
                cls()
                COMENTARIO = input("Ingresar texto del comentario: ")
                repetir = False
            
            elif rta == '2':
                cls()
                COMENTARIO = ""
                print("Ahora hay que ingresar los usuarios de las cuentas que vamos a etiquetar SIN EL @")
                print("Para salir ingresar 0")
                while salir == False:
                    usuario = input("Ingresar Usuario: ")
                    if usuario == "0":
                        salir = True
                    else:
                        arrobas.append(usuario)

                for i in arrobas:
                    print(i)

                rta = input("Esta es la lista ¿estás seguro? S/N: ")
                if rta == 'N' or 'n':
                    exit()
                repetir = False

        datos["navegador"] = NAVEGADOR
        datos["link"] = LINK
        datos["comentario"] = COMENTARIO
        datos["arrobas"] = arrobas

        datos_json = json.dumps(datos, indent = 4)

        with open("datos.json", "w") as archivo:
            archivo.write(datos_json)