import nltk
from newspaper import Article
from gtts import gTTS

# Descargar los datos necesarios para nltk
nltk.download('punkt')
nltk.download('punkt_tab')

def convert_article_to_audio(url, output_file):
    # Obtener el artículo de la URL
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    # Obtener el texto del artículo
    text = article.text

    # Imprimir el texto del artículo
    print(text)

    # Convertir el texto a voz
    try:
        tts = gTTS(text=text, lang='es')
        tts.save(output_file)
        print(f"El archivo de audio ha sido guardado como {output_file}")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo de audio: {e}")

if __name__ == "__main__":
    url = input("Introduce la URL del artículo: ")
    output_file = "articulo.mp3"
    convert_article_to_audio(url, output_file)
