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
Funcion auxiliar para convertir un string de "euros" obtenido de la web 
que devuelva un número flotante que corresponda al precio del string
"""
def Precio_a_Numero(Dato):
	Precio_Descompuesto=''
	whitelist = string.letters + string.digits
	for char in Dato:
		if(char in string.letters + string.digits):
			Precio_Descompuesto += char

	return float(Precio_Descompuesto)/100 #Divido entre 100 para que de el precio en euros, en vez de en centimos



"""
Funcion de búsqueda que utiliza selenium para 
acceder a la web concreta de un artículo dado un filtro
"""
def Busqueda(driver, filtro):
	driver.get("http://www.dia.es/compra-online/")
	driver.find_element_by_xpath("//input[@id='search']").send_keys(filtro)
	driver.find_element_by_xpath("//input[@type='image']").click()
	driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img") .click()
	return driver


"""
Funcion que, dado un filtro, busca la 
URL del artículo e imprime su precio y descripción, además de devolver el precio

El total lo incremento FUERA de esta función por la dificultad añadida de las variables por
referencia en python
"""
def Imprimir_y_Anadir(Max, Total, cantidad, driver, filtro):
	driver = Busqueda(driver, filtro)
	url = requests.get(driver.current_url)
	#Mediante requests obtengo la web html
	
	Contenido = html.fromstring(url.content)
	#Con LXML puedo convertir el html en un string plano para así localizar xpaths

	Descripcion = Contenido.xpath('//h1[@itemprop="name"]/text()')
	Precio = Contenido.xpath('//span[@itemprop="price"]/text()')
	if(Almacenable(Max, Total, Precio_a_Numero(Precio[0]))):
		print 'Producto: ', Descripcion[0].strip()
		print 'Precio: ', Precio[0]
		print 'Unidades: ', cantidad
		return Precio_a_Numero(Precio[0])*cantidad
	else:
		return 0;

def Almacenable(Max, Total, Precio):
	return Max >= Total+Precio