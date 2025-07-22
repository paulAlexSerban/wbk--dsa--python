from cap import cap_text


class TestCap:
    def test_one_word(self):
        text = "python"
        result = cap_text(text)
        assert result == "Python"

    def test_multiple_words(self):
        text = "monty python"
        result = cap_text(text)
        assert result == "Monty Python"
