from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/Average_value')
def get_avr_data():
    with open('source/hw.csv', mode='r') as file:
        height_list = []
        weight_list = []

        for i in file:

            data = i.split()

            for j in data:
                try:
                    height_value = float(data[1][:-1])
                    weight_value = float(data[2])
                    height_list.append(height_value * 2.54)
                    weight_list.append(weight_value / 2.20462)
                except:
                    continue

    return f'Average height - {round(sum(height_list) / len(height_list), 1)}cm, ' \
           f'average weight - {round(sum(weight_list) / len(weight_list), 1)}kgs'


@app.route('/requirements')
def view_requirements():
    with open('requirements.txt', 'r') as f:
        content = f.read()

        return render_template('template.html', content=content)


app.run(debug=True)
