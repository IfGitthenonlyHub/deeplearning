import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbG9uZ2VzdFdQSShzZWxmLCBob3VyczogTGlzdFtpbnRdKSAtPiBpbnQ6CiAgICAgICAgc3RhY2sscmVzLGZpcnN0PTAsMCx7fQogICAgICAgIGZvciBkYXksaSBpbiBlbnVtZXJhdGUoaG91cnMpOgogICAgICAgICAgICBzdGFjaz1zdGFjaysxIGlmIGk+OCBlbHNlIHN0YWNrLTEKICAgICAgICAgICAgZmlyc3Quc2V0ZGVmYXVsdChzdGFjaywgZGF5KQogICAgICAgICAgICBpZiBzdGFjaz4wOnJlcz1kYXkrMQogICAgICAgICAgICBlbGlmIHN0YWNrLTEgaW4gZmlyc3Q6CiAgICAgICAgICAgICAgICByZXM9bWF4KHJlcyxkYXktZmlyc3Rbc3RhY2stMV0pCiAgICAgICAgcmV0dXJuIHJlcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
