from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()  # Lê o JSON enviado pelo webhook
    print("\n=== Novo Webhook Recebido ===")
    print(data)  # Mostra no terminal o conteúdo
    print("=============================\n")
    filename = "webhook.json"

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    # Aqui você poderia fazer qualquer ação: salvar no banco, enviar e-mail, etc.
    return jsonify({"status": "Webhook recebido com sucesso!"}), 200

@app.route("/", methods=["GET"])
def home():
    return "Servidor de Webhook Flask está rodando denovo! 🚀"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
