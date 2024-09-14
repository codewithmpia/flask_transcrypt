import os
import sys
import subprocess

class FlaskTranscrypt:
    """
    FlaskTranscrypt is a Flask extension that integrates Transcrypt, a Python to JavaScript compiler.
    It automatically compiles Python files in a specified source directory to JavaScript before each request.

    Attributes:
        app (Flask): The Flask application instance.
        compiled (bool): A flag to indicate whether the compilation has been done.

    Methods:
        __init__(self, app=None): Initializes the FlaskTranscrypt object with an optional Flask app.
        init_app(self, app): Initializes the Flask app with the FlaskTranscrypt extension.
        compile_transcrypt(self): Compiles Python files to JavaScript using Transcrypt.

    Example:

    from flask import Flask
    from flask_transcrypt import FlaskTranscrypt

    app = Flask(__name__)
    transcrypt = FlaskTranscrypt(app)

    if __name__ == "__main__":
        app.run()

    In your template, add the following script tag to include the compiled JavaScript file:

    <script type="module" src="{{ url_for('static', filename='__target__/name_for_file.js') }}"></script>
    """

    def __init__(self, app=None):
        # Initialize the FlaskTranscrypt object with an optional Flask app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # Initialize the Flask app with the FlaskTranscrypt extension
        self.app = app

        # Set default configuration values for the source and target directories
        app.config.setdefault("TRANSCRYPT_SOURCE_DIR", app.static_folder)
        app.config.setdefault("TRANSCRYPT_TARGET_DIR", os.path.join(app.static_folder, "__target__"))

        # Register the compile_transcrypt method to run before each request
        app.before_request(self.compile_transcrypt)

    def compile_transcrypt(self):
        # Check if the compilation has already been done
        if not hasattr(self, "compiled"):
            # Get the source and target directories from the app configuration
            source_dir = self.app.config["TRANSCRYPT_SOURCE_DIR"]
            target_dir = self.app.config["TRANSCRYPT_TARGET_DIR"]

            # Walk through the source directory to find Python files
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    if file.endswith(".py"):
                        # Construct the full path to the source file
                        source_file = os.path.join(root, file)
                        # Run the Transcrypt compiler on the source file
                        subprocess.run([sys.executable, "-m", "transcrypt", "-b", "-n", source_file])

            # Log that the Transcrypt compilation is completed
            self.app.logger.info("Transcrypt compilation completed.")

            # Set the compiled attribute to True to avoid recompilation
            self.compiled = True
