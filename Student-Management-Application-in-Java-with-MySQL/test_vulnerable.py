# test_vulnerable.py

import os
import subprocess
import cgi

def insecure_os_command(user_input):
    # Command Injection vulnerability
    os.system(f"ls {user_input}")

def insecure_subprocess(user_input):
    # Another Command Injection vulnerability
    subprocess.call(f"ping {user_input}", shell=True)

def insecure_file_upload():
    # Unsafe file upload example
    form = cgi.FieldStorage()
    fileitem = form['file']
    if fileitem.filename:
        # Vulnerable to path traversal attack
        filepath = "/uploads/" + fileitem.filename
        with open(filepath, 'wb') as f:
            f.write(fileitem.file.read())

def main():
    user_input = input("Enter something: ")
    insecure_os_command(user_input)
    insecure_subprocess(user_input)
    insecure_file_upload()

if __name__ == "__main__":
    main()

