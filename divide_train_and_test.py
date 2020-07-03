from sklearn.model_selection import train_test_split
import os


class divide_dataset():
    def __init__(self,datapath):
        self.datapath = datapath

    def divide_data(self,train_list,test_list,filepath,i):
        all_dirs = os.listdir(filepath)
        train_datas,test_datas = train_test_split(all_dirs,test_size=0.25,random_state=0)
        train_datas = [path+" "+str(i) for path in train_datas]
        test_datas = [path+" "+str(i) for path in test_datas]
        train_list.extend(train_datas)
        test_list.extend(test_datas)


        # 调用这个方法就可以
    def read_images_path(self):
        train_list = []
        test_list = []
        i = 0
        for dir in os.listdir(self.datapath):
            self.divide_data(train_list, test_list, os.path.join(datapath, dir), i)
            i += 1
        return train_list, test_list


if __name__ == '__main__':
    datapath = 'D:\DataSets\HMDB51'
    divide = divide_dataset(datapath)
    train_list,test_list = divide.read_images_path()
    print(len(train_list))
    print(len(test_list))
