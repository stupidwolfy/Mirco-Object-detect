# Mirco-Object-detect
 Microcontroller 2020 Project
 
## Pi side :camera:
* ### Setup
    * (Optional) Create and use new virtual environment
        ```{python}
        pip3 install virtualenv
        python3 -m venv env
        source ./venv/bin/activate
        ```   
    * Install requirement packages
        ```Python
        pip3 install -r requirements.txt
        ```
* ### Run
    * (Optional) Activate virtual environment
        ```Python
        source ./venv/bin/activate
        ```   
    * Generate/save setting file
        ```Python
        python3 Setting.py
        ```
        Note: Use ctrl+c to exit without save
    
    * Run main python script
        ```Python
        python3 main.py
        ```
        Note: You can pass arguments or leave it to load from saved file.

## Client side :computer:
* ### Setup
    * (Optional) Create and use new virtual environment
        ```Python
        pip3 install virtualenv
        python3 -m venv env
        ./env/Scripts/activate
        ```   
    * Install requirement packages
        ```Python
        pip3 install -r requirements.txt
        ```
    

    * Run client script
        ```Python
        python3 client_gui.py
        ```
