def huffman_decode (dictionary, text):
    res = ""
    while text:
        for k in dictionary.keys():
            if text.startswith(k):
                res += dictionary[k]
                text = text[len(k):]
    return res

def main():
    letters_cnt, _ = list(map(int, input().split(" ")))
    code = dict()
    for _ in range(letters_cnt):
        s, c = input().split(": ")
        code[c] = s
    encoded_text = input()
    print(huffman_decode(code, encoded_text))
    
if __name__ == "__main__":
    main()