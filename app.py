from flask import Flask,render_template,request
import mysql.connector as mysql
from flask import request
import os

app=Flask(__name__)

conn=mysql.connect(host='localhost',database='bankdb',user='root',password='3579_9977@14')
cursor=conn.cursor()

@app.route('/')
def page():
    return render_template('index.html')

@app.route('/customer')
def customer_page():
    cursor.execute("SELECT * FROM customer;")
    data = cursor.fetchall()
    return render_template('customer.html',data=data)

@app.route('/transfer')
def transfer_page():
    return render_template('transfer.html')


@app.route('/transfer',methods=['GET','POST'])
def transfermoney():
    if(request.method=='POST'):
        sender=request.form.get('sender')
        receiver=request.form.get('receiver')
        amtwds=request.form.get('amtwds')
        senderacc=request.form.get('accsender')
        receiveracc=request.form.get('accreceiver')
        amount=request.form.get('amount')
        cursor=conn.cursor()
        cursor.execute("UPDATE customer SET balance = balance - %s WHERE  Account = %s" , (amount,senderacc))
        cursor.execute("UPDATE customer SET balance = balance + %s WHERE  Account = %s" , (amount,receiveracc))   

        cursor.execute("INSERT INTO history (sender, receiver, amount) VALUES (%s,%s,%s)" , (sender,receiver,amtwds))
        conn.commit() 
        cursor.close()
        return render_template('transfer.html')

@app.route('/history_cus')
def history_cus():
    cursor.execute("select transactid,sender,receiver,amount from history;")
    data1 = cursor.fetchall()
    return render_template('history_cus.html',data1=data1)  


if __name__=="__main__":
    app.run(debug=True,port=8010)