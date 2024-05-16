from flask import Flask, render_template, request, redirect
import smtplib
import datetime
import uuid
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book_trip', methods=['POST'])
def book_trip():
    if request.method == 'POST':
        name = request.form['fullName']
        email = request.form['email']
        message = request.form['message']
        start_date = request.form['startDate']
        end_date = request.form['endDate']
        start_time = request.form['startTime']
        end_time = request.form['endTime']

        # receiver_email = config('RECEIVER_EMAIL')
        # Replace 'jamalourika.tours@gmail.com' with your actual email address
        receiver_email = 'kwabenaampoforealtor@gmail.com'

        # Send email for each booking
        success = send_email(name, email, message, receiver_email, start_date, end_date, start_time, end_time)

        return render_template('index.html', success=success)

def send_email(name, email, message, receiver_email, start_date, end_date, start_time, end_time):
    try:
        # Generate a unique identifier for each email
        email_id = str(uuid.uuid4())

        # sender_email = config('SENDER_EMAIL')
        # sender_password = config('SENDER_PASSWORD')
        sender_email = 'kwabenaampoforealtor@gmail.com'
        sender_password = 'gylhrzfqitsxtnzo'

        subject = 'New Trip Booking'

        # Convert date strings to datetime objects
        start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d')

        # Format dates to "12th December, 2024" format
        formatted_start_date = start_date_obj.strftime('%d %B, %Y')
        formatted_end_date = end_date_obj.strftime('%d %B, %Y')

        body = f'Name: {name}\nEmail: {email}\nStart Date: {formatted_start_date}\nEnd Date: {formatted_end_date}\nStart Time: {start_time}\nEnd Time: {end_time}\nMessage: {message}'

        msg = MIMEMultipart()
        msg.attach(MIMEText(body, 'plain'))
        msg['Subject'] = subject
        msg['From'] = name
        msg['To'] = receiver_email

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


if __name__ == '__main__':
    app.run(debug=True)
