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
print "Carro 1 2 3 "
try:
    Choice=int(raw_input('Elija tipo de carro:'))
except ValueError:
    print "Escriba un número por favor"

#Creo un driver de Selenium con el navegador PhantomJS (Navegador oculto)
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)


Total = 0 #Esta variable almacenará el precio del carrito.

if Choice == 1:
	print "---   CARRITO DE COMPRA DE PRODUCTOS BASICO   ---"
	Total += algoritmos.Imprimir_y_Anadir(driver, "DIA arroz largo 1kg")
	Total += algoritmos.Imprimir_y_Anadir(driver, "DIA lentejas pardina bolsa 1 Kg")
	Total += algoritmos.Imprimir_y_Anadir(driver, "DIA menestra de verduras bolsa 1 kg")
	Total += algoritmos.Imprimir_y_Anadir(driver, "DIA atun claro en aceite de oliva contenido bajo en sal pack 3 latas 156gr")
	Total += algoritmos.Imprimir_y_Anadir(driver, "DIA aceite de oliva extra virgen botella 750 ml")
	Total += algoritmos.Imprimir_y_Anadir(driver, "DIA leche semidesnatada envase 1 lt")
	Total += algoritmos.Imprimir_y_Anadir(driver, "LA RECETA huevos frescos categoria A clase M estuche 12 uds")
	Total += algoritmos.Imprimir_y_Anadir(driver, "DIA garbanzo extra bolsa 1 KG")
	Total += algoritmos.Imprimir_y_Anadir(driver, "Dia azucar 1kg")
	Total += algoritmos.Imprimir_y_Anadir(driver, "DIA yogur natural azucarado pack 12")
	Total += algoritmos.Imprimir_y_Anadir(driver, "DIA agua natural 1.5l")
	Total += algoritmos.Imprimir_y_Anadir(driver, "DIA barra pan")
	Total += algoritmos.Imprimir_y_Anadir(driver, "DIA macarron paquete")
	Total += algoritmos.Imprimir_y_Anadir(driver, "DIA refresco cola")
	Total += algoritmos.Imprimir_y_Anadir(driver, "DIA zumo exprimido naranja envase 1 lt")
elif Choice == 2:
    print('Zero')
elif Choice == 3:
    print('Single')
else:
    print('Error de inserción')

if Choice >=1 && Choice <= 3: 
	print 'PRECIO TOTAL DEL CARRITO DE COMPRA: ', Total, ' €'

driver.quit()