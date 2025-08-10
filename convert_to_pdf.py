#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import webbrowser
import time

def convert_html_to_pdf(html_file, pdf_file):
    """
    Abre el archivo HTML en el navegador para que el usuario pueda guardarlo como PDF
    """
    try:
        # Abrir el archivo HTML en el navegador
        webbrowser.open(f'file://{os.path.abspath(html_file)}')
        
        print(f"✅ Archivo HTML abierto en el navegador")
        print(f"📋 Instrucciones:")
        print(f"   1. Presiona Ctrl + P en el navegador")
        print(f"   2. Selecciona 'Guardar como PDF'")
        print(f"   3. Guarda como: {pdf_file}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    html_file = "cv_richard.html"
    pdf_file = "CV_Richard_LinkedIn.pdf"
    
    # Verificar que el archivo HTML existe
    if not os.path.exists(html_file):
        print(f"❌ Error: No se encontró el archivo {html_file}")
        return
    
    print("🔄 Abriendo CV en el navegador...")
    
    # Abrir en navegador
    success = convert_html_to_pdf(html_file, pdf_file)
    
    if success:
        print("🎉 ¡Sigue las instrucciones en el navegador!")

if __name__ == "__main__":
    main()
