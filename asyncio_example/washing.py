import asyncio
import time


async def washing_machine():
    await asyncio.sleep(1)
    print("washing clothes 🧼")
    await asyncio.sleep(2)
    print("Washing machine is done! hang the cloths now.✅")
    return "🧦"


async def eat_breakfast():
    print("Having breakfast 🍳")
    asyncio.sleep(3)
    print("Done having breakfast ✅")


async def do_laundry():
    print("Starting to do laundry..")
    cloths = await washing_machine()
    time.sleep(1)
    print(f"Finished washing {cloths}.")


async def main():
    task1 = asyncio.create_task(do_laundry())
    task2 = asyncio.create_task(eat_breakfast())
    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())
