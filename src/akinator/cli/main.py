import click
import pandas as pd


@click.command()
@click.option("--data", default="./data.csv", help="path of akinator data")
def do(data):
    df = pd.read_csv(data)
    history = []

    while len(df['Solution']) > 1:
        question = pick_question(df)
        yn = ask_yn_question(question)
        history.append("{} {}".format(question, yn))
        print("{}\n".format("\n".join(history)))
        print()

        if yn:
            _df = df[df[question] >= 0]
            if(len(df['Solution']) == len(_df['Solution'])):
                break
            else:
                df = _df
        else:
            _df = df[df[question] <= 0]
            if(len(df['Solution']) == len(_df['Solution'])):
                break
            else:
                df = _df

    if(len(df['Solution']) == 0):
        print("あれっ？そんなキャラクターはいますか？")
    else:
        yn = ask_yn_question(
            "あなたの選んだキャラクターは{}ですね？".format(df['Solution'].values[0]))
        if yn:
            print("Yay!!")
        else:
            print("あれっ？間違えましたか？")


def pick_question(df):
    q = df.loc[:, df.columns != 'Solution'].mean(
        numeric_only=True).abs().idxmin()
    return q


def say(message):
    print(message)


def ask(message):
    return input("{}\n".format(message))


def ask_yn_question(message):
    return ask("{} [Y/n]".format(message)) in ["Yes", "yes", "Y", "y"]
