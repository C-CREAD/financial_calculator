# Financial Calculator (Flask Version)

## Table of Contents
- [Description](#description)
- [Intallation](#installation)
- [Usage](#usage)
- [Credits](#credits)


## Description
This is the Flask version of the terminal capstone project illustrating a financial calculator. This small project is showcased using the Flask Web Framework, allowing users to calculate their investments and bonds via standard HTML and Bootstrap CSS as the front end and Flask with Python as the back end. If you would like to see the terminal version of this project, [click here.](https://github.com/C-CREAD/financial_calculator/tree/main)

As mentioned in the main branch, you will have access to the following options: 
1. Investment - Calculates the user's potential investment through simple or compound interest over a certain period.
2. Bond - Calculates the user's potential bond repayment of a house over a certain period.


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
     python financial_calculator.py 
     ```
8. Access the following link shown in your terminal:
     ```sh
     http://127.0.0.1:5000
     ```
     ![image](https://github.com/user-attachments/assets/814f610a-8dc0-4737-9599-2a41fc11250d)


## Usage
Once the project is installed, a menu will be displayed showing the following options between **investment** and **bond**
![image](https://github.com/user-attachments/assets/421fd520-c82c-4815-ac64-54840deb9658)


### Investment
For this option, you are requested to enter the following:
1. Enter the deposit amount as an integer or float. 
2. Enter the interest rate as an integer or float (excluding the percentage symbol %).
3. Enter the number of years to invest as an integer.
4. Enter the 'Calculate Returns' button after entering the necessary values to display the results:
   - User Input.
     ![image](https://github.com/user-attachments/assets/95466bc1-1f09-4278-baff-abe2bb55a121)

   - Results.
     ![image](https://github.com/user-attachments/assets/80b599dd-9258-4b7b-a3a6-973706eeb8d7)

### Bond
For this option, you are requested to enter the following:
1. Enter the present value of the house as an integer or float.
2. Enter the interest rate as an integer or float (excluding the percentage symbol %).
3. Enter the number of months to repay the bond as an integer.
4. Enter the 'Calculate Repayment' button after entering the values to display the results:
   - User Input.
     ![image](https://github.com/user-attachments/assets/cf14de74-183c-443a-bfc4-c49fb1b9f9fa)

   - Results.
     ![image](https://github.com/user-attachments/assets/933de3ce-929b-41a7-907e-44c3d5d091d6)


## Credits
Shingai Dzinotyiweyi [GitHub Profile](https://github.com/C-CREAD)

[Repository Link](https://github.com/C-CREAD/financial_calculator/tree/version_flask) 
