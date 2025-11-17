import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG5leHRHcmVhdGVyRWxlbWVudChzZWxmLCBuKToKICAgICAgICAgIiIiCiAgICAgICAgIDQ0MzMyMjExIC0+IC0xCiAgICAgICAgIDMzNDQyMjExIC0+IDM0MTEyMjM0CiAgICAgICAgIDIyNDQzMzExIC0+IDIzMTEyMzQ0CiAgICAgICAgIDp0eXBlIG46IGludAogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgcyA9IHN0cihuKQogICAgICAgICBsID0gbGVuKHMpCiAgICAgICAgIGRpZ2l0cyA9IFtpbnQoYykgZm9yIGMgaW4gc10KICAgICAgICAgCiAgICAgICAgIGkgPSBsIC0gMQogICAgICAgICB3aGlsZSBpID4gMCBhbmQgc1tpXSA8PSBzW2ktMV06CiAgICAgICAgICAgICBpIC09IDEKICAgICAgICAgaWYgaSA9PSAwOgogICAgICAgICAgICAgcmV0dXJuIC0xCiAgICAgICAgIAogICAgICAgICBqID0gbCAtIDEKICAgICAgICAgd2hpbGUgaiA+IGktMSBhbmQgc1tqXSA8PSBzW2ktMV06CiAgICAgICAgICAgICBqIC09IDEKICAgICAgICAgCiAgICAgICAgIGRpZ2l0c1tpLTFdLCBkaWdpdHNbal0gPSBkaWdpdHNbal0sIGRpZ2l0c1tpLTFdCiAgICAgICAgIHJlcyA9IGRpZ2l0c1s6aV0gKyBzb3J0ZWQoZGlnaXRzW2k6XSkKICAgICAgICAgcmVzID0gaW50KCcnLmpvaW4oc3RyKGQpIGZvciBkIGluIHJlcykpCiAgICAgICAgIGlmIHJlcyA+IDIgKiogMzE6CiAgICAgICAgICAgICByZXR1cm4gLTEKICAgICAgICAgcmV0dXJuIHJlcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
