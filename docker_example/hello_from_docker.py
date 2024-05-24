import datetime
from time import sleep

import pandas as pd

print("Hello world from Docker!!!")

while True:
    df = pd.DataFrame(
        data={
            "timestamp": [datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=7)],
            "col2": [3, 4],
        }
    )
    print(f"{df}")
    sleep(2)

# docker build -t my_image .
# docker run --rm -it --name my_cont -d my_image

# docker exec -it my_cont bash


# docker build -t quiz_image .
# docker run --rm -it --name quiz_cont -d quiz_image
