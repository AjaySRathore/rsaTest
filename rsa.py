from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


class RSAPrivatekey:
    def __init__(self, p, q, e) -> None:
        self.n = p * q
        self.e = e
        phi = (p-1) * (q-1)
        self.d = pow(e, -1, mod=phi)
        self.p = p
        self.q = q
        self.dmp1 = self.d % (p-1)
        self.dmq1 = self.d % (q-1)
        self.iqmp = pow(q, -1, mod=p)
    

def write_rsa_key_to_pem(key, path):
    rsa_key = rsa.RSAPrivateNumbers(
        p=key.p, q=key.q, d=key.d,
        dmp1=key.dmp1, dmq1=key.dmq1, iqmp=key.iqmp,
        public_numbers=rsa.RSAPublicNumbers(e=key.e, n=key.n)
    ).private_key(default_backend())

    pem_data = rsa_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open(path, 'wb') as pem_file:
        pem_file.write(pem_data)


if __name__ == "__main__":
    key = RSAPrivatekey(17, 31, 7)
    write_rsa_key_to_pem(key, "test.pem")