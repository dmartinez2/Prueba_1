import webbrowser as web
import sys
import pyautogui
from time import sleep
import os
import colorama
from colorama import Fore
colorama.init()
print('Di que día se celebra la compe (Número y Mes): '+Fore.LIGHTMAGENTA_EX)
print('')
dia_compe = (input('   '))
print(Fore.RESET)
print('Di la fecha límite para inscribir a los deportistas (Número y Mes): '+Fore.LIGHTMAGENTA_EX)
print('')
dia_tope = (input('   '))
print(Fore.RESET)
os.system("cls")
print('La compe se celebrará el día: '+Fore.LIGHTMAGENTA_EX+ f' {dia_compe}'+Fore.RESET+'.')
print(' ')
print('Y la fecha límite para inscribir es: '+Fore.LIGHTMAGENTA_EX+ f' {dia_tope}'+Fore.RESET+'.')
print(' ')
print('Si es correcto, escribe "si" en minúsculas: '+Fore.LIGHTMAGENTA_EX)
print('')
segur = (input('   '))
print(Fore.RESET)
if segur != 'si':
    exit()
os.system("cls")
file = open("F:/PROYECTOS/Zalcu/Bot_Whatsapp/contactos2.txt", "r")
file.read()
file.closed
file.close()
file.closed
prueba = open("F:/PROYECTOS/Zalcu/Bot_Whatsapp/pruebas.txt", "r")
prueba.read()
prueba.closed
prueba.close()
prueba.closed
print('Mira si la lista de los nombres y números: '+Fore.LIGHTMAGENTA_EX+ '"contactos2.txt"' +'\033[39m'+' está actualizada.')
print(' ')
print('Si es correcto, escribe "si" en minúsculas: '+Fore.LIGHTMAGENTA_EX)
print('')
segur2 = (input('   '))
print(Fore.RESET)
if segur2 != 'si':
    exit()
os.system("cls")
print('Mira si la lista de las pruebas: '+Fore.LIGHTMAGENTA_EX+ '"pruebas.txt"' +'\033[39m'+' está actualizada.')
print(' ')
print('Si es correcto, escribe "si" en minúsculas: '+Fore.LIGHTMAGENTA_EX)
print('')
segur3 = (input('   '))
print(Fore.RESET)
if segur3 != 'si':
    exit()
print(Fore.RESET)
os.system("cls")
x=0
row = []
crimefile = open("F:/PROYECTOS/Zalcu/Bot_Whatsapp/contactos2.txt", 'r')
for linea in crimefile.readlines():
    row.append([linea])
    for i in linea.split(","):
        row[-1].append(i)
resto = len(row)
int(resto)
resto2 = resto * 7
with open("F:/PROYECTOS/Zalcu/Bot_Whatsapp/contactos2.txt", "r") as file:
    for datas in file:
        os.system('cls')
        print('Quedan: '+Fore.MAGENTA+f'{resto} contactos'+Fore.RESET)
        resto = resto -1
        datos=datas.split()
        nombre = datos[0]
        telefo = datos[1]         
        with open("F:/PROYECTOS/Zalcu/Bot_Whatsapp/pruebas.txt", "r") as prueba:
            for prubs in prueba:
                texto = [
                    (f'Hola {nombre}, necesito que me digas que pruebas vas a querer hacer el proximo dia {dia_compe}.'),
                    (prubs),
                    (f'Tienes de plazo hasta el dia {dia_tope} para enviarme las pruebas de la compe.')
                ]       
        web.open("https://web.whatsapp.com/send?phone=+34"+telefo)
        print(Fore.CYAN + 'Procesando.'+ Fore.MAGENTA +f'   {resto2}s'+Fore.RESET)
        resto2 = resto2-1
        sleep(1)
        print(Fore.CYAN + 'Procesando..'+ Fore.MAGENTA +f'  {resto2}s'+Fore.RESET)
        resto2 = resto2-1
        sleep(1)
        print(Fore.CYAN + 'Procesando...'+ Fore.MAGENTA +f' {resto2}s'+Fore.RESET)
        resto2 = resto2-1
        sleep(1)
        print(Fore.CYAN + 'Procesando....'+ Fore.MAGENTA +f'{resto2}s'+Fore.RESET)
        resto2 = resto2-1
        sleep(1)
        print(Fore.YELLOW + 'Cargando. '+ Fore.MAGENTA +f'    {resto2}s'+Fore.RESET)
        resto2 = resto2-1
        sleep(1)
        print(Fore.YELLOW + 'Cargando.. '+ Fore.MAGENTA +f'   {resto2}s'+Fore.RESET)
        resto2 = resto2-1
        sleep(1)
        print(Fore.YELLOW + 'Cargando... '+ Fore.MAGENTA +f'  {resto2}s'+Fore.RESET)
        resto2 = resto2-1     
        vueltas = 4
        for line in texto:
            sleep(0.25)
            vueltas = vueltas-1
            print(Fore.MAGENTA+f'Nº de mensajes restantes: {vueltas}'+Fore.RESET)
            pyautogui.typewrite(line)           
            pyautogui.press("enter")
file.close()
print(' ')
print(Fore.GREEN+'Listo')
sleep(2)