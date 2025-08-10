# 📄 CV Richard - Generador de PDF para LinkedIn

Este proyecto crea un CV profesional en PDF para LinkedIn basado en la información proporcionada por Richard.

## 📁 Archivos Incluidos

- `cv_richard.html` - CV en formato HTML con diseño moderno
- `convert_simple.py` - Script simple para convertir HTML a PDF usando pdfkit
- `convert_to_pdf.py` - Script avanzado usando WeasyPrint
- `convert_with_wkhtmltopdf.py` - Script alternativo usando wkhtmltopdf
- `requirements_simple.txt` - Dependencias simples de Python
- `requirements.txt` - Dependencias avanzadas de Python
- `README.md` - Este archivo de instrucciones

## 🚀 Opciones para Generar el PDF

### Opción 1: Usando el Navegador (Más Simple) ⭐

1. **Abrir el archivo HTML:**
   - Haz doble clic en `cv_richard.html`
   - Se abrirá en tu navegador predeterminado

2. **Imprimir como PDF:**
   - Presiona `Ctrl + P` (o `Cmd + P` en Mac)
   - Selecciona "Guardar como PDF"
   - Guarda el archivo como `CV_Richard_LinkedIn.pdf`

### Opción 2: Usando pdfkit (Simple con Python)

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements_simple.txt
   ```

2. **Instalar wkhtmltopdf:**
   - Descarga desde: https://wkhtmltopdf.org/downloads.html
   - Instala el ejecutable
   - Asegúrate de que esté en el PATH del sistema

3. **Generar el PDF:**
   ```bash
   python convert_simple.py
   ```

### Opción 3: Usando WeasyPrint (Avanzado)

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **En Windows, también necesitarás GTK+:**
   - Descarga desde: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer
   - Instala el ejecutable

3. **Generar el PDF:**
   ```bash
   python convert_to_pdf.py
   ```

## 📋 Características del CV

✅ **Diseño Moderno y Profesional**

- Gradientes y colores atractivos
- Tipografía clara y legible
- Layout responsive

✅ **Secciones Completas**

- Información de contacto
- Sobre mí
- Experiencia actual
- Stack tecnológico
- Proyectos destacados
- Objetivos profesionales
- Intereses de colaboración

✅ **Optimizado para LinkedIn**

- Formato A4 estándar
- Diseño profesional
- Información estructurada
- Fácil de leer

## 🎨 Personalización

Puedes personalizar el CV editando el archivo `cv_richard.html`:

- **Colores:** Cambia los valores de color en el CSS
- **Contenido:** Modifica el texto en las secciones correspondientes
- **Diseño:** Ajusta el CSS para cambiar el layout

## 📞 Información de Contacto

El CV incluye:

- 📧 **Email:** richard.mateo.obando@gmail.com
- 📱 **Teléfono:** +34 642 297 705
- 💼 **LinkedIn:** [Richard Mateo Obando Ladino](https://www.linkedin.com/in/richard-mateo-obando-ladino-5b3214250)
- 🐙 **GitHub:** [@Elminero26](https://github.com/Elminero26)
- 🔧 **GitLab:** [@Eltopito](https://gitlab.com/Eltopito)

**¡Toda la información de contacto está actualizada y lista para usar!**

## 🎯 Resultado Final

Al completar cualquiera de las opciones, tendrás un archivo `CV_Richard_LinkedIn.pdf` listo para:

- Subir a LinkedIn
- Enviar por email
- Imprimir
- Compartir en redes profesionales

¡Tu CV profesional está listo! 🚀
