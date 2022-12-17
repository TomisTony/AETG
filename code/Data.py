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
            "cata1": [1, 2, 3],
            "cata2": [4, 5, 6, 7],
            "cata3": [8, 9]
        }


class JD_Data(Data):
    def __init__(self) -> None:
        super().__init__()
        self.catagory = ["品牌", "能效等级", "支持IPv6", "类型",
                         "处理器", "固态硬盘", "内存容量", "屏幕刷新率"]
        self.catagory_num = len(self.catagory)
        self.detail = {
            "品牌": ["hp", "lenovo", "huawei", "dell", "ASUS", "ThinkPad", "Apple"],
            "能效等级": ["一级能效", "二级能效", "三级能效", "五级能效"],
            "支持IPv6": ["支持IPv6", "不支持IPv6"],
            "类型": ["轻薄本", "游戏本", "高端轻薄本", "高端游戏本", "移动工作站"],
            "处理器": ["麒麟", "AMD", "intel i5", "intel i7", "intel i9"],
            "固态硬盘": ["128G", "512G", "1T", "2T", "4T"],
            "内存容量": ["4G", "6G", "8G", "16G", "32G", "64G", "128G"],
            "屏幕刷新率": ["60Hz", "90Hz", "120Hz", "144Hz", "240Hz"],
        }


class XC_Data(Data):
    def __init__(self) -> None:
        super().__init__()
        self.catagory = ["出行", "出发地", "目的地", "出发日期", "仅看直飞", "舱类型", "乘客人数"]
        self.catagory_num = len(self.catagory)
        self.detail = {
            "出行": ["单程", "往返", "多程"],
            "出发地": ["北京", "上海", "广州", "深圳", "成都", "杭州", "武汉", "西安", "重庆"],
            "目的地": ['中国','香港','首尔','中国','台北','东京','新加坡','中国澳门','曼谷','大阪','胡志明市'],
            "出发日期": ["1号","2号","3号","4号","5号","6号","7号",],
            "仅看直飞": ["true", "false"],
            "舱类型": ['经济/超经舱','公务/头等舱','公务舱','头等舱'],
            "乘客人数": ["1人","2人","3人","4人","5人",],
        }


jd_data = JD_Data()
test_data = Test_Data()
xc_data = XC_Data()
