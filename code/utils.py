import itertools
import numpy as np
import random


class util:

    @staticmethod
    def calculate_total_pairs_count(data_len_list: list, wise_num: int) -> int:
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
            result = result.union(
                util.__get_pairs_in_data_len_list_from_combination(data_len_list, combination))
        return sorted(result)

    @staticmethod
    def __get_pairs_in_data_len_list_from_combination(data_len_list: list, combination: tuple) -> set[tuple]:
        init_choosed_element_list = util.get_list_of_negative1(
            len(data_len_list))
        return util.__RECUR_get_pairs_in_data_len_list_from_subcombination(
            data_len_list,
            init_choosed_element_list,
            combination)

    '''
    return the [-1,-1,...] , which length = list_len
    '''
    @staticmethod
    def get_list_of_negative1(list_len) -> list:
        result = []
        for i in range(list_len):
            result.append(-1)
        return result

    '''
    Recursive function.
    Update the choosed_element_list based on the first element in `subcombination`.
    '''
    @staticmethod
    def __RECUR_get_pairs_in_data_len_list_from_subcombination(
        data_len_list: list,
        choosed_element_list: list,
        subcombination: tuple
    ) -> set[tuple]:
        result = set()
        choosed_element_index = subcombination[0] - 1
        choosed_element_num = data_len_list[choosed_element_index]

        for i in range(choosed_element_num):
            choosed_element_list_impl = choosed_element_list.copy()
            choosed_element_list_impl[choosed_element_index] = i

            if (len(subcombination) == 1):
                choosed_element_tuple = tuple(choosed_element_list_impl)
                result.add(choosed_element_tuple)
            else:
                result = result.union(
                    util.__RECUR_get_pairs_in_data_len_list_from_subcombination(
                        data_len_list,
                        choosed_element_list_impl,
                        subcombination[1:]))

        return sorted(result)

    '''
    candidate: list of choosed index of each catagory
    '''
    @staticmethod
    def get_covered_pairs_count_of_candidate(
        uncovered_pairs: set[tuple],
        candidate: tuple,
    ) -> int:
        return len(util.get_covered_pairs_of_candidate(uncovered_pairs, candidate))

    @staticmethod
    def get_covered_pairs_of_candidate(
        uncovered_pairs: set[tuple],
        candidate: tuple,
    ) -> list[tuple]:
        # wise_num equals the length of first element in uncovered_pairs
        wise_num = util.__get_wise_num_from_uncovered_pairs(uncovered_pairs)
        covered_pairs = []
        combinations = list(itertools.combinations(
            range(len(candidate)), wise_num))
        init_test_case = util.get_list_of_negative1(len(candidate))
        for combination in combinations:
            test_case = init_test_case.copy()
            for index in combination:
                test_case[index] = candidate[index]
            if tuple(test_case) in uncovered_pairs:
                covered_pairs.append(tuple(test_case))
        return covered_pairs

    @staticmethod
    def __get_wise_num_from_uncovered_pairs(uncovered_pairs : list[tuple]):
        pair = uncovered_pairs[0]
        wise_num = 0
        for i in range(len(pair)):
            if pair[i] != -1 : wise_num += 1
        return wise_num

    '''
    Return the element
    '''
    @staticmethod
    def randomly_choose_one_element_from_list(data_list: list) -> int:
        return random.choice(data_list)

    '''
    We make a matrix of uncovered_pairs. Each element(not -1) in 
    incomplete_candidate will have the chance to find the matcher
    in its corresponding column. And finally the sum is the overlapping
    num of matchers.
    '''
    @staticmethod
    def get_contained_count_of_incomplete_candidate(
        incomplete_candidate: list[int],
        uncovered_pairs: list[tuple]
    ) -> int:
        matrix = np.array(uncovered_pairs)
        candidate_length = len(incomplete_candidate)
        matching_list = []
        for i in range(candidate_length):
            if incomplete_candidate[i] != -1:
                colomn_i = matrix[:,i]
                # matching_list is the list of matched row index list 
                # of each element in incomplete_candidate(except -1)
                matching_list.append(np.where(colomn_i == incomplete_candidate[i]))
        sum = 0
        # why use [0][0], you can check the matching_list format in debugger
        first_match = matching_list[0][0].tolist()
        for i in range(len(first_match)):
            match_count = 0
            for matcher in matching_list:
                if first_match[i] in matcher[0].tolist(): match_count += 1
            # if we find a row appears in every matcher, then
            # we find one uncovered_pair contain the incomplete_candidate
            if match_count == len(matching_list): sum += 1
        return sum

    
    '''
    Use combination to break up the incomplete_candidate to pairs(in format [-1,-1,2,3,4,-1,...])
    Return the sum of contained count of pairs.
    '''
    @staticmethod
    def get_covered_count_of_incomplete_candidate(
        incomplete_candidate: list[int],
        uncovered_pairs: list[tuple]
    ) -> int:
        # wise_num equals the length of first element in uncovered_pairs
        wise_num = util.__get_wise_num_from_uncovered_pairs(uncovered_pairs)
        choosed_catagory_list: list = []
        for i in range(len(incomplete_candidate)):
            if incomplete_candidate[i] != -1:
                choosed_catagory_list.append(i)
        combinations = list(itertools.combinations(
            range(len(choosed_catagory_list)), wise_num))
        
        sum = 0
        for combination in combinations:
            choosed_pair = util.__get_choosed_pair_from_combination(
                combination, choosed_catagory_list, incomplete_candidate)
            sum += util.get_contained_count_of_incomplete_candidate(choosed_pair,uncovered_pairs)
        return sum

    '''
    Based on combination and choosed_catagory_list, return the choosed pair.
    Combination means the combination in choosed_catagory_list.
    We need read the it through the element in combination to know which
    catagory is used to make up pair.
    '''
    @staticmethod
    def __get_choosed_pair_from_combination(
        combination: list[int],
        choosed_catagory_list: list[int],
        candidate: list[int],
    ) -> list[int]:
        choosed_pair_catagory_list = []
        for i in combination:
            choosed_pair_catagory_list.append(choosed_catagory_list[i])

        result = []
        for i in range(len(candidate)):
            result.append(
                candidate[i] if i in choosed_pair_catagory_list else -1
            )
        return result
