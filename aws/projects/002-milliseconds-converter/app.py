from flask import Flask, render_template, request

app = Flask(__name__)


def calculate(num):
    num = int(num)
    if num < 1000:
        return f"just {num} millisecons"
    else:
        return f"{bool((num//(1000*60*60))%60) * f'{(num//(1000*60*60))} hour/s'} {bool(num//(1000*60)%60) * f'{((num//(1000*60))%60)} minute/s'} \
            {bool((num//1000)%60) * f'{((num//1000)%60)} seconds/s'}"
        


def check(number):
    if number.isdigit() == False:
        return True
    elif int(number) < 1:
        return True
    else:
        return False


        


@app.route("/", methods = ['GET', 'POST'])
def head():
    if request.method == 'POST':
        valid = request.form['number']
        validation = check(valid)
        if validation:
            return render_template('index.html', not_valid = validation)
        else:
            result = calculate(valid)
            return render_template('result.html', milliseconds = valid, result = result, developer_name = 'Hakan Diki')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)