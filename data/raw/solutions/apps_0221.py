import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAKICAgIGRlZiByYWJpbkthcnAoc2VsZiwgTCwgbnVtcyk6CiAgICAgICAgaCA9IDAKICAgICAgICBhID0gMjYKICAgICAgICBNT0QgPSAyKiozMgogICAgICAgIGZvciBpIGluIHJhbmdlKEwpOgogICAgICAgICAgICBoID0gKGggKiBhICsgbnVtc1tpXSkgJSBNT0QKICAgICAgICAgICAKICAgICAgICBhTCA9IHBvdyhhLCBMLCBNT0QpCiAgICAgICAgc2VlbiA9IHtofQogICAgICAgIGZvciBzdGFydCBpbiByYW5nZSgxLCBsZW4obnVtcyktTCsxKToKICAgICAgICAgICAgaCA9IChoICphIC0gbnVtc1tzdGFydC0xXSAqIGFMICsgbnVtc1tzdGFydCtMLTFdKSAlIE1PRAogICAgICAgICAgICBpZiBoIGluIHNlZW46CiAgICAgICAgICAgICAgICByZXR1cm4gc3RhcnQKICAgICAgICAgICAgc2Vlbi5hZGQoaCkKICAgICAgICByZXR1cm4gLTEKICAgIAogICAgZGVmIGxvbmdlc3REdXBTdWJzdHJpbmcoc2VsZiwgUzogc3RyKSAtPiBzdHI6ICAgCiAgICAgICAgbnVtcyA9IFtvcmQoY2gpLW9yZCgnYScpIGZvciBjaCBpbiBTXQogICAgICAgIGwsIHIgPSAwLCBsZW4oUykKICAgICAgICB3aGlsZSBsIDwgcjoKICAgICAgICAgICAgbWlkID0gbCArIChyLWwpIC8vIDIKICAgICAgICAgICAgaWYgc2VsZi5yYWJpbkthcnAobWlkLCBudW1zKSAhPSAtMToKICAgICAgICAgICAgICAgIGwgPSBtaWQgKyAxCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICByID0gbWlkCiAgICAgICAgc3RhcnQgPSBzZWxmLnJhYmluS2FycChsLTEsIG51bXMpCiAgICAgICAgcmV0dXJuIFNbc3RhcnQ6c3RhcnQrbC0xXQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
