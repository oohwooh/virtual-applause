from discord import AudioSource


class MixedAudioSource(AudioSource):
    def __init__(self, *streams):
        self.streams = []
        for stream in streams:
            self.streams.append(stream)

    def read(self):
        out_bytes = bytes()
        in_bytes = []
        if len(self.streams) >= 1:
            for stream in self.streams:
                tbytes = stream.read()
                if tbytes == b'':
                    self.streams.remove(stream)
                    if len(in_bytes) == 0:
                        return b"\0" * 3840
                elif len(tbytes) < 3840:
                    len_diff = 3840 - len(stream)
                    tbytes += "\0" * len_diff
                    in_bytes.append(tbytes)
                else:
                    in_bytes.append(tbytes)
            for i in range(0, 3840, 2):  # 3840 = 20ms of 16-bit audio
                total = int(sum([int.from_bytes((byte[i],byte[i+1]), byteorder='little') for byte in in_bytes]) / len(in_bytes))
                out_bytes += total.to_bytes(2, byteorder='little')
            return out_bytes
        return b"\0" * 3840

    def add_stream(self, stream):
        self.streams.append(stream)
