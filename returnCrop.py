# %matplotlib inline
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from glob import glob
import numpy as np
from sklearn import datasets, linear_model

class ReturnCrop:
    def returnCrop(state,area,capital):
        xls_data = sorted(glob('Dataset/*.xls'))

        # state = "Maharashtra"
        apple = []
        year = []
        sheetnames = []

        required_elements = [5,6,7,8,9,11,12,13,14,15,21]

        for xls in xls_data:
            xl = pd.ExcelFile(xls)
            sheetnames = sheetnames + xl.sheet_names
        y = set(sheetnames)
        y = list(y)

        items = np.zeros((len(y),11,11))
        possible_crops = []
        for xls in xls_data:
            xl = pd.ExcelFile(xls)
            for sheet in sorted(xl.sheet_names):
                if sheet.startswith("Coco"):
                    continue
                df = xl.parse(sheet, skiprows=3)
                df.iloc[6,1] = df.iloc[0,1]
                df.iloc[0,1] = np.nan
                df.iloc[14,1] = df.iloc[7,1]
                df.iloc[7,1] = np.nan
                df = df[df.iloc[:,1].notnull()]
                df.drop(df.columns[[0,2]],axis=1,inplace=True)
                df = df.iloc[:21,:]
        #         df[state].shape
                if state in df.columns:
                    possible_crops.append(sheet)
                try:
                    for i,element in enumerate(required_elements):
                        items[y.index(sheet),i,int(xls[8:12])-2004] = df[state].iloc[element]
                except:
                    pass
            year.append([int(xls[8:12])])

        for i in range(0,len(items)):
            for j in range(0,len(items[0])):
                for k in range(0,len(items[0][0])):
                    if np.isnan(items[i,j,k]):
                        items[i,j,k] = 0
        for i in range(0,len(items)):
            for j in range(0,len(items[0])):
                for k in range(0,len(items[0][0])):
                    if np.isnan(items[i,j,k]):
                        items[i,j,k] = np.mean(items[i][j])
        models = [[0 for y in range(0,len(items[0]))] for x in range(0,len(items))] 
        for i in range(0,len(items)):
            for j in range(0,len(items[0])):
                models[i][j] = linear_model.LinearRegression()
                models[i][j].fit(year, items[i,j])

        
        all_crops=[]
        ans = np.zeros((len(y),11))
        cost = np.zeros((len(y)))
        gain = np.zeros((len(y)))
        supp = 1500
        for i in range(0,len(items)):
            for j in range(0,len(items[0])):
                ans[i][j] = models[i][j].predict(2017)
        max_num=0
        max_index=0
        for i in range(0,len(items)):
            for j in range(0,int(len(ans[0])/2)):
                cost[i]+=ans[i][j]*ans[i][j+5]
        #     print((ans[i][len(items[0])-1]*supp-cost[i])*2)
            all_crops.append((int(ans[i][len(items[0])-1])*int(supp)-int(cost[i]))*int(area))
            if ((int(ans[i][len(items[0])-1])*int(supp)-int(cost[i]))*int(area)) > max_num:
                max_num = ((int(ans[i][len(items[0])-1])*int(supp)-int(cost[i]))*int(area))
                max_index = i
<<<<<<< HEAD
                
        return y[max_index], ans[max_index]
=======
        print(max(all_crops),y[max_index])
        crops_possible = list(set(possible_crops))
        print(crops_possible)
        return y[max_index], ans[max_index], crops_possible
>>>>>>> 1c8fdadee888f3d5ee1464f0ca3f7e44cf783adf
