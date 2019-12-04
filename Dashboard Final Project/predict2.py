import pickle
# from pandas import DataFrame
# from sklearn.pipeline import Pipeline

model=pickle.load(open('pipeline_nlp2.sav','rb'))
# real_columns=['Clean Review','Rating']

def predict2(data):
    hasil2 = model.predict([data])
    if(hasil2=='Worst'):
        hasil2='Seems like the customer dont like the product. the review value is:\nWorst'
    else:
        hasil2='Thankyou for liking our product. the review value is:\nBest'
    return hasil2


