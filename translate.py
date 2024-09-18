from googletrans import Translator

def translate_phrase(phrase):
    """Translates a given phrase into Spanish, Japanese, Latin, and Italian."""
    translator = Translator()

    # Define the target languages (language codes)
    languages = {
        'Spanish': 'es',
        'Japanese': 'ja',
        'Latin': 'la',
        'Italian': 'it'
    }

    translations = {}

    # Perform translation for each language
    for language, code in languages.items():
        try:
            translated = translator.translate(phrase, dest=code)
            translations[language] = translated.text
        except Exception as e:
            translations[language] = f"Error: {str(e)}"

    return translations

def main():
    """Main function to handle CLI input and output the translations."""
    import argparse

    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="QUALIA: A multilingual translation tool.")
    parser.add_argument('phrase', type=str, help="The phrase you want to translate.")

    args = parser.parse_args()
    phrase = args.phrase

    # Get the translations
    translations = translate_phrase(phrase)

    # Output the translations
    print("\nTranslations:")
    for language, translation in translations.items():
        print(f"{language}: {translation}")

if __name__ == "__main__":
    main()
