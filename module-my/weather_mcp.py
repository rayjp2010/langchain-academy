# mcp server to return random weather using fastmcp

import random
from typing import Dict
from fastmcp import FastMCP
from pydantic import BaseModel

# Create the FastMCP server
mcp = FastMCP(name="Weather MCP Server")

class Weather(BaseModel):
    city: str
    temperature: int
    condition: str
    humidity: int
    wind_speed: float
    pressure: int
    description: str

@mcp.tool()
async def get_weather(city: str) -> Weather:
    """Get current weather for a specified city. Returns random weather data."""
    conditions = ["sunny", "cloudy", "rainy", "snowy", "stormy", "foggy", "partly cloudy"]
    
    weather_data = {
        "city": city,
        "temperature": random.randint(-10, 35),  # Temperature in Celsius
        "condition": random.choice(conditions),
        "humidity": random.randint(30, 90),  # Humidity percentage
        "wind_speed": round(random.uniform(0, 25), 1),  # Wind speed in km/h
        "pressure": random.randint(980, 1030),  # Atmospheric pressure in hPa
        "description": f"Random weather data for {city}"
    }
    
    return weather_data


if __name__ == "__main__":
    # Run the MCP server
    # By default, this runs with stdio transport for local clients
    # Use mcp.run(transport="http", port=8000) for HTTP transport
    mcp.run(transport="streamable-http")
