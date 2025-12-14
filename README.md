# React2Shell Scanner

A security tool for detecting Next.js prototype pollution vulnerabilities that could lead to remote code execution.

## 📋 Description

React2Shell is a Python-based vulnerability scanner that tests web applications for prototype pollution vulnerabilities in Next.js applications. It sends specially crafted payloads to detect if a target is vulnerable to this security flaw.

## ⚠️ Disclaimer

**This tool is for educational and authorized security testing purposes only.** 

- Only test applications you own or have explicit permission to test
- Unauthorized testing may be illegal in your jurisdiction
- The author is not responsible for misuse of this tool

## 🚀 Features

- **Single URL Testing** - Test individual websites quickly
- **Batch Testing** - Scan multiple URLs from a file
- **Color-Coded Output** - Easy-to-read results with visual indicators
- **Progress Tracking** - Monitor scan progress in real-time
- **Summary Reports** - Get comprehensive statistics after batch scans

## 📦 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Install Dependencies

```bash
pip install requests
```

Or if you have a requirements.txt:

```bash
pip install -r requirements.txt
```

## 💻 Usage

### Basic Commands

```bash
# Display help
python React2Shell.py -h
python React2Shell.py --help

# Test a single URL
python React2Shell.py -u https://example.com

# Test multiple URLs from a file
python React2Shell.py -l urls.txt
```

### Options

| Option | Long Form | Description |
|--------|-----------|-------------|
| `-u` | `--url` | Test a single URL |
| `-l` | `--list` | Test multiple URLs from a text file |
| `-h` | `--help` | Display help information |

## 📝 Examples

### Testing a Single URL

```bash
python React2Shell.py -u https://vulnerable-site.com
```

**Output:**
```
✓ No Vulnerability Detected
[✓] This site appears to be secure.

📊 HTTP Status: 200
```

### Testing Multiple URLs

Create a text file named `urls.txt`:

```
https://site1.com
https://site2.com
https://site3.com
```

Run the scanner:

```bash
python React2Shell.py -l urls.txt
```

**Output includes:**
- Individual test results for each URL
- Color-coded vulnerability status
- Final summary with statistics

## 🎨 Output Interpretation

### Status Indicators

- ✓ **Green** - Site is secure, no vulnerability detected
- ⚠️ **Red** - Vulnerability detected! Site is exploitable
- ❌ **Red** - Error occurred during testing

### Summary Report

After batch scanning, you'll see:
- **Total URLs Tested** - Number of sites scanned
- **Vulnerable Sites** - How many sites are exploitable
- **Secure Sites** - How many sites are safe
- **Failed Requests** - How many tests encountered errors

## 📂 File Structure

```
react2shell/
├── React2Shell.py          # Main scanner script
├── urls.txt                # Sample URL list (optional)
├── requirements.txt        # Python dependencies (optional)
└── README.md              # This file
```

## 🔧 How It Works

1. The script sends a crafted multipart form data payload to the target
2. The payload attempts to exploit prototype pollution in Next.js
3. It executes the `id` command on vulnerable systems
4. The response is analyzed for signs of successful exploitation
5. Results are displayed with clear vulnerability status

## 🛡️ Vulnerability Details

This scanner detects a specific Next.js prototype pollution vulnerability where:
- Improperly validated user input can modify object prototypes
- Attackers can inject malicious code through form data
- Successful exploitation can lead to remote code execution

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is provided for educational purposes. Use responsibly and ethically.

## 👤 Author
### Maimo Harris (Dracula)
### https://linkedin.com/in/maimoharris
### wa.me/+237680226898
Security Research Tool - Use with caution and authorization

## 🐛 Troubleshooting

### Common Issues

**"Module 'requests' not found"**
```bash
pip install requests
```

**"Permission denied" errors**
- Ensure you have write permissions in the directory
- Run with appropriate permissions if needed

**Connection timeouts**
- Check your internet connection
- Target site may be blocking automated requests
- Try increasing timeout values in the code

**File not found (urls.txt)**
- Ensure the file exists in the same directory
- Use full file path if necessary
- Check file permissions

## 📞 Support

For issues or questions:
- Check existing documentation
- Review error messages carefully
- Ensure all prerequisites are met

---

**Remember:** Always obtain proper authorization before testing any systems you don't own.
