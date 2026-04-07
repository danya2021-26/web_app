from flash import Flask,render_template
app=Flash(_name_)
@app.route('/')
def home():
    return render_template('index.html',title="home page")
if _name_ =='_main_':
    app.run(host='127.0.0.1',port=8080,debug=True)