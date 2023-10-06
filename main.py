text = input("Введіть текст: ")
sentences = text.split('.') or text.split('?') or text.split('!')
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
num_sentences = len(sentences)
print(f"Кількість речень у введеному тексті: {num_sentences}")
