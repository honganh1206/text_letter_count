
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import string

def main():
    word_dict = read_data()
    create_bar_plot(word_dict)

def read_data():
    word_dict = {}
    file = Path('automateboringstuff\The Picture of Dorian Gray.txt').read_text(encoding="utf8")
    for char in file:                                   # counting each letter in the text
        word_dict.setdefault(char, 0) 
        word_dict[char] += 1                               # word_dict become a DICT here
    return word_dict

def create_bar_plot(count_num):                             # param is a dict

    alphabet_list = list(string.ascii_lowercase)            # _letters for both uppercase and lowercase
    filtered_dict = {}

    for key, value in sorted(count_num.items()):            # need .items() for 2 VARS (keys:values) + keyword SORTED
        if key in alphabet_list:
            filtered_dict[key] = value

    counts = []                             # take the numbers of times each letter appears and add them to a list
    for letter in filtered_dict:
        counts.append(filtered_dict[letter])
    

    data = {
        'x':list(filtered_dict.keys()),
        'y':counts
    }
    sns.barplot(x = 'x',y = 'y', data= data)
    plt.savefig("word_count.png")


if __name__ == '__main__':
    main()
