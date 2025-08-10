#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pdfkit

def convert_html_to_pdf_simple(html_file, pdf_file):
    """
    Convierte HTML a PDF usando pdfkit (más simple de instalar)
    """
    try:
        # Configuración para pdfkit
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': 'UTF-8',
            'no-outline': None,
            'enable-local-file-access': None
        }
        
        # Convertir HTML a PDF
        pdfkit.from_file(html_file, pdf_file, options=options)
        
        print(f"✅ PDF generado exitosamente: {pdf_file}")
        return True
        
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
    
    print("🔄 Convirtiendo HTML a PDF con pdfkit...")
    
    # Convertir a PDF
    success = convert_html_to_pdf_simple(html_file, pdf_file)
    
    if success:
        print(f"📄 El archivo PDF está listo: {pdf_file}")
        print("🎉 ¡Tu CV está listo para LinkedIn!")
    else:
        print("💡 Para instalar wkhtmltopdf en Windows:")
        print("   1. Descarga desde: https://wkhtmltopdf.org/downloads.html")
        print("   2. Instala el ejecutable")
        print("   3. Asegúrate de que esté en el PATH del sistema")

if __name__ == "__main__":
    main()
