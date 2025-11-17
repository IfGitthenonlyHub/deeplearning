import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CgogICAgZGVmIGZpbmRMZW5ndGhPZlNob3J0ZXN0U3ViYXJyYXkoc2VsZiwgYXJyOiBMaXN0W2ludF0pIC0+IGludDoKICAgICAgICBBPWFycgogICAgICAgIE4gPSBsZW4oQSkKICAgICAgICBqID0gTi0xCiAgICAgICAgd2hpbGUgaiA+PSAxIGFuZCBBW2otMV0gPD0gQVtqXToKICAgICAgICAgICAgaiAtPSAxCiAgICAgICAgcmVzID0gagogICAgICAgIGZvciBpIGluIHJhbmdlKE4pOgogICAgICAgICAgICBpZiBpID49IGogb3IgKGkgPiAwIGFuZCBBW2ldIDwgQVtpLTFdKTogCiAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICB3aGlsZSBqIDwgTiBhbmQgQVtpXSA+IEFbal06ICAgIAogICAgICAgICAgICAgICAgaiArPSAxCiAgICAgICAgICAgIHJlcyA9IG1pbihyZXMsIGotaS0xKQogICAgICAgIHJldHVybiByZXM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
