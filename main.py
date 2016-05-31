# -*- coding: utf-8 -*-
import algoritmos

print "PROGRAMA DE INICIO"
print "Carro 1 2 3 "
try:
    Choice=int(raw_input('Elija tipo de carro:'))
except ValueError:
    print "Escriba un número por favor"


driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
Total = 0

print "---   CARRITO DE COMPRA DE PRODUCTOS BASICO   ---"

if Choice == 1:
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
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')



#Accedo a la URL del día


print 'PRECIO TOTAL DEL CARRITO DE COMPRA: ', Total, ' €'

driver.quit()