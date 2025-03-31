# Blog Coder

# INTEGRANTES

1. Alexis Borsato

2. Axel Godoy

3. Victoria Cruz Pintor

## Capturas de Pantalla

A continuación, se muestran algunas capturas de pantalla de la aplicación en funcionamiento:

### Iniciar sesión

![Iniciar sesión](/imgs/inicio_sesion.png)

### Crear Post

![Posts](/imgs/posts.png)

### Comentarios del post

![Comentarios del post](/imgs/Comentarios.png)

### Inicio

![Inicio](/imgs/inicio.png)

![Inicio](/imgs/inicio2.png)

### Perfil

![Perfil](/imgs/perfil.png)
![Editar perfil](/imgs/edicion_perfil.png)

### Contacto

![Contacto](/imgs/contacto.png)

# PARA PROBAR LA APP

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Alexmaxter/ProyectoFinal-BorsatoGodoyCruzp
cd ProyectoFinal-BorsatoGodoyCruzp
code .
```

### 2. Crear Entorno Virtual

Instalar `virtualenv` si no lo tienes:

```bash
pip install virtualenv
```

Crear un entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual:

- En sistemas Unix/Linux/Mac:

```bash
source venv/bin/activate
```

- En sistemas Windows:

```bash
. venv/Scripts/activate
```

### 3. Instalar Dependencias

Instalar las dependencias del proyecto especificadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Hacer migraciones

```bash
py manage.py makemigrations
py manage.py migrate
```

### 5. Levantar servidor

```bash
python manage.py runserver
```

## Funcionalidades

1. Inicio →

- Resumen del ultimo post
- Búsqueda de posts
- Usuarios registrados
- Se muestran 3 posteos seleccionados al azar

2. Acerca de →

- Breve resumen de los integrantes del proyecto

3. Blog →

- Botones: Crear y buscar
- Muestra todos los post publicados
- Sección de comentarios

4. Contacto →

- Formulario de contacto

5. Registro, inicio de sesión

6. Perfil de usuario →

- Gestión del perfil
- Información del usuario y últimos post
- Apartado redes del usuario
- Cambiar contraseña
- Cerrar sesión

7. Apartado Admin

- Se ve usuarios, posteos y comentarios
- Cada usuario y post tiene su imagen
