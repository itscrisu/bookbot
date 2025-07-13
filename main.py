import sys

from stats import get_num_words, count_characters, sort_characters

def get_book_text(filepath):
  with open(filepath) as file:
    return file.read()

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  path = sys.argv[1]
  text = get_book_text(path)

  word_count = get_num_words(text)
  char_counts = count_characters(text)
  sorted_characters = sort_characters(char_counts)

# ============ BOOKBOT ============
# Analyzing book found at books/frankenstein.txt...
# ----------- Word Count ----------
# Found 75767 total words
# --------- Character Count -------
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for char in sorted_characters:
    print(f"{char['char']}: {char['num']}")
  print("============ END ============")

main()