"""IDoji (Identifiable Distributed Onique Juxtaposed Identifier) library.

This module provides unique IDoji objects and the functions for generating
them. These objects can be used as a replacement for UUID to uniquely identify
or label objects of all sorts.

An IDoji can be used interchangeably with UUIDs as they encode the same
information in less visual space, although visually more appealing.  UUIDs can
also be freely converted to and from IDojis, making it a perfect replacement.

"""
import struct
from typing import List, Optional, Union
from uuid import UUID, uuid4

EMOTE_START_OFFSET = 0x0001F600
# Offsets for emote ranges we want to use
# only 256 emoticons are needed: log(2^128)/log(256)
EMOTE_OFFSETS = ((0, 79), (780, 826), (845, 888), (890, 971), (991, 993))
IDOJI_LEN = 16  # length of an IDoji


class IDoji:
    """Represents an IDoji, which is meant as an unique identifier."""

    def __init__(self, value: Optional[Union[str, UUID, int]] = None):
        """Create an IDoji from a sufficient input or randomly.

        Use either a string of 32 hexadecimaldigits, a single 128-bit integer,
        an UUID object or generate one randomly.

        :param value: UUID like value to generate the IDoji from

        """
        if not isinstance(value, (str, int, UUID, type(None))):
            raise TypeError("value not of type 'str', 'UUID', 'int' or 'None'")

        self.value = value
        initial_value: UUID

        if isinstance(value, UUID):
            initial_value = value
        elif isinstance(value, int):
            initial_value = UUID(int=value)
        elif isinstance(value, str):
            if self.valid_idoji(value):
                initial_value = self.to_uuid(value)
            else:
                initial_value = UUID(hex=value)
        else:
            initial_value = uuid4()

        self.uuid: UUID = initial_value

        emotes = self._generate_emotelist()

        nonce = [emotes[w] for w in struct.unpack("16B", self.uuid.bytes)]

        # pylint: disable=consider-using-f-string
        self.idoji = "{}{}{}{}-{}{}-{}{}-{}{}-{}{}-{}{}{}{}".format(*nonce)

    @classmethod
    def _generate_emotelist(cls) -> List[str]:
        """Generate a list of all possible emotes that can make up a IDoji."""
        emotes: List[str] = []

        for offset in EMOTE_OFFSETS:
            start, end = offset

            for char_offset in range(start, end + 1):
                emote = chr(EMOTE_START_OFFSET + char_offset)
                emotes.append(emote)

        return emotes

    @classmethod
    def _strip_idoji(cls, idoji: str) -> str:
        """Strip all non emoji characters from an IDoji for better processing.

        :param idoji: Strip unwanted characters from this value
        :returns: IDoji string representation with only emojis

        """
        emotes = cls._generate_emotelist()
        idoji_stripped = []
        for char in idoji:
            if char in emotes:
                idoji_stripped.append(char)

        return "".join(idoji_stripped)

    @classmethod
    def valid_idoji(cls, idoji: str) -> bool:
        """Check for a valid idoji string.

        :param idoji: String representation of a IDoji
        :returns: True in case of a valid idoji

        """
        if not isinstance(idoji, str):
            raise TypeError("Invalid idoji, supply string representation")

        idoji_stripped = cls._strip_idoji(idoji)

        return len(idoji_stripped) == IDOJI_LEN

    @classmethod
    def to_uuid(cls, idoji: str) -> UUID:
        """Convert the string representation of an IDoji to an UUID.

        :param idoji: IDoji string representation
        :returns: UUID object

        """
        if not cls.valid_idoji(idoji):
            raise ValueError("Invalid value given, not an IDoji")

        emotes = cls._generate_emotelist()
        idoji_stripped = cls._strip_idoji(idoji)
        indizies = []

        for emote in idoji_stripped:
            indizies.append(emotes.index(emote))

        # splat indizies since struct needs different arguments for packing
        byteval = struct.pack("16B", *indizies)

        return UUID(bytes=byteval)

    def __str__(self) -> str:
        """Output the idoji directly.

        :returns: IDoji for this object

        """
        return self.idoji

    def __int__(self):
        """Calculate the int representation of the IDoji object.

        :returns: Int value of the current IDoji

        """
        return int(self.uuid)

    def __repr__(self) -> str:
        """Return the representation on how to instantiate this IDoji.

        :returns: Representation of this IDoji

        """
        class_name = type(self).__name__
        return f"{class_name}({str(self.uuid)!r})"

    def __eq__(self, other):
        """Comparison operator for IDoji.

        :param other: Other object to compare against
        :returns: True if objects are equal

        """
        if isinstance(other, (int, str, UUID)):
            try:
                return self.uuid == type(self)(other).uuid
            except ValueError:
                return False
        elif isinstance(other, IDoji):
            return self.uuid == other.uuid

        return False

    def __lt__(self, other):
        """Comparison operator for IDoji.

        :param other: Other object to compare against
        :returns: True if objects are equal

        """
        if isinstance(other, (int, str, UUID)):
            return self.uuid < type(self)(other).uuid
        if isinstance(other, IDoji):
            return self.uuid < other.uuid

        return NotImplemented

    def __le__(self, other):
        """Comparison operator for IDoji.

        :param other: Other object to compare against
        :returns: True if objects are equal

        """
        return self < other or self == other

    def __sub__(self, other):
        """Arithmetic operator for IDoji.

        :param other: Other object to compare against
        :returns: True if objects are equal

        """
        return type(self)(int(self) - other)

    def __add__(self, other):
        """Arithmetic operator for IDoji.

        :param other: Other object to compare against
        :returns: True if objects are equal

        """
        return type(self)(int(self) + other)

    def __hash__(self):
        """Hash idoji based on its int representation.

        :returns: Hash of integer representation

        """
        return hash(int(self))


def __main():
    """Output an IDoji for use in the shell."""
    random_idoji = IDoji()
    print(random_idoji.uuid)
    print(random_idoji)


if __name__ == "__main__":
    __main()  # pragma: no cover
