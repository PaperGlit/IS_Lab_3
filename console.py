from encode import encode
from decode import decode
from save_to_file import save
from is_valid_input import is_valid_input


def main():
    while True:
        prompt = input("1 - Encode text, 2 - Decode text\n"
                       "Your choice: ")
        match prompt:
            case "1":
                input_text = input("Enter the text to encode: ").upper()
                if not is_valid_input(input_text):
                    print("Wrong text format, please try again.")
                    continue
                text = encode(input_text)
                print(f"Encoded text - {text}")
                save_input = input("Would you like to save the input? (y/n): ").upper()
                if save_input in ["Y", "YES"]:
                    save(text)
            case "2":
                input_text = input("Enter the text to decode: ").upper()
                if not is_valid_input(input_text):
                    print("Wrong text format, please try again.")
                    continue
                text = decode(input_text)
                print(f"Decoded text: {text}")
                save_input = input("Would you like to save the input? (y/n): ").upper()
                if save_input in ["Y", "YES"]:
                    save(text)
            case _:
                break