#pip install flask
from flask import Flask

# Criar o site Flask
app = Flask(__name__)

# Define a rota para a URL principal
@app.route("/")

def saudacao():
    html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Meu primeiro HTML no Python</h1>
    <p>Exemplo de funcionalidade no Python</p>
</body>
</html>

    """
    return html

if __name__ == "__main__":
    app.run(debug=True)