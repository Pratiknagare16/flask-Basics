from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    student_name = "Alex"
    return render_template('index.html', name=student_name)

@app.route('/profile')
def profile():
    user_data = {
        'name': 'Pratik',
        'age': 22,
        'course': 'Full Stack Intern',
        'email': 'nagarepratik001@gmail.com',      
        'city': 'Nashik',               
        'is_enrolled': True
    }

    return render_template(
        'profile.html',
        name=user_data['name'],
        age=user_data['age'],
        course=user_data['course'],
        email=user_data['email'],
        city=user_data['city'],
        is_enrolled=user_data['is_enrolled']
    )

@app.route('/skills')
def skills():
    programming_skills = ['Python', 'HTML', 'CSS', 'JavaScript', 'Flask']
    return render_template('skills.html', skills=programming_skills)

@app.route('/projects')
def projects():
    project_list = [
        {'name': 'Personal Website', 'status': 'Completed', 'tech': 'HTML/CSS'},
        {'name': 'Flask Blog', 'status': 'In Progress', 'tech': 'Python/Flask'},
        {'name': 'Weather App', 'status': 'Planned', 'tech': 'JavaScript'},
    ]
    return render_template('projects.html', projects=project_list)











@app.route('/grades')
def grades():
    grades = {
        "Python": 95,
        "Web Development": 88,
        "DSA": 79,
        "Maths": 85
    }
    return render_template("grades.html", grades=grades)

if __name__ == '__main__':
    app.run(debug=True)
