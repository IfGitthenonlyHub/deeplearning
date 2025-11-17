import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBtYXRoIGltcG9ydCAqCmZvciBfIGluIHJhbmdlKGludChpbnB1dCgpKSk6CgluPWludChpbnB1dCgpKQoJYT1saXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkKCXo9YS5jb3VudCgxKS1hLmNvdW50KDIpCgljPWFbOm5dCglkPWFbbjpdCglqaz17MDowfQoJYj0wCglmb3IgaSBpbiByYW5nZShuKToKCQl4PWRbaV0KCQlpZiB4PT0xOgoJCQliLT0xCgkJZWxzZToKCQkJYis9MQoJCWlmIGIgbm90IGluIGprOgoJCQlqa1tiXT1pKzEKCWFucz0xMDAwMDAwCgliPTAKCWk9MQoJaWYgej09MDoKCQlhbnM9MAoJZm9yIHggaW4gY1s6Oi0xXToKCQlpZiB4PT0xOgoJCQliLT0xCgkJZWxzZToKCQkJYis9MQoJCWlmIC16LWIgaW4gams6CgkJCWFucyA9IG1pbihhbnMsaStqa1stei1iXSkKCQlpKz0xCglpZiAteiBpbiBqazoKCQlhbnM9bWluKGFucyxqa1stel0pCglwcmludChhbnMp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
