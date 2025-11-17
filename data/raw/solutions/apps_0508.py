import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwppbnB1dD1zeXMuc3RkaW4ucmVhZGxpbmUKZnJvbSBiaXNlY3QgaW1wb3J0IGJpc2VjdF9sZWZ0Cm4scT1tYXAoaW50LGlucHV0KCkuc3BsaXQoKSkKc3RvcD1bXQpmb3IgaSBpbiByYW5nZShuKToKCXMsdCx4PW1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKQoJc3RvcC5hcHBlbmQoKHMsdCx4KSkKc3RvcC5zb3J0KGtleT1sYW1iZGEgeDp4WzJdKQpkPVtpbnQoaW5wdXQoKSlmb3IgaSBpbiByYW5nZShxKV0KUj1bLTFdKnEKYW5zPVstMV0qcQpmb3Igcyx0LHggaW4gc3RvcDoKCSNs44GL44KJcuOBq+OBguOCi+WMuumWk+OBrmFuc+OCknjjgavmm7TmlrDjgZfjgZ/jgYQKCWw9YmlzZWN0X2xlZnQoZCxzLXgpCglyPWJpc2VjdF9sZWZ0KGQsdC14KQoJd2hpbGUgbDxyOgoJCWlmIFJbbF09PS0xOiPmnIDlt6bjgYzjgb7jgaDnorrlrprjgZfjgabjgYTjgarjgYTloLTlkIgKCQkJYW5zW2xdPXgKCQkJUltsXT1yCgkJCWwrPTEKCQllbHNlOgoJCQlsPVJbbF0j56K65a6a44GX44Gm44GE44KL44Go44GT44KN44KS6aOb44Gw44GZCmZvciB4IGluIGFuczoKCXByaW50KHgp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
