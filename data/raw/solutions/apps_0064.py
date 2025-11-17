import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("eT1sYW1iZGE6WyptYXAoaW50LGlucHV0KCkuc3BsaXQoKSldCmZvciBfIGluIHJhbmdlKGludChpbnB1dCgpKSk6CiAgICBuLHQ9bWFwKGludCxpbnB1dCgpLnNwbGl0KCkpCiAgICBhPVswXSt5KCkrW3RdCiAgICBsLGg9MCxuKzEKICAgIHRsPXRoPTAKICAgIHdoaWxlIGgtbD4xOgogICAgICAgIGRsPShhW2wrMV0tYVtsXSkvKGwrMSkKICAgICAgICBkaD0oYVtoXS1hW2gtMV0pLyhuKzItaCkKICAgICAgICBpZiB0bCtkbD50aCtkaDp0aCs9ZGg7aC09MQogICAgICAgIGVsc2U6dGwrPWRsO2wrPTEKICAgIHNoLHNsPW4rMi1oLGwrMQogICAgaWYgdGw+dGg6dGwsdGg9dGgsdGw7c2gsc2w9c2wsc2gKICAgIHByaW50KHRoKyhhW2hdLWFbbF0tKHRoLXRsKSpzbCkvKHNoK3NsKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
