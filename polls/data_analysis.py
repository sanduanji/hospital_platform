import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from pyecharts.charts import Pie
import random
import os

# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [11, 12, 13, 10, 10, 10]
# pie = Pie("饼图示例")
# pie.add("", attr, v1, is_label_show=True)
# pie.render('pie.html')

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker


def analysis():
    path = '/Users/saber/Downloads/result.csv'
    in_data = pd.read_csv(path, header=0)

    print(in_data.iloc[2].values.tolist())
    print(len(in_data))


    print(in_data['组织学类型'][2])
    print(in_data['组织学分级'][2])
    print(in_data['浸润深度'][2])
    print(in_data['脉管内癌栓'][2])
    print(in_data['神经侵犯'][2])
    print(in_data['淋巴结转移情况'][2])

    print()

    print(type(in_data['组织学类型']))
    print(type(in_data['报告日期'][20]))
    # 组织学类型

    cnt_dict = {}

    def add_one(key, val):
        if key in cnt_dict:
            cnt_dict[key].append(val)
        else:
            cnt_dict[key] = [val]

    for item in in_data['组织学类型']:
        if type(item).__name__ == 'str':
            if item.find('腺癌') != -1 or item.find('腺瘤') != -1:
                add_one('腺癌', item)
            elif item.find('黑色素瘤') != -1:
                add_one('黑色素瘤', item)
            elif item.find('未见') != -1 and item.find('残留') != -1:
                add_one('未见癌残留', item)
            elif item.find('鳞状细胞癌') != -1:
                add_one('鳞状细胞癌', item)
            elif item.find('印戒细胞癌') != -1:
                add_one('印戒细胞癌', item)
            elif item.find('粘膜慢性炎') != -1:
                add_one('粘膜慢性炎', item)
            elif item.find('腺鳞癌') != -1:
                add_one('腺鳞癌', item)
            elif item.find('神经内分泌癌') != -1 or item.find('神经内分泌瘤') != -1:
                add_one('神经内分泌癌', item)
            else:
                add_one('其他', item)
        else:
            #         add_one('', item)
            pass  # 空的不处理

    print(len(cnt_dict))
    print(len(cnt_dict['腺癌']))

    for key, item in cnt_dict.items():
        print('"', key, '"', ' : ', len(item))

    keys = cnt_dict.keys()
    cnt_keys = []

    for key in keys:
        cnt_keys.append(len(cnt_dict[key]))

    print('\n', '-*-' * 10, '\n')

    print(keys)
    print(cnt_keys)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

    # explode = (0,0.1,0,0,0,0,0,0,0,0)

    # 2）创建画布
    plt.figure(figsize=(20, 8), dpi=100)

    plt.pie(cnt_keys, labels=keys, autopct='%1.2f%%', colors=['b', 'g', 'y', 'c', 'm', 'y', 'k', 'c'], startangle=250)

    plt.title("组织学类型")

    plt.axis('equal')  # 该行代码使饼图长宽相等

    plt.legend()  # 显示图例

    # plt.show()


    c = (
        Pie()
            .add("", [list(z) for z in zip(keys, cnt_keys)], center=["50%", "50%", "80%", "10%"], )
            .set_colors(["blue", "green", "yellow", "pink", "orange", "purple"])
            .set_global_opts(title_opts=opts.TitleOpts(title="大肠癌病例组织学类型可视化"),
                             legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"), )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .render("zuzhi.html")
    )

    from snapshot_phantomjs import snapshot
    from pyecharts.render import make_snapshot
    img_root = '/Users/saber/Downloads/testsite/polls/'
    img_name = 'zuzhi.png'
    img_path = os.path.join(img_root, img_name)
    img_path = '/Users/saber/Downloads/testsite/static/zuzhi.png'
    make_snapshot(snapshot, "zuzhi.html", img_path)  # 生成svg图片


analysis()