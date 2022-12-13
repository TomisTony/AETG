import sys
from itertools import pairwise

from Data import Data, test_data
from utils import util


class AETG:
    def __init__(self, data: Data, wise_num: int) -> None:
        self.data: Data = data
        self.data_len_list: list[int] = data.get_data_len_list()
        self.catagory_num = data.catagory_num
        self.wise_num = wise_num
        self.uncovered_pairs: set[tuple] = util.get_sorted_uncovered_pairs_from_data_len_list(
            self.data_len_list, self.wise_num)
        self.total_pairs_count = util.calculate_total_pairs_count(self.data_len_list,self.wise_num)
        self.test_times = 20  # The number of test times for find a better candicate
        self.result: list[tuple] = []

    def aetg(self) -> list[list]:
        while len(self.uncovered_pairs) > 0:
            candidates: list[tuple] = self.__randomly_generate_candidates()
            test_case:tuple = self.__choose_better_candidate(candidates)
            self.result.append(test_case)
        return self.result

    def __randomly_generate_candidates(self) -> list[tuple]:
        candidates: list[tuple] = []
        for i in range(self.test_times):
            candidate: list[int] = []
            # choose first catagory
            catagory, index = self.__find_most_frequent_catagory_and_para()
            candidate[catagory] = index

            candidate = self.__choose_other_catagories(candidate)
            candidates.append(tuple(candidate))
        return candidates

    def __choose_better_candidate(self, candidates: list[tuple]) -> tuple:
        pass

    '''
    Return the value of catagory and its specific index.
    First return value is catagory's index.
    Second is its specific index.
    '''
    def __find_most_frequent_catagory_and_para(self) -> tuple[int, int]:
        pass

    '''
    After we choose our first catagory, we will choose other catagories.
    Return: a complete candidate
    '''
    def __choose_other_catagories(self, candidate) -> list[int]:
        pass

    

if __name__ == "__main__":
    data_len_list = test_data.get_data_len_list()
    print(util.calculate_total_pairs_count(data_len_list, 2))
    # print(util.RECUR_get_pairs_from_subcombination(data_len_list,util.get_init_candidate_list(len(data_len_list)),(1,2)))
    print(util.get_sorted_uncovered_pairs_from_data_len_list(data_len_list, 3))
