# main.py vs server.py - Which One to Use?

## Quick Answer

**Use `main.py`** - It's the full-featured version that's more impressive for the bounty.

---

## Detailed Comparison

| Feature | main.py | server.py |
|---------|---------|-----------|
| **Size** | 6.7 KB | 2.7 KB |
| **Endpoints** | 6 endpoints | 3 endpoints |
| **Logging** | ✅ Full logging | ❌ Minimal |
| **CORS** | ✅ Enabled | ❌ Not included |
| **Payment tracking** | ✅ Payment log | ❌ No tracking |
| **Error handling** | ✅ Comprehensive | ✅ Basic |
| **Demo mode** | ✅ Works without wallet | ✅ Works without wallet |
| **Documentation** | ✅ Auto-docs at /docs | ✅ Auto-docs at /docs |
| **Stats endpoint** | ✅ Yes | ❌ No |

---

## main.py Features

### Endpoints

1. **`GET /`** - Root with full API information
2. **`GET /health`** - Health check with x402 status
3. **`GET /api/free`** - Free data endpoint (demo)
4. **`GET /api/premium`** - 402 Payment Required endpoint
5. **`GET /api/payment-info`** - Payment configuration & logs
6. **`GET /api/stats`** - Server statistics

### Additional Features

- ✅ **Payment logging** - Tracks payment attempts
- ✅ **CORS middleware** - Allows cross-origin requests
- ✅ **Comprehensive logging** - Detailed server logs
- ✅ **Payment instructions** - Step-by-step guide in 402 response
- ✅ **Demo mode support** - Works even without configured wallet
- ✅ **Statistics tracking** - Monitor server usage

### Example 402 Response (main.py)

```json
{
  "error": "Payment Required",
  "message": "This endpoint requires payment to access",
  "payment": {
    "amount": "0.10",
    "currency": "USDC",
    "payment_address": "YOUR_WALLET",
    "token_mint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
    "network": "solana-devnet",
    "description": "Premium market data access",
    "timestamp": "2026-02-05T22:47:00.000000"
  },
  "instructions": {
    "step_1": "Create a Solana transaction with the specified amount",
    "step_2": "Send to the payment_address",
    "step_3": "Include transaction signature in X-Payment-Authorization header",
    "step_4": "Retry the request with the authorization header"
  }
}
```

---

## server.py Features

### Endpoints

1. **`GET /`** - Root endpoint
2. **`GET /health`** - Health check
3. **`GET /premium-data`** - 402 Payment Required endpoint

### Characteristics

- ✅ **Minimal** - Just the essentials
- ✅ **Simple** - Easy to understand
- ✅ **Lightweight** - Smaller footprint
- ✅ **Clear** - Straightforward implementation

### Example 402 Response (server.py)

```json
{
  "error": "Payment Required",
  "x402_payment": {
    "amount": "0.10",
    "token_mint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
    "payment_address": "YOUR_WALLET",
    "network": "solana-devnet",
    "description": "Premium market data access"
  }
}
```

---

## Which One Should You Use?

### Use main.py if:
- ✅ You want to impress bounty judges
- ✅ You want more endpoints to demonstrate
- ✅ You want payment tracking/logging
- ✅ You want comprehensive features
- ✅ **Recommended for bounty submission**

### Use server.py if:
- ✅ You want absolute minimal implementation
- ✅ You're learning the protocol
- ✅ You want the simplest possible code
- ✅ You're building a proof-of-concept

---

## Setup Script (setup.sh)

The `setup.sh` script works with **both** implementations.

### What it does:

1. ✅ Checks for Python 3
2. ✅ Checks for pip
3. ✅ Creates virtual environment
4. ✅ Installs dependencies
5. ✅ Provides next-step instructions

### How to use:

```bash
# Make executable
chmod +x setup.sh

# Run it
./setup.sh

# Follow the printed instructions
```

### Manual alternative:

```bash
# Create venv
python3 -m venv venv
source venv/bin/activate

# Install deps
pip install -r requirements.txt

# Copy config
cp .env.example .env
nano .env  # Edit with your wallet

# Run server
python3 main.py  # or python3 server.py
```

---

## Recommendation for Bounty

**Use main.py** because:

1. **More impressive** - Shows you built a complete system
2. **Better demo** - Multiple endpoints to show judges
3. **Professional** - Logging, CORS, error handling
4. **Trackable** - Payment log shows it's working
5. **Educational** - Includes instructions in API responses

The extra 4KB is worth it for the bounty submission.

---

## Can You Use Both?

**No** - they're alternatives, not complements.

Both files define a FastAPI `app` and run on the same port (8402).

**Choose one:**
- `python3 main.py` ← Recommended
- `python3 server.py` ← Alternative

---

## For Your GitHub Repo

**Include both** in the repo with a note:

> **Note:** This repo includes two server implementations:
> - `main.py` - Full-featured (recommended)
> - `server.py` - Minimal version
> 
> Run either one, not both simultaneously.

This shows you understand progressive enhancement and can build both minimal and feature-rich implementations.

---

## Bottom Line

**For the bounty: Use `main.py`**

It's more complete, more professional, and more impressive—without being overcomplicated.
