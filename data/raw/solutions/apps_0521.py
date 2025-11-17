import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IG1hdGgNCmZvciBfIGluIHJhbmdlKGludChpbnB1dCgpKSk6DQoJbiA9IGludChpbnB1dCgpKQ0KCXhzID0gbGlzdChtYXAoaW50LGlucHV0KCkuc3BsaXQoKSkpDQoJcCxxID0gbWFwKGludCxpbnB1dCgpLnNwbGl0KCkpDQoJYW5nbGVzID0gc29ydGVkKG1hdGguYXRhbigoeC1wKS9xKSBmb3IgeCBpbiB4cykNCglwcmludChzdW0oYW5nbGVzW24vLzI6XSktc3VtKGFuZ2xlc1s6bi8vMl0pKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
