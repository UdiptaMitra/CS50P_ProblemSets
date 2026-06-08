def f(*args, **kwargs):
    print("Named:", kwargs)
    print("Positional:", args)


f(100, 50, 25, galleons=100, sickles=50, knuts=25)
