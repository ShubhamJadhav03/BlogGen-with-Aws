---
🤖 AI-Powered Serverless Blog Generator
A full-stack web application that leverages AWS Bedrock, Lambda, and API Gateway to generate blog posts on any topic, 
with a user-friendly frontend built using Streamlit.

<img width="962" height="876" alt="image" src="https://github.com/user-attachments/assets/351ae142-1662-4efa-b469-d40f93334d7c" />


---
🌟 Overview
This project demonstrates the power of serverless architecture and generative AI. 
The user enters a blog topic into a simple web interface, which calls a serverless backend on AWS. 
An AWS Lambda function invokes the Amazon Bedrock service (using the Nova model) to generate a well-written, 
200-word blog post. The generated article is then saved to an S3 bucket for storage and simultaneously returned 
to the user's screen.

---
🏗️ Architecture
The application follows a modern serverless architecture, ensuring scalability, low cost, and minimal operational overhead.


<img width="1293" height="577" alt="image" src="https://github.com/user-attachments/assets/657f9cca-bc6a-42b8-9d75-27e570678f46" />



---
✨ Features
- Dynamic Content Generation: Utilizes Amazon Bedrock's powerful AI models to write unique blog posts on demand.
- Serverless Backend: Built entirely on AWS Lambda, API Gateway, and S3 for a cost-effective and auto-scaling solution.
- Interactive Frontend: A clean, modern, and responsive user interface created with Python's Streamlit framework.
- Persistent Storage: All generated blogs are automatically saved to an Amazon S3 bucket with a timestamped filename.
- Custom Theming: Features a sleek dark theme for a better user experience.

---
🛠️ Tech Stack
Frontend:
- Streamlit - For building the interactive web UI.
- Requests - For making HTTP requests to the backend API.

Backend:
- AWS Lambda - For serverless compute and backend logic.
- Amazon Bedrock - For generative AI capabilities.
- Amazon API Gateway - To create and manage the REST API endpoint.
- Amazon S3 - For durable object storage.
- AWS IAM - For managing permissions and roles.

Programming Language:
- Python 3.9+

---
🚀 Setup and Installation
To get this project running, you need to set up the AWS backend first, followed by the local frontend.

1. Backend Setup (AWS)
   **Prerequisites:** An AWS account with access to Lambda, API Gateway, S3, and Amazon Bedrock.

   - **Create an S3 Bucket:**
     Navigate to the S3 console and create a new bucket (e.g., `awsstoragebloggeneration`). Note down the bucket name.

   - **Create an IAM Role:**
     Go to the IAM console and create a new Role.
     Choose AWS service as the trusted entity and Lambda as the use case.
     Attach the following policies:
       - AWSLambdaBasicExecutionRole (for CloudWatch logs)
       - AmazonS3FullAccess (or a more restrictive policy allowing `s3:PutObject` to your bucket).
       - AmazonBedrockFullAccess (for invoking the model).
     Name the role (e.g., `BlogGeneratorLambdaRole`) and create it.

   - **Create the Lambda Function:**
     Navigate to the Lambda console and create a new function.
     - Select Author from scratch.
     - Function name: `BlogGeneratorFunction`.
     - Runtime: Python 3.9 (or newer).
     - Architecture: x86_64.
     - Permissions: Choose Use an existing role and select the `BlogGeneratorLambdaRole` you just created.
     - Copy the code from `lambdaFunction.py` and paste it into the Lambda code editor.
     - Go to Configuration > Environment variables and add a new variable:
       - Key: `S3_BUCKET_NAME`
       - Value: `your-s3-bucket-name`
     - Deploy the function.

   - **Create an API Gateway Trigger:**
     In your Lambda function's overview, click Add trigger.
     - Select API Gateway.
     - Choose Create a new API.
     - Type: REST API.
     - Security: Open.
     - Click Add.
     - Once created, an API endpoint URL will be generated. Copy this URL.

2. Frontend Setup (Local Machine)
   **Prerequisites:** Python 3.9+ and pip installed.

   - Clone the Repository:
     '''
     git clone https://github.com/your-username/your-repo-name.git
     cd your-repo-name
     '''

   - Create a Virtual Environment:
     '''
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     '''

   - Install Dependencies:
     '''
     pip install -r requirements.txt
     '''

   - Configure the API Endpoint:
     Open the `frontend.py` file.
     Find the `API_GATEWAY_URL` variable and paste the URL you copied from the API Gateway setup.
     '''
     API_GATEWAY_URL = "https://your-api-id.execute-api.us-east-1.amazonaws.com/dev/blog-generation"
     '''

   - Run the Streamlit App:
     '''
     streamlit run frontend.py
     '''
     Your web browser should automatically open with the application running!

---
💡 Usage
- Open the web application in your browser.
- Enter any topic you want a blog about in the text input field.
- Click the "✨ Generate Blog" button.
- Wait a few moments for the AI to process the request.
- The generated blog will appear on the screen in an expandable box.

---
🎨 Theming
The dark theme is configured by default using the `.streamlit/config.toml` file. 
You can customize the colors in this file to match your personal preference.

---
🔮 Future Improvements
- [ ] Model Selection: Add a dropdown to allow users to choose from different Bedrock models (e.g., Anthropic Claude).
- [ ] Blog History: Implement a feature to view previously generated blogs directly in the UI (by listing objects from the S3 bucket).
- [ ] "Surprise Me" Button: Add a button to generate a blog on a random, trending topic.
- [ ] Containerize: Dockerize the Streamlit application for easier deployment.

---
📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
