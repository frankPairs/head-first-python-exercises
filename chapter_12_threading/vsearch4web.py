from flask import Flask, render_template, request, session, copy_current_request_context
from DBcm import UseDatabase, ConnectionDBError, SQLError
from threading import Thread
from time import sleep

import vsearch
from authchecker import check_logged_in


app = Flask(__name__)
app.config['db'] = {
    'host': '127.0.0.1',
    'user': 'postgres',
    'password': 'postgres',
    'dbname': 'vsearchlogDB',
}
app.secret_key = 'thisissecret'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'OK'


@app.route('/logout')
def do_logout() -> str:
    if 'logged_in' in session:
        session.pop('logged_in', None)

    return 'OK'


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        try:
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

                sleep(15)
        except ConnectionDBError as err:
            print('Ups, there was a DB connection error: ' + str(err))
        except SQLError as err:
            print('Is you query correct?: ' + str(err))
        except Exception as err:
            print('Unknown DB exception: ' + str(err))

    title = 'Here your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(vsearch.search_for_letters(phrase, letters))

    try:
        thread = Thread(target=log_request, args=(request, results))
        thread.start()
    except Exception as err:
        print(str(err))

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
@check_logged_in
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





if __name__ == '__main__':
    app.run(debug=True)
