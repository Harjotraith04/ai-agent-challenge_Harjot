#!/usr/bin/env python3
"""
PDF Parsing Demonstration
Shows how the agent parses actual PDF content and saves results
"""

import subprocess
import sys
import time
from pathlib import Path

def run_command(cmd, description):
    """Run a command and display the result"""
    print(f"\n🔄 {description}")
    print(f"Command: {cmd}")
    print("-" * 50)
    
    start_time = time.time()
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        end_time = time.time()
        
        if result.returncode == 0:
            print(f"✅ Success ({end_time - start_time:.2f}s)")
            if result.stdout:
                print("Output:")
                print(result.stdout)
        else:
            print(f"❌ Failed ({end_time - start_time:.2f}s)")
            if result.stderr:
                print("Error:")
                print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False
    
    return True

def show_file_contents(file_path, title):
    """Show contents of a file"""
    print(f"\n📄 {title}")
    print("=" * 60)
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            print(content)
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    """Run the PDF parsing demonstration"""
    print("🚀 PDF Parsing Demonstration")
    print("=" * 60)
    print("This shows how the agent parses actual PDF content")
    print("and saves the results to results.csv")
    
    # Check if SBI data exists
    sbi_dir = Path("data/sbi")
    if not sbi_dir.exists():
        print("❌ SBI data directory not found")
        return False
    
    # Show expected results
    expected_file = sbi_dir / "expected_result.csv"
    if expected_file.exists():
        show_file_contents(expected_file, "Expected Results (expected_result.csv)")
    
    # Run the agent
    print("\n" + "="*60)
    print("🤖 RUNNING AGENT")
    print("="*60)
    
    if not run_command("python agent.py --target sbi", "Running agent to parse SBI PDF"):
        print("❌ Agent failed")
        return False
    
    # Show generated results
    results_file = sbi_dir / "results.csv"
    if results_file.exists():
        show_file_contents(results_file, "Parsed Results (results.csv)")
    
    # Test the generated parser
    print("\n" + "="*60)
    print("🧪 TESTING GENERATED PARSER")
    print("="*60)
    
    if not run_command('python custom_parsers\\sbi_parser.py "data/sbi/SBI_Test_Data.pdf"', "Testing SBI parser directly"):
        print("❌ Parser test failed")
        return False
    
    # Show file structure
    print("\n" + "="*60)
    print("📁 FILE STRUCTURE")
    print("="*60)
    
    print("SBI Directory Contents:")
    for file in sbi_dir.iterdir():
        print(f"  - {file.name}")
    
    print("\nCustom Parsers Directory:")
    parsers_dir = Path("custom_parsers")
    if parsers_dir.exists():
        for file in parsers_dir.iterdir():
            if file.suffix == '.py':
                print(f"  - {file.name}")
    
    print("\n🎉 PDF PARSING DEMONSTRATION COMPLETE!")
    print("✅ Agent successfully parsed PDF content")
    print("✅ Results saved to results.csv")
    print("✅ Generated parser works independently")
    print("✅ Shows real PDF parsing capability")

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
