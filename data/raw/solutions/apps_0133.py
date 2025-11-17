import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBzeXMgaW1wb3J0IG1heHNpemUKZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgQ291bnRlcgpjbGFzcyBTb2x1dGlvbjoKICAgIGRlZiBiYWxhbmNlZFN0cmluZyhzZWxmLCBzKToKICAgICAgICBuID0gbGVuKHMpCiAgICAgICAgcmlnaHQgPSAwCiAgICAgICAgY2hhcnMgPSBDb3VudGVyKHMpCiAgICAgICAgcmVzID0gbWF4c2l6ZQogICAgICAgIGZvciBsZWZ0IGluIHJhbmdlKG4pOgogICAgICAgICAgICB3aGlsZSByaWdodCA8PSBuIC0gMSBhbmQgYW55KGNoYXJzW2NdID4gbiAvLyA0IGZvciBjIGluICdRV0VSJyk6CiAgICAgICAgICAgICAgICBjaGFyc1tzW3JpZ2h0XV0gLT0gMQogICAgICAgICAgICAgICAgcmlnaHQgKz0gMQogICAgICAgICAgICBpZiBhbGwoY2hhcnNbY10gPD0gbiAvLyA0IGZvciBjIGluICdRV0VSJyk6CiAgICAgICAgICAgICAgICByZXMgPSBtaW4ocmVzLCByaWdodCAtIGxlZnQpCiAgICAgICAgICAgIGNoYXJzW3NbbGVmdF1dICs9IDEKICAgICAgICByZXR1cm4gcmVz").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
