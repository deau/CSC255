import os
import tempfile
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename

# Roles 2 & 3 
from crypto.keygen import generate_keys
from crypto.cert import create_certificate, verify_certificate


app = Flask(__name__)
app.secret_key = 'dev-secret-key-change-in-production'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1MB max file size

# Create temp directory for file operations
TEMP_DIR = os.path.join(os.path.dirname(__file__), 'temp')
os.makedirs(TEMP_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {'pem'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    """Generate keys and certificate"""
    try:
        # Create unique temp directory for this generation
        gen_dir = tempfile.mkdtemp(dir=TEMP_DIR)

        # Generate keys
        private_key_path, public_key_path = generate_keys(gen_dir)

        # Create certificate
        cert_path = create_certificate(public_key_path, gen_dir)

        # Store paths in session-like manner (using temp dir name as ID)
        session_id = os.path.basename(gen_dir)

        return render_template('generate.html',
                             private_key=private_key_path,
                             public_key=public_key_path,
                             certificate=cert_path,
                             session_id=session_id)

    except Exception as e:
        flash(f'Error generating keys/certificate: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/download/<session_id>/<filename>')
def download(session_id, filename):
    """Download generated files"""
    try:
        # Validate filename for security
        safe_filename = secure_filename(filename)
        if safe_filename not in ['private_key.pem', 'public_key.pem', 'certificate.pem']:
            flash('Invalid file requested', 'error')
            return redirect(url_for('index'))

        # Construct file path
        file_path = os.path.join(TEMP_DIR, session_id, safe_filename)

        if not os.path.exists(file_path):
            flash('File not found', 'error')
            return redirect(url_for('index'))

        return send_file(file_path, as_attachment=True, download_name=safe_filename)

    except Exception as e:
        flash(f'Error downloading file: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/authenticate', methods=['GET', 'POST'])
def authenticate():
    """Show authentication page and handle certificate upload"""
    if request.method == 'GET':
        return render_template('authenticate.html')

    # Handle POST - certificate upload
    try:
        if 'certificate' not in request.files:
            flash('No file uploaded', 'error')
            return redirect(url_for('authenticate'))

        file = request.files['certificate']

        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(url_for('authenticate'))

        if not allowed_file(file.filename):
            flash('Invalid file type. Please upload a .pem file', 'error')
            return redirect(url_for('authenticate'))

        # Save uploaded file to temp location
        upload_dir = tempfile.mkdtemp(dir=TEMP_DIR)
        filename = secure_filename(file.filename)
        cert_path = os.path.join(upload_dir, filename)
        file.save(cert_path)

        # Verify certificate
        is_valid = verify_certificate(cert_path)

        # Clean up uploaded file
        try:
            os.remove(cert_path)
            os.rmdir(upload_dir)
        except:
            pass

        if is_valid:
            return render_template('success.html')
        else:
            return render_template('fail.html')

    except Exception as e:
        flash(f'Error processing certificate: {str(e)}', 'error')
        return redirect(url_for('authenticate'))


@app.errorhandler(413)
def too_large(e):
    flash('File too large. Maximum size is 1MB', 'error')
    return redirect(url_for('authenticate'))


if __name__ == '__main__':
    print("=" * 60)
    print("CSC255 Group 3 Project - Flask App")
    print("=" * 60)
    print("All modules loaded successfully!")
    print("=" * 60)
    app.run(debug=True, port=5000)
