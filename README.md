# Sensor de ocupación

Este proyecto corresponde al software del dispositivo denominado "Sensor de ocupación", desarrollado para la Universidad del Valle. Su objetivo es contabilizar la cantidad de personas que ingresan y salen de un determinado recinto, manteniendo un registro de dichos eventos en una base de datos alojada en Firebase y administrada por la universidad.

El microcontrolador principal del dispositivo es el ESP32, el cual está integrado en la tarjeta de desarrollo ESP32S DevBoard (30 pines).

El código se desarrolló en el lenguaje Python 3.X, utilizando una versión especial para trabajar con microcontroladores llamada MicroPython. Para ejecutar los comandos de este repositorio, es necesario cargar el sistema operativo de MicroPython en la ESP32. Puedes obtener más información sobre este proceso en el siguiente enlace: [Documentación de MicroPython](https://docs.micropython.org/en/latest/).

Adicionalmente, se requiere la descarga de las librerías base de Arduino, las cuales se instalan junto con su entorno de desarrollo integrado (IDE) disponible en [Arduino Software](https://www.arduino.cc/en/software). Aunque para cargar el código en la ESP32, se recomienda utilizar el IDE Thonny, disponible en [Thonny](https://thonny.org/).