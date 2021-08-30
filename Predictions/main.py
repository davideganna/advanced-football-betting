#     /\      | |                             | | |  ____|        | | | |         | | | |  _ \     | | | | (_)            
#    /  \   __| |_   ____ _ _ __   ___ ___  __| | | |__ ___   ___ | |_| |__   __ _| | | | |_) | ___| |_| |_ _ _ __   __ _ 
#   / /\ \ / _` \ \ / / _` | '_ \ / __/ _ \/ _` | |  __/ _ \ / _ \| __| '_ \ / _` | | | |  _ < / _ \ __| __| | '_ \ / _` |
#  / ____ \ (_| |\ V / (_| | | | | (_|  __/ (_| | | | | (_) | (_) | |_| |_) | (_| | | | | |_) |  __/ |_| |_| | | | | (_| |
# /_/    \_\__,_| \_/ \__,_|_| |_|\___\___|\__,_| |_|  \___/ \___/ \__|_.__/ \__,_|_|_| |____/ \___|\__|\__|_|_| |_|\__, |
#                                                                                                                    __/ |
#                                                                                                                   |___/ 

import pandas as pd
import mav_dataset
import DictsAndLists as DAL

# Options
pd.set_option('display.max_rows', 500)
pd.options.mode.chained_assignment = None  # default='warn'

# View most important features
df = pd.read_csv('merged_datasets/merged_EDISp.csv')

mav_dataset.build_moving_average_dataset(average_N=3, skip_n=0)
