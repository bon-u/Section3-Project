import pandas as pd
import os
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from category_encoders import OneHotEncoder
from sklearn.impute import SimpleImputer 
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import f_regression, SelectKBest

CSV_FILEPATH = os.path.join(os.getcwd(), 'healthcare-dataset-stroke-data.csv')
data=pd.read_csv(CSV_FILEPATH)

#중복제거 및 결측치 제거
df=data.drop_duplicates()
df=df.dropna()
df = df[df.bmi != 'N/A']
#train,val 데이터 나누기
target='stroke'
dt=df.drop([target,'work_type','Residence_type','avg_glucose_level','hypertension','heart_disease','ever_married','smoking_status'],axis=1)
dt=dt.drop(dt.columns[[0]], axis=1)
tg=df[target]
X_train,X_val,y_train,y_val=train_test_split(dt,tg,test_size=0.2, random_state=10)

#모델 파이프라인 생성
pipe= make_pipeline(
    OneHotEncoder(), 
    SimpleImputer(),
    StandardScaler(),
    SelectKBest(f_regression),
    LogisticRegression(
        random_state=2
        ,n_jobs=-1)
)
dists = {  
    'selectkbest__k': range(1, len(X_train.columns)+1)
}
clf= GridSearchCV(
    pipe,
    param_grid=dists,
    cv=3,
    scoring='neg_mean_absolute_error',
    verbose=1)
#모델 훈련
clf.fit(X_train, y_train)
model= clf.best_estimator_
model.fit(X_train,y_train)

#예측 함수
def Predict(values):
    col=['gender','age','bmi']
    user_data=pd.DataFrame(values)
    user_data = user_data.transpose()
    user_data.columns=col
    ans=model.predict(user_data)
    return ans