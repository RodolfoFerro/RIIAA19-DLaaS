![DLaaS](media/banner.png)

![GitHub last commit](https://img.shields.io/github/last-commit/RodolfoFerro/RIIAA19-DLaaS?style=for-the-badge) <br>
![GitHub repo size](https://img.shields.io/github/repo-size/RodolfoFerro/RIIAA19-DLaaS?style=for-the-badge) <br>
![GitHub](https://img.shields.io/github/license/RodolfoFerro/RIIAA19-DLaaS?style=for-the-badge) <br>
[![Slides](https://img.shields.io/static/v1?label=Slides&message=Google%20Slides&color=tomato&style=for-the-badge)](https://docs.google.com/presentation/d/e/2PACX-1vQu3NcX5En0X4fd65-jziWHvPmkU1tUNQurw3lAgfcEHNwtmsaLg4zrE5AKwkYb0cshCXM0p55Is47p/pub?start=false&loop=false&delayms=3000)

## Contenido del taller

El taller fue desarrollado exclusivamente para su uso durante la **Escuela de Verano de la RIIAA 2.0**, y debe estar autocontenido, lo que significa que con este documento explicativo debe bastar para poder seguir y desarrollar el contenido del taller.

Grosso modo, el contenido cubierto a lo largo del taller es el siguiente:
- Motivación (~ 0.2 hrs)
- Requisitos y setup (~ 0.4 hrs)
- Intro al mundo del Deep Learning (~ 1.5 hrs)
- Funcionamiento de APIs:	(~ 2.5 hrs)
  - Requests: Consumo de APIs con Python	
  - Flask: Microframework web de Python		
- Cómo servimos modelos de IA	(~ 4 hrs)

Puedes encontrar los slides en vivo [**AQUÍ**](https://docs.google.com/presentation/d/e/2PACX-1vQu3NcX5En0X4fd65-jziWHvPmkU1tUNQurw3lAgfcEHNwtmsaLg4zrE5AKwkYb0cshCXM0p55Is47p/pub?start=false&loop=false&delayms=3000).

> Es importante mencionar que el curso hará uso de un ambiente en la nube y uno local para el desarrollo del material, por lo que te recomendamos apoyarte de los ayudantes del curso para la instalación de Pythony todos los requerimientos.

## Instrucciones para estudiantes

La mayoría de las prácticas de los talleres se desarrollarán en Python 3.7+ usando la biblioteca [Tensorflow 2.0](https://www.tensorflow.org/), que adopta [Keras](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/keras) como interfaz de alto nivel para construir y entrenar redes neuronales.

#### Requerimientos:
* Una laptop.
* Este repositorio de GitHub clonado y actualizado antes del taller.
* Un sentido aventurero en los datos.
* Un ambiente Python 3.7+ con Anaconda (ver opciones 1 y 2 abajo).

Los talleres serán impartidos usando *notebooks* de Jupyter, documentos con código ejecutable, texto, ecuaciones, visualizaciones, imágenes y demás material. Los *notebooks* se pueden crear y ejecutar en la nube vía Google Colab (opción 1) o de manera local en tu computadora a través de [Jupyter Notebooks o JupyterLab](https://jupyter.org/) (opción 2).

### Opcion 1: Google Colab

[Colab](https://colab.research.google.com) es un servicio de Google para ejecutar *notebooks* en la nube. Provee ambientes de Python 2 y 3 con CPUs, GPUs y TPUs. ¡Y es gratis! Solo necesitas tener una cuenta de Google o crear una.

Recomendamos que elijas un ambiente con Python 3 y GPU. Para activarlo:

* Abre el menú `Entorno de ejecución`
* Elige la opción `Restablecer todos los entornos de ejecución...` .
* Vuelve a abrir `Entorno de ejecución`
* Elige `Cambiar tipo de entorno de ejecución`
* Selecciona Python 3 como `Tipo de ejecución` y GPU de la lista de `Acelerador por hardware`

La siguiente captura de pantalla ilustra este proceso.

![](media/escoge_acelerador.png)

En [Colab](https://colab.research.google.com) puedes crear un nuevo *notebook*, subir uno existente desde tu computadora o importarlo de Google Drive o GitHub.

### Opcion 2: Ambiente local

Para tener la versión de Python 3.7+ (**añadido Python al PATH**) y todas las bibliotecas instaladas en cualquier plataforma, recomendamos que uses [**Anaconda**](https://www.anaconda.com/) y generes un ambiente con el archivo `environment.yml` de este repositorio usando una terminal y el comando:

```bash
conda env create -n riiaa19 -f environment.yml
```

Cambia el nombre `riia19` por tu nombre favorito para el ambiente o puedes remover la bandera `-n riia19` para dejar el nombre default del ambiente (`DLaaS`).

Para activar el ambiente que creaste, en una terminal ingresa el comando

```bash
conda activate riiaa19

# O en su defecto

conda activate DLaaS
```

Una vez activado, puedes ejecutar la aplicación de Jupyter Notebook

```bash
jupyter notebook
```
O de JupyterLab

```bash
jupyter lab
```

Este último comando abrirá una pestaña o ventana en tu navegador web, como se muestra en la siguiente captura de pantalla:

![](media/jupyter_lab.png)

Al igual que en Google Colab, puedes crear un nuevo *notebook* seleccionando el botón `New` y posteriormente `Python 3`. De forma alternativa, puedes abrir uno existente seleccionando el archivo del *notebook* (con extensión `.ipynb`) dentro del directorio donde ejecutaste Jupyter Notebook. Con el botón `Upload` agregas archivos que se encuentran en otra parte de tu computadora a este directorio. Para cerrar Jupyter Notebook, presiona el botón `Quit` y posteriormente cierra la pestaña o ventana de tu navegador web.

Para desactivar el ambiente `riiaa19` de Anaconda simplemente haz

```
conda deactivate
```

***

### Atribuciones

- Este repositorio cuenta con una  [MIT License](https://github.com/RodolfoFerro/RIIAA19-DLaaS/blob/master/LICENSE).
- Los íconos creados por [DinosoftLabs](https://www.flaticon.com/authors/dinosoftlabs) y [Flat Icons](https://www.flaticon.com/authors/flat-icons) de <https://www.flaticon.com/> cuentan con una licencia [CC 3.0 BY](http://creativecommons.org/licenses/by/3.0/).
