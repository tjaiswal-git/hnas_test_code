import max_common_word_with_order as max_common


def get_max_common_word():
    total_word_list = max_common.top_word_based_on_order('data.txt', 10)
    print(total_word_list)


def get_no_common_word_based_on_max_range():
    total_word_list = max_common.top_word_based_on_order('data.txt', 25)
    print(total_word_list)


if __name__ == "__main__":
    get_max_common_word()
    get_no_common_word_based_on_max_range()
