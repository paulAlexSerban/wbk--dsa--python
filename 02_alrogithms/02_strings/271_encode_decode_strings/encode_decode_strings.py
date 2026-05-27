from typing import List


class EncodeDecodeStrings:
    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for s in strs:
            encoded_string.append(f"{len(s)}#{s}")
        return "".join(encoded_string)

    def decode(self, s) -> List[str]:
        if not s:
            return []
        # Initialize the index to start decoding
        i = 0
        decoded_strings = []
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            decoded_strings.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decoded_strings
