# WSAA-assignments


This repository contains the assignments for the "Web Services and Applications" module. It includes solutions to the programming tasks, as well as supporting data files used in the assignments.

## Table of Contents

- [About](#about)
- [Files and Structure](#files-and-structure)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Running the code](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Author](#author)

## About

The **PFDA-assignments** repository holds the code and necessary files for the assignments completed as part of the **Programming for Data Analytics** course. The assignments involve applying programming techniques to analyze datasets and develop solutions based on provided tasks.

## Files and Structure

The repository includes the following files and structure:

- `.gitignore`: Specifies which files and directories should not be tracked by Git.  
- `assignment2-carddraw.py`: A Python programme that uses the Deck of Cards API to draw five cards from a deck.  
- `assignment03-cso.py`: A Python programme that retrieves the Exchequer Account dataset from the CSO and saves it.  
- `assignment04-github.py`: A Python script that updates a file in a GitHub repository by replacing 'Andrew' with '*author name*'.  
- `cso.json`: A JSON file generated as a result of running `assignment03-cso.py`.  
- `README.md`: A file providing an overview of the repository.  
- `Step_by_step.txt`: A text file located in the repository, required to demonstrate the functionality of `assignment04-github.py`.  

## Getting Started

To get started with this project, clone the repository to your local machine.

## Prerequisites

Ensure that you have Python installed on your system. 

You may also need a software like VS Code or similar to run the code. Good idea is to run virtual environment to have full compatibility.

## Installing

1. Clone the repository:
   ```bash
   git clone https://github.com/TomUszyn/WSAA-assignments.git
   
2. Navigate to the project directory:
   ```bash
   cd WSAA-assignments

## Running the Code

You can run Python files using **Visual Studio Code (VS Code)**, which is a powerful code editor with excellent support for Python.  
If you don't have VS Code installed, you can download it from [here](https://code.visualstudio.com/).

### Steps:

1. **Open the project folder** in VS Code. Your Python scripts should be located **outside** the `venv/` folder.
2. **Ensure the file path is correct.**
3. **Open the integrated terminal**: `View` > `Terminal`.
4. **Create and activate a virtual environment** to ensure compatibility and isolate dependencies:

   - Create a virtual environment (this will create a new `venv/` folder):
     ```bash
     python -m venv venv
     ```

   - Activate the virtual environment:
     - On **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - On **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```

   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

   - To deactivate the virtual environment after running:
     ```bash
     deactivate
     ```

5. **API Key Safety**  
   For security, it's recommended to store your API keys in a separate configuration file (e.g. `config.py`) rather than hardcoding them into your scripts.

   - Create a `config.py` file in your project directory:
     ```python
     # config.py
     config = {
         "githubk": "github_pat_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
     }
     ```

   - In your Python script, import the key:
     ```python
     from config import config as cfg
     apiKey = cfg["githubk"]
     ```

   - Add `config.py` to `.gitignore` to prevent it from being uploaded to GitHub:
     ```
     # .gitignore
     config.py
     ```

6. **How to Generate a GitHub API Key (Personal Access Token):**

   If you're working with the GitHub API, follow these steps to create a **Personal Access Token**:

   1. Log in to GitHub.
   2. Go to **Settings** > **Developer settings**.
   3. Click **Personal access tokens** > **Fine-grained tokens**.
   4. Give it a name and (optionally) set an expiration date.
   5. Choose the repository (or all repos) you want access for.
   6. Under **Repository permissions**, grant the necessary access (e.g., `Contents: Read and write`).
   7. Click **Generate token**.
   8. Copy and store this token securely—**you won’t be able to see it again**.
   9. Paste it into your `config.py` as shown above.

7. **Run the script** using:
   ```bash
   python filename.py
   ```

   Replace filename.py with the actual script name (e.g., `assignment03-cso.py`).


## License

This repository is licensed under the MIT License - see the [LICENCE](LICENSE) file for more details.

## Acknowledgments

Special thanks to the lecturer for providing a well-structured and practical module covering key topics such as data representation (CSV, XML, JSON), HTTP protocols, RESTful APIs, and API testing tools like Postman and CURL. The introduction to public APIs, OAuth authentication, and Flask for creating custom APIs offered valuable hands-on experience. Topics like linking to data sources, using JQuery and AJAX, and hosting web services helped connect theory to real-world applications. This module has greatly enhanced understanding of web services and API integration.

## Author

I am a student at Atlantic Technical University in Ireland, currently pursuing a Higher Diploma in Science in Computing (Data Analytics). I have a strong foundation in computing with a particular focus on data analysis and web services. My technical skills include:

* **Operating Systems**: Proficient in the Windows family and Linux (especially Ubuntu).
* **Programming**: Python programming with a focus on data analysis and web development.
* **Databases**: Basic knowledge of MySQL for data storage and management.
* **Web Technologies**: Familiar with Apache for web server management, and Flask for building dynamic web applications.
* **Scripting**: Experience with Bash scripting and YAML for automation and configuration.
* **Web Services**: Practical experience in creating and managing web applications with CRUD operations, dynamic interfaces using **AJAX**, and third-party API integration.

I am enthusiastic and hardworking, passionate about analysing real-world and virtual datasets. I enjoy working on data-driven projects that provide insights and drive decisions.