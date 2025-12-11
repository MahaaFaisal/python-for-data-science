import os


def ft_tqdm(lst: range) -> None:
    percentage = 0
    fill = "█"
    time_elapsed = "00:22"
    etc = "02:25"
    it_per_s = 10

    print(os.get_terminal_size)
    for idx, i in enumerate(lst):
        print("\r{}%|{}| {}/{} [{}:{},  {}it/s]".format(
            percentage, fill, idx, len(lst), time_elapsed, etc, it_per_s),
            end="\r")
        yield i
    print("\r{}%|{}| {}/{} [{}:{},  {}it/s]".format(
        percentage, fill, idx + 1, len(lst), time_elapsed, etc, it_per_s),
        end="\r")
