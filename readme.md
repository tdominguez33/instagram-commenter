# Comentador para instagram

Eu vos! Si, vos pibe. ¿Estás cansado de no ganar nunca en tu vida un sorteo de instagram? Yo también, por eso tengo la solución para la gente como nosotros que no tenemos suerte para estas cosas: **TRAMPA** Bueno *técnicamente* no es "Trampa" solo es un pequeño programa que comenta por vos cada un minuto los nombres de todos tus amigos para hacer 1400 comentarios por día (siempre que tengas tantos amigos para arrobar, no hago magia).  

Por eso no lo considero trampa, lo podría hacer uno mismo, requiere una cantidad considerable de esfuerzo pero alguien con muchas ganas <s> y amigos </s> lo puede hacer. Pero te voy a dejar la parte moral a vos, yo solo programo.

## *"¡Excelente! ¿Dónde firmo?"* - Vos en este instante (Probablemente)

Pará emoción, primero hay un par de cosas que necesitas saber antes de poder usar este programa:

1. El programa así como viene necesita que le configures tu usuario y contraseña (No Mabel, nadie te va a robar la contraseña, no sos tan importante. De todos modos, si seguís desconfiando, el programa es código abierto por una razón...)
2. Además de configurar el inicio de sesión, hay que agregarle las cuentas que vamos a arrobar: este programa no usa bots ni nada por el estilo, la idea es generar los comentarios más genuinos posibles (si empezas a arrobar cuentas árabes random, seguro los del sorteo se dan cuenta y ni te cuentan si ganas). 
3. El programa necesita que tengas el navegador **Chrome** o el **Firefox** (el del zorro) ya instalado.

## *"Bueno no pasa nada, me la re banco y configuro todo"*
¡Excelente! hace falta más gente como vos en este país.  
Todo esto puede ser configurado ni bien abrís el programa por primera vez en la consola (la opción recomendable si no sabes nada) o podes configurarlo en un archivo **JSON**.

## *"¿JSON? ¿Como el destripador?"*
No boludo, ese es Jack. Jason es el de la motosierra.  
Podemos pensar un archivo JSON como un diccionario en el que uno genera las palabras y le dice a la computadora qué significan, eso es todo lo que hace falta saber.  
Así debería verse el archivo JSON que tenemos que generar:

    {
      "navegador": 0,
      "link": "https://www.instagram.com/p/BuNGZMzn5BE/",
      "comentario": "",
      "arrobas": [
        "badbunnypr",
        "willyrex",
        "willsmith"
      ],
      "arrobasReutilizables": 0
    }

 - "link" es el link *(duh)* de la publicación a comentar.
 - En "arrobas" van los usuarios de las cuentas que vamos a etiquetar.
 - A las otras cosas no le des bola, las explico más adelante.
    
El archivo debería llamarse **datos.json** (así calcado, sin mayúsculas ni nada) y tiene que estar **EN LA MISMA CARPETA** que el programa principal.

## *"Bueno, entiendo, ¿pero cómo hago ese archivo?"*
La manera más fácil es abrir el archivo directamente y configurar tus datos en el programa, eso genera todo solo. Después si queres agregar usuarios para arrobar o cambiar de publicación, podés abrir el archivo JSON con cualquier editor de texto (bloc de notas por ejemplo) y cambiar los valores que quieras.

O podés simplemente copiar el ejemplo de arriba en [esta página](https://codebeautify.org/jsonviewer) y reemplazarlo con tus datos (la misma página te da opción para bajarlo ya con formato JSON y todo).

## *"¿Che pero qué es eso de arrobasReutilizables que hay en el JSON?"*
Sos muy observador, bien ahí.
Ese dato es el que hace al programa importante: el programa por defecto comenta a cada persona solamente **dos (2)** veces cada uno, esto es principalmente porque tengo ansiedad y no quiero molestar a mis conocidos con 40 notificaciones de que los arrobé en un sorteo de salame.  

"arrobasReutilizables" le marca al programa la cantidad de usuarios a los que podemos arrobar la mayor cantidad posible de veces (obvio cuantos más tengas, más cantidad de comentarios se van a poder formar).  
Por ejemplo, si tengo a 5 personas y el arrobasReutilizables en 5 el programa va a hacer combinaciones con esas 10 personas de la siguiente manera:  

    - @persona1 @persona2
    - @persona1 @persona3
    - @persona1 @persona4
    - @persona1 @persona5
    - @persona2 @persona1
    - @persona2 @persona3
    - @persona2 @persona4
    - ...

Y así hasta que se acaben, después de eso vuelve al modo de comentar a cada persona 2 veces.  
**MUY IMPORTANTE:** Si se considera la variable arrobasReutilizables los usuarios que va a utilizar son los que esten **PRIMEROS** en la lista, esto quiere decir que si en la lista tengo:

    {
          "navegador": 0,
          "link": "https://www.instagram.com/p/BuNGZMzn5BE/",
          "comentario": "",
          "arrobas": [
            "pepe",
            "fulano",
            "mengano",
            "marcelo",
            "jorge"
          ],
          "arrobasReutilizables": 3
    }
    
Solo se van a hacer repeticiones "completas" con "pepe", "fulano" y "mengano", y a los otros dos los va a comentar dos veces nomás.

**MUY IMPORTANTE PARTE 2:** Esta variable solo se puede cambiar editando el JSON, así que sentite especial, es medio un secreto de estado esto.

## *"¿Y como me logueo en Instagram"*
Tranquilo fiera, ya tenemos todo solucionado, una vez que completes todos los datos, se va a abrir un navegador con la página del login de Instagram, te logueas ahí, volves a la consola, apretás enter y ya quedan guardados todos tus datos para poder loguarte automáticamente cada vez que abras el programa.

## *"Che ya me estas cansando ¿algo más?"*
Nop, con eso ya tenés todo lo que hace falta para usar el programa, solo te queda esperar a que el programa comente, tranqui, una vez que abrís el programa podés dejarlo minimizado y hace las cosas solo, cuando termina se cierra solo.

## *NUEVO!!* Modo comentario simple
Ahora si llegas a encontrar un sorteo que pide que simplemente comentes un texto, como un hashtag por ejemplo, podes usar el programa para hacerlo!!

Ya está todo integrado en la configuración inicial del programa asi que la manera facil es volver a generar el archivo JSON (si ya tenés uno armado te recomiendo simplemente borrarlo y correr el programa).

Si sos medio hacker y te queres hacer el picante podes añadir el texto que querés que se comente en el archivo JSON directamente como en este ejemplo:

    {
      "navegador": 0,
      "link": "https://www.instagram.com/p/BuNGZMzn5BE/",
      "comentario": "#HashtagParaGanar",
      "arrobas": [],
      "arrobasReutilizables": 0
    }

Es mucho muy importante que sepas que si vas a usar el modo de comentario simple, mientras la sección de "comentario" tenga algo, el programa va a ignorar los arrobas y solo va a comentar el texto, es su forma de diferenciar que modo se quiere usar.