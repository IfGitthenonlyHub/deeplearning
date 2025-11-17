import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIGYoYSk6CiAgICBmb3IgaSBpbiByYW5nZShsZW4oYSkpOgogICAgICAgIGlmIGFbaV0gPCBpOiByZXR1cm4gaS0xCiAgICByZXR1cm4gbGVuKGEpLTEKCmRlZiBzb2x2ZShhKToKICAgIGkgPSBmKGEpCiAgICBqID0gbGVuKGEpIC0gMSAtIGYoYVs6Oi0xXSkKICAgIHJldHVybiAiWWVzIiBpZiBpID49IGogZWxzZSAiTm8iCgoKbiA9IGludChpbnB1dCgpKQpmb3IgaSBpbiByYW5nZShuKToKICAgIGlucHV0KCkKICAgIGEgPSBsaXN0KG1hcChpbnQsIGlucHV0KCkuc3RyaXAoKS5zcGxpdCgpKSkKICAgIHByaW50KHNvbHZlKGEpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
