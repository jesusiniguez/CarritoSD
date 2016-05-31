# -*- coding: utf-8 -*-
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import requests


""" 
Usamos: 
	xpath a partir de Firebug
	Selenium para obtener las url de las busquedas
	PhantomJS para no abrir un navegador con selenium
	Requests para obtener el HTML de la url
	LXML para transformar a string un HTML
"""


#Creamos el driver Phantom para que nos consiga la URL del objeto
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)

print "---   CARRITO DE COMPRA DE PRODUCTOS BASICO   ---"

#Accedo a la URL del día
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("DIA arroz largo 1kg")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio1 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio1[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_5873']").click()
driver.find_element_by_xpath("//input[@value='Aceptar']").click()


#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("DIA lentejas pardina bolsa 1 Kg")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio2 = Contenido.xpath('//span[@itemprop="price"]/text()')
print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio2[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_158']").click()

#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("DIA menestra de verduras bolsa 1 kg")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio3 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio3[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_1389']").click()

#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("DIA atun claro en aceite de oliva contenido bajo en sal pack 3 latas 156gr")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio4 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio4[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_50172']").click()


#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("DIA aceite de oliva extra virgen botella 750 ml")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio5 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio5[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_12360']").click()


#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("DIA leche semidesnatada envase 1 lt")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio6 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio6[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_504']").click()


#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("LA RECETA huevos frescos categoria A clase M estuche 12 uds")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio7 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio7[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_14636']").click()


#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("DIA garbanzo extra bolsa 1 KG")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio8 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio8[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_155']").click()


#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("Dia azucar 1kg")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio9 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio9[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_81798']").click()


#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("DIA yogur natural azucarado pack 12")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio10 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio10[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_127145']").click()


#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("DIA agua natural 1.5l")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio11 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio11[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_26995']").click()


#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("DIA barra pan")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio12 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio12[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_38109']").click()


#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("DIA macarron paquete")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio13 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio13[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_50973']").click()


#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("DIA refresco cola")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio14 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio14[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_203767']").click()


#Producto Nuevo
driver.get("http://www.dia.es/compra-online/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("DIA zumo exprimido naranja envase 1 lt")
driver.find_element_by_xpath("//input[@type='image']").click()
driver.find_element_by_xpath(u"//div[@id='content']/div[3]/div/div[2]/div[5]/div/div/a/span/img").click()

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)

Descripcion=Contenido.xpath('//h1[@itemprop="name"]/text()')
Precio15 = Contenido.xpath('//span[@itemprop="price"]/text()')

print 'Producto: ', Descripcion[0].strip()
print 'Precio: ', Precio15[0]
print " "

driver.find_element_by_xpath("//button[@id='addQuantityByProduct_50690']").click()


#CARRITO DE COMPRA ACCESO
driver.get("http://www.dia.es/compra-online/cart")

url = requests.get(driver.current_url)
Contenido = html.fromstring(url.content)
Total = Contenido.xpath('//dd[@itemprop="subtotalPrice"]/text()')

print 'PRECIO TOTAL DEL CARRITO DE COMPRA: ', Total

driver.quit()

"""------------------------------------------------------------------------------------------"""
