import yaml

def test_some_data(config):
    print(config)

    with open(config) as fh:
        conf = yaml.load(fh, Loader=yaml.FullLoader)
    print(conf)
