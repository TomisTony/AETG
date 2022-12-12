class Data:
    def __init__(self) -> None:
        self.catagory = list()
        self.catagory_num = 0
        self.data = dict()
        pass

    '''
    data_len_list: A list save each catagory's length of data
    Such as data_len_list=[1,2,3] means catagory[0] has 1 element, catagory[1] has 2 elements,
    catagory[3] has 3 elements.
    '''
    def get_data_len_list(self):
        data_len_list = []
        for key in self.catagory:
            data_len_list.append(len(self.data[key]))
        return data_len_list
    

class Test_Data(Data):
    def __init__(self) -> None:
        super()
        self.catagory = ["cata1", "cata2", "cata3"]
        self.catagory_num = len(self.catagory)
        self.data = {
            "cata1" : [1,2,3],
            "cata2" : [4,5,6,7],
            "cata3" : [8,9]
        }
 

test_data = Test_Data()