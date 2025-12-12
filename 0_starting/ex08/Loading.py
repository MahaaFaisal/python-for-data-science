import os
from time import sleep


def ft_tqdm(lst: range) -> None:
    width = os.get_terminal_size().columns

    for idx, i in enumerate(lst):
        percentage = round((idx / len(lst)) * 100)
        progress = round(idx / len(lst) * (width - 39))
        bar = f"{'█' * progress:<{width - 39}}"

        print("\r{}%|{}| {}/{}]".format(
            '%3s' % percentage, bar, idx, len(lst)),
            end="\r")
        yield i

    print("\r{}%|{}| {}/{}]".format(
        100, bar, len(lst), len(lst)), end="\r")
