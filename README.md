# Laboratorio 1 Análisis estadístico de señales
## Shara Cetina y Juanita Gómez
## Descripción
Este proyecto contiene el código para analizar y caracterizar una señal biomédica en función de parámetros estadísticos, empleando funciones aritméticas y comandos específicos de un entorno de
programación.
## Propósito
<p align="justify">
Esta práctica es muy importante para futuros ingenieros biomédicos que se encuentran en formación académica, principalmente para aquellos que quieren incursionar en el campo de análisis de señales. Les ayuda a entender el comportamiento de estas señales y el porqué es tan importante conocer cómo se ve la presencia de un ruido, ya sea por temas de cables, respiración, mala toma de datos, etc; a partir de los resultados con unos buenos cálculos estadísticos se lograría un mejor entendimiento de esta, brindando prontos diagnósticos al paciente.
  
## Metodología
<p align="justify">
Para comprobar la importancia de un buen análisis de señales se realizó la toma de dos electrocardiográficas, las cuales fueron modificadas para observar su comportamiento ante distintas situaciones. Primeramente se tomó una señal del repositorio Physionet a la cual se le calcularon todos los valores estadísticos importantes (media, desviación estándar, curtosis,.. etc), por consiguiente se realizó lo mismo pero con una señal proveniente de un generador de señales, el cual nos permitía adquirir una señal muy perfecta,a partir de esta se repitió el procedimiento pero con la diferencia de que a la última se le fueron añadiendo diferentes tipos de ruidos con el propósito de observar cómo iban cambiando frente a estos. Todo esto con el fin de observar en qué se diferencia una señal real, en este caso la descargada de physionet y la ideal del generador de señales. 

<p align="justify">  
Con ayuda de Spyder, una multiplataforma que nos posibilita programar en python, permitió la adquisición de la señal obtenida en python, gracias a la librería “wfdb” la cual physionet también trabaja, después de su exportación se le realizaron los cálculos propuestos y el de la frecuencia cardiaca, la cual se hizo con ayuda de la librería “find_peaks”, este mismo proceso se hizo con la señal cardiaca adquirida por el DAQ, y para finalizar con programó un código que le produjera un ruido de diferentes tipos a la señal, de esta manera se logra ver su comportamiento con y sin ruido.

## Diagrama de flujo
<img width="1024" height="768" alt="1" src="https://github.com/user-attachments/assets/1e8ec0ab-5f21-4762-96cd-dd3364512b04" />
<img width="1024" height="768" alt="2" src="https://github.com/user-attachments/assets/2df97a7a-348b-4769-a679-fca7a4dc21b7" />
<img width="1024" height="768" alt="PARTE B" src="https://github.com/user-attachments/assets/50fd5325-d73e-4ed2-94c6-0eb55baa63d5" />
<img width="1103" height="708" alt="2b" src="https://github.com/user-attachments/assets/f16d3a0f-53c5-43d6-8f27-c08964289e44" />

## Discusión
__¿Los valores estadísticos calculados sobre la señal sintética son exactamente iguales a los obtenidos a partir de la señal real? ¿Por qué?__
<p align="justify">
Los valores estadísticos calculados sobre la señal sintética no son exactamente iguales a los obtenidos a partir de la señal real, debido a que estas ultimas presentan ruidos fisiológicos o ambientales como el movimiento del paciente, la interferencia eléctrica, o el contacto de electrodos, por otro lado, la señal sintética se simula en un entorno ideal, sin ruido, con un ritmo cardiaco normal sin alteraciones. Además, existen diferencias en la frecuencia cardíaca, lo que modifica la distribución temporal de los complejos QRS. 
Por otra parte, se observan diferencias importantes en la media y la desviación estándar, lo que puede demostrar que las señales no están centradas o escaladas de la misma forma. Por último, la señal real proviene de un paciente sometido a 4 fármacos que prolongan el intervalo QT (según la investigación en PhysioNet), lo que altera la morfología del ECG y afecta parámetros como la asimetría y la curtosis.
