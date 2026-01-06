from flask import Flask, render_template, request

app = Flask(__name__)

PERSONAL_INFO = {
    'name': 'Pratik',
    'title': 'Web Developer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'nagarepratik001@gmail.com',
    'github': 'https://github.com/pratiknagare16',
    'linkedin': 'www.linkedin.com/in/pratik-nagare001'
}

SKILLS = [
    {'name': 'Python', 'level': 80},
    {'name': 'HTML/CSS', 'level': 75},
    {'name': 'Flask', 'level': 60},
    {'name': 'JavaScript', 'level': 50},
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'A Flask portfolio.', 'tech': ['Flask', 'HTML'], 'status': 'Completed'},
    {'id': 2, 'name': 'Todo App', 'description': 'Task manager.', 'tech': ['Flask', 'SQLite'], 'status': 'In Progress'},
    {'id': 3, 'name': 'Weather App', 'description': 'Weather dashboard.', 'tech': ['API'], 'status': 'Planned'},
]

PRODUCTS = {
    1: {"name": "Laptop", "price": 55000},
    2: {"name": "Phone", "price": 25000},
    3: {"name": "Headphones", "price": 3000},
    4: {"name": "Keyboard", "price": 1500},
    5: {"name": "Mouse", "price": 800},
    6: {"name": "Smart Watch", "price": 4500},
    7: {"name": "Bluetooth Speaker", "price": 2200},
    8: {"name": "Gaming Controller", "price": 3200},
    9: {"name": "Webcam", "price": 1800},
    10: {"name": "Power Bank", "price": 1200},
    11: {"name": "USB-C Hub", "price": 1600},
    12: {"name": "External Hard Drive", "price": 6500},
    13: {"name": "Wireless Earbuds", "price": 4200},
    14: {"name": "Laptop Stand", "price": 900},
    15: {"name": "Microphone", "price": 3500}
}


@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)

@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)

@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)

@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)






@app.route('/product/<int:product_id>')
def product_page(product_id):
    product = PRODUCTS.get(product_id)
    return render_template('product.html', info=PERSONAL_INFO, product=product, product_id=product_id)







@app.route('/category/<category_name>/product/<int:product_id>')
def category_product(category_name, product_id):
    product = PRODUCTS.get(product_id)
    return render_template('category_product.html',
                           info=PERSONAL_INFO,
                           category=category_name,
                           product=product,
                           product_id=product_id)


@app.route("/products")
def all_products():
    return render_template("all_products.html", info=PERSONAL_INFO, products=PRODUCTS)



@app.route('/search')
def search():
    query = request.args.get("q", "").lower()
    results = {}

    for pid, product in PRODUCTS.items():
        if query in product["name"].lower():
            results[pid] = product

    return render_template(
        "search.html",
        info=PERSONAL_INFO,
        query=query,
        results=results
    )

@app.route('/search/<query>')
def search_query(query):
    query = query.lower()
    results = {}

    for pid, product in PRODUCTS.items():
        if query in product["name"].lower():
            results[pid] = product

    return render_template(
        "search.html",
        info=PERSONAL_INFO,
        query=query,
        results=results
    )


if __name__ == '__main__':
    app.run(debug=True)
