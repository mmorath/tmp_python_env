# TMP_PYTHON_ENV

This project is structured to demonstrate the use of two different Python dependency management and packaging tools in separate but similar environments. One environment (`python_venv`) uses `pip` with a virtual environment, which is a traditional method for installing and managing Python packages. Here, `pip` is responsible for installing packages listed in a `requirements.txt` file within an isolated virtual environment. This approach is widely used due to its simplicity and direct integration with Python's ecosystem.

The other environment (`python_poetry`) utilizes `Poetry`, an advanced packaging and dependency management tool. Poetry provides an all-in-one solution for project dependency management, packaging, and publishing. It uses a `pyproject.toml` file to maintain dependencies, which allows for deterministic builds and streamlined package management. Poetry also handles virtual environments internally, eliminating the need for separate environment management.

In summary, both `pip` and `Poetry` serve the purpose of managing project dependencies, but `Poetry` offers additional features for package creation and publishing, improved dependency resolution, and simplifies the configuration with a single `pyproject.toml` file as opposed to multiple files like `requirements.txt` and `setup.py`.

In the beginning i did create a copy of the python_venv folder structure and named it python_poetry. If you want to follow along, please...steps what needs to be done are noted in the following 

To transform the existing Python application using a virtual environment (`python_venv`) to one using Poetry (`python_poetry`), you will need to carry out several steps. Below is a detailed description of how to migrate your `python_venv` project to a `python_poetry` project:

## Prequisits

Install poetry...for this a "install_poetry.sh" script exists 
with
  ```sh
  chmod +x install_poetry.sh 
  /install_poetry.sh
  export PATH="$HOME/.local/bin:$PATH"
  source $HOME/.profile
  ```
potry should be installed, Note: You may admin privileages for that 


1. **Initialize Poetry Project:**
   In the `python_poetry` directory, run `poetry init`. This command will help you create a new `pyproject.toml` file, which is the configuration file for Poetry. You will be prompted to define the project's dependencies and development dependencies; you can skip this for now if you plan to add them manually from the `requirements.txt`.

2. **Add Dependencies:**
   Review the `requirements.txt` file in your `python_venv` directory. You will add each listed package to the new Poetry project by running `poetry add <package>` for each dependency. For development dependencies (like testing libraries), use `poetry add --dev <package>`.

   For example:
   ```sh
   cd python_poetry
   poetry add requests flask
   poetry add --dev pytest
   ```

3. **Configure the Python Version:**
   Define the Python version that your project is using. You can find this information in the `python_venv` directory, likely within a configuration file or the `Dockerfile`. Specify this version in your `pyproject.toml` under `[tool.poetry.dependencies]` like so:
   ```toml
   [tool.poetry.dependencies]
   python = "^3.8"  # Use your project's Python version
   ```

4. **Migrate Scripts and Configurations:**
   If you have any scripts or configurations in `installEnv.sh` that are related to setting up the environment, you’ll need to migrate those as well. For example, environment variables can be managed outside of Poetry, but you should ensure that they are correctly set up in the environment where your Poetry-managed application runs.

5. **Update the Dockerfile:**
   You will need to update the `Dockerfile` in the `python_poetry` directory to use Poetry instead of pip. Here is an example of what the Dockerfile may look like after modification:

   ```Dockerfile
   FROM python:3.8-slim

   # Set the working directory to /app
   WORKDIR /app

   # Copy the current directory contents into the container at /app
   COPY . /app

   # Install Poetry
   RUN pip install poetry

   # Disable virtual environment creation by poetry
   # as Docker provides isolation already
   RUN poetry config virtualenvs.create false

   # Install the project dependencies
   RUN poetry install --no-dev

   # Run the app
   CMD ["python", "./src/main.py"]
   ```

6. **Remove `requirements.txt`:**
   Once you have verified that your application works with Poetry, you can remove the `requirements.txt` from the `python_poetry` directory, as it is no longer needed.

7. **Update Documentation:**
   Modify the `README.md` in the `python_poetry` directory to include instructions for setting up the project using Poetry. This should include information on how to install Poetry and how to use it to install the project's dependencies.

8. **Test the Application:**
   After setting up Poetry and updating the Dockerfile, build your Docker image and run it to ensure that everything works as expected. Test thoroughly to verify that all dependencies are correctly installed and that your application behaves correctly.

9. **Commit Changes:**
   Once you're satisfied with the setup, commit the changes to your version control system, documenting the migration from `python_venv` to `python_poetry`.

By following these steps, you should be able to successfully migrate your application from using a virtual environment with pip to managing its dependencies with Poetry.