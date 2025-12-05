# CSC255 Group 3 Certificate Project
### Alex Alvarez, Andrew Warrington, Ji Hea Hwang, Mila Savina

## How to Run the Flask Application

### Prerequisites

1. **Python 3.8 or higher** must be installed
2. **pip** package manager

### Installation Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd /path/to/CSC255
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Access the application:**
   - Open a web browser
   - Navigate to: `http://127.0.0.1:5000`

3. **Stop the server:**
   - Press `Ctrl+C` in the terminal

### Using the Application

#### Generate Keys and Certificate:
1. Click "Generate Keys & Certificate" on the home page
2. Keys and certificate will be automatically generated
3. Download any or all of the generated files:
   - `private_key.pem`
   - `public_key.pem`
   - `certificate.pem`

#### Verify a Certificate:
1. Click "Authenticate Certificate" on the home page
2. Upload a `.pem` certificate file
3. System will display success or failure based on verification

### Test Files

1. **`test_keygen.py`** - Tests for key generation functionality
   - Key pair generation
   - File creation and format validation
   - Error handling

2. **`test_cert.py`** - Tests for certificate operations
   - Certificate creation
   - Certificate verification
   - Validation logic

3. **`test_flask_app.py`** - Tests for web application
   - Route functionality
   - File uploads
   - Security features

### Running Tests

```bash
python test_cert.py
python test_keygen.py
python test_flask_app.py
```

