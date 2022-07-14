# Comentador para instagram

Eu vos! Si, vos pibe. ¿Estas cansado de no ganar nunca en tu vida un sorteo de instagram? Yo también, por eso tengo la solución para la gente como nosotros que no tenemos suerte para estas cosas: **TRAMPA** Bueno *técnicamente* no es "Trampa" solo es un pequeño programa que comenta por vos cada un minuto los nombres de todos tus amigos para hacer 1400 comentarios por dia (Siempre que tengas tantos amigos para arrobar, no hago magia).  

Por eso no lo considero trampa, lo podria hacer uno mismo, requiere una cantidad considerable de esfuerzo pero alguien con muchas ganas <s> y amigos </s> lo puede hacer. Pero te voy a dejar la parte moral a vos, yo solo programo.

## *"Excelente! ¿Donde Firmo?"* - Vos en este instante (Probablemente)

Pará emoción, primero hay un par de cosas que necesitas saber antes de poder usar este programa. :

1. El programa así como viene necesita que le configures tu usuario y contraseña (No Mabel, nadie te va a robar la contraseña, no sos tan importante. De todos modos si seguis desconfiando el programa es código abierto por una razón...)
2. Además de configurar el inicio de sesión hay que agregarle las cuentas que vamos a arrobar, este programa no usa bots ni nada por el estilo, la idea es generar los comentarios mas genuinos posibles, además si empezas a arrobar cuentas árabes random seguro los del sorteo se dan cuenta y ni te cuentan si ganas.
3. El programa necesita que tengas el navegador **Firefox** (El del zorro) instalado y descomprimas y copies [este archivo](https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-win64.zip) (si tenes Windows de 64 bits), o [este](https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-win32.zip) (si tenes de 32 bits), en la carpeta de instalación del Firefox.

## *"Bueno no pasa nada, me la re banco y configuro todo"*
¡Excelente! hace falta más gente como vos en este país.  
Todo esto puede ser configurado por primera vez ni bien abris el programa por primera vez en la consola (La opcón recomendable si no sabes nada) o podes configurarlo en un archivo **JSON**.

## *"¿JSON? ¿Como el destripador?"*
No boludo ese es Jack, Jason es el de la motosierra.  
Podemos pensar un archivo JSON como un diccionario en el que uno genera las palabras y le dice a la computadora que significan, eso es todo lo que hace falta saber.  
Así deberia verse el archivo JSON que tenemos que generar:

    {
      "user": "therock",
      "password": "password123",
      "link": "https://www.instagram.com/p/BuNGZMzn5BE/",
      "arrobas": [
        "badbunnypr",
        "willyrex",
        "willsmith"
      ],
      "arrobasReutilizables": 0
    }

 - "user" es tu usuario de Instagram.  
 - "password" es tu contraseña.
 - "link" es el link *(duh)* de la publicación a comentar.
    
El archivo deberia llamarse **datos.json** (Así calcado, sin mayusculas ni nada) y tiene que estar **EN LA MISMA CARPETA** que el programa principal.

## *"Bueno, entiendo, ¿pero como hago ese archivo?"*
La manera más facil es abrir el archivo directamente y configurar tus datos en el programa, eso genera todo solo. Después si queres agregar usuarios para arrobar o cambiar de publicación podes abrir el archivo JSON con cualquier editor de texto (bloc de notas por ejemplo) y cambiar los valores que quieras.

O podes simplemente copiar el ejemplo de arriba en [esta página](https://codebeautify.org/jsonviewer) y reemplazarlo con tus datos, la misma página te da opción para bajarlo ya con formato JSON y todo.

## *"¿Che pero que es eso de arrobasReutilizables que hay en el JSON?"*
Sos muy observador, bien ahí.
Ese dato es el que hace al programa importante, el programa por defecto comenta a cada persona solamente **dos (2)** veces cada uno, esto es principalmente porque tengo ansiedad y no quiero molestar a mis conocidos con 40 notificaciones de que los arrobe en un sorteo de salame.  

"arrobasReutilizables" le marca al programa la cantidad de usuarios a los que podemos arrobar la mayor cantidad posible de veces (Obvio cuantos más tengas más cantidad de comentarios se van a poder formar).  
Por ejemplo si tengo a 5 personas y el arrobasReutilizables en 5 el programa va a hacer combinaciones con esas 10 personas de la siguiente manera:  

    - @persona1 @persona2
    - @persona1 @persona3
    - @persona1 @persona4
    - @persona1 @persona5
    - @persona2 @persona1
    - @persona2 @persona3
    - @persona2 @persona4
    - ...

Y así hasta que se acaben, despues de eso vuelve al modo de comentar a cada persona 2 veces.
**MUY IMPORTANTE:** Si se considera la variable arrobasReutilizables los usuarios que va a utilizar son los que esten **PRIMEROS** en la lista, esto quiere decir que si en la lista tengo:

    {
          "user": "therock",
          "password": "password123",
          "link": "https://www.instagram.com/p/BuNGZMzn5BE/",
          "arrobas": [
            "pepe",
            "fulano",
            "mengano",
            "marcelo",
            "jorge"
          ],
          "arrobasReutilizables": 3
    }
    
Solo se van a hacer repeticiones "completas" con "pepe", "fulano" y "mengano" y a los otros dos los va a comentar dos veces nomás.

**MUY IMPORTANTE PARTE 2:** Esta variable solo se puede cambiar editando el JSON, así que sentite especial, es medio un secreto de estado esto.

## *"Che ya me estas cansando ¿algo más?"*
Nop, con eso ya tenes todo lo que hace falta para usar el programa, solo te queda esperar a que el programa comente, tranqui, una vez que abris el programa podes dejarlo minimizado y hace las cosas solo, cuando termina se cierra solo.