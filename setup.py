from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="flask-transcrypt",
    version="0.1.1", 
    py_modules=["flask_transcrypt"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "transcrypt"
    ],
    description="Flask extension to integrate Transcrypt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="codewithmpia",
    author_email="codewithmpia@gmail.com",
    url="https://github.com/codewithmpia/flask_transcrypt",
    project_urls={
        "Source": "https://github.com/codewithmpia/flask_transcrypt",
        "Tracker": "https://github.com/codewithmpia/flask_transcrypt/issues",
        "Author": "https://github.com/codewithmpia",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Framework :: Flask"
    ],
)
