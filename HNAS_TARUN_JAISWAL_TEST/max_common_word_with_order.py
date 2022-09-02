from collections import Counter


# this code to complete took time 15 to 30 min

def top_word_based_on_order(file_path, topN):
    all_contents = []
    with open(file_path) as file_open:
        words = [word for line in file_open for word in line.split()]
        counter_dict = Counter(words)
        flg = False
        for word, count in counter_dict.most_common():
            if topN <= count:
                flg = True
                all_contents.append("Word name is :" + str(word) + " count is :" + str(count))
        if not flg:
            return "No most common word found"
        return all_contents
