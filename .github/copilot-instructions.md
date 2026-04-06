# AI Coding Agent Instructions

## Codebase Overview

This is a **SENAC Python programming learning repository** containing educational scripts demonstrating core Python concepts and practical applications. Files are **standalone learning examples**, not a unified application.

### Key Characteristics

- **Purpose**: Educational demonstrations for SENAC programming courses
- **Structure**: ~40 independent Python scripts covering different topics
- **No framework architecture** - scripts are self-contained examples
- **Mixed dependencies**: Each script lists its required libraries in comments (e.g., `#pip install flask`)
- **Data files**: CSV and JSON files (`alunos.csv`, `alunos.json`) used as sample data in various scripts
- **External tools**: Tesseract-OCR included for text recognition tasks

---

## Topic Organization

### Database & Data Persistence
- `alunos_db.py` - MySQL database operations (create tables, CRUD operations on student records)
- `json=cadastro.py` - JSON file handling
- Data files: `alunos.csv`, `alunos.json`, `pessoas.csv`

### Data Analysis & Manipulation
- `data_pandas.py` - Pandas DataFrame operations (filtering, grouping, statistics)
- `estrutura_dados.py` - Python data structures (lists, tuples, dicts with practical examples)
- `excel_spreadsheets.py` - Excel file creation using xlsxwriter

### Web & Network
- `raspagem.py` - Web scraping with BeautifulSoup and requests
- `raspagem=senac.py`, `raspagem=urllib.py` - Variations of scraping techniques
- `flasky.py` - Flask web framework basics

### GUI & Desktop Applications
- `cep_gui.py` - Tkinter GUI with external API integration (ViaCEP postal code lookup)
- `cep_gui_aula.py` - Classroom variant of CEP GUI
- `combobox.py` - Tkinter combobox widget example
- `mp3player.py`, `mp3player=remote.py` - Audio playback
- `windowsize.py` - Window management

### Automation & Scripting
- `pyAutoGUI=Excel=ConditionalFormatting.py` - Automating Excel operations
- `PyAutoGUI=lixeira.py` - System automation (trash operations)
- `robo.py` - General automation script
- `ler_pdf_falar.py` - PDF reading + text-to-speech

### Text & Image Processing
- `ocr.py` - OCR using Tesseract
- `transcription_easyocr.py` - EasyOCR alternative
- Tesseract-OCR directory contains trained models for English and Portuguese

### Utility Scripts
- `principal.py` - Imports and uses `funcion.py` module
- `funcion.py` - Simple module with helper functions (e.g., `saudar()`)
- `primeira.py`, `imc.py`, `media_nota.py` - Basic calculation scripts
- `while-caldendar.py` - Loop and calendar demonstrations

---

## Development Patterns & Conventions

### Module Organization
- **No package structure** - scripts import directly from sibling files
- `funcion.py` serves as a utilities module (contains reusable functions)
- Import pattern: `import funcion` then `funcion.saudar()`

### Database Connections
- MySQL is the standard database backend (`alunos_db.py` uses `mysql.connector`)
- Connection details hardcoded: `host="localhost"`, `user="root"`, `password=""`, `database="escola"`
- Pattern: Define `conectar()` function, use in CRUD operations

### Data Handling Defaults
- **CSV format**: Comma-separated, with headers in first row (see `alunos.csv`)
- **JSON format**: Array of objects with fields like `nome`, `idade`, `curso` (see `alunos.json`)
- **DataFrame**: Student records with columns: `nome`, `cidade`, `idade`, `curso`, `nota`

### Error Handling
- Minimal error handling in existing code - scripts expect valid inputs
- Exception handling exists in API calls (`requests.get()` with timeout)
- Use `messagebox` for user-facing errors in Tkinter apps

### Language & Locale
- **Portuguese** - Code comments and user-facing strings are in Portuguese
- Scripts demonstrate Brazilian context (cities like São Paulo, Osasco; phone formats)

---

## Common Tasks & Patterns

### Adding a New Script
1. List required libraries in a `#pip install` comment at top
2. Keep script self-contained (don't create new modules unless reusable)
3. If it manipulates student data, use the standard fields: `nome`, `idade`, `curso`, `nota`
4. Follow existing comment style (Portuguese, concise)

### Working with Data Files
- Load CSV: `pd.read_csv('alunos.csv')` (see `data_pandas.py`)
- Load JSON: Standard `json.load()` or direct list comprehension
- Save to Excel: Use `xlsxwriter.Workbook()` pattern from `excel_spreadsheets.py`

### GUI Development
- Use `tkinter` (tk) for desktop applications
- Pattern: Create window, add widgets, bind event handlers
- For external API calls (like CEP lookup), use `requests` library
- Display results via `messagebox.showinfo()` or `messagebox.showerror()`

### External APIs
- ViaCEP API: `https://viacep.com.br/ws/{cep}/json/` - Returns address data
- HTTPBin: `https://httpbin.org/html` - Used for testing HTML scraping
- Always handle missing/error responses (check `'erro'` key in JSON)

---

## Dependencies & Tools

### Python Packages (Install as needed)
```
mysql-connector-python    # Database connections
flask                     # Web framework
beautifulsoup4            # Web scraping
requests                  # HTTP requests
pandas                    # Data analysis
xlsxwriter                # Excel file creation
easyocr                   # Optical character recognition
pyautogui                 # GUI automation
tkinter                   # Desktop GUIs (built-in)
```

### External Tools
- **Tesseract-OCR**: Pre-installed in `Tesseract-OCR/` directory with Portuguese language models
- **MySQL**: Expected to be running locally for database scripts

---

## Debugging Notes

- **Virtual environment**: `.venv/` directory exists - activate before running scripts
- **Common issues**:
  - Database scripts require MySQL running and schema named "escola"
  - CEP GUI requires internet connection for ViaCEP API
  - OCR scripts require Tesseract path configuration
  - GUI scripts require display environment (won't run in headless mode)

