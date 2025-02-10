from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

faq_data = {
    "What are your working hours?": "We are open from 9 AM to 6 PM.",
    "How do I reset my password?": "Click on 'Forgot Password' on the login page.",
    "Where is your office located?": "Our office is located at [Your Office Address].",
    "How can I contact support?": "You can contact support at support@example.com.",
    "What payment methods do you accept?": "We accept credit/debit cards, PayPal, and bank transfers.",
    "Do you have a refund policy?": "Yes, we offer a 30-day refund policy.",
    "How do I update my account details?": "You can update your details in the 'My Account' section.",
    "Can I cancel my subscription?": "Yes, you can cancel your subscription anytime from your account settings.",
    "Do you offer customer support on weekends?": "Yes, our support team is available 24/7.",
    "How long does shipping take?": "Shipping takes 3-5 business days."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_answer", methods=["POST"])
def get_answer():
    data = request.get_json()
    question = data.get("question")

    if question in faq_data:
        answer = faq_data[question]
    else:
        answer = "Sorry, I don't have an answer for that."

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
