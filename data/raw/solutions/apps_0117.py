import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBzeXMgaW1wb3J0IHN0ZGluCmlucHV0ID0gc3RkaW4ucmVhZGxpbmUKCnRlc3RzID0gaW50KGlucHV0KCkpCmZvciB0ZXN0IGluIHJhbmdlKHRlc3RzKToKICAgIG4sIG0gPSBsaXN0KG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkpCiAgICBhID0gW1swXSAqIG0gZm9yIF8gaW4gcmFuZ2UobildCiAgICByID0gW1tpbnQoaSkgZm9yIGkgaW4gaW5wdXQoKS5zcGxpdCgpXSBmb3IgXyBpbiByYW5nZShuKV0KICAgIGMgPSBbW2ludChpKSBmb3IgaSBpbiBpbnB1dCgpLnNwbGl0KCldIGZvciBfIGluIHJhbmdlKG0pXQogICAgeiA9IFtbLTEsIC0xXSBmb3IgXyBpbiByYW5nZShuICogbSArIDEpXQogICAgCiAgICBmb3IgaSBpbiByYW5nZShuKToKICAgICAgICBmb3IgaiBpbiByYW5nZShtKToKICAgICAgICAgICAgeltyW2ldW2pdXVswXSA9IGoKICAgIGZvciBpIGluIHJhbmdlKG0pOgogICAgICAgIGZvciBqIGluIHJhbmdlKG4pOgogICAgICAgICAgICB6W2NbaV1bal1dWzFdID0gagoKICAgIGZvciBpIGluIHJhbmdlKDEsIG4gKiBtICsgMSk6CiAgICAgICAgYVt6W2ldWzFdXVt6W2ldWzBdXSA9IGkKCiAgICBmb3IgaSBpbiBhOgogICAgICAgIHByaW50KCcgJy5qb2luKFtzdHIoaikgZm9yIGogaW4gaV0pKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
