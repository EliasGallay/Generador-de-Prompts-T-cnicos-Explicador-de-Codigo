# app/utils/costs.py
def approx_tokens(chars: int) -> int:
    # Regla simple ~4 chars por token
    return max(1, round(chars / 4))

def estimate_cost(prompt_chars: int, completion_chars: int, model: str="gpt-4o-mini") -> dict:
    toks_in = approx_tokens(prompt_chars)
    toks_out = approx_tokens(completion_chars)

    pricing = {
        "gpt-4o-mini": {"in": 0.00015, "out": 0.0006},  # USD por 1k tokens (ejemplo)
    }
    p = pricing.get(model, pricing["gpt-4o-mini"])
    usd = (toks_in/1000)*p["in"] + (toks_out/1000)*p["out"]
    return {"model": model, "tokens_in": toks_in, "tokens_out": toks_out, "usd": round(usd, 4)}
