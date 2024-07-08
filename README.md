# ZOO.

### Descripción

Un programa realizado en Python que permite calcular el precio de la entrada al ZOO partiendo de una lista de precios determinada.

### Tabla de Contenidos

0. [Requisitos](#requisitos)
1. [Instalación](#instalación)
2. [Uso](#uso)
3. [Contribuciones](#contribuciones)
4. [Contacto](#contacto)

## Requisitos

- Python 3.12

## Instalación

1. Clona el repositorio

````cmd
git clone https://github.com/alonsoagustin/zoo.git

2. Crea un entorno virtual e instala las dependencias

```cmd
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
````

3. Ejecuta el siguiente Script

```cmd
python main.py
```

## Uso

Introduce, una a una, la edad de las personas que deseen ingresar al ZOO.

### Input

```cmd
 RESUMEN DE COMPRA
 Bebés............... 00.00 ..... 00 ..... €00.00
 Niños............... 14.00 ..... 00 ..... €00.00
 Adultos............. 23.00 ..... 00 ..... €00.00
 Jubilados........... 18.00 ..... 00 ..... €00.00
 ------------------------------------------------
 TOTAL: €00.00

 Ingrese una edad: 33
```

### Output

```cmd
 RESUMEN DE COMPRA
 Bebés............... 00.00 ..... 00 ..... €00.00
 Niños............... 14.00 ..... 00 ..... €00.00
 Adultos............. 23.00 ..... 01 ..... €23.00
 Jubilados........... 18.00 ..... 00 ..... €00.00
 ------------------------------------------------
 TOTAL: €23.00

 Ingrese una edad:
```

## Contribuciones

Cualquier contribución es bienvenida. Por favor sigue los siguientes pasos:

1. Fork el repositorio
2. Crea tu rama (`git checkout -b feature/nueva-feature`)
3. Haz un commit de tus cambios (`git commit -am 'Añadir nueva feature'`)
4. Push a la rama (`git push origin feature/nueva-feature`)
5. Abre un Pull Request

## Contacto

Agustin Alonso - [@alonsoiagustin](https://x.com/alonsoiagustin) - alonsoiagustin@gmail.com
