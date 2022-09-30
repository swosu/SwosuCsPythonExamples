working through
https://www.tensorflow.org/tutorials/images/segmentation

first command:
pip install git+https://github.com/tensorflow/examples.git

results:
C:\Users\EvertJ\git\SwosuCsPythonExamples\Tensor_flow>pip install git+https://github.com/tensorflow/examples.git
Collecting git+https://github.com/tensorflow/examples.git
  Cloning https://github.com/tensorflow/examples.git to c:\users\evertj\appdata\local\temp\pip-req-build-prk5xn0y
  Running command git clone --filter=blob:none -q https://github.com/tensorflow/examples.git 'C:\Users\EvertJ\AppData\Local\Temp\pip-req-build-prk5xn0y'
  Resolved https://github.com/tensorflow/examples.git to commit 3378631ec6e02e49fbbb87e4756b230c4106b9e4
  Preparing metadata (setup.py) ... done
Collecting absl-py
  Downloading absl_py-1.0.0-py3-none-any.whl (126 kB)
     |████████████████████████████████| 126 kB 2.2 MB/s
Requirement already satisfied: six in c:\users\evertj\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\local-packages\python39\site-packages (from tensorflow-examples===3378631ec6e02e49fbbb87e4756b230c4106b9e4-) (1.16.0)
Using legacy 'setup.py install' for tensorflow-examples, since package 'wheel' is not installed.
Installing collected packages: absl-py, tensorflow-examples
    Running setup.py install for tensorflow-examples ... done
Successfully installed absl-py-1.0.0 tensorflow-examples-3378631ec6e02e49fbbb87e4756b230c4106b9e4-
WARNING: You are using pip version 21.3.1; however, version 22.0.4 is available.
You should consider upgrading via the 'C:\Users\EvertJ\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip' command.

and now we are going to try to run the upgrade.

after the pip install --upgrade pip, I no longer had any complaints when I run the install command a second time.
