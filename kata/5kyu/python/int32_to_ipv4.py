def int32_to_ip(int32):
    return '{}.{}.{}.{}'.format(int32 >> 24, (int32 >> 16) & 0xFF, (int32 >> 8) & 0xFF, int32 & 0xFF)
