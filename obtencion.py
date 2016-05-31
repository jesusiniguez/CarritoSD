# -*- coding: utf-8 -*-
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import requests
import string

""" 
Usamos: 
	xpath a partir de Firebug
	Selenium para obtener las url de las busquedas
	PhantomJS para no abrir un navegador con selenium
	Requests para obtener el HTML de la url
	LXML para transformar a string un HTML
	string para limpiar los textos de €
"""


#Funcion auxiliar para convertir un string de "euros" obtenido de la web 
#que devuelva un número flotante que corresponda al precio del string
def Precio_a_Numero(Dato):
	Precio_Descompuesto=''
	whitelist = string.letters + string.digits
	for char in Dato:
		if(char in string.letters + string.digits):
			Precio_Descompuesto += char

	return float(Precio_Descompuesto)/100


def Busqueda(driver, filtro):
	driver.get("http://www.dia.es/compra-online/")
	driver.find_element_by_xpath("//input[@id='search']").send_keys(filtro)
	driver.find_element_by_xpath("//input[@type='image']").click()
	driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img") .click()

def Imprimir_y_Anadir(driver, filtro):
	Busqueda(driver, filtro)
	url = requests.get(driver.current_url)
	Contenido = html.fromstring(url.content)

	Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
	Precio = Contenido.xpath('//span[@itemprop="price"]/text()')

	print 'Producto: ', Descripcion[0].strip()
	print 'Precio: ', Precio[0]
	print " "
	return Precio_a_Numero(Precio[0])

#Creamos el driver Phantom para que nos consiga la URL del objeto
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
Total = 0

print "---   CARRITO DE COMPRA DE PRODUCTOS BASICO   ---"

#Accedo a la URL del día
Total += Imprimir_y_Anadir(driver, "DIA arroz largo 1kg")
Total += Imprimir_y_Anadir(driver, "DIA lentejas pardina bolsa 1 Kg")
Total += Imprimir_y_Anadir(driver, "DIA menestra de verduras bolsa 1 kg")
Total += Imprimir_y_Anadir(driver, "DIA atun claro en aceite de oliva contenido bajo en sal pack 3 latas 156gr")
Total += Imprimir_y_Anadir(driver, "DIA aceite de oliva extra virgen botella 750 ml")
Total += Imprimir_y_Anadir(driver, "DIA leche semidesnatada envase 1 lt")
Total += Imprimir_y_Anadir(driver, "LA RECETA huevos frescos categoria A clase M estuche 12 uds")
Total += Imprimir_y_Anadir(driver, "DIA garbanzo extra bolsa 1 KG")
Total += Imprimir_y_Anadir(driver, "Dia azucar 1kg")
Total += Imprimir_y_Anadir(driver, "DIA yogur natural azucarado pack 12")
Total += Imprimir_y_Anadir(driver, "DIA agua natural 1.5l")
Total += Imprimir_y_Anadir(driver, "DIA barra pan")
Total += Imprimir_y_Anadir(driver, "DIA macarron paquete")
Total += Imprimir_y_Anadir(driver, "DIA refresco cola")
Total += Imprimir_y_Anadir(driver, "DIA zumo exprimido naranja envase 1 lt")

print 'PRECIO TOTAL DEL CARRITO DE COMPRA: ', Total, ' €'

driver.quit()

"""------------------------------------------------------------------------------------------"""