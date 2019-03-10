import scipy
from sklearn.decomposition import PCA  # scikit-learnのPCAクラス


def myPCA(df):
    df_std = scipy.stats.zscore(df, ddof=0)  # 各指標を標準化　#type : numpy.ndarrayに変換される
    pca = PCA()
    pca.fit(df_std)  # ここでpcaが完了．主成分負荷量やらスコアやらは計算されてる．
    transformed = pca.fit_transform(df_std)  # スコアを呼び出す
    assert isinstance(transformed, object), print('うんち')  # もしtransformedがobjectでなければ,print('うんち')を実行する
    print(transformed)
    print(pca.components_)
    return transformed
