__author__ = 'dgraziotin'

import libckan.logic.action.get


def test_package_search_non_existing():
    results = libckan.logic.action.get.package_search(q='idonotexisth0pefllt123')
    assert results['success'] is True
    assert results['result']['count'] == 0
    assert results['result']['results'] == []

def test_package_search():
    results = libckan.logic.action.get.package_search(q='test')
    assert results['success'] is True
    assert results['result']['count'] > 0
    assert len(results['result']['results']) > 0


def test_package_list():
    results = libckan.logic.action.get.package_list()
    assert results['success'] is True
    assert len(results['result']) > 0
