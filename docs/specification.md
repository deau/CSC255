# Technical Specification

**Group Members:** Alex Alvarez, Andrew Warrington, Ji Hea Hwang, Mila Savina

## Project Overview

This project implements a web-based certificate management system using Flask that allows users to generate RSA key pairs, create self-signed X.509 certificates, and verify certificate authenticity.

## Core Functions Implemented

### 1. Key Generation Module (`crypto/keygen.py`)

#### `generate_keys(output_dir: str) -> tuple[str, str]`
- **Purpose:** Generates a 2048-bit RSA key pair
- **Parameters:**
  - `output_dir`: Directory path for saving key files
- **Returns:** Tuple containing paths to private and public key files
- **Error Handling:**
  - Type checking for input parameters
  - Comprehensive exception handling for key generation failures
  - Permission and file system error handling

### 2. Certificate Management Module (`crypto/cert.py`)

#### `create_certificate(public_key_path: str, output_dir: str) -> str`
- **Purpose:** Creates a self-signed X.509 certificate
- **Parameters:**
  - `public_key_path`: Path to the public key PEM file
  - `output_dir`: Directory for saving the certificate
- **Returns:** Path to the created certificate file
- **Error Handling:**
  - File existence validation
  - Directory write permission checks
  - Key loading error handling

#### `verify_certificate(cert_path: str) -> bool`
- **Purpose:** Verifies the authenticity and validity of a certificate
- **Parameters:**
  - `cert_path`: Path to the certificate PEM file
- **Returns:** Boolean indicating certificate validity
- **Error Handling:**
  - Graceful handling of invalid signatures
  - Exception handling for malformed certificates

### 3. Flask Web Application (`app.py`)

#### Routes and Functionality

**(GET)** - Home page
- Displays main landing page with navigation options

**`/generate` (POST)** - Key and certificate generation
- Creates temporary directory for each generation session
- Calls `generate_keys()` to create RSA key pair
- Calls `create_certificate()` to create self-signed certificate
- Returns page with download links for all generated files
- Session management using temporary directory naming

**`/download/<session_id>/<filename>` (GET)** - File download
- File download with filename validation
- Allowed files: `private_key.pem`, `public_key.pem`, `certificate.pem`
- Uses `secure_filename()` for security
- Path traversal protection

**`/authenticate` (GET/POST)** - Certificate verification
- GET: Displays upload form
- POST: Handles certificate file upload and verification
- Validates file type (.pem only)
- Calls `verify_certificate()` for authentication
- Returns success or failure page based on verification result
- File size limit: 1MB

## Technical Dependencies

- **Python:** 3.8+
- **cryptography:** RSA key generation, X.509 certificates, digital signatures
- **Flask:** Web framework for routing and HTTP handling
