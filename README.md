# Financial Calculator (FastAPI Version)

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)


## Description
This is the FastAPI version of the terminal capstone project illustrating a financial calculator. The web app will showcase a menu for the following two operations:
1. Investment - Calculates the user's potential investment through simple or compound interest over a certain period.
2. Bond - Calculates the user's potential bond repayment of a house over a certain period.

To visit other versions of this project, click on the following links:
- [Flask Version](https://github.com/C-CREAD/financial_calculator/tree/version_flask)
- [Terminal Version](https://github.com/C-CREAD/financial_calculator/tree/main)

## Installation 
To install this project on your computer, you can run the following commands:
1. Create a directory (folder) where you wish to install the project.
2. Open your terminal/command prompt and navigate to the selected directory
3. In this directory, type the following command:
     ```sh
     git clone https://github.com/C-CREAD/financial_calculator
     ```
4. Navigate to the project folder inside the directory from above:
     ```sh
     cd financial_calculator
     ```

5. Create a virtual environment:
     ```sh
     python -m venv .venv
     ```

6. Install the required packages:
     ```sh
     pip install -r requirements.txt
     ```

7. Run the program using the following command:
     ```sh
     fastapi dev financial_calculator.py
     ```
8. Access the following link shown in your terminal:
     ```sh
     http://127.0.0.1:8000
     ```
     <img width="755" height="726" alt="image" src="https://github.com/user-attachments/assets/a9887f7d-8cd4-4a56-9eaf-e7817a0b7c38" />


## Usage
Once the project is installed, a menu will be displayed showing the following options between **investment** and **bond**
<img width="953" height="491" alt="image" src="https://github.com/user-attachments/assets/55d162a4-8a4a-4c58-a88d-e0032c26c19c" />


### Investment
For this option, you are requested to enter the following:
1. Enter the deposit amount as an integer or float. 
2. Enter the interest rate as an integer or float (excluding the percentage symbol %).
3. Enter the number of years to invest as an integer.
4. Both simple and compound interests will be displayed:
   <img width="894" height="944" alt="image" src="https://github.com/user-attachments/assets/c571d72a-b813-4fe0-907f-9d487d5a5450" />

### Bond
For this option, you are requested to enter the following:
1. Enter the present value of the house as an integer or float.
2. Enter the interest rate as an integer or float (excluding the percentage symbol %).
3. Enter the number of months to repay the bond as an integer.

The bond repayment will be displayed.
<img width="933" height="939" alt="image" src="https://github.com/user-attachments/assets/fe420b63-7e89-4bac-ac8a-8e2997358103" />


### Exit Program
Enter CTRL + C in the terminal or close the web app tab.

## Credits
Shingai Dzinotyiweyi [GitHub Profile](https://github.com/C-CREAD)
