import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwojc3lzLnN0ZGluID0gb3BlbigiaSIsInIiKQoKZm9yIF8gaW4gcmFuZ2UoIGludChpbnB1dCgpKSApOgoKICAgIG4sIG0gPSBsaXN0KG1hcChpbnQsICBpbnB1dCgpLnNwbGl0KCkpKQogICAgYWRqID0gWyBbXSBmb3IgXyBpbiByYW5nZShuKzEpIF0KCiAgICBmb3IgXyBpbiByYW5nZShtKToKICAgICBzcmMsIGRlc3QgPSBsaXN0KG1hcChpbnQsICBpbnB1dCgpLnNwbGl0KCkpKQogICAgIGFkaltzcmNdLmFwcGVuZChkZXN0KQogICAgIGFkaltkZXN0XS5hcHBlbmQoc3JjKQoKICAgIHByaW50KCggbWF4KCBtYXgoIFtsZW4oYSkgZm9yIGEgaW4gYWRqXSApICwgMyAgICBcCiAgaWYgYW55KCBub3Qgc2V0KGFkalt4XSkuaXNkaXNqb2ludChhZGpbeV0pICAgICBcCiAgZm9yIHggaW4gcmFuZ2UobGVuKGFkaikpIGZvciB5IGluIGFkalt4XSApICAgICBcCiAgZWxzZSBtYXgoIFtsZW4oYSkgZm9yIGEgaW4gYWRqXSApICkgKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
