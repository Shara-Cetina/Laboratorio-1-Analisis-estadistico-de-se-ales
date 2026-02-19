# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 20:38:42 2026

@author: Shara Cetina y Juanita Gomez
"""
#Importar librerias
import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.stats import skew, kurtosis

#Parte A 

#Carga de archivo escogido
ruta = r'C:\Users\manue\Desktop\ECG grafica\00ed2097-cd14-4f03-ab33-853da5be5550'
record = wfdb.rdrecord(ruta, sampfrom=0, sampto=1000) 

#Graficar la señal
wfdb.plot_wfdb(record=record, title='Señal ECG completa')

# Extraer canal 1
senal = record.p_signal[:, 0]

# Frecuencia de muestreo
fs = record.fs
print ("Parte A")
print("Frecuencia de muestreo:", fs)

# Detectar picos R
picos, _ = find_peaks(senal, distance=fs*0.6)

# Calculo frecuencia cardiaca
tiempos = picos / fs
intervalos_rr = np.diff(tiempos)
frecuencia_cardiaca = 60 / np.mean(intervalos_rr)
print("Frecuencia cardiaca aproximada:", frecuencia_cardiaca, "BPM" )

# Graficar señal con picos
tiempo = np.arange(len(senal)) / fs
plt.figure()
plt.plot(tiempo, senal)
plt.plot(tiempo[picos], senal[picos], "x")
plt.title("ECG con detección de picos R")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

# CALCULOS MANUALES

N = len(senal)
sumatotal = 0.0
contador_muestras = 0
suma_para_promedio = 0.0
suma_diferencias_cuadrado = 0.0
suma_cubos = 0.0
suma_cuartas = 0.0

# Media de la señal
for valor in senal:
    sumatotal = sumatotal + valor
    contador_muestras = contador_muestras + 1
    
if contador_muestras > 0:
    promedio_manual = sumatotal / contador_muestras
else:
    promedio_manual = 0

# Desviación estándar
for valor in senal:
    suma_para_promedio += valor
    
for valor in senal:
    diferencia = valor - promedio_manual
    suma_diferencias_cuadrado += diferencia * diferencia 
    
varianza_manual = suma_diferencias_cuadrado / N
std_manual = varianza_manual**0.5

# Coeficiente de variación
cv_manual = std_manual/abs(promedio_manual)

# Histograma
# Encontrar valores minimos y maximos
max_val = senal[0] 
min_val = senal[0] 
for valor in senal:
    if valor > max_val:
        max_val = valor
    if valor < min_val:
        min_val = valor

# Definir el número de bins
num_bins = 20
rango = max_val - min_val
ancho_bin = rango / num_bins

frecuencias = [0]* num_bins

# Clasificar cada dato en su bin correspondiente
for valor in senal:
    # Calculamos el índice del bin para este valor
    indice = int((valor - min_val) / ancho_bin)
    
    # Ajuste para el valor máximo exacto para que no se salga del índice
    if indice == num_bins:
        indice = num_bins - 1
        
    frecuencias[indice] = frecuencias[indice] + 1

# Crear las etiquetas de los bins (eje X) para la gráfica
centros_bins = []
for i in range(num_bins):
    centro = min_val + (i + 0.5) * ancho_bin
    centros_bins.append(centro)
    
# Asimetría (skewness)
for valor in senal:
    diferencia = valor - promedio_manual
    suma_cubos = suma_cubos + (diferencia ** 3)

asimetria = (suma_cubos / N) / (std_manual ** 3)

# Curtosis
for valor in senal:
    diferencia = valor - promedio_manual
    suma_cuartas = suma_cuartas + (diferencia ** 4)

curtosis = ((suma_cuartas / N) / (std_manual ** 4))-3
print("")
print("===== CALCULOS DESDE CERO =====")

print("Media:", promedio_manual)
print("Desviación estándar:", std_manual)
print("Coeficiente de variación:", cv_manual)
print("Asimetria:", asimetria)
print("Curtosis:", curtosis)

# Mostrar el histograma
plt.figure(figsize=(10, 5))
plt.bar(centros_bins, frecuencias, width=ancho_bin, color='blue', edgecolor='black')
plt.title('Histograma Manual')
plt.xlabel('Amplitud')
plt.ylabel('Frecuencia (conteo de muestras)')
plt.show()

# CALCULOS CON FUNCIONES PREDETERMINADAS

media_np = np.mean(senal)
std_np = np.std(senal, ddof=1)
cv_np = std_np/media_np
skew_np = skew(senal)
kurt_np = kurtosis(senal)

print ("")
print("===== CON FUNCIONES =====")
print("Media:", media_np)
print("Desviación estándar:", std_np)
print("Coeficiente de variación:", cv_np)
print("Asimetria:", skew_np)
print("Curtosis:", kurt_np)

plt.figure()
plt.hist(senal, bins=20)
plt.title("Histograma de la señal ECG")
plt.xlabel("Amplitud")
plt.ylabel("Frecuencia")
plt.show()

#==============================================================================
#Parte B
print("")
print("Parte B")

# Cargar archivo
SenalClase = np.loadtxt("ECGgraficaClase.txt")
fs = 1000 
tiempo = np.arange(len(SenalClase)) / fs

# Graficar
plt.figure()
plt.plot(tiempo, SenalClase)
plt.title("ECG Generado")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# Detectar picos R
picos, _ = find_peaks(SenalClase, distance=fs*0.6)

# Calcular frecuencia cardiaca
tiempos = picos / fs
intervalos_rr = np.diff(tiempos)
frecuencia_cardiaca = 60 / np.mean(intervalos_rr)
print("Frecuencia cardiaca aproximada:", frecuencia_cardiaca, "BPM" )

# Graficar señal con picos
tiempo = np.arange(len(SenalClase)) / fs
plt.figure()
plt.plot(tiempo, SenalClase)
plt.plot(tiempo[picos], SenalClase[picos], "x")
plt.title("ECG con detección de picos R")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

# CALCULOS MANUALES

N = len(SenalClase)
sumatotal = 0.0
contador_muestras = 0
suma_para_promedio = 0.0
suma_diferencias_cuadrado = 0.0
suma_cubos = 0.0
suma_cuartas = 0.0

# Media
for valor in SenalClase:
    sumatotal = sumatotal + valor
    contador_muestras = contador_muestras + 1
    
if contador_muestras > 0:
    promedio_manual = sumatotal / contador_muestras
else:
    promedio_manual = 0

# Desviación estándar
for valor in SenalClase:
    suma_para_promedio += valor
    
for valor in SenalClase:
    diferencia = valor - promedio_manual
    suma_diferencias_cuadrado += diferencia * diferencia 
    
varianza_manual = suma_diferencias_cuadrado / N
std_manual = varianza_manual**0.5

# Coeficiente de variación
cv_manual = std_manual/abs(promedio_manual)

# Histograma
# Encontrar valores minimos y maximos
max_val = SenalClase[0] 
min_val = SenalClase[0] 
for valor in SenalClase:
    if valor > max_val:
        max_val = valor
    if valor < min_val:
        min_val = valor

# Definir el número de bins
num_bins = 30
rango = max_val - min_val
ancho_bin = rango / num_bins

# Crear una lista para las frecuencias (conteo de cada bin)
frecuencias = [0]* num_bins

# Clasificar cada dato en su bin correspondiente
for valor in SenalClase:
    # Calculamos el índice del bin para este valor
    indice = int((valor - min_val) / ancho_bin)
    
    # Ajuste para el valor máximo exacto para que no se salga del índice
    if indice == num_bins:
        indice = num_bins - 1
        
    frecuencias[indice] = frecuencias[indice] + 1

# Crear las etiquetas de los bins (eje X) para la gráfica
centros_bins = []
for i in range(num_bins):
    centro = min_val + (i + 0.5) * ancho_bin
    centros_bins.append(centro)

# Asimetría (skewness)
for valor in SenalClase:
    diferencia = valor - promedio_manual
    suma_cubos = suma_cubos + (diferencia ** 3)

asimetria = (suma_cubos / N) / (std_manual ** 3)

# Curtosis
for valor in SenalClase:
    diferencia = valor - promedio_manual
    suma_cuartas = suma_cuartas + (diferencia ** 4)

#Puede restarle 3 como aparece en algunas formulas 
curtosis = ((suma_cuartas / N) / (std_manual ** 4))-3

print("")
print("===== CALCULOS DESDE CERO =====")

print("Media:", promedio_manual)
print("Desviación estándar:", std_manual)
print("Coeficiente de variación:", cv_manual)
print("Asimetria:", asimetria)
print("Curtosis:", curtosis)
 
plt.figure(figsize=(10, 5))
plt.bar(centros_bins, frecuencias, width=ancho_bin, color='blue', edgecolor='black')
plt.title('Histograma Manual')
plt.xlabel('Amplitud')
plt.ylabel('Frecuencia (conteo de muestras)')
plt.show()

# CALCULOS CON FUNCIONES PREDETERMINADAS

media_np = np.mean(SenalClase)
std_np = np.std(SenalClase, ddof=1)
cv_np = std_np/media_np
skew_np = skew(SenalClase)
kurt_np = kurtosis(SenalClase)

plt.figure()
plt.hist(SenalClase, bins=30)
plt.title("Histograma de la señal ECG")
plt.xlabel("Amplitud")
plt.ylabel("Frecuencia")
plt.show()

print("")
print("===== CON FUNCIONES =====")
print("Media:", media_np)
print("Desviación estándar:", std_np)
print("Coeficiente de variación:", cv_np)
print("Asimetria:", skew_np)
print("Curtosis:", kurt_np)

#==============================================================================
# Parte C
#A
# Cargar señal
data = np.loadtxt("ECGgraficaClase.txt")
N = len(data)
print("")
print("Parte C")
print("Número de muestras:", N)
print("")

# Frecuencia de muestreo
fs = 1000   
t = np.arange(N) / fs   # Vector de tiempo en segundos

# Quitar offset (centrar señal)
data = data - np.mean(data)

# Calcular potencia de la señal
potencia_senal = np.mean(data**2)

# Definir directamente la desviación estándar del ruido
sigma_ruido = 0.1   # Valor libre

# Generar ruido Gaussiano
ruido = np.random.normal(0, sigma_ruido, N)

# Contaminar señal
senal_ruidosa = data + ruido

# Calcular SNR real
potencia_ruido_real = np.mean(ruido**2)

SNR_real = 10 * np.log10(potencia_senal / potencia_ruido_real)

print("SNR con ruido Gaussiano:", SNR_real, "dB")

# Graficar señal + ruido Gaussiano
plt.figure(figsize=(12,6))
plt.plot(t,senal_ruidosa)
plt.title("ECG con ruido Gaussiano")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

#B
# La señal ya fue cargada previamente

# Generar Ruido Impulso
porcentaje_impulso = 0.02   # 2% de muestras afectadas
num_impulsos = int(porcentaje_impulso * N)

senal_impulso = data.copy()

# Elegir posiciones aleatorias
indices = np.random.choice(N, num_impulsos, replace=False)

# Amplitud del impulso
amplitud_impulso = 4 * np.std(np.abs(data))

senal_impulso[indices] = amplitud_impulso * np.random.choice([-1, 1], size=num_impulsos)

# Calcular SNR

ruido_impulso = senal_impulso - data
potencia_ruido2 = np.mean(ruido_impulso**2)

SNR_impulso = 10 * np.log10(potencia_senal / potencia_ruido2)

print("")
print("SNR con ruido impulso:", SNR_impulso, "dB")

# Graficar
plt.figure(figsize=(12,6))
plt.plot(t,senal_impulso)
plt.title("ECG con ruido Impulso")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

#C
# La señal ya fue cargada previamente
# Artefacto 60 Hz
f_artefacto = 60
amplitud_ruido = 0.2

seno_60hz = amplitud_ruido * np.sin(2*np.pi*f_artefacto*t)

# Potencia del ruido (solo el seno 60 Hz)
potencia_ruido = np.mean(seno_60hz**2)

# Señal contaminada
ecg_con_ruido = data + seno_60hz

# Calcular SNR
SNR_artefacto = 10 * np.log10(potencia_senal / potencia_ruido)
print("")
print("SNR con ruido artefacto:", SNR_artefacto, "dB")

# Graficar
plt.figure(figsize=(12,6))
plt.plot(t,ecg_con_ruido)
plt.title("ECG con ruido Artefacto de 60Hz")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()