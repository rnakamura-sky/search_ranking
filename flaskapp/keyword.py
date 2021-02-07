from flask import Blueprint, request, render_template, flash, redirect, url_for
from flaskapp.db import get_db 

bp = Blueprint('keyword', __name__, url_prefix='/keyword')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        keyword = request.form['keyword']
        error = None
        db = get_db()

        if not keyword:
            error = 'Keyword is required'
        elif db.execute(
            'SELECT id FROM keyword WHERE text = ?;', (keyword,)
        ).fetchone() is not None:
            error = f'Keyword {keyword} is already registered.'
        
        if error is None:
            db.execute(
                'INSERT INTO keyword (text) VALUES (?);', (keyword,)
            )
            db.commit()
            return redirect(url_for('keyword.index'))
        flash(error)
        
    return render_template('keyword/register.html')

@bp.route('/list', methods=('GET',))
def index():
    db = get_db()
    keywords = db.execute(
        'SELECT id, text, del FROM keyword ORDER BY id;'
    ).fetchall()
    return render_template('keyword/index.html', keywords=keywords)
