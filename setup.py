from setuptools import setup

setup(
    name="flask-transcrypt",
    version="0.1",
    py_modules=["flask_transcrypt"],
    install_requires=[
        "Flask",
        "transcrypt"
    ],
    description="Flask extension to integrate Transcrypt",
    author="codewithmpia",
    author_email="codewithmpia@gmail.com",
    url="https://github.com/codewithmpia/flask_transcrypt",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Licence :: OSI Approved :: MIT Licence",
        "Programming Language :: Python :: 3",
        "Framework :: Flask"
    ],
)