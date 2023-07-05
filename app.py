
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required
from datetime import timedelta
import smtplib
from email.message import EmailMessage
from threading import Timer
import random

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
jwt = JWTManager(app)

users = []

@app.route('/users', methods=['POST'])
def create_user():
    email = request.json['email']
    password = request.json['password']

    for user in users:
        if user['email'] == email:
            return jsonify({'error': 'Email already exists'}), 400

    users.append({'email': email, 'password': password, 'verified': False})
    return jsonify({'message': 'User created successfully'}), 201


verification_codes = {}

def send_email(email, otp):
    msg = EmailMessage()
    msg.set_content(f'Your OTP is: {otp}')

    msg['Subject'] = 'Email Verification OTP'
    msg['From'] = 'your_email@example.com'
    msg['To'] = email

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your_email@example.com', 'your_email_password')
        smtp.send_message(msg)

@app.route('/users/verify', methods=['POST'])
def send_verification_email():
    email = request.json['email']
    user = next((user for user in users if user['email'] == email), None)

    if user:
        otp = str(random.randint(100000, 999999))
        verification_codes[email] = otp

        Timer(180, expire_otp, args=[email]).start()
        send_email(email, otp)

        return jsonify({'message': 'Verification email sent'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

def expire_otp(email):
    if email in verification_codes:
        del verification_codes[email]




@app.route('/users/verify', methods=['POST'])
def verify_user():
    email = request.json['email']
    otp = request.json['otp']

    if email in verification_codes and verification_codes[email] == otp:
        user = next((user for user in users if user['email'] == email), None)

        if user:
            user['verified'] = True
            del verification_codes[email]
            return jsonify({'message': 'User verified successfully'}), 200

    return jsonify({'error': 'Invalid OTP or Email'}), 400



@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    user = next((user for user in users if user['email'] == email), None)

    if user and user['verified'] and user['password'] == password:
        access_token = jwt.encode({'email': email}, app.config['JWT_SECRET_KEY'])
        return jsonify({'access_token': access_token}), 200

    return jsonify({'error': 'Invalid credentials or user not verified'}), 401


@app.route('/users', methods=['GET'])
@jwt_required
def get_users():
    return jsonify(users), 200


if __name__ == '__main__':
    app.run()
