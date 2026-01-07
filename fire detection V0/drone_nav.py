import asyncio
from mavsdk import System

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("-- Waiting for drone")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print("-- Arming")
    await drone.action.arm()

    print("-- Taking off")
    await drone.action.takeoff()
    await asyncio.sleep(5)

    print("-- Going to fire location")
    # Example coords — update with actual GPS
    fire_lat, fire_lon, fire_alt = 28.7, 77.1, 10
    await drone.action.goto_location(fire_lat, fire_lon, fire_alt)

    print("-- Hovering at target")
    await asyncio.sleep(10)

    print("-- Landing")
    await drone.action.land()

if __name__ == "__main__":
    asyncio.run(run())
