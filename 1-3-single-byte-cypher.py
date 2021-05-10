import binascii


input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


def xor_hex_and_char(input_hex: str, guess_character_decimal: int) -> bytes:
    """XORs a hexadecimal numbers and a single character decimal number

    Args:
        input_hex (str): an input string in hexadecimal format
        guess_character_decimal (int): a single decimal value betwen 0 and 255 inclusive

    Returns:
        bytes: a bytestring
    """

    input_decimal = int(input_hex, 16)  # to base10

    # convert the guess character into a repeating fixed length string
    guess_character_hex = f"{guess_character_decimal:x}"  # to base16
    guess_hex = guess_character_hex.rjust(
        2, "0"
    )  # ensure it's two characters, e.g. `a` -> `0a`
    guess_hex = guess_hex * (len(input) // len(guess_hex))  # repeat until
    guess_decimal = int(guess_hex, 16)  # to base10

    result_decimal = guess_decimal ^ input_decimal  # XOR
    result_hex = f"{result_decimal:x}".rjust(len(input), "0")

    return binascii.unhexlify(result_hex), guess_character_hex


def filter_strings(possible_answers):
    """filters bytestrings for those that can be decoded into native strings"""
    sentences = []
    for (answer, key) in possible_answers:
        try:
            answer = answer.decode()
            sentences.append([answer, key])
        except UnicodeDecodeError:
            continue
    return sentences


def check_phrases(sentence):
    """checks if a sentence contains common phrases in the English language

    Returns:
        Boolean: True if it does, false if not
    """

    # A list of common phrases in the English language
    COMMON_PHRASES = [" a ", " of ", " an "]

    if any(phrase in sentence[0] for phrase in COMMON_PHRASES):
        return True
    return False


if __name__ == "__main__":
    # all the possible answers
    possible_answers = (xor_hex_and_char(input, number) for number in range(256))

    # filtered for answers that can be decoded into native strings
    filtered_answers = filter_strings(possible_answers)

    # filtered further for those that contain common English phrases
    final_answer = [answer for answer in filtered_answers if check_phrases(answer)]

    # print out the array containing the single final answer
    print(final_answer)