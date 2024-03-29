from PIL.GribStubImagePlugin import GribStubImageFile
import numpy as np
import pandas as pandas
import dill
from src.exception import CustomException
import sys
import os
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys) # type: ignore


def evaluate_model(X_train,X_test,y_train,y_test,models,params):
    try:
        report={}
        for i in range(len(list(models))):
            model=list(models.values())[i]
            param=params[list(params.keys())[i]]
            gs=GridSearchCV(model,param,cv=3)
            gs.fit(X_train,y_train)
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            y_pred_train=model.predict(X_train)
            y_pred_test=model.predict(X_test)

            r2_square_train=r2_score(y_train,y_pred_train)
            r2_square_test=r2_score(y_test,y_pred_test)

            report[list(models.keys())[i]]=r2_square_test
            return report

    except Exception as e:
        raise CustomException(e,sys) # type: ignore


    