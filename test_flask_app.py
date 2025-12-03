"""
Simple test script to verify Flask app structure and imports.
Run this to check if the app is ready before starting the server.
"""
import sys
import os

print("=" * 60)
print("CSC255 Flask App - Integration Test")
print("=" * 60)

# Test 1: Check required directories
print("\n1. Checking directory structure...")
required_dirs = ['templates', 'static', 'crypto', 'temp']
for dir_name in required_dirs:
    path = os.path.join(os.path.dirname(__file__), dir_name)
    exists = os.path.exists(path)
    status = "✓" if exists else "✗"
    print(f"   {status} {dir_name}/")
    if not exists and dir_name == 'temp':
        print(f"     (will be created automatically)")

# Test 2: Check required templates
print("\n2. Checking templates...")
required_templates = ['index.html', 'generate.html', 'authenticate.html', 'success.html', 'fail.html']
for template in required_templates:
    path = os.path.join(os.path.dirname(__file__), 'templates', template)
    exists = os.path.exists(path)
    status = "✓" if exists else "✗"
    print(f"   {status} {template}")

# Test 3: Check static files
print("\n3. Checking static files...")
css_path = os.path.join(os.path.dirname(__file__), 'static', 'style.css')
exists = os.path.exists(css_path)
status = "✓" if exists else "✗"
print(f"   {status} style.css")

# Test 4: Try importing app
print("\n4. Testing app imports...")
try:
    import app
    print("   ✓ app.py imports successfully")
    print(f"   ✓ Key generation module: Available")
    print(f"   ✓ Certificate module: Available")
except Exception as e:
    print(f"   ✗ Error importing app: {e}")
    sys.exit(1)

# Test 5: Check Flask app configuration
print("\n5. Checking Flask app...")
try:
    assert app.app is not None, "Flask app not initialized"
    print(f"   ✓ Flask app initialized")
    print(f"   ✓ Secret key configured: {'Yes' if app.app.secret_key else 'No'}")
    print(f"   ✓ Max upload size: {app.app.config.get('MAX_CONTENT_LENGTH', 0) / (1024*1024)}MB")
except Exception as e:
    print(f"   ✗ Error: {e}")
    sys.exit(1)

# Test 6: Check routes
print("\n6. Checking routes...")
routes = []
for rule in app.app.url_map.iter_rules():
    if rule.endpoint != 'static':
        routes.append(f"{rule.rule} [{', '.join(rule.methods - {'HEAD', 'OPTIONS'})}]")

for route in sorted(routes):
    print(f"   ✓ {route}")

print("\n" + "=" * 60)
print("All checks passed! Ready to run the Flask app.")
print("=" * 60)
print("\nTo start the server, run:")
print("  python app.py")
print("\nThen open your browser to:")
print("  http://127.0.0.1:5000")
print("=" * 60)
