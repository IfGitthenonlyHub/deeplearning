import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgc3ViYXJyYXlzV2l0aEtEaXN0aW5jdChzZWxmLCBBLCBLKToKICAgICAgICByZXR1cm4gc2VsZi5hdE1vc3RLKEEsIEspIC0gc2VsZi5hdE1vc3RLKEEsIEsgLSAxKQoKICAgIGRlZiBhdE1vc3RLKHNlbGYsIEEsIEspOgogICAgICAgIGNvdW50ID0gY29sbGVjdGlvbnMuQ291bnRlcigpCiAgICAgICAgcmVzID0gaSA9IDAKICAgICAgICBmb3IgaiBpbiByYW5nZShsZW4oQSkpOgogICAgICAgICAgICBpZiBjb3VudFtBW2pdXSA9PSAwOiBLIC09IDEKICAgICAgICAgICAgY291bnRbQVtqXV0gKz0gMQogICAgICAgICAgICB3aGlsZSBLIDwgMDoKICAgICAgICAgICAgICAgIGNvdW50W0FbaV1dIC09IDEKICAgICAgICAgICAgICAgIGlmIGNvdW50W0FbaV1dID09IDA6IEsgKz0gMQogICAgICAgICAgICAgICAgaSArPSAxCiAgICAgICAgICAgIHJlcyArPSBqIC0gaSArIDEKICAgICAgICByZXR1cm4gcmVz").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
