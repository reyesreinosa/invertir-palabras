from flask import Flask, request, render_template_string

app = Flask(__name__)

# Función para invertir palabras
def invertir_palabra(palabra: str) -> str:
    if len(palabra) <= 1:
        return palabra
    else:
        return palabra[-1] + invertir_palabra(palabra[:-1])

def invertir_frase(frase: str) -> str:
    palabras = frase.split()
    return ' '.join(invertir_palabra(palabra) for palabra in palabras)

# Página HTML con botón borrar
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Conversor al revés</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: #f9f9f9;
            padding: 40px 20px;
            text-align: center;
            max-width: 500px;
            margin: auto;
        }
        input, button {
            padding: 12px;
            margin: 10px 5px;
            font-size: 18px;
            border-radius: 8px;
            border: 1px solid #ccc;
            width: 40%;
            min-width: 120px;
        }
        button {
            background-color: #007AFF;
            color: white;
            border: none;
            cursor: pointer;
        }
        button#borrar {
            background-color: #E5E5EA;
            color: #1C1C1E;  /* texto oscuro para que contraste */
        }
        .resultado {
            margin-top: 20px;
            font-size: 20px;
            color: #333;
            word-wrap: break-word;
        }
    </style>
</head>
<body>
    <h1>Conversor al revés</h1>
    <form method="post" id="formulario">
        <input id="inputFrase" name="frase" placeholder="Escribe tu frase aquí" size="30" required
            value="{{ request.form.get('frase','') }}">
        <br>
        <button type="submit">Invertir</button>
        <button type="button" id="borrar" onclick="limpiar()">Borrar</button>
    </form>
    {% if resultado %}
        <div class="resultado">{{ resultado }}</div>
    {% endif %}

    <script>
        function limpiar() {
            document.getElementById('inputFrase').value = '';
            // Opcional: quitar resultado también sin recargar la página
            const res = document.querySelector('.resultado');
            if(res) res.innerHTML = '';
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = ""
    if request.method == "POST":
        frase = request.form["frase"]
        resultado = invertir_frase(frase)
    return render_template_string(HTML, resultado=resultado)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)



