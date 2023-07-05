# email-otp-verification-api

In this project, I am using the Flask framework to build the User Verification API. Flask is a micro web framework written in Python that allows developers to create web applications and APIs with minimal boilerplate code. It is lightweight, flexible, and easy to use, making it an excellent choice for small to medium-sized projects.

Here are some of the key features of Flask:

1. Routing: Flask provides a simple and intuitive routing system, allowing developers to define URL routes and associate them with specific view functions.

2. Request-Response Handling: Flask makes it easy to handle incoming HTTP requests and generate appropriate HTTP responses. It supports various response formats, such as JSON, HTML, and more.

3. Template Rendering: Flask allows you to render dynamic HTML pages using templates. It includes Jinja2 as the default templating engine.

4. Request Context: Flask provides a request context that allows you to access request-specific data within view functions, making it easy to access form data, cookies, headers, etc.

5. Extension Support: Flask has a rich ecosystem of extensions that can be used to add additional functionality to the application, such as Flask-Mail for sending emails, Flask-JWT for handling JWT authentication, etc.

6. Development Server: Flask comes with a built-in development server, making it convenient for testing and development purposes.

7. NoSQL ORM: Flask does not include an Object-Relational Mapping (ORM) system by default, but it can be integrated with various ORMs like SQLAlchemy for database management.

Overall, Flask's simplicity and flexibility make it a popular choice for building web applications and APIs, especially when you need a lightweight and easy-to-use framework for smaller projects.

# Running Locally
git clone:`https://github.com/python-hacked/email-otp-verification-api.git`
cd email-otp-verification-api

python3 -m venv venv
linux:`source env/bin/activate`  # On Windows, use: `venv\Scripts\activate`

pip install -r requirements.txt

Create a .env file in the root directory and add the following variables:
EMAIL_USERNAME=your_email_username
EMAIL_PASSWORD=your_email_password
JWT_SECRET_KEY=your_jwt_secret_key


Run the Flask application:`python app.py`

# Access the API:
The API will be available at http://127.0.0.1:5000/.

To create a user, make a POST request to http://127.0.0.1:5000/users with JSON data containing the email and password.
To send a verification email with OTP, make a POST request to http://127.0.0.1:5000/users/verify with JSON data containing the email.
To verify the user with OTP, make another POST request to http://127.0.0.1:5000/users/verify with JSON data containing the email and OTP.
To log in and get a JWT token, make a POST request to http://127.0.0.1:5000/login with JSON data containing the email and password (if the user is verified, you will get a JWT token).
To get the listing of all users, make a GET request to http://127.0.0.1:5000/users with a valid JWT token in the Authorization header (Bearer token)

# AWS Deployment Process
Create an EC2 Instance:

Log in to the AWS Management Console.
Go to EC2 and click "Launch Instance."
Select an Amazon Machine Image (AMI) of your choice (e.g., Amazon Linux 2 AMI).
Choose the instance type and configure other settings.
Add security group rules to allow incoming traffic to your API's port (e.g., port 80 for HTTP).
Review and launch the instance.
Set up SSH access:

Download the private key (.pem) file when prompted during instance creation.
Use the following command to set permissions for the private key:`chmod 400 your-key.pem`

Connect to the instance using SSH:`ssh -i your-key.pem ec2-user@your-ec2-instance-ip`

Install necessary dependencies on the EC2 instance:`sudo yum update -y`
`sudo yum install python3 git -y`

# Output Process
For successful API calls, you will receive appropriate JSON responses with status codes (e.g., 200 for success, 400 for bad request, etc.).
To test the API locally, you can use tools like curl or use a web-based API client like Postman or Insomnia.
When running on AWS, you can use your API's public IP or associated domain name to access the API.
The API provides proper error messages for validation failures, expired OTP, and unauthorized access.
The database (if configured) will store user information, and you can retrieve the listing of all users through the appropriate API endpoint.

# Note
This is a basic implementation of the User Verification API. For production deployment, additional security measures, error handling, and scalability considerations should be taken into account. Also, make sure to secure sensitive information like environment variables and database credentials in a production environment.



