
from sanic import Sanic
from sanic.response import text, json
from my_blueprint import bp 
app = Sanic()

"""
Request: 
request.files (dictionary of File objects) - 上传文件列表
request.json (any) - json数据
request.args (dict) - get数据
request.form (dict) - post表单数据
"""
# https://blog.csdn.net/mbugatti/article/details/53406417
@app.route("/json")
def post_json(request):
    return json({ "received": True, "message": request.json })
 
@app.route("/form")
def post_form(request):
    return json({ "received": True, "form_data": request.form, "test": request.form.get('test') })
 
@app.route("/files")
def post_files(request):
    test_file = request.files.get('test')
 
    file_parameters = {
        'body': test_file.body,
        'name': test_file.name,
        'type': test_file.type,
    }
    return json({ "received": True, "file_names": request.files.keys(), "test_file_parameters": file_parameters })
 
@app.route("/query_string")
def query_string(request):
    return json({ "parsed": True, "args": request.args, "url": request.url, "query_string": request.query_string })

# <number_arg:number>
@app.route("/<name::[A-z0-9]{0,5}>")
async def test(request, name):
    return text(f'Hello {name}!')

from sanic.exceptions import ServerError
 
@app.route('/killme')
def i_am_ready_to_die(request):
    raise ServerError("Something bad happened")

if __name__ == "__main__":
    app.register_blueprint(bp)
    app.run(host="127.0.0.1", port=8000)