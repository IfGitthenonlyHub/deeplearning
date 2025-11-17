import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("bD1bXQpuPWludChpbnB1dCgpKQpmb3IgaSBpbiByYW5nZShuKToKIGwuYXBwZW5kKGxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKSkKaWYobj09MSk6CiBwcmludCgxKQplbHNlOgogYz0yCiBmb3IgaSBpbiByYW5nZSgxLG4tMSk6CiAgaWYobFtpXVswXS1sW2ldWzFdPmxbaS0xXVswXSk6CiAgIGM9YysxCiAgZWxpZihsW2ldWzBdK2xbaV1bMV08bFtpKzFdWzBdKToKICAgbFtpXVswXSs9bFtpXVsxXQogICBjPWMrMQogcHJpbnQoYyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
