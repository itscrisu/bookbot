def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_characters(char_counts):
  char_list = []

  for char, count in char_counts.items():
    if char.isalpha():
      char_list.append({"char": char, "num": count})
  

  char_list.sort(key=lambda item: item["num"], reverse=True)
  return char_list
