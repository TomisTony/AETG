class Data:
    def __init__(self) -> None:
        self.catagory = list()
        self.catagory_num = 0
        self.detail = dict()
        pass

    '''
    data_len_list: A list save each catagory's length of data
    Such as data_len_list=[1,2,3] means catagory[0] has 1 element, catagory[1] has 2 elements,
    catagory[3] has 3 elements.
    '''
    def get_data_len_list(self):
        data_len_list = []
        for key in self.catagory:
            data_len_list.append(len(self.detail[key]))
        return data_len_list
    

class Test_Data(Data):
    def __init__(self) -> None:
        super().__init__
        self.catagory = ["cata1", "cata2", "cata3"]
        self.catagory_num = len(self.catagory)
        self.detail = {
            "cata1" : [1,2,3],
            "cata2" : [4,5,6,7],
            "cata3" : [8,9]
        }

class JD_Data(Data):
    def __init__(self) -> None:
        super().__init__()
        self.catagory = ["品牌", "能效等级", "支持IPv6", "类型", "处理器", "固态硬盘", "内存容量", "屏幕刷新率", "厚度", "机身材质"]
        self.catagory_num = len(self.catagory)
        self.detail = {
            "品牌" : ["hp", "lenovo", "huawei", "dell" ,"ASUS", "ThinkPad", "Apple","MI","honor"],
            "能效等级":["一级能效","二级能效","三级能效","五级能效"],
            "支持IPv6":["支持IPv6", "不支持IPv6"], 
            "类型" : ["轻薄本", "游戏本", "高端轻薄本", "高端游戏本", "移动工作站"], 
            "处理器" : ["麒麟", "AMD", "intel i5", "intel i7", "intel i9"], 
            "固态硬盘" : ["128G", "512G", "1T", "2T", "4T"], 
            "内存容量" : ["4G", "6G", "8G", "16G", "32G", "64G", "128G"], 
            "屏幕刷新率" : ["60Hz", "90Hz", "120Hz", "144Hz", "240Hz"],
            "厚度": ["15.0mm及以下","15.1-18.0mm","18.1-20.0mm","20.0mm以上"],
            "机身材质": ["金属","金属+复合材质","复合材质","含碳纤维"]

        }
        
 
jd_data = JD_Data()
test_data = Test_Data()