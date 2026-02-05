#!/bin/bash
# X402-Open Bounty Setup Script for Termux
set -e

echo "========================================="
echo "X402-Open Bounty - Setup Script"
echo "========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed"
    echo "Install with: pkg install python"
    exit 1
fi

echo "✓ Python3 found: $(python3 --version)"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "ERROR: pip3 is not installed"
    echo "Install with: pkg install python-pip"
    exit 1
fi

echo "✓ pip3 found"

# Create virtual environment (optional but recommended)
if [ ! -d "venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "========================================="
echo "✓ Setup complete!"
echo "========================================="
echo ""
echo "Next steps:"
echo "1. Copy .env.example to .env:"
echo "   cp .env.example .env"
echo ""
echo "2. Edit .env and add your Solana wallet address:"
echo "   nano .env"
echo ""
echo "3. Run the server:"
echo "   source venv/bin/activate"
echo "   python3 main.py"
echo ""
echo "4. In another terminal, expose with ngrok:"
echo "   ngrok http 8402"
echo ""
