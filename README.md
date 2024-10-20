# Number to Text Translator

This script translates a given number into its textual representation in English (or other languages) and then reads the result aloud using the `pyttsx3` library.

## Features

- Converts numbers (including decimal numbers) into English words.
- Handles both integer and decimal parts of a number.
- Pronounces the result aloud once the conversion is complete.
- The script can handle numbers up to billions.
- It supports up to three decimal places for more precise translations.

## Requirements

To run this script, you'll need the following Python libraries:

- `pyttsx3`: for text-to-speech functionality.
- `deep_translator`: for translation functionality

You can install the required libraries by running the following command:

```bash
pip install pyttsx3
pip install deep_translator
