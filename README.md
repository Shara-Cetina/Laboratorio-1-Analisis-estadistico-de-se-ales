# Laboratorio No.1 "Análisis estadístico de señales"
## Shara Cetina y Juanita Gómez
## Descripción
Este proyecto contiene el código para analizar y caracterizar una señal biomédica en función de parámetros estadísticos, empleando funciones aritméticas y comandos específicos de un entorno de
programación.
## Propósito
<p align="justify">
Esta práctica es muy importante para futuros ingenieros biomédicos que se encuentran en formación académica, principalmente para aquellos que quieren incursionar en el campo de análisis de señales. Les ayuda a entender el comportamiento de estas señales y el porqué es tan importante conocer cómo se ve la presencia de un ruido, ya sea por temas de cables, respiración, mala toma de datos, etc; a partir de los resultados obtenidos se realizan cálculos estadísticos pertinenetes que les permita mejorar su entendimiento, además de ayudar a brindar diagnósticos prontos al paciente.
  
## Metodología
<p align="justify">
Para comprobar la importancia de un buen análisis de señales se realizó la toma de dos electrocardiográficas, las cuales fueron modificadas para observar su comportamiento ante distintas situaciones. Primeramente se tomó una señal del repositorio Physionet a la cual se le calcularon todos los valores estadísticos importantes (media, desviación estándar, curtosis,.. etc), por consiguiente se realizó lo mismo pero con una señal proveniente de un generador de señales, el cual nos permitía adquirir una señal muy perfecta, a partir de esta se repitió el procedimiento pero con la diferencia de que a la última se le fueron añadiendo diferentes tipos de ruidos con el propósito de observar cómo iban cambiando frente a estos. Todo esto con el fin de observar en qué se diferencia una señal real, en este caso la descargada de physionet y la ideal del generador de señales. 

<p align="justify">  
Con ayuda de Spyder, una multiplataforma que nos posibilita programar en python, permitió la adquisición de la señal obtenida en python, gracias a la librería “wfdb” la cual physionet también trabaja, después de su exportación se le realizaron los cálculos propuestos y el de la frecuencia cardiaca, la cual se hizo con ayuda de la librería “find_peaks”, este mismo proceso se hizo con la señal cardiaca adquirida por el DAQ, y para finalizar con programó un código que le produjera un ruido de diferentes tipos a la señal, de esta manera se logra ver su comportamiento con y sin ruido.

## Diagrama de flujo
## Parte A
<img width="1024" height="768" alt="1" src="https://github.com/user-attachments/assets/e41fa865-f3e8-485a-9629-2fc6c196c184" />

<img width="1024" height="768" alt="2" src="https://github.com/user-attachments/assets/a08de90d-691a-4cfd-ac28-682e9e8d84a4" />

<img width="1024" height="768" alt="3" src="https://github.com/user-attachments/assets/63c10fc7-996d-470d-81f0-a036ee70bcfa" />

<img width="1024" height="768" alt="Parte A (1)" src="https://github.com/user-attachments/assets/86214a4a-e6d7-4d40-8b18-ef00b0db51c7" />

<img width="1024" height="768" alt="5" src="https://github.com/user-attachments/assets/5e557de7-6f3a-4bb4-bd55-1c0000f30597" />

<img width="1024" height="768" alt="Parte A" src="https://github.com/user-attachments/assets/658c43d5-1415-4eab-8c72-3a6a50c483ab" />



## Parte B

<img width="1024" height="768" alt="1" src="https://github.com/user-attachments/assets/2876f8ca-718c-4ef5-85e2-c30312887fc7" />

<img width="1024" height="768" alt="2" src="https://github.com/user-attachments/assets/0f0327fb-3709-4597-9c7f-f318782dc1fe" />

<img width="1024" height="458" alt="35" src="https://github.com/user-attachments/assets/4ec97c54-18d4-400d-a1d3-5c43feb12e61" />



## Parte C

<img width="1024" height="768" alt="PARTE C" src="https://github.com/user-attachments/assets/3f33d883-195e-4a65-99b9-e269b5ffb32d" />

<img width="1024" height="768" alt="PARTE 2C" src="https://github.com/user-attachments/assets/f7b51cfd-71f5-4769-b33b-fc8124c30b95" />

## Resultados
Al realizar el paso a paso de los diagramas de flujo enunciados anteriormente, se obtiene:
* **Señal obtenida de la plataforma PhysioNet:**
  
![p](https://github.com/user-attachments/assets/88fef053-8803-4b59-839b-b0e24162afe2)
* **Histogramas:**

![p1](https://github.com/user-attachments/assets/f6dd0c00-b5f3-4adf-b2db-3a9cc264baff)

![p2](https://github.com/user-attachments/assets/feea9479-6cce-4636-8b5b-63a88eadcd51)

 
* **Datos calculados manualmente y con las funciones predeterminadas:**

![WhatsApp Image 2026-02-18 at 23 58 06](https://github.com/user-attachments/assets/80c9f9dc-3776-46f5-ac8f-2fe6daf7d7b8)

![nb](https://github.com/user-attachments/assets/c4f9914f-a897-4e08-aa7e-6df0da36c6e7) 

![kc](https://github.com/user-attachments/assets/8951eee0-df06-450c-956f-0105d3489dbd)
 
 
* **Señal simulada:**

![p3](https://github.com/user-attachments/assets/139fbacf-4926-4168-b882-bf201e807174)

 
* **Histograma de señal simulada:**
  
![p5](https://github.com/user-attachments/assets/dfff1bf0-41dc-4df0-9684-d7abec40d4ea)

![p4](https://github.com/user-attachments/assets/02e0296d-d619-4cfa-9a05-e5207a145ec5)


* **Señal con ruido:**

- Gaussiano
  
![p6](https://github.com/user-attachments/assets/cbe6366f-2c8e-45be-ae42-da2888b5e5a4)

  - Impulso

![p7](https://github.com/user-attachments/assets/d7ed6c73-a348-4b92-b8a0-aa9ea8bff2b3)


  - Artefacto

![p8](https://github.com/user-attachments/assets/495171f4-3406-4e2b-9715-f4b83efb5b9f)



## Discusión
**¿Los valores estadísticos calculados sobre la señal sintética son exactamente iguales a los obtenidos a partir de la señal real? ¿Por qué?**
<p align="justify">
Los valores estadísticos calculados sobre la señal sintética no son exactamente iguales a los obtenidos a partir de la señal real, debido a que estas ultimas presentan ruidos fisiológicos o ambientales como el movimiento del paciente, la interferencia eléctrica, o el contacto de electrodos, por otro lado, la señal sintética se simula en un entorno ideal, sin ruido, con un ritmo cardiaco normal sin alteraciones. Además, existen diferencias en la frecuencia cardíaca, lo que modifica la distribución temporal de los complejos QRS. 
Por otra parte, se observan diferencias importantes en la media y la desviación estándar, lo que puede demostrar que las señales no están centradas o escaladas de la misma forma. Por último, la señal real proviene de un paciente sometido a 4 fármacos que prolongan el intervalo QT (según la investigación en PhysioNet), lo que altera la morfología del ECG y afecta parámetros como la asimetría y la curtosis.

**¿Afecta el tipo de ruido el valor de la SNR calculado? ¿Cuáles podrían ser las razones?**
<p align="justify"> 
La SNR es la relación potencia de la señal y la potencia del ruido, es por esto mismo que según el tipo de ruido puede cambiar ya que cada uno maneja una distribución de energía distinta, por ejemplo, el ruido gaussiano divide su potencia de manera uniforme y continua, generando una alteración moderada en la señal, mientras que el ruido impulso concentra mucha energía en puntos de tiempo breves (picos), lo que altera el promedio de potencia, debido a que esta se calcula a partir del cuadrado de la amplitud, lo que reduce más la SNR.
