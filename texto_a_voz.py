import nltk #nltk es el Kit de Herramientas de Lenguaje Natural.
from newspaper import Article #newspaper es biblioteca que obtiene y analiza artículos de noticias.
from gtts import gTTS #gTTS: biblioteca de Google Text-to-Speech para convertir texto a voz.

# Descargar los datos necesarios para nltk
'''nltk. punkt se usa para la tokenización de oraciones, y punkt_tab se utiliza para 
ciertas configuraciones de tokenización.'''
nltk.download('punkt') # tokenización de oraciones
nltk.download('punkt_tab')# configuraciones de tokenización.

def convert_to_audio(url, output_file):
    # Obtener el artículo de la URL
    article = Article(url)
    article.download()#guarda el HTML de la página en atributo del objeto Article.
    article.parse()#analiza el contenido HTML descargado y extrae el texto del artículo.
    article.nlp() #nlp() aplica técnicas de Procesamiento de Lenguaje Natural 
    # al artículo, como la obtención de resumen y palabras clave.

    # Obtener el texto del artículo
    text = article.text

    # Imprimir el texto del artículo
    print(text)

    # Convertir el texto a voz
    try:
    #En esta parte, utilizamos gTTS para convertir el texto del artículo a voz.
        tts = gTTS(text=text, lang='es')
        tts.save(output_file)# Guardamos el archivo en output_file.
        print(f"El archivo de audio ha sido guardado como {output_file}")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo de audio: {e}")

if __name__ == "__main__":
    url = input("Introduce la URL del artículo: ")
    output_file = "articulo.mp3"
    convert_to_audio(url, output_file)
