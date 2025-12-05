# CSC255 Group 3 Certificate Project - Final Summary

**Course:** CSC255
**Group:** 3
**Members:** Alex Alvarez, Andrew Warrington, Ji Hea Hwang, Mila Savina

## Summary

This project implements a complete web-based certificate management system that demonstrates core concepts of public key cryptography, digital certificates, and secure web application development. The system allows users to generate RSA key pairs, create self-signed X.509 certificates, and verify certificate authenticity through aweb interface built with Flask.

## Project Objectives

The primary objectives of this project were to:

1. **Implement RSA key pair generation** using cryptographic libraries
2. **Create self-signed X.509 certificates** with formatting and digital signatures
3. **Develop certificate verification functionality** to validate certificate authenticity
4. **Build a user-friendly web interface** for certificate management operations
5. **Ensure secure file handling** and error management throughout the application

All objectives were successfully achieved, resulting in a functional certificate management system.


## Technical Implementation

### Cryptography Core

The project leverages the Python `cryptography` library to implement:

- **2048-bit RSA key generation** with proper serialization to PEM format
- **Self-signed X.509 certificate creation** with SHA256 signatures
- **Certificate verification** including signature validation, date checking, and structural validation

### Web Application Architecture

The Flask-based web application provides three main features:

1. **Key Generation and Certificate Creation**
   - Generation of complete key pair and certificate
   - Secure download capability for all generated files
   - Session-based temporary file management

2. **Certificate Authentication**
   - File upload interface with security restrictions
   - Real-time certificate verification
   - Clear success/failure feedback

3. **Security Features**
   - File type validation (.pem only)
   - File size restrictions (1MB limit)
   - Secure filename handling to prevent path traversal
   - Temporary file cleanup

## Key Accomplishments

1. **Functional Cryptographic Implementation**
   - Successfully generates valid RSA key pairs
   - Creates properly formatted X.509 certificates
   - Accurately verifies certificate authenticity

2. **Robust Error Handling**
   - Exception handling throughout the codebase
   - Type checking and input validation
   - Informative error messages

3. **Security Consciousness**
   - Input sanitization for file uploads
   - Path traversal protection
   - File type and size restrictions
   - Secure temporary file management

4. **Complete Test Coverage**
   - Unit tests for key generation module
   - Unit tests for certificate operations
   - Tests for Flask application

5. **Professional Documentation**
   - Detailed inline code comments
   - Technical specification
   - Clear setup and usage instructions

## Conclusion

Certificate Project successfully demonstrates a comprehensive understanding of public key cryptography, digital certificates, and secure web application development. The implementation is functional, secure, and well-documented, meeting all project objectives.

The project serves as both a practical tool for understanding certificate operations and a foundation for learning about real-world PKI systems. Through collaborative development, the team gained valuable experience in cryptographic programming, web security, and professional software engineering practices.
