#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
    BEKOPortfolioSolution:贝克欧产品组合解决方案
    系统选择
    单项/多项独立选择
    版本：开发
"""

# 输入工作条件（
#           1、流量、温度、压力
#           2、颗粒、水、油的三项条件，可以是数值、等级、或者空压机类型和安装地点）
#           3、其它条件(非必需)，水，环境温湿度
#           ）
def input():
    return True

# 根据入口与出口条件，选择合适的方案，返回方案代码
def SystemSelection(inParticle,inWater,inOil,outParticle,outWater,outOil):
    solutionNo=0
    return solutionNo

# 根据产品选型参数
def BEKOMAT_Selection():
    BEKOMAT_selectedModel=0
    return BEKOMAT_selectedModel

if __name__ == '__main__':

# TODO 输入工作条件
#   工作条件  1、流量、温度、压力
#           2、颗粒、水、油的三项条件，可以是数值、等级、或者空压机类型和安装地点）
#           3、其它条件(非必需)，水，环境温湿度
#   系统选型or产品选型？
#   UI界面
# TODO 工作条件处理
#   上述工作条件转换成程序用，例如颗粒输入等级，转化为数值；单位转化为标准单位（非必需，如固定输入单位）
# TODO 选择系统方案
#     step1 选择适合的系统，即产品组合   （如果是系统选择，10多条产品线）
#     step2 对系统方案上的产品进行规格选型（如果是产品单选，直接跳到此步，7类产品？）
# TODO 对外展现方案
#   UI界面

