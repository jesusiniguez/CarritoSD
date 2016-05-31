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