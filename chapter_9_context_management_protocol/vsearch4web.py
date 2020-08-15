from flask import Flask, render_template, request, escape
from DBcm import UseDatabase
import vsearch

app = Flask(__name__)
app.config['db'] = {
    'host': '127.0.0.1',
    'user': 'postgres',
    'password': 'postgres',
    'dbname': 'vsearchlogDB',
}


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    title = 'Here your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(vsearch.search_for_letters(phrase, letters))

    log_request(request, results)
    return render_template('results.html',
                           the_letters=letters,
                           the_phrase=phrase,
                           the_results=results,
                           the_title=title,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_log() -> 'html':
    titles = ('Phrase', 'Letters', 'Remote address', 'User Agent', 'Results')
    contents = []

    with UseDatabase(app.config['db']) as cursor:
        _SQL = """
            SELECT phrase, letters, ip, browser_string, results
            FROM logs
          """

        cursor.execute(_SQL)
        rows = cursor.fetchall()

    for row in rows:

        log = {
           'phrase': row[0],
           'letters': row[1],
           'remote_addr': row[2],
           'user_agent': row[3],
           'res': row[4]
        }

        contents.append(log)

    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


def log_request(req: 'flask_request', res: str) -> None:
    with UseDatabase(app.config['db']) as cursor:
        _SQL = """
            INSERT INTO logs (phrase, letters, ip, browser_string, results)
            VALUES (%s, %s, %s, %s, %s)
          """

        cursor.execute(_SQL, (
            req.form['phrase'],
            req.form['letters'],
            req.remote_addr,
            req.user_agent.browser,
            res,))


if __name__ == '__main__':
    app.run(debug=True)
