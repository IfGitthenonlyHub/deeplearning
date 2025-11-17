import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dCA9IGludChpbnB1dCgpKQoKZm9yIF8gaW4gcmFuZ2UodCk6CiAgICBuLCBtID0gW2ludCh4KSBmb3IgeCBpbiBpbnB1dCgpLnNwbGl0KCldCiAgICBncmlkID0gW1tpbnQoeCkgZm9yIHggaW4gaW5wdXQoKS5zcGxpdCgpXSBmb3IgXyBpbiByYW5nZShuKV0KCiAgICByb3dzID0gc3VtKDEgZm9yIHggaW4gZ3JpZCBpZiBhbGwoeSA9PSAwIGZvciB5IGluIHgpKQogICAgY29scyA9IHN1bSgxIGZvciBqIGluIHJhbmdlKG0pIGlmIGFsbChncmlkW2ldW2pdID09IDAgZm9yIGkgaW4gcmFuZ2UobikpKQoKICAgIHJlcyA9IG1pbihyb3dzLCBjb2xzKQoKICAgIHByaW50KCJBc2hpc2giIGlmIHJlcyAlIDIgZWxzZSAiVml2ZWsiKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
