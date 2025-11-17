import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Zm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToNCglzdD1pbnB1dCgpDQoJcT1pbnQoaW5wdXQoKSkNCglxaT1saXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkNCgluPWxlbihzdCkNCgl0cmFja2VyPTANCgkjIGxhc3RDbG9zZT0tMQ0KCWFucz1bLTFdKm4NCglzdGFjaz1bXQ0KCWZvciBpIGluIHJhbmdlKG4tMSwtMSwtMSk6DQoJCWlmIHN0W2ldPT0nKSc6DQoJCQlzdGFjay5hcHBlbmQoaSsxKQ0KCQkJaWYgaSE9bi0xOg0KCQkJCWFuc1tpXT1hbnNbaSsxXQ0KCQkJIyBsYXN0Q2xvc2U9aSsxDQoJCQl0cmFja2VyLT0xDQoJCWVsaWYgdHJhY2tlcjwwIGFuZCBzdFtpXT09JygnOg0KCQkJYW5zW2ldPXN0YWNrLnBvcCgpDQoJCQl0cmFja2VyKz0xDQoJIyBwcmludChhbnMpDQoJZm9yIGkgaW4gcmFuZ2UocSk6DQoJCXByaW50KGFuc1txaVtpXS0xXSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
