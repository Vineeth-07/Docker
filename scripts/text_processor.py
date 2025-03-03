import os
import re
import socket
from collections import Counter

# Define file paths
data_path = "/home/data"
output_path = "/home/data/output/result.txt"

def count_words(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        text = file.read().lower()
        words = re.findall(r"\b\w+(?:'\w+)?\b", text)  # Handles contractions
        return words, Counter(words)

def get_top_words(counter, n=3):
    return counter.most_common(n)

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

def main():
    file1 = os.path.join(data_path, "IF-1.txt")
    file2 = os.path.join(data_path, "AlwaysRememberUsThisWay-1.txt")

    words1, counter1 = count_words(file1)
    words2, counter2 = count_words(file2)

    total_words1 = len(words1)
    total_words2 = len(words2)
    grand_total = total_words1 + total_words2

    top_words1 = get_top_words(counter1)
    top_words2 = get_top_words(counter2)

    ip_address = get_ip_address()

    output = f"""Word Count in IF-1.txt: {total_words1}
    Word Count in AlwaysRememberUsThisWay-1.txt: {total_words2}
    Grand Total Words: {grand_total}

    Top 3 Words in IF-1.txt:
    {top_words1}

    Top 3 Words in AlwaysRememberUsThisWay-1.txt (Handling Contractions):
    {top_words2}

    Container IP Address: {ip_address}
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(output)

    print(output)

if __name__ == "__main__":
    main()