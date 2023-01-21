from string import ascii_lowercase as alphabet

class Option:
    encode = "e"
    decode = "d"

alphabet = list(alphabet)
#print(f"alphabet: {alphabet}")

def get_offset(_sym: str, _key_offset: int, _option: str) -> str:
    alphabet_len  = len(alphabet)
    current_key_index = alphabet.index(_sym)
    #print(f"Current index: {current_key_index}")
    if _option == Option.encode:
        final_index = current_key_index + _key_offset
        if final_index > (alphabet_len - 1):
            final_index = final_index - alphabet_len
    elif _option == Option.decode:
        final_index = current_key_index - _key_offset
    else:
        raise NameError
    final_sym = alphabet[final_index]
    return final_sym
        

option = input('Enter e/d to encode/decode: ')
key = int(input('Enter your key: '))
word = input('Enter your input: ')
new_word = ""
for _sym in word:
    new_word += get_offset(_sym, key, option)
print(f"Final word: {new_word}")

