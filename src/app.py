# Language: python
from flask import Flask, request, session, redirect, url_for
from nlp.processor import NLPProcessor

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key for production
chatbot = NLPProcessor()

@app.route("/", methods=["GET", "POST"])
def index():
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        query = request.form.get('query')
        response = chatbot.extract_information(query)
        history = session.get('history')
        history.append({'query': query, 'response': response})
        session['history'] = history
        return redirect(url_for('index'))

    history_html = ""
    for item in session.get('history', []):
        history_html += f"<p><strong>You:</strong> {item['query']}</p>"
        history_html += f"<p><strong>Chatbot:</strong> {item['response']}</p><hr>"

    return f'''
    <html>
    <head><title>CDP Support Chatbot</title></head>
    <body>
      <h2>Customer Data Platform Support Chatbot</h2>
      {history_html}
      <form action="/" method="post">
        <input type="text" name="query" style="width:300px;" placeholder="Ask your question here">
        <input type="submit" value="Ask">
      </form>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)