from flask import Flask, render_template, request

app = Flask(__name__)

#@app.route('/', methods=['GET', 'POST'])
#def check_age():
#    if request.method == 'POST':
#        name = request.form['name']
#        age = int(request.form['age'])
#        if age >= 18:
#            message = f"Pozdravljen, {name}! Si polnoleten."
#        else:
#            message = f"Pozdravljen, {name}! Nisi še polnoleten."
#        return render_template('index.html', message=message)
#    return render_template('index.html')

@app.route('/sum', methods=['GET', 'POST'])
def sum_numbers():
    if request.method == 'POST':
        numbers = request.form['numbers']
        numbers_list = [int(num) for num in numbers.split(',')]
        total = sum(numbers_list)
        return render_template('sum.html', total=total)
    return render_template('sum.html')


if __name__ == '__main__':
    app.run(debug=True)