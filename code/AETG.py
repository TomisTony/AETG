import sys
from itertools import pairwise

from Data import test_data
from utils import util

class AETG:
    def __init__(self, data, wise_num) -> None:
        self.data = data
        self.data_len_list = util.get_data_len_list(self.data,self.data)
        self.wise_num = wise_num

    def aetg(self):
        pass

if __name__ == "__main__":
    # if(len(sys.argv) < 3):
    #     print("Too less arguments! Give Command as follow:\npython AETG.py [2/3] [xc/jd]\n")
    # else:
    #     print(sys.argv[1],sys.argv[2])
    # a = pairwise([0,1,2,3,4,5,6])
    # print(a)

    data_len_list = test_data.get_data_len_list()
    print(util.calculate_all_pairs_num(data_len_list,2))
    # print(util.RECUR_get_pairs_from_subcombination(data_len_list,util.get_init_candidate_list(len(data_len_list)),(1,2)))
    print(util.get_sorted_uncovered_pairs_from_data_len_list(data_len_list,3))


    
        


