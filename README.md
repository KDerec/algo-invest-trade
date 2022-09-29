<div id="top"></div>


<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/KDerec/algo-invest-trade/blob/master/images/logo.png"><img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Algorithms</h3>
  <p align="center">
    This student project is the #5 of my training.<br>You can follow the previous <a href="https://github.com/KDerec/chesstournamentmanager">here</a> and next one <a href="https://github.com/KDerec/litreview">here</a>.
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
### 🌱 Developed skills
- Deconstruct a **problem**.
- Develop an **algorithm** to solve a problem.
- Compare algorithms using **Big-O notation**, **time complexity** and **memory analysis**.
### 📖 Scenario
I have just joined **AlgoInvest&Trade**, a financial company specialized in investment. 
The company seeks to **optimize** its investment strategies with the help of **algorithms**, in order to generate more profits for its clients.
### 🚧 Project goal
**Found the best combination** of market stocks to buy in stocks lists define by them name, cost, and profit.  
### 🚀 Deliverable
**Bruteforce** algorithm and **dynamic programming** are use to found the best combination.  
**Plotting graph** to compare the time complexity of the two algorithms for a list of 20 stocks. 
**Display the best stocks list** to buy with invested capital and total profit.  

Result example for [data.csv](https://github.com/KDerec/algo-invest-trade/blob/master/data/data.csv) and **bruteforce algorithm**: 

    Montant du bénéfice : 99.08€.
    Liste d'action acheté : ['Action-4', 'Action-5', 'Action-6', 'Action-8', 'Action-10', 'Action-11', 'Action-13', 'Action-18', 'Action-19', 'Action-20'].
    Montant de l'investissement : 498.0€.
    Temps d'exécution du programme : 1.4999400000000005 secondes.

Graph of **time complexity** ploted with **matplotlib** for bruteforce and optimized algorithms:

<a href="https://github.com/KDerec/algo-invest-trade/blob/master/images/time_complexity.jpg"><img src="images/time_complexity.jpg"></a>

<p align="right">(<a href="#top">back to top</a>)</p>


## Built With
* [Python](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Installation
1. <a href="#python-installation">Install Python</a> ;
2. Clone the project in desired directory ;
   ```sh
   git clone https://github.com/KDerec/algo-invest-trade.git
   ```
3. Change directory to project folder ;
   ```sh
   cd path/to/algo-invest-trade
   ```
4. Create a virtual environnement *(More detail to [Creating a virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment))* ;
    * For Windows :
      ```sh
      python -m venv env
      ```
    * For Linux :
      ```sh
      python3 -m venv env
      ```
5. Activate the virtual environment ;
    * For Windows :
      ```sh
      .\env\Scripts\activate
      ```
    * For Linux :
      ```sh
      source env/bin/activate
      ```
6. Install package of requirements.txt ;
   ```sh
   pip install -r requirements.txt
   ```
7. Run main.py and let yourself be guided by the application.


### Python installation
1. Install Python. If you are using Linux or macOS, it should be available on your system already. If you are a Windows user, you can get an installer from the Python homepage and follow the instructions to install it:
   - Go to [python.org](https://www.python.org/)
   - Under the Download section, click the link for Python "3.xxx".
   - At the bottom of the page, click the Windows Installer link to download the installer file.
   - When it has downloaded, run it.
   - On the first installer page, make sure you check the "Add Python 3.xxx to PATH" checkbox.
   - Click Install, then click Close when the installation has finished.
2. Open your command prompt (Windows) / terminal (macOS/ Linux). To check if Python is installed, enter the following command (this should return a version number.):
   ``` sh
   python -V
   # If the above fails, try:
   python3 -V
   # Or, if the "py" command is available, try:
   py -V
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact
Kévin Dérécusson - kevin.derecusson@outlook.fr

Project Link: [https://github.com/KDerec/algo-invest-trade](https://github.com/KDerec/algo-invest-trade)

<p align="right">(<a href="#top">back to top</a>)</p>

<i>This student project is the #5 of my training.  
You can follow the previous <a href="https://github.com/KDerec/chesstournamentmanager">here</a> and next one <a href="https://github.com/KDerec/litreview">here</a>.</i>
