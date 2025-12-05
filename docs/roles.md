# CSC255 Group 3 Certificate Project - Role Assignments

**Course:** CSC255
**Group:** 3

## Role Assignments

- **Andrew Warrington** — Role 1: Flask Integrator
- **Ji Hea Hwang** — Role 2: Key Generation
- **Alex Alvarez** — Role 3: Certificate Creation & Verification
- **Mila Savina** — Role 4: Documentation, QA, Packaging

## Project Roles and Responsibilities

### Andrew Warrington — Role 1: Flask Integrator

**Primary Responsibilities:**
- Flask Web Application Development
- User interface implementation
- Route handling and application logic
- Integration of cryptographic modules

**Technical Accomplishments:**
- Integrated backend cryptography with frontend interface
- Implemented secure file handling with validation (file type: .pem only, max size: 1MB)
- Created user experience with clear navigation
- Proper HTTP request/response handling for all operations
- Safe temporary file management with cleanup procedures

### Ji Hea Hwang — Role 2: Key Generation

**Primary Responsibilities:**
- RSA Key Generation Implementation
- Cryptographic key pair generation logic
- PEM serialization and file output

**Technical Accomplishments:**
- Implemented secure key pair generation
- Handling of RSA parameters (public exponent: 65537, key size: 2048)
- Type checking and validation for input parameters
- Exception handling for cryptographic operations (ValueError, OSError, PermissionError)
- Minimal, clean code implementation

### Alex Alvarez — Role 3: Certificate Creation & Verification

**Primary Responsibilities:**
- Certificate Creation + Verification
- X.509 certificate generation
- Digital signature verification
- Ensuring crypto coherence by keeping creation and verification together

**Technical Accomplishments:**
- Created self-signed X.509 certificates
- Implemented certificate verification with multiple validation steps
- Handling of certificate expiration dates
- Cryptographic signature verification using public key infrastructure
- Kept creation and verification in same module to reduce format mismatches and subtle bugs

### Mila Savina — Role 4: Documentation, QA, Packaging

**Primary Responsibilities:**
- Coordinator with Test/QA Focus
- Documentation and coordination
- Quality assurance and integration support

**Documentation Tasks:**
- Produced `docs/specification.md` — technical description coverage.
- Produced `docs/project_summary.md` — project final summary.
- Created `docs/roles.md`.
- Update `README.md`
- Created and executed manual test checklist for complete flow validation
- Integration testing and debugging

## Collaborative Efforts

### All Team Members Participated In:

1. **Project Planning**
   - Initial design discussions
   - Architecture decisions
   - Module interface definitions

2. **Code Reviews**
   - Peer review of implementations
   - Bug identification and fixes
   - Code quality improvements

3. **Testing**
   - Manual testing of complete application
   - Bug reporting and resolution

4. **Documentation**
   - Code comments and docstrings
   - Technical specification review
   - README updates

5. **Debugging Sessions**
   - Collaborative problem-solving
   - Integration issue resolution
   - Performance optimization

## Communication and Collaboration

**Tools Used:**
- GitHub for version control (assumed)
- Regular team meetings for coordination
- Code reviews for quality assurance
- Shared documentation for consistency


The project demonstrates effective teamwork, with clear role divisions allowing for efficient parallel development while maintaining cohesive integration through regular coordination and shared API standards.
