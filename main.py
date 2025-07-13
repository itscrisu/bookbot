def get_book_text(filepath):
  with open(filepath) as file:
    return file.read()

def get_word_count(text):
  words = text.split()
  return len(words)

def main():
  text = get_book_text("books/frankenstein.txt")
  num_words = get_word_count(text)
  print(f"{num_words} words found in the document")

main()