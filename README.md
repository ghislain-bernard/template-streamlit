## template-stremlit

[![streamlit.webp](streamlit.webp)](https://streamlit.io) 

### usage

```console
$ streamlit run view.py

  You can now view your Streamlit app in your browser.

  URL: http://127.0.0.1:8501

^C  Stopping...

$ yapf --in-place --verbose view.py module/__init__.py module/blue.py module/red.py module/white.py
Reformatting view.py
Reformatting module/__init__.py
Reformatting module/blue.py
Reformatting module/red.py
Reformatting module/white.py

$ pylint --verbose view.py module/__init__.py module/blue.py module/red.py module/white.py
Using config file /home/user/git/template-streamlit/.pylintrc

$ mypy view.py module/__init__.py module/blue.py module/red.py module/white.py
Success: no issues found in 2 source files

$ make clean

/!\ cleaning...
rm --force --recursive --verbose module/__pycache__
removed 'module/__pycache__/__init__.cpython-311.pyc'
removed 'module/__pycache__/blue.cpython-311.pyc'
removed 'module/__pycache__/white.cpython-311.pyc'
removed 'module/__pycache__/red.cpython-311.pyc'
removed directory 'module/__pycache__'
...done
```

> MIT License  
> ghislain.bernard@gmail.com
