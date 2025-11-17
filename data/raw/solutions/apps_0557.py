import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("IyBjb29rIHlvdXIgZGlzaCBoZXJlCnQ9aW50KGlucHV0KCkpCmZvciBfIGluIHJhbmdlKHQpOgogbixtPW1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKQogYT1saXN0KCkKIGZvciBfIGluIHJhbmdlKG4pOgogIGEuYXBwZW5kKDEwKQogZm9yIF8gaW4gcmFuZ2UobSk6CiAgaSxqLGs9bWFwKGludCxpbnB1dCgpLnNwbGl0KCkpCiAgZm9yIHogaW4gcmFuZ2UoaS0xLGopOgogICBhW3pdPWFbel0qawpwcmludChzdW0oYSkvL24p").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
