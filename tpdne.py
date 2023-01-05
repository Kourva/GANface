import requests, random, sys
from tqdm import tqdm, trange


def random_name():
    return "".join(random.choices("abcdef0ghi9jklmn8op7qrst6u5v4wx3y2z1", k=10))


def this_persion_does_not_exist(Len=1):
    """
    Get image from ThisPersonDoesNotExist.com
    """
    downloaded = []
    print("\r\033[1;32m[Info]:\033[1;31m Downloading %s images\033[m" % Len)

    for i in tqdm(
        [x for x in range(Len)],
        unit="pic",
        ascii=" ▮",
        smoothing=0.9,
        colour="red",
        dynamic_ncols=True,
    ):
        image = requests.get("https://thispersondoesnotexist.com/image", stream=True)
        file_name = random_name()
        with open(f"images/{file_name}.jpg", "wb") as data:
            for chunk in image:
                data.write(chunk)
        downloaded.append(file_name)

    if Len > 1:
        print()
        print("\r\033[1;32m[Info]:\033[1;31m Got all data:\n\033[m")
        print(*downloaded, sep=" ; ")
    else:
        print()
        print(
            "\r\033[1;32m[Info]:\033[1;31m File saved in image/%s.jpg\n\033[m"
            % downloaded[0]
        )


length = int(sys.argv[1]) if len(sys.argv) > 1 else 1
this_persion_does_not_exist(Len=length)
