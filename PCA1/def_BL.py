# 速度と加速度の評価指標を体長で割る
# 引数はデータフレーム(index : 個体番号，columns : 評価指標)

# ----------------------memo----------------------
# df.locでDataFlame内のデータの参照ができる．
# example : df.loc[index1:index2, colmns1:colmns2]
# ------------------------------------------------

bl_list = [32.50, 31.91, 29.88, 33.49, 35.17, 30.99, 35.05, 31.74, 35.73, 32.62]  # 体長


def BL(df):
    for n in range(10):
        df.loc[n + 1, 'speed':'speed_std'] = df.loc[n + 1, 'speed':'speed_std'] / bl_list[n]  # 個体ごとに体長で割る
        df.loc[n + 1, 'accel':'accel_std'] = df.loc[n + 1, 'accel':'accel_std'] / bl_list[n]
    return df
