import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtVHJpcGxldHMoc2VsZiwgbnVtczE6IExpc3RbaW50XSwgbnVtczI6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIAogICAgICAgIGRlZiBoZWxwZXIoYSwgYik6CiAgICAgICAgICAgIGNvdW50ID0gQ291bnRlcih4ICoqIDIgZm9yIHggaW4gYSkKICAgICAgICAgICAgcmV0dXJuIHN1bShjb3VudFt4ICogeV0gZm9yIHgsIHkgaW4gaXRlcnRvb2xzLmNvbWJpbmF0aW9ucyhiLCAyKSkKCiAgICAgICAgcmV0dXJuIGhlbHBlcihudW1zMSwgbnVtczIpICsgaGVscGVyKG51bXMyLCBudW1zMSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
