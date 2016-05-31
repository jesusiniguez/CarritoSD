# Proyecto CarritoSD Supermercado DIA

## Autores.
 * **Juan Sevillano Hernández.**
 * **David Moreno Del Valle.**
 * **Jesús Íñiguez García.**
 * **Miguel Ángel Fernández Montilla.**

## Introducción
Hemos creado una aplicación desarrollada en Python con el fin de facilitar las compras de forma online en la página web del Supermercado [DIA](http://www.dia.es/compra-online/ "Página web del DIA"). Estos productos que hemos buscado representan a los productos de primera necesidad a la hora de realizar un buen carrito de compra, nos hemos basado según las indicaciones de la siguiente imagen. ![IMAGEN](http://cdn01.ib.infobae.com/adjuntos/162/infografia/010/533/0010533787.jpg?0000-00-00-00-00-00 "Listado de Productos")

Las aplicación a sido desarrollada en Python utilizandos las herramientas:
 * **XPATH a partir de Firebug.**  
 ![IMAGEN](http://securityidiots.com/post_images/xpath_logo.png "xpaht")
 * **Selenium para obtener las url de las búsquedas.**  
 ![IMAGEN](http://www.seleniumhq.org/images/big-logo.png "selenium")
 * **PhatomJS para no abrir un navegador con Selenium.**  
 ![IMAGEN](http://phantomjs.org/img/phantomjs-logo.png "phantomjs")
 * **Requests para obtener el HTML de la URL.**  
 ![IMAGEN](http://docs.python-requests.org/en/master/_static/requests-sidebar.png "requests")
 * **LXML para transformar a String un HTML.**  
 ![IMAGEN](http://lxml.de/s5/tagpython.png "LXML")

## Explicación del Desarrollo de la Aplicación.
 1. La aplicación establecerá una conexión a la pagina web del Supermercado [DIA](http://www.dia.es/compra-online/ "Página web del DIA").
 2. El cliente elige el tipo de carrito de compra que quiere realizar, según quiera productos para celiacos, diabéticos o productos normales.
 3. El cliente introduce el precio máximo del Carrito de Compra que vamos a generar.
 4. La aplicación generará el Carrito de Compra en función de las opciones elegidas anteriormente.
 5. La aplicación mostrará la Descripción del producto añadido al Carrito de Compra.
 6. La aplicación mostrará el Precio del producto añadido al Carrito de Compra.
 7. La aplicación repite los puntos 5 y 6 mientras que el Total del Carrito de Compra sea inferior al valor introducido en el punto 3.
 8. La aplicación mostrará el Total del Carrito de Compra.

## Histórico de Cambios.
La idea inicial consistía en una aplicación para rastrear varios Supermercados y compare productos, mostrando que Supermercado vende el producto más barato y cual es su precio. Debido a que la mayoría de los Supermercados tienen las páginas web con un Protocolo seguro de transferencia de hipertexto (HTTPS), nos dimos cuenta que no podíamos realizar busquedas de productos, ante esto nos decidimos a realizar la aplicación que solamente trabaje con el Supermercado DIA ya que dicha página web no emplea el Protocolo seguro de transferencia de hipertexto (HTTPS).

Una vez realizado este cambio, hemos decidido cambiar el tipo de busqueda de productos, ya que al principio íbamos a buscar y comparar productos para ver en que supermercado eran más baratos, y ahora ya que solo utilizamos un Supermercado realizamos búsquedas de Carritos con productos para celíacos, para diabéticos y productos normales.

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
