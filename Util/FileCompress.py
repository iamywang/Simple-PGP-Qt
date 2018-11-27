import zipfile
import zlib


def write_file(str0, zipf, file):
    zipf = zipfile.ZipFile(zipf, 'w')
    zipf.writestr(file, str0, compress_type=zipfile.ZIP_DEFLATED)


def read_file(zipf, file):
    zipf = zipfile.ZipFile(zipf, 'r')
    str1 = zipf.read(file)
    return str1


def compress_txt(str0):
    str1 = zlib.compress(str0)
    return str1


def decompress_txt(str1):
    str2 = zlib.decompress(str1)
    return str2
