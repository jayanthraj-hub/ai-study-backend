from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"answer": "No question received."})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful study assistant."},
            {"role": "user", "content": question}
        ]
    )

    answer = response["choices"][0]["message"]["content"]

    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
