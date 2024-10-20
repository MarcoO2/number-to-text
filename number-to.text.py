# pip3 install deep_translator
# pip3 install pyttsx3
# if the script doesn't speak on Linux type in terminal: sudo apt update && sudo apt install espeak ffmpeg libespeak1
# Library to translate the text in output
from deep_translator import GoogleTranslator
import pyttsx3

rounds = {
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety"
}

numbers = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

specials = {
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty"
}

def modify(n):
    if ',' in n :
        n = n.replace(',' , '.')
    n = float(n)
    n = round(n, 3)  # Change ,3 to add or reduce numbers after .
    return n

def convert(n):
    a = ' '

    if n == 0:
        return numbers[0]

    outputText = []

    # If the number is negative, add minus to output and make it positive
    if n < 0:
        outputText.append("Minus")
        n = abs(n)

    if(".0" in str(n)):  # To verify that the number is Integer
        n = int(n)

    # Split integer part to decimal part
    if '.' in str(n):
        integer_part, decimal_part = str(n).split('.')
        integer_part = int(integer_part)
        outputText.append(integer_conversion(integer_part))
        outputText.append("Point")
        decimal_part = int(decimal_part)
        outputText.append(integer_conversion(decimal_part))
    else:
        outputText.append(integer_conversion(int(n)))

    return a.join(outputText)

def integer_conversion(n):
    outputText = []

    while n > 0:
        if n >= 1000000000:
            billion = n // 1000000000
            outputText.append(integer_conversion(billion))
            outputText.append("Billion")
            n %= 1000000000
        elif n >= 1000000:
            million = n // 1000000
            outputText.append(integer_conversion(million))
            outputText.append("Million")
            n %= 1000000
        elif n >= 1000:
            thousand = n // 1000
            outputText.append(integer_conversion(thousand))
            outputText.append("Thousand")
            n %= 1000
        elif n >= 100:
            hundred = n // 100
            outputText.append(integer_conversion(hundred))
            outputText.append("Hundred")
            n %= 100
        elif n >= 20:
            tens = (n // 10) * 10
            outputText.append(rounds[tens])
            n %= 10
        elif n >= 10:
            outputText.append(specials[n])
            n = 0
        else:
            outputText.append(numbers[n])
            n = 0

    return ' '.join(outputText)

def main():
    print(" Insert value: ")
    val = input(" ")
    val = modify(val)
    print(" Insert language (it, de, en ...): ")
    lan = input(" ")

    conversion = convert(val)
    translated = GoogleTranslator(source='auto', target=lan).translate(conversion)
    print(" " + translated)
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)  # Change to 0 for male voice
    engine.say(translated)
    engine.runAndWait()

if __name__ == "__main__":
        main()
