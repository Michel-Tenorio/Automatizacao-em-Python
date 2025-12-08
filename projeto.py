import PyPDF2
import os

merger = PyPDF2.PdfMerger()


lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

for arquivos in lista_arquivos:
    if ".pdf" in arquivos:
        merger.append(f"arquivos/{arquivos}")
                      
merger.write("PDF final.pdf")