# url_shortener by Fernando Sanchez Quiros


URL SHORTENER

Visión general

Desarrollar una página web, que haga la función de acortar una url, de forma que el usuario obtenga una url nueva de menor tamaño, más legible,  y cuyo link es de la misma validez que el inicial.
Objetivos

  1.Acortar url: A través de peticiones web el usuario obtenga una url más corta y sencilla .
  2.Url: La url tiene que tener la característica de poder tener fecha de caducidad, el usuario también puede tener su url sin fecha de caducidad de forma que perdure en la base de datos (sqlite) de forma permanente. 
  3.Interfaz gráfica: La página web contará con interfaz gráfica de forma que se pueda poner de carácter público y así obtener una fuente de ingresos(publicidad, banners,etc).
  4.Ranking: La página web tendrá un ranking que muestre los links más solicitados de ser acortados y sin fecha de caducidad.
  5.Test: Habrá una cobertura del 100% de test sobre el código desarrollado 
  6.Documentación: Se deberá aportar toda la documentación de todo el proyecto desarrollado para que otro equipo pueda mantener o  aumentar su funcionalidad.
Especificaciones
  1.Características.

    Api web.
    Interfaz gráfica.
    Link con caducidad a demanda del usuario
    Cobertura de test del 100%
    Ranking de urls más exitosos

  2.Descripción de la api.
    Un servicio acortador de URL que toma cualquier URL y genera una versión más corta y legible. Se realizará a través de las siguientes rutas con su descripción:
    /new -> method POST, a través del cual hago una petición a la base de datos que me devuelva la URL acortada y sino existe que genere una y nos la proporcione.
    {
    “code”: “/codigo”
    }
    /ranking->method GET, se hace una solicitud a la base de datos de que nos de las 5 urls co mayor número de clicks.
    devuelve:
    [
    {
    “url”:” www.x.com”
    “url_new”: “/codigo”
    “clicks”:”x”
    }
    ]
    /clicks/{código}->method GET, se hace una solicitud a la base de datos de que nos dé el número de veces que la url inicial ha sido acortada.
    {
    “url”:” www.x.com”
    “clicks”:”x”
    }
    /{codigo}->GET, Redirected a la página inicial aportada por el usuario.






  3.Descripción arquitectónica.
    El proyecto se va a desarrollar con Django 3.6, cuyo esquema de archivos es el siguiente:
    Archivos del proyecto
    __init__.py: Este es un archivo vacío que le dice a Python que debe considerar este directorio como un paquete de Python.
    manage.py: Este archivo contiene una porción de código que permite interactuar con el proyecto de Django de muchas formas. 
    settings.py: Este archivo contiene todas las configuraciones para el proyecto.
    urls.py: Contiene las rutas que están disponibles en el proyecto.
    Archivos de la aplicación
    __init__.py: Este es un archivo vacío que le dice a Python que debe considerar este directorio como un paquete de Python..
    models.py: En este archivo se declara la base de datos.
    views.py: En este archivo se declaran las funciones de la vista.
    test.py: En este archivo se declaran las pruebas necesarias para la aplicación
    módulo code generator: Generador de code unico
    modulo db.py: Archivo en el cual se almacena la base de datos





  4.Descripción del flujo de trabajo con Git .
    Se va a desarrollar el trabajo con una rama Master, y luego diversas ramas(branch) de trabajo descritas a continuación:
    Branch para cada una de las funciones que se requieran para las peticiones web con sus diferentes características.
    Branch de trabajo diferente para la base de datos.
    Branch la interfaz gráfica.


