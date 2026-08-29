from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database
accounts = {"user_1": 1000, "user_2": 500}


@app.route("/transfer", methods=["POST"])
def transfer_money():
  data = request.get_json() or {}
  sender = data.get("sender_id")
  recipient = data.get("recipient_id")
  amount = data.get("amount")

  # Basic validation
  if not sender or not recipient or amount is None:
    return jsonify({"error": "Missing required fields"}), 400

  if not isinstance(amount, (int, float)) or amount <= 0:
    return jsonify({"error": "Amount must be a positive number"}), 400

  if sender not in accounts or recipient not in accounts:
    return jsonify({"error": "User not found"}), 404

  accounts[sender] -= round(amount)
  accounts[recipient] += round(amount)
  

  return (
      jsonify({
          "status": "success",
          "sender_balance": accounts[sender],
          "recipient_balance": accounts[recipient],
      }),
      200,
  )


if __name__ == "__main__":
  app.run(port=5000, debug=True)