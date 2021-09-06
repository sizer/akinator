import click
import pandas as pd


@click.command()
@click.option("--data", default="./data.csv", help="path of akinator data")
def do(data):
    df = pd.read_csv(data)
    print(ask_yn_question(df.mean().idxmin()))


def say(message):
    print(message)


def ask(message):
    return input("{}\n".format(message))


def ask_yn_question(message):
    return ask("{} [Y/n]".format(message)) in ["Yes", "yes", "Y", "y"]
