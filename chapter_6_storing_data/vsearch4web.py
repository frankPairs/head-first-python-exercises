from flask import Flask, render_template, request, escape
import vsearch

app = Flask(__name__)


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
    titles = ('Form Data', 'Remote address', 'User Agent', 'Results')
    contents = []

    with open('vsearch.log') as log:
        for line in log:
            [form, remote_addr, user_agent, res] = line.split('|')

            log = {
                'form': escape(form),
                'remote_addr': remote_addr,
                'user_agent': user_agent,
                'res': res
            }

            contents.append(log)

    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents
    )


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


if __name__ == '__main__':
    app.run(debug=True)
