from flask import Flask
from flask import render_template, redirect
from forms.wayform import WayForm
from forms.breadform import BreadForm
from forms.endform import EndForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['GET', 'POST'])
def base():
    form = WayForm()
    if form.validate_on_submit():
        return redirect('/test')
    return render_template('main.html', form=form, title='Хлебный тест')


@app.route('/test', methods=['GET', 'POST'])
def test():
    form = BreadForm()
    if form.validate_on_submit():
        return redirect(f'/result/{form.select.raw_data[0]}')
    return render_template('test.html', form=form, title='Хлебный тест')


@app.route('/result/<res>', methods=['GET', 'POST'])
def result(res):
    form = EndForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('result.html', title='Хлебный результат', res=res, form=form)


def main():
    app.run(port=8080, host="127.0.0.1")


if __name__ == '__main__':
    main()