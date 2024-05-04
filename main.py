import asyncio
#import baml_py
from baml_py import Image
#from pydantic import BaseModel
import time
#from baml_client import client
from baml_client.types import ClassWithImage, FakeImage
from baml_client import BamlClient

# poetry add baml-py baml-cli
# poetry run python -m baml_cli generate --from baml_src --to baml_client --type 'python/pydantic'

runtime = BamlClient.from_directory("baml_src")


async def main():
    #b = BamlClient.from_directory("baml_src")
    spongebob_image = Image(
        url="https://i.kym-cdn.com/photos/images/original/002/807/304/a0b.jpeg"
    )
    print("image", spongebob_image)

    print("image.url", spongebob_image.url)

    orc_image = Image(
        url="https://i.kym-cdn.com/entries/icons/original/000/033/100/eht0m1qg8dk21.jpg"
    )

    full_obj = ClassWithImage(
        myImage=spongebob_image,
        param2="ocean",
        fake_image=FakeImage(
            url="https://i.kym-cdn.com/entries/icons/original/000/033/100/eht0m1qg8dk21.jpg"
        ),
    )

    #res = await b.call_function(
    #    "DescribeImage2", args={"classWithImage": full_obj, "img2": orc_image}, ctx={}
    #)
    #print("res-------\n", res)

    res2 = await runtime.DescribeImage2(classWithImage=full_obj, img2=orc_image)
    print("res2-------\n", res2)

    


start_time = time.perf_counter()

asyncio.run(main())

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
