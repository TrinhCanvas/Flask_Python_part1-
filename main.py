from flask import Flask, request, json

app = Flask(__name__)
print("Chương trình quản lý sinh viên Python")

data = [{
    'id': '1',
    'name': 'Nam'
}, {
    'id': '2',
    'name': 'Tuan'
}]


@app.route("/", methods=['POST'])
def addstudent():
    id = request.form.get('id')
    name = request.form.get('name')

    obj = {
        'id': id,
        'name': name,
    }
    data.append(obj)
    print(obj)
    return json.dumps(obj)


@app.route("/", methods=['get'])
def ex():

    return json.dumps(data)


@app.route("/<id>", methods=['delete'])
def delete_student(id):

    for i in range(0, len(data)-1):
        if data[i]['id'] == id:
            data.pop(i)

    return json.dumps(data)

# put dùng cập nhật lại dữ liệu (có thể đổi tên)
@app.route("/<id>", methods=['put'])
def update_student(id):

    for i in range(0, len(data)-1):
        if data[i]['id'] == id:
            data[i]['name'] = request.form.get('name')

    return "succesfull"


@app.route("/<id>", methods=['get'])
def get_studentbyid(id):

    for i in range(0, len(data)-1):
        if data[i]['id'] == id:
            return json.dumps(data[i])

    return "not found"



if __name__ == '__main__':
    app.run(debug=True)

