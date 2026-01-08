# tests/test_eval.py
# Hidden evaluation tests for grading
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import calculate_seasonal_price


class TestEvaluation:
    """Hidden evaluation tests for grading."""
    
    def test_peak_season_february(self):
        """Test peak season February."""
        result = calculate_seasonal_price("Pearl", "02/14")
        assert "280.5" in result  # 187 * 1.5
        
    def test_peak_season_march(self):
        """Test peak season March."""
        result = calculate_seasonal_price("Gold", "03/01")
        assert "393.0" in result  # 262 * 1.5
        
    def test_off_season_may(self):
        """Test off-season May."""
        result = calculate_seasonal_price("Rose", "05/15")
        assert "93.75" in result  # 75 * 1.25
        
    def test_off_season_june(self):
        """Test off-season June."""
        result = calculate_seasonal_price("Sapphire", "06/20")
        assert "140.0" in result  # 112 * 1.25
        
    def test_off_season_august(self):
        """Test off-season August."""
        result = calculate_seasonal_price("Emerald", "08/10")
        assert "156.25" in result  # 125 * 1.25
        
    def test_peak_season_november(self):
        """Test peak season November."""
        result = calculate_seasonal_price("Sapphire", "11/25")
        assert "168.0" in result  # 112 * 1.5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
