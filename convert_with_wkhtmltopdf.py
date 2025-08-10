#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys

def convert_with_wkhtmltopdf(html_file, pdf_file):
    """
    Convierte HTML a PDF usando wkhtmltopdf
    """
    try:
        # Comando para wkhtmltopdf
        cmd = [
            'wkhtmltopdf',
            '--page-size', 'A4',
            '--margin-top', '0.75in',
            '--margin-right', '0.75in',
            '--margin-bottom', '0.75in',
            '--margin-left', '0.75in',
            '--encoding', 'UTF-8',
            '--no-outline',
            '--enable-local-file-access',
            html_file,
            pdf_file
        ]
        
        # Ejecutar el comando
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ PDF generado exitosamente: {pdf_file}")
            return True
        else:
            print(f"❌ Error en wkhtmltopdf: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ wkhtmltopdf no está instalado o no está en el PATH")
        return False
    except Exception as e:
        print(f"❌ Error al generar PDF: {str(e)}")
        return False

def main():
    html_file = "cv_richard.html"
    pdf_file = "CV_Richard_LinkedIn.pdf"
    
    # Verificar que el archivo HTML existe
    if not os.path.exists(html_file):
        print(f"❌ Error: No se encontró el archivo {html_file}")
        return
    
    print("🔄 Convirtiendo HTML a PDF con wkhtmltopdf...")
    
    # Convertir a PDF
    success = convert_with_wkhtmltopdf(html_file, pdf_file)
    
    if success:
        print(f"📄 El archivo PDF está listo: {pdf_file}")
        print("🎉 ¡Tu CV está listo para LinkedIn!")
    else:
        print("💡 Para instalar wkhtmltopdf en Windows:")
        print("   1. Descarga desde: https://wkhtmltopdf.org/downloads.html")
        print("   2. Instala el ejecutable")
        print("   3. Asegúrate de que esté en el PATH del sistema")
        print("   4. O usa la ruta completa al ejecutable")

if __name__ == "__main__":
    main()
