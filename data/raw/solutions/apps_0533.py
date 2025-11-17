import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("IyBjb29rIHlvdXIgZGlzaCBoZXJlCmZvciB0IGluIHJhbmdlKGludChpbnB1dCgpKSk6CiAgICBrLG49bWFwKGludCwgaW5wdXQoKS5zcGxpdCgpKQogICAgYT1saXN0KG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkpWzpuXQogICAgbHN0PVtdCiAgICBmb3IgaSBpbiByYW5nZShuKToKICAgICAgICBpZiBhW2ldPT1rOgogICAgICAgICAgICBsc3QuYXBwZW5kKGkpCiAgICBpZiBsZW4obHN0KT4wOgogICAgICAgIHByaW50KG1heChsc3QpLW1pbihsc3QpKQogICAgZWxzZToKICAgICAgICBwcmludCgwKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
