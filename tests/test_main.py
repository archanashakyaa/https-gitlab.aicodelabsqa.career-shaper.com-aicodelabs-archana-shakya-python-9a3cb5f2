# tests/test_main.py
import pytest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import calculate_seasonal_price


class TestSeasonalPriceCalculator:
    """Test suite for seasonal price calculator."""
    
    def test_peak_season_emerald_january(self):
        """Test Emerald in peak season (January)."""
        result = calculate_seasonal_price("Emerald", "01/15")
        assert "187.5" in result
        assert "Welcome to seasonal collections" in result
        
    def test_off_season_pearl_july(self):
        """Test Pearl in off-season (July)."""
        result = calculate_seasonal_price("Pearl", "07/20")
        assert "233.75" in result
        assert "Welcome to seasonal collections" in result
        
    def test_off_season_sapphire_april(self):
        """Test Sapphire in off-season (April)."""
        result = calculate_seasonal_price("Sapphire", "04/10")
        assert "140.0" in result
        assert "Welcome to seasonal collections" in result
        
    def test_invalid_product_name(self):
        """Test invalid product name."""
        result = calculate_seasonal_price("Diamond", "01/15")
        assert "Not available in our collection" in result
        assert "Welcome to seasonal collections" in result
        
    def test_invalid_date_month_too_high(self):
        """Test invalid date with month > 12."""
        result = calculate_seasonal_price("Rose", "13/32")
        assert "Enter a valid date" in result
        assert "Welcome to seasonal collections" in result
        
    def test_invalid_date_day_too_high(self):
        """Test invalid date with day > 31."""
        result = calculate_seasonal_price("Rose", "12/32")
        assert "Enter a valid date" in result
        
    def test_peak_season_october(self):
        """Test peak season month October."""
        result = calculate_seasonal_price("Rose", "10/15")
        assert "112.5" in result  # 75 * 1.5
        
    def test_peak_season_december(self):
        """Test peak season month December."""
        result = calculate_seasonal_price("Gold", "12/25")
        assert "393.0" in result  # 262 * 1.5
        
    def test_off_season_september(self):
        """Test off-season month September."""
        result = calculate_seasonal_price("Emerald", "09/30")
        assert "156.25" in result  # 125 * 1.25
        
    def test_invalid_date_format(self):
        """Test invalid date format."""
        result = calculate_seasonal_price("Rose", "1-15")
        assert "Enter a valid date" in result
        
    def test_invalid_date_month_zero(self):
        """Test invalid date with month 0."""
        result = calculate_seasonal_price("Rose", "00/15")
        assert "Enter a valid date" in result
        
    def test_all_products_exist(self):
        """Test that all specified products exist."""
        products = ["Emerald", "Pearl", "Gold", "Sapphire", "Rose"]
        for product in products:
            result = calculate_seasonal_price(product, "01/15")
            assert "Not available" not in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
