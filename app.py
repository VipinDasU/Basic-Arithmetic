import random
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def vipi():
    global num_of_mangoes
    num_of_mangoes = random.randint(1, 10)
    global money
    money = random.randrange(100, 2000, 100)
    global balance
    balance = (money-(num_of_mangoes*200))
    if(balance<0):
        wrd = "should give"
    elif(balance>0):
        wrd = "get"
    else:
        wrd = "get"
    return render_template('index.html', num_of_mangoes=num_of_mangoes, money=money, wrd=wrd)

@app.route('/submit', methods=['POST'])
def sub():
    ans = request.form.get('ans')
    if(int(ans)==abs(balance)):
        result = "Your answer is correct"
    else:
        result = "Your answer is wrong"
    global an
    an = "Number of Kg of mangoes = " + str(num_of_mangoes) + ", Money given = " + str(money) + ", Balance =" + ans
    return render_template('result.html', result=result, an=an, balance=balance, ans=ans)
if __name__ == '__main__':
    app.run(debug=True)





