import pytest
from solution import function_name


class TestFunctionName:
    def test_basic_case(self):
        assert function_name(input) == expected_output
    
    def test_edge_case(self):
        assert function_name(edge_input) == expected_output
    
    def test_invalid_input(self):
        with pytest.raises(ValueError):
            function_name(invalid_input)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
