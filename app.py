from flask import Flask, render_template, request, redirect, url_for;
app = Flask(__name__)



student_name = ["Spongebob", "Jimmy Neutron", "Alice"]

@app.route('/')
def fetch_student_list():
    student_with_index = list(enumerate(student_name))
    return render_template('index.html', students = student_with_index)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    if name:
        student_name.append(name)
        return  redirect(url_for('fetch_student_list'))

@app.route('/delete/<string:name>')
def delete_student(name):
    student_name.remove(name)
    return redirect(url_for('fetch_student_list'))

@app.route('/delete-with-index/<int:index>')
def delete_student_with_index(index):
    student_name.pop(index)
    return redirect(url_for('fetch_student_list'))

@app.route('/select/<string:name>')
def selected_student(name):
    print("selected " , name);
    return redirect(url_for('fetch_student_list'))

@app.route('/edit_student/<int:index>', methods = ['POST'])
def edit_student(index):
    new_name = request.form.get("new_name")
    student_name[index] = new_name
    return redirect(url_for('fetch_student_list'))

if __name__ == '__main__':
    app.run(debug=True)