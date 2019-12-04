from flask import Flask, render_template, request, url_for
from datas import Department_Name, Class_Name
from prediction import prediction
from predict2 import predict2
from plots import count_type1, count_type2, count_type3
app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('home.html')

@app.route('/prediction', methods=['GET','POST'])
def prediction1():
    if request.method=='POST':
        data = request.form
        data = data.to_dict()
        data['Age'] = int(data['Age'])
        data['Positive Feedback Count'] = int(data['Positive Feedback Count'])
        hasil = prediction(data)

        return render_template('result.html' , hasil_pred=hasil)
    return render_template('prediction.html', data_department= Department_Name, data_class=Class_Name)

@app.route('/predict2',methods=['POST','GET'])
def prediction2():
    if request.method=='POST':
        data = request.form
        data = data.to_dict()
        new_data = str(data['Clean Review'])
        #print(new_data)
        hasil2 = predict2(new_data)
        return render_template('result2.html' ,hasil_pred2=hasil2)
    return render_template('predict2.html')

@app.route('/table')
def login():
    return render_template('table.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/summary')
def summa():
    return render_template('summary.html')

@app.route('/plots')
def plots():
    plot1 = count_type1()
    plot2 = count_type2()
    plot3 = count_type3()
    return render_template('plots.html' , data=plot1, data2=plot2, data3=plot3)

@app.route('/plots2')
def plots2():
    return render_template('plots2.html')

@app.route('/plots3')
def plots3():
    return render_template('plots3.html')


if __name__ =='__main__':
    app.run(debug=True,port=9000)