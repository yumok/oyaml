import sys
from collections import OrderedDict

import pytest

import oyaml as yaml


d = OrderedDict([('k1', 'v1'), ('k3', 'v3'), ('k2', 'v2')])


def test_dump():
    assert yaml.dump(d) == '{k1: v1, k3: v3, k2: v2}\n'


def test_load():
    loaded = yaml.load('{k1: v1, k3: v3, k2: v2}')
    assert loaded == {'k1': 'v1', 'k3': 'v3', 'k2': 'v2'}


@pytest.mark.skipif(sys.version_info >= (3,7), reason="requires python3.6-")
def test_loads_to_ordered_dict():
    loaded = yaml.load('{k1: v1, k3: v3, k2: v2}')
    assert isinstance(loaded, OrderedDict)


@pytest.mark.skipif(sys.version_info < (3,7), reason="requires python3.7+")
def test_loads_to_std_dict():
    loaded = yaml.load('{k1: v1, k3: v3, k2: v2}')
    assert not isinstance(loaded, OrderedDict)
    assert isinstance(loaded, dict)


def test_anchors_and_references():
    text = '''
        defaults:
          all: &all
            product: foo
          development: &development
            <<: *all
            profile: bar

        development:
          platform:
            <<: *development
            host: baz
    '''
    expected_load = {
        'defaults': {
            'all': {
                'product': 'foo',
            },
            'development': {
                'product': 'foo',
                'profile': 'bar',
            },
        },
        'development': {
            'platform': {
                'host': 'baz',
                'product': 'foo',
                'profile': 'bar',
            },
        },
    }
    assert yaml.load(text) == expected_load
