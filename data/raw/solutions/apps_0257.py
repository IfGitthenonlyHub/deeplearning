import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgZGVxdWUKCmNsYXNzIFNvbHV0aW9uOgogICAgZGVmIG1heFByb2JhYmlsaXR5KHNlbGYsIG46IGludCwgZWRnZXMsIHN1Y2NQcm9iLCBzdGFydDogaW50LCBlbmQ6IGludCkgLT4gZmxvYXQ6CgogICAgICAgIG0gPSBbe30gZm9yIGkgaW4gcmFuZ2UobildCiAgICAgICAgZm9yIGVkZ2UsIGQgaW4gemlwKGVkZ2VzLCBzdWNjUHJvYik6CiAgICAgICAgICAgIHMsIGUgPSBlZGdlCiAgICAgICAgICAgIG1bc11bZV0gPSBtW2VdW3NdID0gZAoKICAgICAgICByZXMgPSBbMF0gKiBuCiAgICAgICAgcmVzW3N0YXJ0XSA9IDEKICAgICAgICBxID0gW1stMSwgc3RhcnRdXQoKICAgICAgICB3aGlsZSBxIGFuZCByZXNbZW5kXSA9PSAwOgogICAgICAgICAgICB0bXAgPSBoZWFwcS5oZWFwcG9wKHEpCiAgICAgICAgICAgIHByb2IsIGN1ciA9IC10bXBbMF0sIHRtcFsxXQogICAgICAgICAgICByZXNbY3VyXSA9IHByb2IKICAgICAgICAgICAgZm9yIG54dCwgbnAgaW4gbVtjdXJdLml0ZW1zKCk6CiAgICAgICAgICAgICAgICBpZiByZXNbbnh0XSAhPSAwOiBjb250aW51ZQogICAgICAgICAgICAgICAgaGVhcHEuaGVhcHB1c2gocSwgWy1ucCAqIHByb2IsIG54dF0pCiAgICAgICAgcmV0dXJuIHJlc1tlbmRd").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
