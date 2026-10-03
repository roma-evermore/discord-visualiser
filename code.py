from pypresence import Presence
import time

CLIENT_ID = ""
RPC = Presence(CLIENT_ID)
RPC.connect()

RPC.update(
    details="Hot",
    state="GaySex",
    start=int(time.time()),
    large_image="4021204",
    large_text="GaySex",
    small_image="627b93a33ade65a2dc8e192cdf64db32",
    small_text="GaySex",
    party_size=[1,3],
    buttons=[
        {
            "label": "Join",
            "url": "https://rt.pornhub.com/gay/video/search?search=gay+sex"
        }
    ]
)

print("Rich Presence is now running!")

while True:
    time.sleep(15)
