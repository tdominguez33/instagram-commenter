from os.path import exists
import json

def start():
    if not exists("datos.json"):

        salir = False
        arrobas = []

        repetir = True

        datos = {
            "user": "user",
            "password": "password",
            "link": "link",
            "comentario": "comentario",
            "arrobas": [],
            "arrobasReutilizables": 0
        }

        while repetir == True:
            USER = input("Ingresar Usuario: ")
            rta = input("'" + USER + "' este es tu usuario ingresado, ¿Es correcto? S/N: ")
            if rta == 'S':
                repetir = False

        repetir = True

        while repetir == True:
            PASSWORD = input("Ingresar Contraseña: ")
            rta = input("'" + PASSWORD + "' este es tu contraseña ingresada, ¿Es correcta? S/N: ")
            if rta == 'S':
                repetir = False

        repetir = True

        while repetir == True:
            LINK = input("Ingresar link de la publicación a comentar: ")
            rta = input("'" + LINK + "' este es la página ingresada, ¿Es correcta? S/N: ")
            if rta == 'S':
                repetir = False
        
        repetir = True

        while repetir == True:
            rta = input("Seleccione el tipo de comentario a hacer: Comentario Simple [1] / Comentario con usuarios [2]: ")
            if rta == '1':
                COMENTARIO = input("Ingresar texto del comentario: ")
                repetir = False
            
            elif rta == '2':
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
                if rta == 'N':
                    exit()
                repetir = False


        datos["user"] = USER
        datos["password"] = PASSWORD
        datos["link"] = LINK
        datos["comentario"] = COMENTARIO
        datos["arrobas"] = arrobas

        datos_json = json.dumps(datos, indent = 4)

        with open("datos.json", "w") as archivo:
            archivo.write(datos_json)