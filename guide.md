# Guía del proyecto Streamlit de Ciencia de Datos

## 1. Qué se ha realizado

Se desarrolló una aplicación en Streamlit para:
- cargar un dataset CSV,
- explorar la estructura inicial del archivo,
- visualizar métricas y distribuciones,
- analizar variables clave y presentar resultados de forma interactiva.

El proyecto usa como dataset base el archivo ubicado en:
- archive/material.csv

## 2. Estructura del proyecto

- app.py: aplicación principal de Streamlit.
- archive/: carpeta con los datasets originales y el script de ejemplo.
- requirements.txt: dependencias necesarias para ejecutar el proyecto.
- README.md: descripción breve del proyecto.
- guide.md: esta guía paso a paso.

## 3. Dependencias necesarias

Instala estas dependencias con Python 3.10 o superior:

```powershell
pip install streamlit pandas
```

O, si prefieres usar el archivo de dependencias incluido:

```powershell
pip install -r requirements.txt
```

## 4. Cómo replicar el proyecto desde cero

### Paso 1: crear la carpeta del proyecto
Crea una carpeta nueva y entra en ella.

### Paso 2: crear un entorno virtual (recomendado)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, ejecuta:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### Paso 3: instalar dependencias
```powershell
pip install streamlit pandas
```

### Paso 4: crear el archivo principal
Crea un archivo llamado `app.py` con la lógica de la aplicación Streamlit.

### Paso 5: agregar el dataset
Coloca tu CSV dentro de una carpeta llamada `archive/`.

### Paso 6: ejecutar la aplicación
```powershell
streamlit run app.py
```

## 5. Cómo usar la aplicación

1. Abre la URL que muestra Streamlit en tu navegador.
2. En la barra lateral podrás cargar un archivo CSV propio si lo deseas.
3. La app mostrará:
   - métricas generales del dataset,
   - vista previa de los datos,
   - tipos de columnas y valores nulos,
   - resumen estadístico,
   - visualizaciones interactivas.

## 6. Cómo verificar que funciona correctamente

### Verificación rápida
Ejecuta:
```powershell
streamlit run app.py
```

Luego abre la URL local que aparezca, normalmente:
```text
http://localhost:8501
```

### Verificación con Python
También puedes confirmar que las dependencias están disponibles con:
```powershell
python -m pip show streamlit pandas
```

### Verificación de respuesta del servidor
Si quieres comprobar que el servidor está activo:
```powershell
curl -I http://localhost:8501/
```

Debe devolver una respuesta `200 OK`.

## 7. Solución de problemas comunes

### El comando `streamlit` no se reconoce
Usa la versión de Python instalada explícitamente:
```powershell
python -m streamlit run app.py
```

### Error de permisos en PowerShell
Ejecuta:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### El dataset no carga
Verifica que el archivo exista en `archive/` y que tenga formato CSV válido.

## 8. Resultado esperado

Al ejecutar la app, deberías ver una interfaz interactiva con:
- título del proyecto,
- métricas iniciales,
- tabla previa del dataset,
- resumen estadístico,
- gráficos y visualizaciones relevantes.

Esta guía sirve como referencia para reproducir y continuar desarrollando el proyecto en futuras sesiones.
