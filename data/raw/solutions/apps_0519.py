import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("YSxiLCpjPWxpc3QobWFwKGludCxpbnB1dCgpLnN0cmlwKCkuc3BsaXQoKSkpDQpkPVtdDQplPVtdDQpmb3IgaSBpbiByYW5nZShhKToNCiAgICBlLmFwcGVuZChjW2ldKQ0KICAgIGQuYXBwZW5kKGNbaSthXSkNCkRQMT1bWy0xIGZvciBpIGluIHJhbmdlKGEpXSBmb3IgaiBpbiByYW5nZShhKV0NCmRlZiBEUChsLHIpOg0KICAgIG5vbmxvY2FsIGQsZSxiLERQMQ0KICAgIGlmIGw+PXI6DQogICAgICAgIHJldHVybiAwDQogICAgZWxpZiBEUDFbbF1bcl0hPS0xOg0KICAgICAgICByZXR1cm4gRFAxW2xdW3JdDQogICAgZWxzZToNCiAgICAgICAgI0RQMVtsXVtyXT1tYXgoRFAxW2xdW3JdLERQKGwrMSxyKSkNCiAgICAgICAgI0RQMVtsXVtyXT1tYXgoRFAxW2xdW3JdLERQKGwsci0xKSkNCiAgICAgICAgaWYgZFtsXStiPT1kW3JdOg0KICAgICAgICAgICAgRFAxW2xdW3JdPW1heChEUDFbbF1bcl0sZVtsXStlW3JdK0RQKGwrMSxyLTEpKQ0KICAgICAgICBmb3IgaSBpbiByYW5nZShsLHIpOg0KICAgICAgICAgICAgRFAxW2xdW3JdPW1heChEUDFbbF1bcl0sRFAobCxpKStEUChpKzEscikpDQogICAgcmV0dXJuIERQMVtsXVtyXQ0KcHJpbnQoRFAoMCxhLTEpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
