from .scale_height import estimate_atmospheric_scale_height

def flag_transmission_spectroscopy_targets(planets):
    scored = []

    for p in planets:
        H = estimate_atmospheric_scale_height(
            p["mass_earth"], p["radius_earth"], p["temperature_k"]
        )

        signal = H / (p["radius_earth"] * 6371)
        brightness = 1 / (10 ** (p["star_mag"] / 5))
        score = signal * brightness * p["transit_depth"] * 1e6

        scored.append({**p, "scale_height_km": H, "score": score})

    return sorted(scored, key=lambda x: x["score"], reverse=True)
