import stat
import os
from os.path import abspath, dirname, join

def basic_PageRank(num, out_degree, des_nodes, beta):
    '''
    n是节点总个数
    number是每个节点的出度字典
    to_nodes是每个有出度的节点指向的节点数组字典
    '''
    old = {}
    new = {}
    sum = 0
    for node in out_degree.keys():
        old[node] = 1 / num
        new[node] = 0
        sum = sum + abs(new[node] - old[node])

    while sum >= 1e-5:
        for node in out_degree.keys():
            for des_node in des_nodes[node]:
                new[des_node] = new[des_node] + beta * old[node] / out_degree[node]

        s = 0
        for node in out_degree.keys():
            s = s + new[node]
        for node in out_degree.keys():
            new[node] = new[node] + (1 - s) / num

        sum = 0
        for node in out_degree.keys():
            sum = sum + abs(new[node] - old[node])
            old[node] = new[node]
            new[node] = 0

    return old


def block_PageRank(num, block, out_degree, src_nodes, beta):
    '''
    param num: 是节点个数
    param block: 是分块大小
    param out_degree:　是每个节点的出度字典
    param src_nodes: 每个节点的源节点
    
    description:这个函数时通过block strip的方式对数组进行优化
    '''




if __name__ == '__main__':
    f = open('WikiData.txt', 'r')
    lines = f.readlines()
    # 数据转换
    all_data = []
    for line in lines:
        data = line.split()
        all_data.append(data)

	# 读取节点个数,创建稀疏矩阵
    num = 0  # 节点总个数
    out_degree = {}  # 节点的出度字典
    des_nodes = {}  # 节点指向的节点
    for data in all_data:
        # 计算节点个数
        for i in [0, 1]:
            if data[i] not in out_degree.keys():
                num = num + 1
                out_degree[data[i]] = 0
                des_nodes[data[i]] = []

        # 创建稀疏矩阵
        if data[1] not in des_nodes[data[0]]:
            out_degree[data[0]] = out_degree[data[0]] + 1
            des_nodes[data[0]].append(data[1])
    # print(num) 7115
    basic_result = sorted(basic_PageRank(num, out_degree, des_nodes, 0.85).items(), key=lambda item: item[1], reverse=True)

    # 写文件
    root = os.path.abspath(join(dirname(abspath(__file__)), 'Result'))
    if not os.path.exists(root):
        os.makedirs(root)
    else:
        for fileList in os.walk(root):
            for name in fileList[2]:
                os.chmod(os.path.join(fileList[0], name), stat.S_IWRITE)
                os.remove(os.path.join(fileList[0], name))
    basic = os.path.abspath(join(dirname(abspath(__file__)), 'Result\\' + 'Result.txt'))
    # 写结果
    with open(basic, 'w') as f1:
        for i in range(100):
            f1.write('[' + basic_result[i][0] + ']' + '   ' + '[%.8f]' % basic_result[i][1] + '\n')

    for i in range(100):
        print(basic_result[i][0] + '  ' + '%.8f' % basic_result[i][1])

    os.system("pause")