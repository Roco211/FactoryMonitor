import requests
import pytest


def test_models_get_pass():
    # 获取已维护的机种列表
    res = requests.get("http://localhost:8000/api/v1/device-alerts/models")
    response = res.json()
    if response['status'] == 'success':
        assert True
    else:
        assert False


def test_lines_get_pass():
    # 获取已维护的机种列表
    res = requests.get("http://localhost:8000/api/v1/device-alerts/lines")
    response = res.json()
    if response['status'] == 'success':
        assert True
    else:
        assert False


def test_stations_get_pass():
    # 获取已维护的机种列表
    res = requests.get("http://localhost:8000/api/v1/device-alerts/stations")
    response = res.json()
    if response['status'] == 'success':
        assert True
    else:
        assert False

#
#
# # 获取已维护的线别列表
# print("获取已维护的线别列表")
# res = requests.get("http://localhost:8000/api/v1/device-alerts/lines")
# response = res.json()
# print("原始响应:", response)
# print("实际数据获取:", response['data'])
# print("实际数据类型:", type(response['data']))
# print("\n")
#
#
#
# # 获取已维护的站别列表
# print("获取已维护的站别列表")
# res = requests.get("http://localhost:8000/api/v1/device-alerts/stations")
# response = res.json()
# print("原始响应:", response)
# print("实际数据获取:", response['data'])
# print("实际数据类型:", type(response['data']))
# print("\n")


"""
参考输出

获取已维护的机种列表
原始响应: {'code': 200, 'status': 'success', 'message': '获取机种成功', 'data': ['V73F', 'V76A', 'V76AMY', 'V76R', 'V73FL']}
实际数据获取: ['V73F', 'V76A', 'V76AMY', 'V76R', 'V73FL']
实际数据类型: <class 'list'>



获取已维护的线别列表
原始响应: {'code': 200, 'status': 'success', 'message': '获取线别成功', 'data': ['O21', 'C21', 'P11']}
实际数据获取: ['O21', 'C21', 'P11']
实际数据类型: <class 'list'>



获取已维护的站别列表
原始响应: {'code': 200, 'status': 'success', 'message': '获取站别成功', 'data': ['A7', 'A1', 'A01', 'A03', 'A09', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20', 'A26', 'A27', 'A28', 'A29', 'A30', 'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'IP_A7', 'IP_A9', 'A9']}
实际数据获取: ['A7', 'A1', 'A01', 'A03', 'A09', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20', 'A26', 'A27', 'A28', 'A29', 'A30', 'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'IP_A7', 'IP_A9', 'A9']
实际数据类型: <class 'list'>
"""
