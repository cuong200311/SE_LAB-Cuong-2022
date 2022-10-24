from app import sale_app
from flask import render_template, request
from app import dao


@sale_app.route('/')
def index():
    categories = dao.load_categories()
    cate_id = request.args.get('category')
    proc = dao.load_products(category_id=cate_id)
    return render_template('index.html', categories=categories, products=proc)


if __name__ == '__main__':
    sale_app.run(debug=True)
