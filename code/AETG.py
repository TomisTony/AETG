from Data import Data, test_data, jd_data, xc_data
from utils import util
import numpy as np


class AETG:

    def __init__(self, data: Data, wise_num: int) -> None:
        self.data: Data = data
        self.data_len_list: list[int] = self.data.get_data_len_list()
        self.catagory_num = self.data.catagory_num
        self.catagory_names: list[str] = self.data.catagory
        self.wise_num = wise_num
        self.uncovered_pairs: set[
            tuple] = util.get_sorted_uncovered_pairs_from_data_len_list(
                self.data_len_list, self.wise_num)
        self.total_pairs_count = util.calculate_total_pairs_count(
            self.data_len_list, self.wise_num)
        self.test_times_min = 5  # The number of test times for find a better candicate
        self.test_times_max = 100
        self.result: list[tuple] = []
        self.readable_data: list[list[str]] = []

    def get_csv_result(self,csv_save_path: str) -> None:
        self.__aetg()
        self.__aetg_result_to_readable_data()
        self.__print_data_to_csv(csv_save_path)

    def __aetg(self) -> list[tuple]:
        while len(self.uncovered_pairs) > 0:
            print("new turn begin! len(ucps)=",len(self.uncovered_pairs))
            candidates: list[tuple] = self.__randomly_generate_candidates()
            better_candidate: tuple = self.__choose_better_candidate(
                candidates)
            self.__update_uncovered_pairs(better_candidate)
            self.result.append(better_candidate)
        return self.result

    def __aetg_result_to_readable_data(self) -> None:
        for candidate in self.result:
            readable_candidate: list[str] = []
            for i in range(len(candidate)):
                catagory_name = self.catagory_names[i]
                if catagory_name in self.data.detail:
                    catagory_datas = self.data.detail[catagory_name]
                    readable_candidate.append(catagory_datas[candidate[i]])
            self.readable_data.append(readable_candidate)

    def __print_data_to_csv(self, csv_save_path: str) -> None:
        import csv
        with open(csv_save_path, 'w', newline='') as f:
            write = csv.writer(f, dialect=('excel'))
            write.writerow(self.catagory_names)
            write.writerows(self.readable_data)

    def __randomly_generate_candidates(self) -> list[tuple]:
        candidates: list[tuple] = []
        # each loop, we will have the same first catagory
        catagory, index = self.__find_most_frequent_catagory_and_para()
        test_times = self.__get_test_time()
        for i in range(test_times):
            candidate: list[int] = util.get_list_of_negative1(
                self.catagory_num)
            # fill in the first catagory
            candidate[catagory] = index

            candidate = self.__choose_other_catagories(candidate)
            candidates.append(tuple(candidate))
        return candidates

    '''
    Change the test_time dynamically
    '''
    def __get_test_time(self) -> int:
        uncovered_pairs_len = len(self.uncovered_pairs)
        percent = uncovered_pairs_len / self.total_pairs_count
        diff = self.test_times_max - self.test_times_min
        return int(self.test_times_max - diff * percent)

    '''
    Choose the candidate with most covered pairs in self.uncovered_pairs
    '''

    def __choose_better_candidate(self, candidates: list[tuple]) -> tuple:
        max_index = 0
        max_coverd_count = util.get_covered_pairs_count_of_candidate(
            self.uncovered_pairs, candidates[0])
        for i in range(1, len(candidates)):
            covered_count = util.get_covered_pairs_count_of_candidate(
                self.uncovered_pairs, candidates[i])
            if covered_count > max_coverd_count:
                max_coverd_count = covered_count
                max_index = i
        return candidates[max_index]

    def __update_uncovered_pairs(self, candidate: tuple) -> None:
        new_covered_pairs: list[tuple] = util.get_covered_pairs_of_candidate(
            self.uncovered_pairs, candidate)
        for pair in new_covered_pairs:
            self.uncovered_pairs.remove(pair)

    '''
    Return the value of catagory and its specific index.
    First return is catagory's index.
    Second is its specific index.
    '''

    def __find_most_frequent_catagory_and_para(self) -> tuple[int, int]:
        matrix = np.array(self.uncovered_pairs)
        most_frequent_index_of_each_catagory: list = []
        appear_times_of_each_most_frequent_index: list = []
        # get the statistics of each catagory
        for i in range(len(self.data_len_list)):
            # get the list of each index appear in the uncovered_pairs
            appear_list = matrix[:, i].tolist()
            while -1 in appear_list:
                appear_list.remove(-1)
            if len(appear_list) == 0:  # in case no element remain
                # these two list need to append too to keep the order
                most_frequent_index_of_each_catagory.append(-1)
                appear_times_of_each_most_frequent_index.append(0)
                continue
            # get the appear count of each index except -1 in one catagory
            appear_count = np.bincount(appear_list)
            max_arg = np.argmax(appear_count)
            most_frequent_index_of_each_catagory.append(max_arg)
            appear_times_of_each_most_frequent_index.append(
                appear_count[max_arg])
        # find the result we need
        most_frequent = np.argmax(appear_times_of_each_most_frequent_index)
        return most_frequent, most_frequent_index_of_each_catagory[most_frequent]

    '''
    After we choose our first catagory, we will choose other catagories.
    Return: a complete candidate
    '''

    def __choose_other_catagories(self, candidate: list[int]) -> list[int]:
        # do not change the get-in arg, make its copy
        result: list[int] = candidate.copy()
        not_selected_catagory: list = self.__get_not_selected_catagory_from_candidate(
            candidate)
        while len(not_selected_catagory) > 0:
            random_choosed_catagory: int = util.randomly_choose_one_element_from_list(
                not_selected_catagory)
            # update not_selected_catagory
            not_selected_catagory.remove(random_choosed_catagory)
            choosed_catagory_count = self.catagory_num - \
                len(not_selected_catagory)
            choosed_index = self.__get_choosed_index_after_first_element(
                choosed_catagory_count, random_choosed_catagory, result)
            result[random_choosed_catagory] = choosed_index

        return result

    def __get_not_selected_catagory_from_candidate(self, candidate: tuple) -> list:
        result = []
        for i in range(self.catagory_num):
            if candidate[i] == -1:
                result.append(i)
        return result

    def __get_choosed_index_after_first_element(
        self,
        choosed_catagory_count: int,
        random_choosed_catagory: int,
        now_candidate: list[int]
    ) -> int:

        count: list[int] = []
        for choosed_index in range(self.data_len_list[random_choosed_catagory]):
            new_candidate = now_candidate.copy()
            new_candidate[random_choosed_catagory] = choosed_index
            if choosed_catagory_count <= self.wise_num:
                choosed_index_count = util.get_contained_count_of_incomplete_candidate(
                    new_candidate, self.uncovered_pairs)
            else:
                choosed_index_count = util.get_covered_count_of_incomplete_candidate(
                    new_candidate, self.uncovered_pairs)
            count.append(choosed_index_count)
        return np.argmax(count)


if __name__ == "__main__":
    # test = AETG(jd_data, 2)
    # print(test.data_len_list)
    # test.get_csv_result('./jd_2pairwise.csv')

    # test1 = AETG(jd_data, 3)
    # print(test1.data_len_list)
    # test1.get_csv_result('./jd_3pairwise.csv')

    # test2 = AETG(xc_data, 2)
    # print(test2.data_len_list)
    # test2.get_csv_result('./xc_2pairwise.csv')

    test3 = AETG(xc_data, 3)
    print(test3.data_len_list)
    test3.get_csv_result('./xc_3pairwise.csv')