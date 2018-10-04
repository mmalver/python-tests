from die import die
def test():
    dice = [die(3),die(5)]
    print dice[0].getValue()
    dice[0].roll()
    print dice[0].getValue()
test()
