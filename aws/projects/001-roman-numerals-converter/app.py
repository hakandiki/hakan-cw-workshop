from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def not_valid(number):
    if number.isdigit() == False:
        print(f"Not Valid Input !!!")
        return True
    else:
        numberlocal = int(number)
        if numberlocal < 1 or numberlocal > 3999:
            return True
        else:
            return False
            
def number_roman(number):
    list=[]
    if number[-1] == "4":
        list.append("IV")
    elif number[-1] == "9":
        list.append("IX")
    else:
        list.append((((int(number[-1])//5)*"V")+(int(number[-1])%5)*"I"))
    if len(number) > 1:
        if number[-2] == "4":
            list.append("IL")
        elif number[-2] == "9":
            list.append("IC")
        else:
            list.append((((int(number[-2])//5)*"L")+(int(number[-2])%5)*"X"))
    if len(number) > 2:
        if number[-3] == "4":
            list.append("ID")
        elif number[-3] == "9":
            list.append("IM")
        else:
            list.append((((int(number[-3])//5)*"D")+(int(number[-3])%5)*"C"))
    if len(number) > 3:
        list.append(int(number[-4])*"M")
    return("".join(list[::-1]))



@app.route("/", methods = ['GET', 'POST'])
def head():
    if request.method == 'POST':
        valid = request.form['number']
        validation = not_valid(valid)
        if validation:
            return render_template('index.html', not_valid = validation)
        else:
            result = number_roman(valid)
            return render_template('result.html', number_decimal = valid, number_roman = result, developer_name = 'Hakan Diki')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)