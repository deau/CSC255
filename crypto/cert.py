import os
import datetime

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import NameOID


def create_certificate(public_key_path: str, output_dir: str) -> str:
    if not os.path.exists(public_key_path):
        raise FileNotFoundError(f"Public key file not found: {public_key_path}")
    
    if not os.path.exists(output_dir):
        raise FileNotFoundError(f"Output directory not found: {output_dir}")
    
    if not os.access(output_dir, os.W_OK):
        raise OSError(f"Output directory is not writable: {output_dir}")
    
    private_key_path = os.path.join(os.path.dirname(public_key_path), "private_key.pem")
    if not os.path.exists(private_key_path):
        raise FileNotFoundError(f"Private key file not found: {private_key_path}")
    
    try:
        with open(public_key_path, "rb") as pub_file:
            public_key = serialization.load_pem_public_key(
                pub_file.read(), backend=default_backend() )
    except Exception as e:
        raise ValueError(f"Failed to load public key: {str(e)}")
    
    try:
        with open(private_key_path, "rb") as private_file:
            private_key = serialization.load_pem_private_key(
                private_file.read(), password=None, backend=default_backend() )
    except Exception as e:
        raise ValueError(f"Failed to load private key: {str(e)}")
    
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Illinois"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "Des Plaines"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "CSC255 Project"),
        x509.NameAttribute(NameOID.COMMON_NAME, "CSC255 self signed Certificate"),
    ])
    
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(public_key)
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
        .sign(private_key, hashes.SHA256(), default_backend())
    )
    
    cert_path = os.path.join(output_dir, "certificate.pem")
    try:
        with open(cert_path, "wb") as cert_file:
            cert_file.write(cert.public_bytes(serialization.Encoding.PEM))
    except Exception as e:
        raise OSError(f"Failed to write certificate file: {str(e)}")
    
    return cert_path


def verify_certificate(cert_path: str) -> bool:
    if not os.path.exists(cert_path):
        return False
    
    try:
        with open(cert_path, "rb") as cert_file:
            cert_data = cert_file.read()
        cert = x509.load_pem_x509_certificate(cert_data, default_backend())
        now = datetime.datetime.utcnow()
        if now < cert.not_valid_before or now > cert.not_valid_after:
            return False
        public_key = cert.public_key()
        if not isinstance(public_key, rsa.RSAPublicKey):
            return False
        if cert.issuer != cert.subject:
            return False
    except Exception:
        return False
    
    return True


def stub_create_certificate(public_key_path: str, output_dir: str) -> str:
    """
    Stub version of create_certificate for testing and parallel development.
    Creates a dummy certificate file that mimics real behavior.
    
    Args:
        public_key_path: Path to the PEM-encoded public key file (not used in stub)
        output_dir: Directory where the certificate should be saved
    
    Returns:
        str: Full path to the created stub certificate file
    """
    cert_path = os.path.join(output_dir, "certificate.pem")
    stub_cert_content = """-----BEGIN CERTIFICATE-----
MIICpDCCAYwCCQDU7T0oqsKx5TANBgkqhkiG9w0BAQsFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjMwMTAxMDAwMDAwWhcNMjQwMTAxMDAwMDAwWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCz
-----END CERTIFICATE-----"""
    
    os.makedirs(output_dir, exist_ok=True)
    with open(cert_path, 'w') as f:
        f.write(stub_cert_content)
    
    return cert_path


def stub_verify_certificate(cert_path: str) -> bool:
    """
    Stub version of verify_certificate for testing and parallel development.
    Returns True if file exists, False otherwise.
    
    Args:
        cert_path: Path to the certificate file to verify
    
    Returns:
        bool: True if file exists, False otherwise
    """
    return os.path.exists(cert_path)
