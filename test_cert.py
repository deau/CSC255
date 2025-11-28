import os
import tempfile

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from crypto.cert import create_certificate, verify_certificate
from crypto.cert import stub_create_certificate, stub_verify_certificate


def create_test_keys(output_dir):
    """Create test RSA key pair for testing certificate functions."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    
    private_key_path = os.path.join(output_dir, "private_key.pem")
    with open(private_key_path, "wb") as file:
        file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))
    
    public_key = private_key.public_key()
    public_key_path = os.path.join(output_dir, "public_key.pem")
    with open(public_key_path, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    
    return private_key_path, public_key_path


def test_certificate_creation_and_verification():
    print("Testing Certificate Creation and Verification Module")
    print("=" * 60)
    
    with tempfile.TemporaryDirectory() as temp_dir:
        private_key_path, public_key_path = create_test_keys(temp_dir)
        try:
            cert_path = create_certificate(public_key_path, temp_dir)
            is_valid = verify_certificate(cert_path)
            print(f"Certificate valid: {is_valid}")
            if not is_valid:
                return False
        except Exception as e:
            print(f"Certificate verification failed: {e}")
            return False
    print("=" * 60)
    return True


def test_stub_functions():
    """Test the stub functions for parallel development."""
    print("Testing Stub Functions")
    print("=" * 60)

    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"\n1. Testing stub certificate creation...")
        stub_cert_path = stub_create_certificate("dummy_key.pem", temp_dir)
        if os.path.exists(stub_cert_path):
            print(f"   ✓ Stub certificate created: {os.path.basename(stub_cert_path)}")
        else:
            print(f"   ✗ Stub certificate not created")
            return False
        
        print(f"\n2. Testing stub certificate verification...")
        is_valid = stub_verify_certificate(stub_cert_path)
        if is_valid:
            print(f"   ✓ Stub verification returned True for existing file")
        else:
            print(f"   ✗ Stub verification should return True")
            return False
        
        is_valid = stub_verify_certificate("nonexistent.pem")
        if not is_valid:
            print(f"   ✓ Stub verification returned False for non-existent file")
        else:
            print(f"   ✗ Stub verification should return False")
            return False
    
    print("\n" + "=" * 60)
    print("✓ STUB TESTS PASSED!")
    print("=" * 60)
    return True


if __name__ == "__main__":
    try:
        success = test_certificate_creation_and_verification()
        if success:
            test_stub_functions()
    except ImportError as e:
        print(f"\n✗ Import error: {e}")
        print("\nMake sure to install dependencies:")
        print("  pip install -r requirements.txt")
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
