#!/usr/bin/env python3
"""
Test script for the generated parser
"""

import pandas as pd
import sys
from pathlib import Path

def test_parser():
    """Test the generated ICICI parser"""
    try:
        # Import the generated parser
        sys.path.insert(0, str(Path("custom_parsers")))
        import icici_parser
        
        # Test the parser
        pdf_path = "data/icici/icici sample.pdf"
        result_df = icici_parser.parse(pdf_path)
        
        # Load expected result
        expected_df = pd.read_csv("data/icici/result.csv")
        
        # Compare DataFrames
        result_df = result_df.reset_index(drop=True)
        expected_df = expected_df.reset_index(drop=True)
        
        # Normalize data for comparison
        result_df = result_df.fillna('')
        expected_df = expected_df.fillna('')
        
        # Check if DataFrames are equal
        are_equal = result_df.equals(expected_df)
        
        if are_equal:
            print("PASS: Parser test PASSED - output matches expected CSV")
            print(f"Successfully parsed {len(result_df)} transactions")
            return True
        else:
            print("FAIL: Parser test FAILED - output doesn't match expected CSV")
            print(f"Expected shape: {expected_df.shape}, Got shape: {result_df.shape}")
            return False
            
    except Exception as e:
        print(f"FAIL: Parser test FAILED with error: {e}")
        return False

if __name__ == "__main__":
    success = test_parser()
    sys.exit(0 if success else 1)
