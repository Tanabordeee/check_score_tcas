import subprocess
import sys
import os
required_packages = ['requests']

# Install missing packages
def install_dependencies():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", *required_packages])

# Check if dependencies are installed, if not, install them
try:
    import requests
except ImportError:
    print("Requests package not found. Installing...")
    install_dependencies()
    import requests

Id = input("เลขบัตรประชาชน : ")
password = input("password : ")

def students_lookup_func():
    students_lookup_url = "https://tcas65.as.r.appspot.com/applicants/student-lookup"
    students_lookup_payload = {
        "citizenId":Id
    }

    students_lookup = requests.post(students_lookup_url , json=students_lookup_payload)
    try:
        students_lookup_json = students_lookup.json()
        session_token = students_lookup_json['token']
        return session_token
    except Exception as e:
        print(e)

def login_func():
    login_url = "https://tcas65.as.r.appspot.com/applicants/login-with-password"
    session_token = students_lookup_func()
    headers = {
        "Sessiontoken":session_token
    }
    login_payload = {
        "citizenId": Id,
        "password": password
        }
    try:
        login = requests.post(login_url , headers=headers,json=login_payload)
        login_json = login.json()
        access_token = login_json['access_token']
        return access_token
    except Exception as e:
        print(e)
access_token = login_func()
def Tgat_Tpat_func():
    Tgat_Tpat_url = "https://tcas65.as.r.appspot.com/applicants/me/exam-applications"
    headers = {
        "Accesstoken":access_token
    }
    try:
        Tgat_Tpat = requests.get(Tgat_Tpat_url , headers=headers)
        Tgat_Tpat_json = Tgat_Tpat.json()
        Tgat_Tpat_arr = Tgat_Tpat_json['applications']
        for i in Tgat_Tpat_arr:
            print("SUBJECT : ", i['subject_name'])
            print("Score : ", i['score'])
            print("percentile score : ", i['pscore'])
            print("Tscore : " , i['tscore'])
            print("-----------------------------------")
    except Exception as e:
        print(e)

def A_level_func():
    A_level_url = "https://tcas65.as.r.appspot.com/applicants/me/exam-applications?type=alevel"
    headers = {
        "Accesstoken":access_token
    }
    try:
        A_level = requests.get(A_level_url , headers=headers)
        A_level_json = A_level.json()
        A_level_arr = A_level_json['applications']
        for j in A_level_arr:
            print("SUBJECT : ",j['subject_name'])
            print("Score : ", j['score'])
            print("percentile score : ", j['pscore'])
            print("Tscore : " , j['tscore'])
            print("-----------------------------------")
    except Exception as e:
        print(e)
Tgat_Tpat_func()
A_level_func()