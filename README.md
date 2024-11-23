[![Build and Push Docker Image](https://github.com/nogibjj/Nruta_Mini_Project_12/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Nruta_Mini_Project_12/actions/workflows/cicd.yml)

# IDS 706 Mini Project 11 - Dockerized Application

### 🏗️ Requirements
Create a simple python application containerized with a dockerfile. The goal here is to both demonstrate running your application within a docker container (using docker run terminal commands) but to also build a docker image in your CI/CD pipeline which will be pushed to Docker Hub or other container management service.

### 🛠️ Setup Instructions
### Cloning the Repository
1. Clone the repository to your local machine:
```
   git clone https://github.com/yourusername/your-repository.git
```

2. Navigate to the project directory:


### 🐳 Build the Docker Image
Build the Docker image using the Makefile
```
make build
```
This command uses the ```Dockerfile``` to create an image tagged to ```de_mini12```.

### 🚀 Run the Docker Container

1. After building the image, run the application in the Docker container:
```
make run
```

2. The Flask app will be accessible at http://127.0.0.1:8000/ on your local machine.

### 🔄 Push the Docker Image to Docker Hub
1. Login to Docker Hub
```
docker login
```

2. Tag and push the image to Docker Hub
```
make push
```

### 💻 Flask Application

The Flask app serves as a basic calculator that can handle four arithmetic operations: Add, Subtract, Multiply, and Divide. The interface is designed as an HTML form where users can input two numbers and select an operation.
	•	URL for calculator interface: http://127.0.0.1:8000/
	•	Supported Operations:
	•	Addition
	•	Subtraction
	•	Multiplication
	•	Division


### 📸 Screenshots

🔨 Docker Build and Run Process
1. Build Output: Here is a screenshot showing the output of the make build command.
<img width="902" alt="Make Build" src="https://github.com/user-attachments/assets/667e61ba-761e-421a-9c5c-8921a6ae2bdb">


2. Run Output: Screenshot of the make run command showing the application running inside the Docker container.
<img width="902" alt="Make run" src="https://github.com/user-attachments/assets/8409c08c-3348-46be-b45f-0702b4c65bb3">

🧮 Flask Application and Calculator Operations
1. Calculator Interface: This is how the user interface looks when accessing the app in the browser.
<img width="730" alt="flask app" src="https://github.com/user-attachments/assets/8f09fa74-10a0-47c0-b8d3-fca8209eb9f4">

2.	Operation Example (Multiplication): Screenshot showing the output when performing a multiplication operation.
<img width="419" alt="Flask Calculation" src="https://github.com/user-attachments/assets/c9a9ac6e-cef7-41b8-9bd8-a885f211e7b3">

🖼️ Dockerized Image
Docker Image: Screenshot of the created Docker image.
<img width="856" alt="Image" src="https://github.com/user-attachments/assets/849704ce-6374-4a38-82b6-30cd25fa0b91">

