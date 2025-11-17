import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoKZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgQ291bnRlcgoKZGVmIGFucyhTKToKCWZyZXFzID0gQ291bnRlcihTKQoJYXJnX21heCA9IG1heChmcmVxcywga2V5PWZyZXFzLmdldCkKCWQgPSB7CgkJJ1InOiAnUCcsCgkJJ1AnOiAnUycsCgkJJ1MnOiAnUicKCX0KCXJldHVybiBkW2FyZ19tYXhdKmxlbihTKQoKVCA9IGludChpbnB1dCgpKQpmb3IgdCBpbiByYW5nZShUKToKCVMgPSBpbnB1dCgpCglwcmludChhbnMoUykp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
