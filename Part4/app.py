from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    posts = {
        1: {'title': 'Getting Started with Flask', 'content': 'Flask is a micro-framework...'},
        2: {'title': 'Understanding Routes', 'content': 'Routes map URLs to functions...'},
        3: {'title': 'Working with Templates', 'content': 'Jinja2 makes HTML dynamic...'},
    }
    post = posts.get(post_id)
    return render_template('post.html', post=post, post_id=post_id)


@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    return render_template('user_post.html', username=username, post_id=post_id)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/links')
def show_links():
    links = {
        'home': url_for('home'),
        'about': url_for('about'),
        'user_alice': url_for('user_profile', username='Alice'),
        'user_bob': url_for('user_profile', username='Bob'),
        'post_1': url_for('show_post', post_id=1),
        'post_2': url_for('show_post', post_id=2),
    }
    return render_template('links.html', links=links)


@app.route('/product/<int:product_id>')
def product_page(product_id):
    products = {
        1: {"name": "Laptop", "price": 55000},
        2: {"name": "Phone", "price": 25000},
        3: {"name": "Headphones", "price": 3000},
        4: {"name": "Keyboard", "price": 1500}
    }
    product = products.get(product_id)
    return render_template("product.html", product=product, product_id=product_id)


@app.route('/category/<category_name>/product/<int:product_id>')
def category_product(category_name, product_id):
    products = {
        1: "Laptop",
        2: "Phone",
        3: "Headphones"
    }
    product = products.get(product_id, "Unknown Product")
    return render_template("category_product.html",
                           category=category_name,
                           product=product,
                           product_id=product_id)


@app.route('/search')
def search_form():
    q = request.args.get("q")
    return render_template("search.html", query=q)

@app.route('/search/<query>')
def search(query):
    return render_template("search.html", query=query)


if __name__ == '__main__':
    app.run(debug=True)
