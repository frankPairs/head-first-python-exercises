from flask import Flask, render_template, request
import vsearch

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    title = 'Here your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(vsearch.search_for_letters(phrase, letters))

    return render_template('results.html',
                           the_letters=letters,
                           the_phrase=phrase,
                           the_results=results,
                           the_title=title,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)
