"""Tests for IDoji."""
from unittest.mock import MagicMock
from uuid import UUID

import pytest

# pylint: disable=import-error
import idoji as idoji_module
from idoji import IDoji


def test_idoji():
    """Tests the flawfless instantiation of an IDoji."""
    IDoji()


def test_idoji_values(uuididoji):
    """Tests that given values generate the correct IDoji."""
    assert str(IDoji(uuididoji.uuid)) == uuididoji.idoji


def test_idoji_from_idojistr(uuididoji):
    """Test that an IDoji object can be instantiated from an idoji string."""
    assert IDoji(uuididoji.idoji).uuid == UUID(uuididoji.uuid)


def test_err_on_invalid_data():
    """Tests that invalid data is recognized as such."""
    with pytest.raises(ValueError):
        IDoji("foo")  # invalid string for UUID conversion

    with pytest.raises(ValueError):
        print(IDoji(2 ** 128).uuid)  # too high for uuid

    with pytest.raises(TypeError):
        IDoji(object)  # invalid type for conversion


def test_repr(uuididoji):
    """Checks that the representation can be used to instantiate an IDoji."""
    assert (
        repr(IDoji(uuididoji.uuid))
        == "IDoji('67b8660e-831c-4f13-8fe9-dfa20d5fbbb5')"
    )


def test_int(uuididoji):
    """Checkts that the we calculate a valid int representation."""
    assert int(IDoji(uuididoji.uuid)) == int(UUID(uuididoji.uuid))


def test_hash(uuididoji):
    """Checkts that the we calculate a valid hash representation."""
    assert hash(IDoji(uuididoji.uuid)) == hash(UUID(uuididoji.uuid))


def test_to_uuid(uuididoji):
    """Tests that an idoji string is converted to an UUID object."""

    assert IDoji.to_uuid(uuididoji.idoji) == UUID(uuididoji.uuid)


def test_to_uuid_raises():
    """Tests that an invalid string raises an exception."""

    with pytest.raises(ValueError):
        IDoji.to_uuid("foo")


def test_valid_idojiid(uuididoji):
    """Tests that a valid IDoji is recognized as such."""
    assert IDoji.valid_idoji(uuididoji.idoji)

    # pure form without any extra characters
    assert IDoji.valid_idoji(uuididoji.idoji.replace("-", ""))


def test_invalid_idoji(uuididoji):
    """Tests that an invalid IDoji is recognized as such."""
    assert not IDoji.valid_idoji("foo")
    assert not IDoji.valid_idoji(uuididoji.idoji[:-1])  # remove last char


def test_valid_idojiid_throw_no_str():
    """Tests that other objects than str are not accepted for validation."""
    with pytest.raises(TypeError):
        IDoji.valid_idoji(object)


def test_compare_idoji_eq(uuididoji):
    """Checks that comparison eq of IDoji objects works."""
    assert IDoji(uuididoji.idoji) == IDoji(uuididoji.uuid)
    assert uuididoji.idoji == IDoji(uuididoji.uuid)
    assert IDoji(uuididoji.uuid) == uuididoji.idoji
    assert IDoji(uuididoji.uuid) == UUID(uuididoji.uuid)
    assert IDoji(uuididoji.uuid) == int(UUID(uuididoji.uuid))
    assert IDoji() != object()
    assert IDoji() != "foo"  # compare to invalid UUID string


def test_compare_idoji_ne(uuididoji):
    """Checks that comparison ne of IDoji objects works."""
    smaller = IDoji(int(UUID(uuididoji.uuid)) - 1)
    assert smaller != IDoji(uuididoji.uuid)
    assert uuididoji.idoji != smaller
    assert smaller != uuididoji.idoji
    assert smaller != UUID(uuididoji.uuid)
    assert smaller != int(UUID(uuididoji.uuid))
    assert IDoji() != object()
    assert IDoji(uuididoji.idoji) == IDoji(uuididoji.uuid)


def test_compare_idoji_lt(uuididoji):
    """Checks that comparison lt of IDoji objects works."""
    smaller = IDoji(int(UUID(uuididoji.uuid)) - 1)

    assert smaller < IDoji(uuididoji.uuid)
    assert smaller < uuididoji.idoji
    assert smaller < UUID(uuididoji.uuid)
    assert smaller < int(UUID(uuididoji.uuid))
    with pytest.raises(TypeError):
        assert IDoji() < object()
    with pytest.raises(ValueError):
        assert IDoji(uuididoji.idoji) < "foo"


def test_compare_idoji_le(uuididoji):
    """Checks that comparison le of IDoji objects works."""
    smaller = IDoji(int(UUID(uuididoji.uuid)) - 1)

    assert smaller <= IDoji(uuididoji.uuid)
    assert smaller <= uuididoji.idoji
    assert smaller <= UUID(uuididoji.uuid)
    assert smaller <= int(UUID(uuididoji.uuid))
    with pytest.raises(TypeError):
        assert IDoji() <= object()


def test_compare_idoji_gt(uuididoji):
    """Checks that comparison gt of IDoji objects works."""
    smaller = IDoji(int(UUID(uuididoji.uuid)) - 1)

    assert IDoji(uuididoji.uuid) > smaller
    assert uuididoji.idoji > smaller
    assert UUID(uuididoji.uuid) > smaller
    assert int(UUID(uuididoji.uuid)) > smaller
    with pytest.raises(TypeError):
        assert IDoji() > object()


def test_compare_idoji_ge(uuididoji):
    """Checks that comparison ge of IDoji objects works."""
    smaller = IDoji(int(UUID(uuididoji.uuid)) - 1)

    assert IDoji(uuididoji.uuid) >= smaller
    assert uuididoji.idoji >= smaller
    assert UUID(uuididoji.uuid) >= smaller
    assert int(UUID(uuididoji.uuid)) >= smaller
    with pytest.raises(TypeError):
        assert IDoji() >= object()


def test_compare_idoji_sub(uuididoji):
    """Checks that substraction of IDoji objects works."""
    smaller = IDoji(int(UUID(uuididoji.uuid)) - 1)

    assert IDoji(uuididoji.uuid) - 1 == smaller
    assert IDoji(uuididoji.uuid) - 0 == IDoji(uuididoji.uuid)
    with pytest.raises(ValueError):
        assert IDoji(0) - 1


def test_compare_idoji_add(uuididoji):
    """Checks that addition of IDoji objects works."""
    bigger = IDoji(int(UUID(uuididoji.uuid)) + 1)

    assert IDoji(uuididoji.uuid) + 1 == bigger
    assert IDoji(uuididoji.uuid) + 0 == IDoji(uuididoji.uuid)
    with pytest.raises(ValueError):
        assert IDoji(2 ** 128 - 1) + 1


def test_inheritance_overwrite(uuididoji):
    """Ensure that redefined functions are called on child classes."""

    class ValidIdojiError(ValueError):
        """Special exception to distinguish between tests."""

    class ToUUIDError(ValueError):
        """Special exception to distinguish between tests."""

    class StripIDojiError(ValueError):
        """Special exception to distinguish between tests."""

    class GenerateEmotelistError(ValueError):
        """Special exception to distinguish between tests."""

    class IDojiChildValidIdoji(IDoji):
        """Test childclass to ensure correct inheritance."""

        @classmethod
        def valid_idoji(cls, idoji):
            """Overwrite method and throw an exception for testing

            :param idoji: String representation of a IDoji

            """
            raise ValidIdojiError

    class IDojiChildToUUID(IDoji):
        """Test childclass to ensure correct inheritance."""

        @classmethod
        def to_uuid(cls, idoji):
            """Overwrite method and throw an exception for testing

            :param idoji: String representation of a IDoji

            """
            raise ToUUIDError

    class IDojiChildStripIDoji(IDoji):
        """Test childclass to ensure correct inheritance."""

        @classmethod
        def _strip_idoji(cls, idoji):
            """Overwrite method and throw an exception for testing

            :param idoji: String representation of a IDoji

            """
            raise StripIDojiError

    class IDojiChildGenerateEmotelist(IDoji):
        """Test childclass to ensure correct inheritance."""

        @classmethod
        def _generate_emotelist(cls):
            """Overwrite method and throw an exception for testing

            :param idoji: String representation of a IDoji

            """
            raise GenerateEmotelistError

    with pytest.raises(ValidIdojiError):
        IDojiChildValidIdoji("")

    with pytest.raises(ValidIdojiError):
        IDojiChildValidIdoji.to_uuid(uuididoji.idoji)

    with pytest.raises(ToUUIDError):
        IDojiChildToUUID(uuididoji.idoji)

    with pytest.raises(ToUUIDError):
        IDojiChildToUUID.to_uuid(uuididoji.idoji)

    with pytest.raises(StripIDojiError):
        IDojiChildStripIDoji(uuididoji.idoji)

    with pytest.raises(GenerateEmotelistError):
        IDojiChildGenerateEmotelist()

    with pytest.raises(GenerateEmotelistError):
        IDojiChildGenerateEmotelist.valid_idoji(uuididoji.idoji)

    with pytest.raises(GenerateEmotelistError):
        IDojiChildGenerateEmotelist.to_uuid(uuididoji.idoji)

    with pytest.raises(GenerateEmotelistError):
        IDojiChildGenerateEmotelist.to_uuid(uuididoji.idoji)


def test_inheritance_comparison(uuididoji):
    """Ensure that comparisons between parent and childclasses work."""

    class IDojiChild(IDoji):
        """Child class to ensure type compatibility."""

    assert IDoji(uuididoji.uuid).__eq__(IDojiChild(uuididoji.idoji))
    assert IDojiChild(uuididoji.uuid).__eq__(IDoji(uuididoji.idoji))


def test_cli_output_main(capsys, monkeypatch, uuididoji):
    """Check that an Idoji and its UUID are output when calling from CLI."""
    mock_idoji_cls = MagicMock()
    mock_idoji_cls.return_value.__str__.return_value = uuididoji.idoji
    mock_idoji_cls.return_value.uuid = uuididoji.uuid
    monkeypatch.setattr(idoji_module, "IDoji", mock_idoji_cls)

    idoji_module.__main()  # pylint: disable=protected-access

    captured = capsys.readouterr()
    assert uuididoji.uuid in captured.out
    assert uuididoji.idoji in captured.out

    assert mock_idoji_cls.call_count == 1  # check instantiation
