# FlaskTranscrypt

FlaskTranscrypt is a Flask extension that integrates Transcrypt, a Python to JavaScript compiler. It automatically compiles Python files in a specified source directory to JavaScript before each request.

## Features

- Automatic compilation of Python files to JavaScript using Transcrypt.
- Easy integration with Flask applications.
- Configurable source and target directories.

## Installation

To install FlaskTranscrypt, you can use pip:

```bash
pip install flask-transcrypt
or 
pip3 install flask-transcrypt
```

## Usage

### Initialization

First, import and initialize the `FlaskTranscrypt` extension in your Flask application:

```python
from flask import Flask
from flask_transcrypt import FlaskTranscrypt

app = Flask(__name__)
transcrypt = FlaskTranscrypt(app)

if __name__ == "__main__":
    app.run()
```

### Configuration

You can configure the source and target directories for the Transcrypt compilation in your Flask application's configuration. If these configurations are not defined, the extension will use the default values:

```python
app.config["TRANSCRYPT_SOURCE_DIR"] = "/path/to/source/directory"
app.config["TRANSCRYPT_TARGET_DIR"] = "/path/to/target/directory"
```

By default, the source directory is set to the Flask application's static folder, and the target directory is set to `__target__` within the static folder.

### Template Integration

In your Flask template, include the compiled JavaScript file using the following script tag:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Transcrypt Example</title>
</head>
<body>
    <!-- Your HTML content goes here -->

    <!-- Include the compiled JavaScript file -->
    <script type="module" src="{{ url_for('static', filename='__target__/name_for_file.js') }}"></script>
</body>
</html>
```

Replace `name_for_file.js` with the actual name of your compiled JavaScript file.

## Example

Here is a complete example of how to use FlaskTranscrypt in a Flask application:

```python
from flask import Flask
from flask_transcrypt import FlaskTranscrypt

app = Flask(__name__)
transcrypt = FlaskTranscrypt(app)

if __name__ == "__main__":
    app.run()
```

In your template (e.g., `index.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Transcrypt Example</title>
</head>
<body>
    <!-- Your HTML content goes here -->

    <!-- Include the compiled JavaScript file -->
    <script type="module" src="{{ url_for('static', filename='__target__/name_for_file.js') }}"></script>
</body>
</html>
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgments

- [Transcrypt](https://www.transcrypt.org/) for the Python to JavaScript compiler.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
