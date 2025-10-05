#!/usr/bin/env python3
"""
Demonstration script for the Agent-as-Coder Challenge
Shows the complete workflow from start to finish
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

def main():
    """Run the complete demonstration"""
    print("🚀 Agent-as-Coder Challenge Demonstration")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not Path("agent.py").exists():
        print("❌ Please run this script from the project root directory")
        sys.exit(1)
    
    # Step 1: Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Step 2: Run the agent
    if not run_command("python agent.py --target icici", "Running the agent to generate ICICI parser"):
        print("❌ Agent failed to generate parser")
        sys.exit(1)
    
    # Step 3: Test the generated parser
    if not run_command("python test_parser.py", "Testing the generated parser"):
        print("❌ Parser test failed")
        sys.exit(1)
    
    # Step 4: Run pytest
    if not run_command("python -m pytest test_parser.py -v", "Running pytest validation"):
        print("❌ Pytest validation failed")
        sys.exit(1)
    
    # Step 5: Show generated parser
    print("\n📄 Generated Parser Preview")
    print("-" * 50)
    parser_path = Path("custom_parsers/icici_parser.py")
    if parser_path.exists():
        with open(parser_path, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines[:20]):  # Show first 20 lines
                print(f"{i+1:2d}: {line.rstrip()}")
            if len(lines) > 20:
                print(f"... and {len(lines) - 20} more lines")
    
    print("\n🎉 Demonstration Complete!")
    print("✅ Agent successfully generated and tested the ICICI parser")
    print("✅ All tests passed")
    print("✅ Parser matches expected CSV format exactly")

if __name__ == "__main__":
    main()
