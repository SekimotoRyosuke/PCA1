# Excelファイルの読み込み関数

import pandas as pd


def excelread(file_name):
    df = pd.read_excel(file_name, index_col=0)  # .xlsxの読み込み．一行目はヘッダ，一列目はラベルになる．
    # print(df)                                 # 読み込み内容の表示
    return df

    '''
    wb = openpyxl.load_workbook(file_name)  #file_nameで指定したExcelシートをopen
    sheet = wb.get_sheet_by_name(sheet)     #sheetで指定したシートを読み込む
    print(type(sheet))
    print('step1クリア')
    return sheet
    
    #読み込んだシートを配列へ
    data = np.zeros((sheet.max_row, sheet.max_column), dtype=np.int)
#    data = [[0 for i in range(sheet.max_column)] for j in range(sheet.max_row)]     #読み込んだデータ数分の配列dataを宣言
    for x in range(0, sheet.max_row):                                               #一つずつ配列に代入
        for y in range(0, sheet.max_column):
            data[x][y] = sheet.cell(row=x+1, column=y+1).value
    print('データ読み込み完了.')
    '''
