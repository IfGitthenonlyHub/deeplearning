import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4SW5jcmVhc2VLZWVwaW5nU2t5bGluZShzZWxmLCBncmlkOiBMaXN0W0xpc3RbaW50XV0pIC0+IGludDoKICAgICAgICAjIFBhZCB3aXRoIGluZiB0byBtYWtlIGltcGxlbWVudGF0aW9uIGVhc2llcgogICAgICAgIElORiA9IC0xMF8wMDAKICAgICAgICBuID0gbGVuKGdyaWQpCgogICAgICAgIHRvdGFsID0gMAogICAgICAgIG1heF9yb3dzID0gW21heChyb3csIGRlZmF1bHQ9SU5GKSBmb3Igcm93IGluIGdyaWRdCiAgICAgICAgIyBUcmFuc3Bvc2UgdGhlIGdyaWQgdG8gbWFrZSBtYXggbGVzcyBjdW1iZXJzb21lCiAgICAgICAgbWF4X2NvbHMgPSBbbWF4KGNvbCwgZGVmYXVsdD1JTkYpIGZvciBjb2wgaW4gemlwKCpncmlkKV0KCiAgICAgICAgZm9yIGksIGJlc3Rfcm93IGluIGVudW1lcmF0ZShtYXhfcm93cyk6CiAgICAgICAgICAgIGZvciBqLCBiZXN0X2NvbCBpbiBlbnVtZXJhdGUobWF4X2NvbHMpOgogICAgICAgICAgICAgICAgbmV3X2hlaWdodCA9IG1pbihiZXN0X3JvdywgYmVzdF9jb2wpCiAgICAgICAgICAgICAgICB0b3RhbCArPSBuZXdfaGVpZ2h0IC0gZ3JpZFtpXVtqXQoKICAgICAgICByZXR1cm4gdG90YWw=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
