import os
from os import listdir 
from os.path import join
RANDOM_STATE = 2020
absolut_path="/workspace/Zindi/TIC-HEAP/"
raw_data_path=join(absolut_path,"data/raw_data")
proc_data_path=join(absolut_path,"data/proc_data")
other_data_path=join(absolut_path,"data/other")
sub_path=join(absolut_path,"outputs/sub")
oof_train_path=join(absolut_path,"outputs/oof/train")
oof_test_path=join(absolut_path,"outputs/oof/test")
expirment_path=join(absolut_path,"outputs/experiments.csv")
tem_data_path=join(absolut_path,"data/tmp_data")
