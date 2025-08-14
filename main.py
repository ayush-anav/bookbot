import sys
from stats import get_num_words, get_num_string, sort_text, print_res

if(len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
FILE_PATH = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

# total num words
total_words = get_num_words(get_book_text(FILE_PATH))

# gets all letter count
count_res = get_num_string(get_book_text(FILE_PATH))

# sort all letter count by reverse order, key = NUM
sorted_count = sort_text(count_res)

# prints the result
print_res(FILE_PATH, total_words, sorted_count)
