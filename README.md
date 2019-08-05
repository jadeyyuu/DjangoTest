# DjangoTest
This is Diango Grils Projct and Food Service Test Cases Sammary.

## Authors
* **Jade Zeng** - *Initial work* - [GitHub](https://github.com/jadeyyuu)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
You need to install the Project from other responsability. This is just test for the project.

### Installing
A step by step series of examples that tell you how to get a development env running.

Start by downloading and installing the selenium python package.
The command is:
```
pip install -U selenium 
```
Next we need to download the actual Selenium web drivers.
The documentations requires that you install then in the Windows path.  
Use this command to find the path:
```
python -c "import sys; print(sys.executable)"
```
An alternate way you can do this is to add the chrome driver and other drivers in the same location as python within a VENV.

## Test Cases List

### Diango Girls Blog
  * [blog1_ATS_login](https://github.com/jadeyyuu/DjangoTest/blob/master/DjangoBlogTest/blog1_ATS_login.py): Test the login and logout function for Admin page.
  * [blog2_ATS_new](https://github.com/jadeyyuu/DjangoTest/blob/master/DjangoBlogTest/blog2_ATS_new.py): Test add new blog on the home page.
  * [blog3_ATS_edit](https://github.com/jadeyyuu/DjangoTest/blob/master/DjangoBlogTest/blog3_ATS_edit.py): Test edit the exit blog on the admin page.
  * [blog4_ATS_delete](https://github.com/jadeyyuu/DjangoTest/blob/master/DjangoBlogTest/blog4_ATS_delete.py): Test delete the exit blog on the admin page.
  
### Maverick Food Service

