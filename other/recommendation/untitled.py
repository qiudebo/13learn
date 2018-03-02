
rdd = sc.parallelize([[(2, 3),(1,4)],[(1,2),(3,5)],[(4,5),(4,3)]])
rdd.flatMap(lambda x:x).collect()

sc.parallelize(["b", "c", "a", "d", "e"]).zipWithUniqueId().collect()

def parse_flow_data(line):
    segment = re.split(r',',line.encode('utf-8').strip())
    catekey = segment[0] + "::" +segment[1]
    catefeatures = segment[5:14] #  分类特征需要 One-Hot-Encoding
    numericalfeatures = segment[15:23]
    return [catekey,catefeatures,numericalfeatures]

def parse_cate_features(line):
    '''
    将分类特征做id映射
    '''
    catefeatures = line[1]
    #return dict(zip(range(len(catefeatures)),catefeatures))
    return zip(range(len(catefeatures)), catefeatures)

def parse_cate_features(line):
    '''
    将分类特征做id映射
    '''
    catefeatures = line[1]
    #return dict(zip(range(len(catefeatures)),catefeatures))
    return zip(range(len(catefeatures)), catefeatures)


def parse_train_features(line):
    catefeatures = line[1]
    numericalfeatures = line[2]
    cat_feature_ohe =[]
    cat_features_indexed = parse_cate_features(catefeatures)
    for k in cat_features_indexed:
        if k in oheMap:
        	cat_feature_ohe.append(float(oheMap.get(k))
        else:
        	cat_feature_ohe.append(0.0)

    for x in range(len(numericalfeatures)):
    	if numericalfeatures[x]<0:
    		numericalfeatures[x] = 0
    features = cat_feature_ohe + numericalfeatures

    return features

click_data_rdd = sc.textFile('/Users/qiudebo/myspark/data/test1')
train_raw_rdd,test_raw_rdd = click_data_rdd.randomSplit([0.8,0.2],17)
train_rdd = train_raw_rdd.map(parse_flow_data)

train_rdd.map(lambda [x,y,z):(x,y,z)).take(1)

train_cate_rdd = train_rdd.map(parse_cate_features)

# 将(特征ID:特征)去重，并进行编号
oheMap = train_cate_rdd.flatMap(lambda x:x).distinct().zipWithIndex().collectAsMap()

ohe_train_rdd = train_rdd.map(parse_train_features)
ohe_train_rdd.take(1)

oheMap.saveAsTextFile("/Users/qiudebo/myspark/output/click")

if __name__ == '__main__':
    main()
