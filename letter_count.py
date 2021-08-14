
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import string

def main():
    word_dict = read_data()
    create_bar_plot(word_dict)

def read_data():
    word_dict = {}
    file = Path('filename.txt').read_text(encoding="utf8")
    for char in file:                                  
        word_dict.setdefault(char, 0) 
        word_dict[char] += 1                               
    return word_dict

def create_bar_plot(count_num):                             

    alphabet_list = list(string.ascii_lowercase)            # _letters for both uppercase and lowercase
    filtered_dict = {}

    for key, value in sorted(count_num.items()):            
        if key in alphabet_list:
            filtered_dict[key] = value
            
    # count letters
    counts = []                           
    for letter in filtered_dict:
        counts.append(filtered_dict[letter])
        
    # visualize data
    data = {
        'x':list(filtered_dict.keys()),
        'y':counts
    }
    sns.barplot(x = 'x',y = 'y', data= data)
    plt.savefig("word_count.png")


if __name__ == '__main__':
    main()
