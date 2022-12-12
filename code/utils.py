import itertools
import numpy as np
class util:

    @staticmethod
    def calculate_all_pairs_num(data_len_list, wise_num):
        sum = 0
        combinations = list(itertools.combinations(range(len(data_len_list)),wise_num))
        for combination in combinations:
            combination_list = []
            for para_index in combination:
                combination_list.append(data_len_list[para_index])
            sum += np.prod(combination_list)
        return sum
