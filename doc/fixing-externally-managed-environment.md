# Fixing "externally-managed-environment" Error When Installing Python Packages

When trying to install a Python package using `pip install .`, you may encounter the following error:

- [Recommended Solution](#-recommended-solution-using-a-virtual-environment)
- [Alternative Solution](#-alternative-forcing-a-system-wide-installation-not-recommended)

```

error: externally-managed-environment

× This environment is externally managed ╰─> To install Python packages system-wide, try apt install python3-xyz, where xyz is the package you are trying to install.
```

```pgsql
If you wish to install a non-Debian-packaged Python package,
create a virtual environment using python3 -m venv path/to/venv.
Then use path/to/venv/bin/python and path/to/venv/bin/pip. 
```

```yaml

This happens because modern Debian-based systems (Ubuntu, Debian, etc.) restrict system-wide `pip` installations to protect the system’s Python environment.
```
---

## ✅ Recommended Solution: Using a Virtual Environment

A **virtual environment (venv)** allows you to install packages in an isolated environment without affecting system-wide Python.

### 🔹 **Step 1: Create a virtual environment**
Run the following command in your project directory:
```bash
python3 -m venv venv
```

his creates a folder `venv/` that will store the isolated Python environment.

### 🔹 **Step 2: Activate the virtual environment**

- On Linux/macOS:

```bash
source venv/bin/activate
```

- On Windows (Command Prompt):

```bash
venv\Scripts\activate
```

- On Windows (PowerShell):

```bash
venv\Scripts\Activate.ps1
```

### 🔹 Step 3: Install the package inside the virtual environment

Now, install your package normally:

```bash
pip install .
```

### 🔹 Step 4: Run the installed package

If your package provides a CLI command, run it like this:

```bash
zystruct
```

Otherwise, you can execute the script manually:

```bash
python src/main.py
```

### 🔹 Step 5: Deactivate the virtual environment when done

To exit the virtual environment:

```bash
deactivate
```

---

## ❌ Alternative: Forcing a System-Wide Installation (NOT RECOMMENDED)

If you really need to install the package globally (which is risky and not recommended), you can bypass the restriction using:

```bash
pip install . --break-system-packages
```
`⚠ Warning`: This can modify system-wide Python packages and potentially break dependencies. Use this method only if you fully understand the risks.

---

## 🛠 Checking Your Python Environment

To verify your Python installation and ensure that you're using the correct version:

```bash
python3 --version
pip --version
```

If pip is missing, install it using:

```bash
sudo apt install python3-pip
```

---

## 🎯 Conclusion

- `Recommended`: Use a virtual environment (venv) to keep your Python setup clean and safe.
- `Not Recommended`: Use --break-system-packages only if necessary, as it can cause system issues.

Following these steps will help you install Python packages safely without running into system restrictions. 🚀

