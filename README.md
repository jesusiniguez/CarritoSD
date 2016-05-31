# Proyecto CarritoSD Supermercado DIA

## Autores.
 * **Juan Sevillano Hernández.**
 * **David Moreno Del Valle.**
 * **Jesús Íñiguez García.**
 * **Miguel Ángel Fernández Montilla.**

## Introducción
Hemos creado una aplicación desarrollada en Python con el fin de facilitar las compras de forma online en la página web del supermercado [DIA](http://www.dia.es/compra-online/ "Página web del DIA"). Estos productos que hemos buscado representan a los productos de primera necesidad a la hora de realizar un buen carrito de compra, nos hemos basado segun las indicaciones de la siguiente imagén. ![IMAGEN](http://cdn01.ib.infobae.com/adjuntos/162/infografia/010/533/0010533787.jpg?0000-00-00-00-00-00 "Listado de Productos")

Las aplicación a sido desarrollada en Python utilizandos las herramientas:
 * **XPATH a partir de Firebug.**  
 ![IMAGEN](http://securityidiots.com/post_images/xpath_logo.png "xpaht")
 * **Selenium para obtener las url de las busquedas.**  
 ![IMAGEN](http://www.seleniumhq.org/images/big-logo.png "selenium")
 * **PhatomJS para no abrir un navegador con Selenium.**  
 ![IMAGEN](http://phantomjs.org/img/phantomjs-logo.png "phantomjs")
 * **Requests para obtener el HTML de la URL.**  
 ![IMAGEN](http://docs.python-requests.org/en/master/_static/requests-sidebar.png "requests")
 * **LXML para transformar a String un HTML.**  
 ![IMAGEN](http://lxml.de/s5/tagpython.png "LXML")

## Explicación del Desarrollo de la Aplicación.
 1. La aplicación establecerá una conexión a la pagina web del supermercado [DIA](http://www.dia.es/compra-online/ "Página web del DIA").
 2. El cliente elige el tipo de carrito de compra que quiere realizar, según quiera productos para celiacos, diabéticos o productos normales.
 3. El cliente introduce el precio máximo del Carrito de Compra que vamos a generar.
 4. La aplicación generará el Carrito de Compra en funcion de las opciones elegidas anteriormente.
 5. La aplicación mostrará la Descripción del producto añadido al Carrito de Compra.
 6. La aplicación mostrará el Precio del producto añadido al Carrito de Compra.
 7. La aplicación repite el paso 5 y 6 mientras que el Total del Carrito de Compra sea inferior al valor introducido en el punto 3.
 8. La aplicación mostrará el Total del Carrito de Compra.

## Planificación y Reparto de Tareas.
**Idea Inicial:**
 * David Moreno Del Valle.
 * Jesús Íñiguez García.
 * Miguel Ángel Fernández Montilla.

**Desarrollo de la Aplicación:**
* Juan Sevillano Hernández.
* Jesús Íñiguez García.

**Redacción de la Documentación:**
* Juan Sevillano Hernández.
* David Moreno Del Valle.
* Jesús Íñiguez García.
* Miguel Ángel Fernández Montilla.

#### Encabezado h4
##### Encabezado h5
###### Encabezado h6

> Cita de texto

*cursiva* 

**negrita**

 `Código`
 
  ```
 Código en 
 varias líneas
 ```

 * Un elemento en una lista no ordenada
 * Otro elemento en una lista

 1. Elemento en una lista enumerada u ordenada.
 2. Otro elemento


 [ENLACE](http://www.dia.es/compra-online/ "http://www.dia.es/compra-online/")

![IMAGEN](http://securityidiots.com/post_images/xpath_logo.png "Título de la imagen")
