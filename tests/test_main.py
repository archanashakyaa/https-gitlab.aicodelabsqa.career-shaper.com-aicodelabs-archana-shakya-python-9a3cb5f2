# tests/test_main.py
import pytest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import calculate_seasonal_price


class TestSeasonalPriceCalculator:
    """Test suite for seasonal price calculator."""
    
    def test_peak_season_emerald_january(self, capsys):
        """Test Emerald in peak season (January)."""
        calculate_seasonal_price("Emerald", "01/15")
        captured = capsys.readouterr()
        assert "187.5" in captured.out
        assert "Welcome to seasonal collections" in captured.out
        
    def test_off_season_pearl_july(self, capsys):
        """Test Pearl in off-season (July)."""
        calculate_seasonal_price("Pearl", "07/20")
        captured = capsys.readouterr()
        assert "233.75" in captured.out
        assert "Welcome to seasonal collections" in captured.out
        
    def test_off_season_sapphire_april(self, capsys):
        """Test Sapphire in off-season (April)."""
        calculate_seasonal_price("Sapphire", "04/10")
        captured = capsys.readouterr()
        assert "140.0" in captured.out
        assert "Welcome to seasonal collections" in captured.out
        
    def test_invalid_product_name(self, capsys):
        """Test invalid product name."""
        calculate_seasonal_price("Diamond", "01/15")
        captured = capsys.readouterr()
        assert "Not available in our collection." in captured.out
        assert "Please try another product." in captured.out
        assert "Welcome to seasonal collections" in captured.out
        
    def test_invalid_date_month_too_high(self, capsys):
        """Test invalid date with month > 12."""
        calculate_seasonal_price("Rose", "13/32")
        captured = capsys.readouterr()
        assert "Enter a valid date" in captured.out
        assert "Welcome to seasonal collections" in captured.out
        
    def test_invalid_date_day_too_high(self, capsys):
        """Test invalid date with day > 31."""
        calculate_seasonal_price("Rose", "12/32")
        captured = capsys.readouterr()
        assert "Enter a valid date" in captured.out
        
    def test_peak_season_october(self, capsys):
        """Test peak season month October."""
        calculate_seasonal_price("Rose", "10/15")
        captured = capsys.readouterr()
        assert "112.5" in captured.out  # 75 * 1.5
        
    def test_peak_season_december(self, capsys):
        """Test peak season month December."""
        calculate_seasonal_price("Gold", "12/25")
        captured = capsys.readouterr()
        assert "393.0" in captured.out  # 262 * 1.5
        
    def test_off_season_september(self, capsys):
        """Test off-season month September."""
        calculate_seasonal_price("Emerald", "09/30")
        captured = capsys.readouterr()
        assert "156.25" in captured.out  # 125 * 1.25
        
    def test_invalid_date_format(self, capsys):
        """Test invalid date format."""
        calculate_seasonal_price("Rose", "1-15")
        captured = capsys.readouterr()
        assert "Enter a valid date" in captured.out
        
    def test_invalid_date_month_zero(self, capsys):
        """Test invalid date with month 0."""
        calculate_seasonal_price("Rose", "00/15")
        captured = capsys.readouterr()
        assert "Enter a valid date" in captured.out
        
    def test_all_products_exist(self, capsys):
        """Test that all specified products exist."""
        products = ["Emerald", "Pearl", "Gold", "Sapphire", "Rose"]
        for product in products:
            calculate_seasonal_price(product, "01/15")
            captured = capsys.readouterr()
            assert "Not available" not in captured.out


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
