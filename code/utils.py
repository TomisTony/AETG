import itertools
import numpy as np


class util:

    @staticmethod
    def calculate_all_pairs_num(data_len_list: list, wise_num: int) -> int:
        sum = 0
        combinations = list(itertools.combinations(
            range(len(data_len_list)), wise_num))
        for combination in combinations:
            combination_list = []
            for para_index in combination:
                combination_list.append(data_len_list[para_index])
            sum += np.prod(combination_list)
        return sum

    @staticmethod
    def get_sorted_uncovered_pairs_from_data_len_list(data_len_list: list, wise_num: int) -> set[tuple]:
        combinations = list(itertools.combinations(
            range(len(data_len_list)), wise_num))
        result = set()
        for combination in combinations:
            result = result.union(util.get_pairs_from_combination(data_len_list,combination))
        return sorted(result)

    @staticmethod
    def get_pairs_from_combination(data_len_list: list, combination: tuple) -> set[tuple]:
        init_candidate_list = util.get_init_candidate_list(len(data_len_list))
        return util.RECUR_get_pairs_from_subcombination(data_len_list, init_candidate_list, combination)

    '''
    return the [-1,-1,...] , which length = list_len
    '''
    @staticmethod
    def get_init_candidate_list(list_len) -> list:
        result = []
        for i in range(list_len):
            result.append(-1)
        return result

    @staticmethod
    def RECUR_get_pairs_from_subcombination(data_len_list: list, candidate_list: list, subcombination: tuple) -> set[tuple]:
        result = set()
        candidate_index = subcombination[0] - 1
        candidate_num = data_len_list[candidate_index]

        for i in range(candidate_num):
            candidate_list_impl = candidate_list.copy()
            candidate_list_impl[candidate_index] = i

            if (len(subcombination) == 1):
                candidate_tuple = tuple(candidate_list_impl)
                result.add(candidate_tuple)
            else:
                result = result.union(util.RECUR_get_pairs_from_subcombination(
                    data_len_list, candidate_list_impl, subcombination[1:]))

        return sorted(result)
