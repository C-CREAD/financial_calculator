from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import math

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


class InvestmentRequest(BaseModel):
    deposit: float
    interest_rate: float
    years: int


class BondRequest(BaseModel):
    present_value: float
    interest_rate: float
    months: int


class InvestmentResponse(BaseModel):
    deposit: float
    interest_rate: float
    years: int
    simple_interest: float
    compound_interest: float


class BondResponse(BaseModel):
    present_value: float
    interest_rate: float
    months: int
    monthly_repayment: float
    total_repayment: float


@app.get("/")
async def read_root():
    """Serve the main HTML file"""
    return FileResponse("static/index.html")


@app.post("/api/calculate-investment", response_model=InvestmentResponse)
async def calculate_investment(request: InvestmentRequest):
    """Calculate investment returns using simple and compound interest formulas

    Simple Interest: A = P(1 + r * t)
    Compound Interest: A = P(1 + r)^t
    """
    # Convert percentage to decimal
    rate = request.interest_rate / 100

    # Simple interest calculation: A = P(1 + r * t)
    simple_interest = round(request.deposit * (1 + rate * request.years), 2)

    # Compound interest calculation: A = P(1 + r)^t
    compound_interest = round(request.deposit * math.pow(1 + rate, request.years), 2)

    return InvestmentResponse(
        deposit=request.deposit,
        interest_rate=request.interest_rate,
        years=request.years,
        simple_interest=simple_interest,
        compound_interest=compound_interest
    )


@app.post("/api/calculate-bond", response_model=BondResponse)
async def calculate_bond(request: BondRequest):
    """Calculate bond repayment using amortization formula

    Monthly Interest Rate: i = annual_rate / 12 / 100
    Monthly Payment: repayment = (i * P) / (1 - (1 + i)^(-n))
    """
    # Convert annual percentage to monthly decimal rate
    monthly_rate = (request.interest_rate / 100) / 12

    # Calculate monthly repayment using amortization formula
    # repayment = (i * P) / (1 - (1 + i)^(-n))
    repayment = round((monthly_rate * request.present_value) / (1 - math.pow(1 + monthly_rate, -request.months)), 2)

    # Calculate total repayment
    total_repayment = round(repayment * request.months, 2)

    return BondResponse(
        present_value=request.present_value,
        interest_rate=request.interest_rate,
        months=request.months,
        monthly_repayment=repayment,
        total_repayment=total_repayment
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)