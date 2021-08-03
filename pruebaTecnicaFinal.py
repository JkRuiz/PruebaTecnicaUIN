# Technical test for UIN developed by Juan Camilo Ruiz Puentes, where a string has to be received and validated if it is a palindrome word and if its length is a fibonacci number
import os
import math
import unidecode
import re

# Method to choose which methods wanna be tested, if option 1 is chosen only the Palindrome method is tested, if option 2 is chosen only the Fibonacci method, and with option 3 both methods are tested
# @return The option chosen by the user (among the three available)
# @Exception Error when the maximum number of attempts is reached (5) and none of the available options (1,2 or 3) was chosen
def chooseMethods():
    # Informative message of which options can be chosen
    print(
        "Por favor elija la opcion (1, 2 o 3) acorde a los metodos que desea probar: \n 1. Validar si una cadena de texto, sin caracteres especiales ni numeros, es Palindrome \n 2. Validar si el tamanio de una cadena de texto, sin caracteres especiales ni numeros, es un numero de Fibonacci \n 3. Ambos metodos"
    )
    # A While loop to iteratively try to get the user to enter a valid option, with a limit of 5 attempts
    attempts = 0
    while attempts < 5:
        userInput = input()
        # Validate that the user's input belongs to the defined options, if it does not belong, the input is requested again
        if userInput not in ["1", "2", "3"]:
            print(
                "La opcion que ha elegido no existe, por favor eliga una opcion valida"
            )
            attempts += 1
        else:
            return userInput
    raise Exception("Numero maximo de intentos para elegir una opcion superado")


# Method for the user to enter the string to test the previously chosen methods, it is additionally verified that the entered string is valid
# @return The string entered by the user
# @Exception Error when the maximum number of attempts (5) is reached and a valid string was not inserted
def receiveInput():
    # While Loop to iteratively try to get the user to enter a valid option, with a limit of 5 attempts
    attempts = 0
    while attempts < 5:
        # Indication to the user that he must enter a text string through the console
        print("Por favor ingrese una cadena de texto")
        # Verify that the user's input is a valid string, if not, a message is displayed with the error and the input is requested again
        userInput = input()
        try:
            validatedInput = validateInput(userInput)
            return validatedInput
        except Exception as e:
            print(e)
            attempts += 1
    raise Exception(
        "Numero maximo de intentos para ingresar una cadena valida superado"
    )


# Method to validate if the string is valid, if it has special characters or numbers an error is thrown
# @param word The string to be validated
# @return True if the string is valid, False otherwise
# @raise Exception If the string has any special character or number
def validateInput(word):
    # Regular expressions are used to define that only a string with letters, accents, periods, commas, question marks, exclamation marks and spaces is accepted (Elements that could have a sentence).
    reg = re.compile("^[a-zA-Zà-ÿÀ-Ÿ,.¡!¿? ]+$")
    if reg.match(word):
        return word
    else:
        # In case of having a different character to those defined, an exception is thrown communicating that the string has invalid characters
        raise Exception(
            "La cadena de texto posee caracteres especiales o numeros, por favor revise la cadena ingresada"
        )


# Method to validate if a string is Palindrome
# @param word The string to be evaluated as a Palindrome word
# @return True if the string is Palindrome, False otherwise
def isPalindrome(word):
    # A variable with the size of the chain and another with half the length since it's only necessary to compare up to half
    lengthWord = len(word)
    middleVal = math.ceil(lengthWord / 2)
    isPalindrome = True

    # Compare the first character with the last, the second with the penultimate, and so on until the middle of the word
    for i in range(0, middleVal):
        # If the values are equal, the comparison continues
        if word[i] == word[(lengthWord - 1) - i]:
            continue
        # If a value does not match, the loop is finished and the word is determined not to be palindrome
        else:
            isPalindrome = False
            break
    return isPalindrome


# Method to validate if a number is a Fibonacci number
# @param number The number to be evaluated as a Fibonacci number
# @return True if the number is a Fibonacci number, False otherwise
def isFibonacciNumber(number):
    # Define the first two numbers of the fibonacci series (fn and fn1) and a variable to save the next number in the sequence
    fn = 0
    fn1 = 1
    actualNumber = 0
    # The numbers of the fibonacci sequence are loop through until the searched number is found or a reached number of the series is greater than searched number, using always the same three variables
    while actualNumber < number:
        actualNumber = fn + fn1
        # In case the current number of the sequence is equal to the received number, True is returned (the number is from the Fibonacci sequence)
        if actualNumber == number:
            return True
        fn = fn1
        fn1 = actualNumber
    # In case of ending the cycle and not having found the number, False is returned (the number is NOT from the Fibonacci sequence)
    return False


# Method for, from the input entered by the user, call the isFibonacciNumber method to validate if the string length is a fibonacci number or not, and inform the user of this result
# @param input The string to be evaluated if its length is a fibonacci number
def validateFibonacciNumber(input):
    # Remove spaces from the length of the string, if desired, the other possible elements (commas, periods, question marks and exclamation marks) could also be removed.
    inputModify = input
    if " " in inputModify:
        inputModify = inputModify.replace(" ", "")
    # Save the length of the string
    inputLen = len(inputModify)
    # Validate if the length is a fibonacci number, and print the result
    print(
        'El tamanio de la cadena "'
        + input
        + '" ('
        + str(inputLen)
        + ") es un numero Fibonacci!"
    ) if isFibonacciNumber(inputLen) else print(
        'El tamanio de la cadena "'
        + input
        + '" ('
        + str(inputLen)
        + ") NO es un numero Fibonacci!"
    )


# Method to call the isPalinbdrome method from the input entered by the user to validate whether or not the string is a Palindrome word, and inform the user of this result
# @param input The string to be evaluated if its a Palindrome word
def validatePalindromeWord(input):
    # Normalize the string, removing spaces and characters other than letters, passing everything to a lower case and replacing the 'ñ' with '#' to differentiate it from the letter 'n'
    inputModify = unidecode.unidecode(input.lower().replace("ñ", "#"))
    for ch in [" ", ",", ".", "¡", "!", "¿", "?"]:
        if ch in inputModify:
            inputModify = inputModify.replace(ch, "")
    # Validate if the string is a Palindrome word, and the result is printed
    print('La cadena "' + input + '" es palindrome!') if isPalindrome(
        inputModify
    ) else print('La cadena "' + input + '" NO es palindrome!')


# Main method for testing the methods
def tech_test():
    try:
        # Ask the user to choose the methods that will be tested
        methods = int(chooseMethods())
        # Ask for the user's input
        input = receiveInput().strip()
        # According to the chosen methods, call the corresponding methods
        if methods == 1:
            validatePalindromeWord(input)
        elif methods == 2:
            validateFibonacciNumber(input)
        else:
            validatePalindromeWord(input)
            validateFibonacciNumber(input)
    except Exception as e:
        print(e)
        exit


if __name__ == "__main__":
    tech_test()

