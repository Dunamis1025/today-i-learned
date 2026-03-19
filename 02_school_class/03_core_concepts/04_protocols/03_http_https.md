# HTTP & HTTPS

HTTP (HyperText Transfer Protocol) and HTTPS (HTTP Secure) are application layer protocols used for communication between a client (browser) and a web server.

---

# What is HTTP?

HTTP transfers web data (HTML, images, etc.) using a request-response model.

### Key Characteristics
- Stateless (each request is independent)
- Uses TCP (port 80)
- Data is plain text (NOT secure)

### Flow
1. Client sends request  
2. Server processes  
3. Server sends response  

---

# HTTP Request

### Structure
- Request Line
- Headers
- Body (optional)

### Example
GET /index.html HTTP/1.1  
Host: example.com  
User-Agent: Chrome  

---

# HTTP Response

### Structure
- Status Line
- Headers
- Body

### Example
HTTP/1.1 200 OK  
Content-Type: text/html  

<html>...</html>  

---

# HTTP Methods

- GET → retrieve data  
- POST → send data  
- PUT → update data  
- DELETE → remove data  

---

# Status Codes

- 200 → OK  
- 404 → Not Found  
- 500 → Server Error  

---

# Problem with HTTP

- Data is NOT encrypted  
- Vulnerable to:
  - MITM attacks  
  - Packet sniffing  
  - Data theft  

---

# What is HTTPS?

HTTPS = HTTP + Encryption (SSL/TLS)

### Key Features
- Uses TCP (port 443)
- Encrypts data
- Secure communication

---

# How HTTPS Works

1. Client connects  
2. Server sends certificate  
3. Client verifies  
4. Secure key exchange  
5. Encrypted communication  

---

# SSL/TLS Certificate

- Verifies server identity  
- Issued by CA (e.g., Let's Encrypt)  
- Contains public key  

---

# Encryption

- Asymmetric → key exchange  
- Symmetric → data transfer  

---

# HTTP vs HTTPS

| Feature | HTTP | HTTPS |
|--------|------|-------|
| Security | ❌ | ✅ |
| Encryption | ❌ | ✅ |
| Port | 80 | 443 |

---

# Summary

- HTTP = fast but insecure  
- HTTPS = secure with encryption  
- Always use HTTPS  

---

# Key Idea

HTTP = postcard  
HTTPS = sealed letter 🔒
