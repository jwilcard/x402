#!/usr/bin/env python3
"""
Test script for x402-open server
Run this to verify your server is working before going public
"""
import requests
import json
import sys

def test_endpoint(url, endpoint, expect_status):
    """Test a single endpoint"""
    full_url = f"{url}{endpoint}"
    print(f"\n{'='*60}")
    print(f"Testing: {full_url}")
    print(f"Expected status: {expect_status}")
    print(f"{'='*60}")
    
    try:
        response = requests.get(full_url, timeout=5)
        print(f"✓ Status code: {response.status_code}")
        
        if response.status_code == expect_status:
            print(f"✓ Expected status code matches!")
        else:
            print(f"✗ Expected {expect_status}, got {response.status_code}")
            return False
            
        print(f"\nResponse headers:")
        for key, value in response.headers.items():
            if 'payment' in key.lower() or 'x-' in key.lower():
                print(f"  {key}: {value}")
        
        print(f"\nResponse body:")
        try:
            print(json.dumps(response.json(), indent=2))
        except:
            print(response.text)
        
        return True
        
    except requests.exceptions.ConnectionError:
        print(f"✗ Connection failed - is server running?")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def main():
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    else:
        base_url = "http://localhost:8402"
    
    print(f"""
╔═══════════════════════════════════════════════════════════╗
║           x402-open Server Test Suite                     ║
╚═══════════════════════════════════════════════════════════╝

Testing server at: {base_url}
""")
    
    tests = [
        ("/", 200, "Root endpoint"),
        ("/health", 200, "Health check"),
        ("/premium-data", 402, "Premium endpoint (should require payment)")
    ]
    
    results = []
    for endpoint, expected_status, description in tests:
        print(f"\n🔍 {description}")
        success = test_endpoint(base_url, endpoint, expected_status)
        results.append(success)
    
    print(f"\n{'='*60}")
    print(f"Test Results: {sum(results)}/{len(results)} passed")
    print(f"{'='*60}\n")
    
    if all(results):
        print("✓ All tests passed! Your server is ready.")
        print("\nNext steps:")
        print("1. Expose server with ngrok: ngrok http 8402")
        print("2. Test public URL with this script")
        print("3. Submit to bounty with your public URL")
    else:
        print("✗ Some tests failed. Check your server configuration.")
        sys.exit(1)

if __name__ == "__main__":
    main()
