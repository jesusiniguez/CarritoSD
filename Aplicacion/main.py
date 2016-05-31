# -*- coding: utf-8 -*-
import algoritmos
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

#Menu inicial
print "PROGRAMA DE INICIO"
print "1. Carrito Básico"
print "2. Carrito para celíacos"
print "3. Carrito para diabéticos"
try:
    Choice=int(raw_input('Elija tipo de carro:'))
except ValueError:
    print "Escriba un número por favor"

try:
    Max=int(raw_input('Elija precio maximo del carro:'))
except ValueError:
    print "Escriba un número por favor"

#Creo un driver de Selenium con el navegador PhantomJS (Navegador oculto)
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)


Total = 0 #Esta variable almacenará el precio del carrito.

if Choice == 1:
	print "---   CARRITO DE COMPRA DE PRODUCTOS BASICO   ---"
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA arroz largo 1kg")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA lentejas pardina bolsa 1 Kg")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA menestra de verduras bolsa 1 kg")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA atun claro en aceite de oliva contenido bajo en sal pack 3 latas 156gr")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA aceite de oliva extra virgen botella 750 ml")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA leche semidesnatada envase 1 lt")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "LA RECETA huevos frescos categoria A clase M estuche 12 uds")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA garbanzo extra bolsa 1 KG")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "Dia azucar 1kg")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA yogur natural azucarado pack 12")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA agua natural 1.5l")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA barra pan")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA macarron paquete")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA refresco cola")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA zumo exprimido naranja envase 1 lt")

elif Choice == 2:
	print "---   CARRITO DE COMPRA DE PRODUCTOS PARA CELÍACOS   ---"
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA arroz largo 1kg")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA lentejas pardina bolsa 1 Kg")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA menestra de verduras bolsa 1 kg")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 2, driver, "DIA atun claro en aceite de oliva contenido bajo en sal pack 3 latas 156gr")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 2, driver, "DIA aceite de oliva extra virgen botella 750 ml")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 6, driver, "DIA leche semidesnatada envase 1 lt")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 2, driver, "LA RECETA huevos frescos categoria A clase M estuche 12 uds")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA garbanzo extra bolsa 1 KG")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "Dia azucar 1kg")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA yogur natural azucarado pack 12")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 3, driver, "DIA agua natural 1.5l")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 2, driver, "DR. SCHAR baguette SIN GLUTEN envase 350 gr")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "GALLO pluma SIN GLUTEN paquete 500 gr")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 6, driver, "DIA refresco cola")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, driver, "DIA zumo exprimido naranja envase 1 lt")

elif Choice == 3:
	print "---   CARRITO DE COMPRA DE PRODUCTOS PARA DIABÉTICOS   ---"
    	Total += lgoritmos.Imprimir_y_Anadir(Max, Total, 1, "DIA arroz integral paquete 1 Kg")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, "DIA lentejas pardina bolsa 1 Kg")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, "DIA menestra de verduras bolsa 1 kg")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 2, "DIA atun claro en aceite de oliva contenido bajo en sal pack 3 latas 156gr")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 2, "DIA aceite de oliva extra virgen botella 750 ml")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 6, "DIA leche semidesnatada envase 1 lt")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 2, "LA RECETA huevos frescos categoria A clase M estuche 12 uds")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, "DIA garbanzo extra bolsa 1 KG")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 12, "DAURA cerveza SIN GLUTEN botella 33 cl")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 2, "DIA postre soja chocolate pack 4 unidades 100 gr")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 3, "DIA agua natural 1.5l")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 2, "DR. SCHAR baguette SIN GLUTEN envase 350 gr")
	Total += algoritmos.Imprimir_y_Anadir(Max, Total, 1, "GALLO pluma SIN GLUTEN paquete 500 gr")
else:
    print('Error de inserción')

if Choice >=1 and Choice <= 3: 
	print 'PRECIO TOTAL DEL CARRITO DE COMPRA: ', Total, ' €'

driver.quit()
