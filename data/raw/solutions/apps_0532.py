import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("bj1pbnQoaW5wdXQoKSkKbW9kdWxvPTE1NzQ2Cm51bT1bMSwxXQpmb3IgaSBpbiByYW5nZSgyLG4rMSk6CiAgICBudW0uYXBwZW5kKChudW1baS0xXStudW1baS0yXSklbW9kdWxvKQpwcmludChudW1bbl0p").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
