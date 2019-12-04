import pickle
from pandas import DataFrame,get_dummies

#model=pickle.load(open('pipeline_classification.sav','rb'))
model=pickle.load(open('finalized_model_copy2.sav','rb'))
real_columns=['Age', 'Rating', 'Positive Feedback Count','Division_Name','Department_Name','Class_Name']
dummy_columns=pickle.load(open('x_under_dummies_colomn_copy2.sav','rb'))
scaler=pickle.load(open('scaler_copy2.sav','rb'))

def prediction(data):

    df= DataFrame(data,index=[0])
    df=df.reindex(columns=dummy_columns, fill_value=0)
    df = scaler.transform(df)
    hasil=model.predict(df)
    if(hasil==0):
        hasil='Customer would not recommend the product'
    else:
        hasil='Customer would like to recommend the product'

    return hasil
