# -*- coding: UTF-8 -*-


#==============> ↓↓↓
#==============> LIBS ↓↓↓

import os
import json
import requests

from time import sleep

#==> LIBS/SE DER ERRO↓↓↓

try:
	import pyfiglet
except:
	os.system('pip install pyfiglet')

#==============> CORES ↓↓↓

R='\033[1;31m' # VERMELHO
C='\033[1;37m' # BRANCO
CY='\033[1;36m' # BRANCO/AMARELO
Y='\033[1;33m' # AMARELO
G='\033[1;32m' # VERDE
NF="\033[0m" # DESFORMATAR
CR="\033[48;5;196m" # BRANCO/VERMELHO

#==============> VARIAVEIS USADAS ↓↓↓

T = False # para While
# "V" para inputs
# "emailT" email para login
# "passT" senha do email

#==============> VARIAVEIS P PRINT ↓↓↓

ch = f'\n   {R}>>> {C}'
a = f'{R}[{C}'
b = f'{R}]{G}'
c = f'{R}>>>{C} '

#==============> FUNÇÕES ↓↓↓

def clear():
	os.system('clear')

#==============> ASCII ↓↓↓

ascii1 = '''
   ──▄────▄▄▄▄▄▄▄────▄───
   ─▀▀▄─▄█████████▄─▄▀▀──
   ─────██─▀███▀─██──────
   ───▄─▀████▀████▀─▄────
   ─▀█────██▀█▀██────█▀──
'''

#==============> FIGLETS ↓↓↓

f1 = pyfiglet.figlet_format('   SWEET', font = 'standard')

#==============> MENU ↓↓↓
clear()
nome = input(f'   {a}+{b} COMO POSSO CHAMAR VOCÊ?{C} ')
while (T == False):
	clear()
	print(f'''          {a}+{b} CODED BY {a}+{b}
{f1}
   {G}[ MEU NÚMERO: {C}+5551997773672 {G}]

   {C} {G} SAWT-TRACKER TOOL {R}[v1.0]
   {C}==============================
   
   {a}01{b} >>>{C} LOCALIZAR IP-ALVO
   {a}02{b} >>>{C} LOCALIZAR SEU IP
   {a}03{b} >>>{C} MUDAR NOME SE ÚSUARIO
   {a}04{b} >>>{C} ENCERRAR
   
   {a}¿{b} API USADA: {C}http://ip-api.com/json/
   
   {NF}{CR}     <WE ARE SAWT SECURITY>     {NF}''')
	v = input(ch) #INPUT PRINCIPAL
	
	if v == '4' or v == '04':
		print(f'\n   {a}+{b} ATÉ MAIS {C}{nome}{G}!{NF}')
		break
	
	
	if v == '3' or v == '03':
		clear()
		print(f'''

   {a}+{b} NOME DE ÚSUARIO ATUAL: {C}{nome}{NF}''')
		nome = input(f'\n   {a}+{b} QUAL SEU NOVO NOME DE USUARIO? {C}')
   
	
	
	
	
	
	if v == '1' or v == '01': # LOCALIZE SEU IP
		while (T == False):
			clear()
			print(f'''
   {NF}{CR}     <WE ARE SAWT SECURITY>     {NF}
   {R}{ascii1}
   
   {G}  IP-TRACKER TOOL {R}[v1.0]
   {C}|———————————————————————|
   {C}|  {a}¿{b} INSIRA O IP {a}¿{b}  {C}|
   {C}|———————————————————————|
   
   {a}01{b} VOLTAR''')
			v = input(ch)
			if v == '1' or v == '01':
				break
			if v == '':
				print(f'\n   {a}+{b}INSIRA ALGO! REINICIANDO...');sleep(5);break
			try:
				ip = requests.get(f'http://ip-api.com/json/{v}')
				ip = ip.json()
				status = ip['status']
				country = ip['country']
				countryC = ip['countryCode']
				region = ip['region']
				regionN = ip['regionName']
				city = ip['city']
				zip = ip['zip']
				lat = ip['lat']
				lon = ip['lon']
				tmz = ip['timezone']
				isp = ip['isp']
				org = ip['org']
				As = ip['as']
				while (T == False):
					clear()
					print(f'''
   {G} CONSULTA EFETUADA!
   {C}<==================>
   {a}+{b} STATUS        {c} {status}
   {a}+{b} COUNTRY       {c} {country}
   {a}+{b} COUNTRY CODE  {c} {countryC}
   {a}+{b} REGION        {c} {region}
   {a}+{b} REGION NAME   {c} {regionN}
   {a}+{b} CITY          {c} {city}
   {a}+{b} ZIP           {c} {zip}
   {a}+{b} LAT           {c} {lat}
   {a}+{b} LON           {c} {lon}
   {a}+{b} TIMEZONE      {c} {tmz}
   {a}+{b} ISP           {c} {isp}
   {a}+{b} ORG           {c} {org}
   {a}+{b} AS            {c} {As}
  
   {a}+{b} USÚARIO: {C}{nome}
   
    {C}⟩⟩⟩ By Sweet Do Shock
   
   {a}01{b} VOLTAR
   {a}02{b} ENCERRAR''')
					v = input(ch)
					if v == '1' or v == '01':
						break
					if v == '2' or v == '02':
						print(f'\n   {a}+{b} ATÉ MAIS {C}{nome}{G}!{NF}')
						T = True
			except:
				print(f'''
   {a}!{b} ERRO!
   {a}!{b} IP NÃO RECONHECIDO
   {a}!{b} REINICIANDO...''');sleep(7)
   
   
	if v == '2' or v == '02':
		ip = requests.get('http://ip-api.com/json/')
		ip = ip.json()
		status = ip['status']
		country = ip['country']
		countryC = ip['countryCode']
		region = ip['region']
		regionN = ip['regionName']
		city = ip['city']
		zip = ip['zip']
		lat = ip['lat']
		lon = ip['lon']
		tmz = ip['timezone']	
		isp = ip['isp']
		org = ip['org']
		As = ip['as']
		print(f'''
   {G} CONSULTA EFETUADA!
   {C}<==================>
   {a}+{b} STATUS        {c} {status}
   {a}+{b} COUNTRY       {c} {country}
   {a}+{b} COUNTRY CODE  {c} {countryC}
   {a}+{b} REGION        {c} {region}
   {a}+{b} REGION NAME   {c} {regionN}
   {a}+{b} CITY          {c} {city}
   {a}+{b} ZIP           {c} {zip}
   {a}+{b} LAT           {c} {lat}
   {a}+{b} LON           {c} {lon}
   {a}+{b} TIMEZONE      {c} {tmz}
   {a}+{b} ISP           {c} {isp}
   {a}+{b} ORG           {c} {org}
   {a}+{b} AS            {c} {As}
  
   {a}+{b} USÚARIO: {C}{nome}
   
    {C}⟩⟩⟩ By Sweet Do Shock
   
   {a}+{b} PRESSIONE ENTER PARA RETORNAR''');input(ch)