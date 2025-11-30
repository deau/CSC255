import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def generate_keys(output_dir: str) -> tuple[str, str]:
    """
    Generate a 2048-bit RSA private key and the corresponding public key, and
    writes them to files in the specified directory.

    Args:
        output_dir (str): Directory where the pem key files will be saved.

    Returns: 
        tuple[str, str]: Paths to the private key file and public key file
        (private_key_path, public_key_path)

    Raises:
        TypeError: If output_dir is not a string.
        FileNotFoundError: If output_dir cannot be created.
        PermissionError: If key files cannot be written because of permissions
        RuntimeError: If key generation or serialization fails, or if an OS
        level error occurs while writing files.
    """

    # type check passed argument
    if not isinstance(output_dir, str):
        raise TypeError(f"output_dir must be a string, got {type(output_dir).__name__}")

    try:
        # generate private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
    except ValueError as e:
        raise RuntimeError(f"Key generation failed: {e}") from e

    try:
        # serialize private key into bytes
        private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
        )

        # get public key associated with private key and serialize it into bytes
        public_key = private_key.public_key()
        public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    except ValueError as e:
        raise RuntimeError(f"Serialization failed: {e}") from e

    try:
        # create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
    except OSError as e:
        raise FileNotFoundError(f"Could not create directory {output_dir}: {e}") from e

    private_path = os.path.join(output_dir, "private_key.pem")
    public_path = os.path.join(output_dir, "public_key.pem")

    try:
        # write private key to file
        with open(private_path, "wb") as private_outfile:
            private_outfile.write(private_pem)

        # write public key to file
        with open(public_path, "wb") as public_outfile:
            public_outfile.write(public_pem)
    except PermissionError as e:
        raise PermissionError(f"Cannot write key files in {output_dir}: {e}") from e
    except OSError as e:
        raise RuntimeError(f"Failed to write key files: {e}") from e

    return private_path, public_path


def stub_generate_keys(output_dir: str) -> tuple[str, str]:
    """
    Stub version of generate_keys for testing and parallel development.
    Creates dummy private and public key files that mimic real behavior.

    Args:
        output_dir: Directory where the private and public key files should be saved

    Returns: 
        tuple[str, str]: Paths to the private key file and public key file
        (private_key_path, public_key_path)
    """

    try:
        # create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
    except OSError as e:
        raise FileNotFoundError(f"Could not create directory {output_dir}: {e}") from e

    private_path = os.path.join(output_dir, "private_key.pem")
    public_path = os.path.join(output_dir, "public_key.pem")

    stub_private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAy3IYKqZsobAWN9RKDe/Q5vX0V0cEL3KiD4c8s45sAkc1jsL1
XpKD8hBU4RWf7iGrdQ9/d08NdpGrY+1i4mMc+O7Rb/E+8zPnDwH5BeFf0f5nS52x
6OCl+MzDOIB776LL7a6Oep21EQFt4mPGm8W+tGgPDsLGceFR6K77+jgkZEnhFoEn
GhIrAqauLrnw6KBvl0OVXWS1Yb/15NDCRv0p1nWyJzjKa0+eWbMQhdMjlhblVq4j
/9gihO0rVRpXNAV/VBg9EP0WTgqLLULkbjjhsZlHdwCVrvV7dEDA9P5cGbUuk6aE
r7cFK+PzeQ91sKc6Io9kHgYf4pNBdn1A44hBYQIDAQABAoIBAAkYqZx0kvxavW+T
GhmL7LT678kcN4Nwlm7nzs6/cjRa3znqHSL0nZor4UOsHhm9XydtgTdCLVmtEzL1
WPvCzzeRJAOjj3s7yZu57Jq29DwVKiSvIRaGvt0EOMFUu1XgW0peCOhSF1eyjul1
qRpracaytWOlUU6jsrAa7NDIBFaIg68PexVJxZtaz4Vyb9bF1WRIVj7iw5vwRdZX
NLLBfdzoFeY8nyPvszfhtTrnbp6X3oaRn/HBSiyFATLTZTtvNazq+gaPe4WPM6Ka
o147L6PedABxFSR1HpuEnqW3b0rWboqSekgEEGfdwF6i75NqexW8lI+wg5W3pvIF
8IN0Uu0CgYEA7hEGmR9hsawUn6AePejtd533Ifj6GjlaE/kZVwoY9loNU0nrwLuJ
t0SZIVTyJcsjkET9BYiUPiDYz6MS0aJjIyJlw4/CwRE1Cjxf8ywJZooDtEeSejHg
rqO4elbSFdSDomTOwGgWa2ykrdw03hF1ftw7DP71/N7AkfoKEomI7RUCgYEA2sVt
FoGuJWnXdP3Ig5tpTlLTzD6QnDA/z6bTZN0UX07lMBMM1esFKbZtKUG53zDtgx2a
nxlOVqMClRCoqR6JV6lwWDc1IKmPv3efWLWno/L1+J/tK/mj5cRY0ovoFe8TgTfn
vtHwXwtOXYnee7jJgWueo8KaWGsLnHJ6hDflTh0CgYBhuuuSgKeCYLo2rWy8zZpu
uJJzh9pkWZb5DBGzAZotx9ogjwARJuvqKGcUn+KoUTRQTYHxe5gfySw4USGwnZFF
IyHTnni8+WtkwFRDZ5iUV6QdpiQjtcYe62cYEfw8qfk/+VJG+nP5tagFF5k8cL5j
TdWQCDrDjE5RnuvzoDJt4QKBgQDHqene4aozoT6wGrL3Uk6w2i1NOki3E94ZQZOr
eY6PUa0gzDIpxp5mrIVCYyclyTzsLoeg7vKtZYcEzzhvaVxF8nGDQZeuYLK+N4np
55jBrAvLxwIp4WQxXpsGRgQiiJlPlNtgL7DmvaXe/uZcGpFmGfemVAST79agCWdB
5tXUDQKBgQDY8kmiuTb/tggz8qjxg8sjxm3sZyuGyjmrts3uLGRVFKxLFqGevjKF
5vzDvFMhXep4D5VlhfUYy5Er96qC7XoXR7DchUAEj6XBiH75F5xdzZkq4LXxfvy0
myQQGt6j8UkKeFiGUuMK+r4j/8ZfMosRhjuaGd8DRSq8kWCEYPjhfA==
-----END RSA PRIVATE KEY-----
"""

    stub_public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAy3IYKqZsobAWN9RKDe/Q
5vX0V0cEL3KiD4c8s45sAkc1jsL1XpKD8hBU4RWf7iGrdQ9/d08NdpGrY+1i4mMc
+O7Rb/E+8zPnDwH5BeFf0f5nS52x6OCl+MzDOIB776LL7a6Oep21EQFt4mPGm8W+
tGgPDsLGceFR6K77+jgkZEnhFoEnGhIrAqauLrnw6KBvl0OVXWS1Yb/15NDCRv0p
1nWyJzjKa0+eWbMQhdMjlhblVq4j/9gihO0rVRpXNAV/VBg9EP0WTgqLLULkbjjh
sZlHdwCVrvV7dEDA9P5cGbUuk6aEr7cFK+PzeQ91sKc6Io9kHgYf4pNBdn1A44hB
YQIDAQAB
-----END PUBLIC KEY-----
"""

    # write stub private key to file
    with open(private_path, "w") as private_outfile:
        private_outfile.write(stub_private_key)

    # write stub public key to file
    with open(public_path, "w") as public_outfile:
        public_outfile.write(stub_public_key)

    return private_path, public_path