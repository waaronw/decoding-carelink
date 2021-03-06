
import glob

class ID:
  VENDOR  = 0x0a21
  PRODUCT = 0x8001

def scan (prefix='/dev/serial/by-id/usb-', postfix='*'):
  usb_id = "%04x_%04x" % (ID.VENDOR, ID.PRODUCT)
  candidate = ''.join([prefix, usb_id, postfix])
  results = glob.glob(candidate)
  return results.pop( )

if __name__ == '__main__':
  candidate = scan( )
  print candidate

