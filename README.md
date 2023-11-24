# transpose-pdf-filenames-to-lowercase
Transpose PDF Filenames to Lowercase.

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)
* [Configuration](#configuration)

#### <a name="prerequisites"></a>Prerequisites
* A complete install of `Python 3.x`.
* Under `Documents`, a folder labelled `News`.
* Under `Downloads`, the `PDF` files you want to rename and move.

#### <a name="setup"></a>Setup
1. Under your `USERPROFILE`, extract `transpose-pdf-filenames-to-lowercase-main.zip`.

**Example**:
```batch
C:\Users\nso89\transpose-pdf-filenames-to-lowercase-main
```
#### <a name="running-the-script"></a>Running the Script
1. Open `cmd.exe` and change the directory to the `transpose-pdf-filenames-to-lowercase-main` folder.

**Example**:
```batch
C:\Users\nso89>cd transpose-pdf-filenames-to-lowercase-main
```
2. Start the `main.py` script.

**Example**:
```batch
C:\Users\nso89\transpose-pdf-filenames-to-lowercase-main>python main.py
```

3. The script changes the file name to lowercase letters, and moves it from `Downloads` to `Documents\News`.

#### <a name="configuration"></a>Configuration
If you need to change the `SOURCE`, `Destination_PARENT` or `VALID_FILE_EXT`:

1. Open the `main.py` script in any text editor.
2. Locate the `SOURCE`, `Destination_PARENT` or `VALID_FILE_EXT` variable.

**Example**:
```python
SOURCE = Path.home().joinpath("Downloads")
Destination_PARENT = Path.home().joinpath("Documents\\News")
VALID_FILE_EXT = ".pdf"
```
3. When you finish changing the variables, save and close the editor.
