def get_num_words(file_string):
    num_words = len(file_string.split())
    return num_words

def get_num_string(file_string):
    text_count = {}
    for words in file_string.lower().split():
        for text in words:
            if text in text_count:
                text_count[text] += 1
            else: 
                text_count[text] = 1
    return text_count


def sort_by(items):
    return items["num"]

def sort_text(text_count):
    sorted_count = []
    
    # creates new list of dict with char and num for sorting
    for key,value in text_count.items():
        sorted_count.append({"char":key, "num":value}) 
    
    # sorts it here
    sorted_count.sort(reverse=True, key=sort_by)
    
    return sorted_count


def print_res(FILE_PATH, total_words, sorted_count):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {FILE_PATH}...\n----------- Word Count ----------\nFound {total_words} total words\n--------- Character Count -------")
    for i in range(0, len(sorted_count)):
        print(f"{sorted_count[i]['char']}: {sorted_count[i]['num']}")