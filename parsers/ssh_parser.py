import sys

def parse_log_line(line):
    if "Failed password" in line:
        print(f"⚠️ Suspicious login attempt: {line.strip()}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ssh_parser.py <auth.log>")
    else:
        with open(sys.argv[1]) as f:
            for line in f:
                parse_log_line(line)
