"""
x402-open Bounty Integration Server
Minimal FastAPI implementation with OpenLibx402 payment middleware
"""
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

# We'll use mock implementation first since real packages may not be available
# This demonstrates the integration pattern for the bounty

app = FastAPI(
    title="x402-open Integration Server",
    description="Minimal server demonstrating OpenLibx402 integration for bounty submission",
    version="1.0.0"
)

# Configuration for x402 payments
X402_CONFIG = {
    "payment_address": os.getenv("X402_PAYMENT_ADDRESS", "DEMO_WALLET_ADDRESS"),
    "token_mint": os.getenv("X402_TOKEN_MINT", "USDC_DEVNET_MINT"),
    "network": "solana-devnet",
    "rpc_url": "https://api.devnet.solana.com"
}

@app.get("/")
async def root():
    """
    Root endpoint - no payment required
    """
    return {
        "message": "x402-open Integration Server",
        "status": "operational",
        "endpoints": {
            "free": "/health",
            "paid": "/premium-data"
        },
        "payment_config": {
            "network": X402_CONFIG["network"],
            "payment_address": X402_CONFIG["payment_address"]
        }
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint - no payment required
    """
    return {
        "status": "healthy",
        "service": "x402-open-server"
    }

@app.get("/premium-data")
async def get_premium_data():
    """
    Premium endpoint - requires x402 payment
    This is where we'd apply the @payment_required decorator
    
    For now, returns data with 402 payment requirement details
    """
    # In real implementation with openlibx402-fastapi:
    # @payment_required(amount="0.10", description="Premium market data")
    
    # Return 402 Payment Required with payment details
    return JSONResponse(
        status_code=402,
        content={
            "error": "Payment Required",
            "x402_payment": {
                "amount": "0.10",
                "token_mint": X402_CONFIG["token_mint"],
                "payment_address": X402_CONFIG["payment_address"],
                "network": X402_CONFIG["network"],
                "description": "Access to premium market data",
                "expires_at": "2026-02-04T00:00:00Z"
            },
            "message": "Send payment to access this endpoint"
        },
        headers={
            "X-Payment-Required": "true",
            "X-Payment-Amount": "0.10",
            "X-Payment-Address": X402_CONFIG["payment_address"]
        }
    )

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8402"))
    uvicorn.run(app, host="0.0.0.0", port=port)
