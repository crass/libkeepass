# -*- coding: utf-8 -*-

__all__ = ['Twofish']

# Add fake modules removed from pyCrypto by pyCryptodome that CryptoPlus expects, but
# doesn't use.
try:
    from Crypto.Cipher import XOR
    del XOR
except ImportError:
    import Crypto.Cipher
    Crypto.Cipher.XOR = None

try:
    from Crypto.Util import randpool
    del randpool
except ImportError:
    import types, sys
    import Crypto.Util
    Crypto.Util.randpool = types.ModuleType("randpool")
    sys.modules['Crypto.Util.randpool'] = Crypto.Util.randpool

try:
    from CryptoPlus.Cipher import python_Twofish as Twofish
except ImportError:
    class _python_Twofish(object):
            def __getattribute__(self, k):
                raise IOError('Using pyCrypto which does not support Twofish encryption, try using CryptoPlus')
    Twofish = _python_Twofish()
