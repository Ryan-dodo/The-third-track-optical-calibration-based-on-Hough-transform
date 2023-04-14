# 第三轨的光学标定研究
## 第三轨背景
目前，国内外对地铁接触轨的检测方法主要有人工检测和机器智能检测，检测时，将接触轨检测尺平放在走行轨轨道上，通过检测尺上的定位块与走行轨作用边密贴，检测尺上带有测量爪、横向游标卡尺和垂向游标卡尺，测量爪和接触轨的下表面和内侧面接触。检测尺上的横向游标卡尺用于测量接触轨水平距离，垂向游标卡尺用于测量接触轨导高值，地铁的维护保养工作一般需要在整条地铁线路上或者长大区间内检测接触轨的几何参数，需要检测人员频繁的下蹲作业，需要大量的人力，检测精度和检测效率低，在一条线路上检测的数据点较少，不能为地铁的保养提供充足的数据支持。
使用接触轨的地铁线路的增多要求接触轨几何参数检测方法向智能化，数字化方向发展。目前接触轨的智能化检测正处在研究开发和工程实验阶段，智能化检测设备主要有接触式检测和非接触式检测两种解决方案。
（1）接触式检测
地铁运行时，列车通过集电靴与接触轨接触，接触式检测方法在集电靴上安装电子接近式传感器，光纤传感器等智能传感器，传感器靠近接触轨时，根据空间距离的不同，会产生不同大小的感应电流，通过外围电路后以电压的形式产生检测信息。
接触式检测的优点是：①安装方便，安装精度要求低；②受天气和光照的影响小；③成本较低，设备调试难度低。
接触式检测方法也存在一些缺点，主要有以下几点：①用于检测的传感器安装在集电靴上，会增加集电靴的重量，影响集电靴和接触轨的接触；②接触式检测的检测精度易受传感器安装距离的影响，检测稳定性低。南昌大学的刘启阳基于接触式测量技术设计了一种摆臂式接触轨检测装置[1]，该装置主要包括搭载在轨检小车上的接触轨测量臂，电子硬件等设备安装在测量臂上，基于检测装置建立了测量装置的测量数学模型，求出了接触轨几何参数测量的机构学正解，设计了电路结构，上下位机软件等。
（2）非接触式检测
非接触式检测方法的检测装置一般安装在悬挂测量梁上，不与集电靴或者接触。主要采用计算机视觉技术，检测设备主要由光源和视觉传感器组成，检测时，光源发出结构光投射到接触轨上产生反射光，视觉传感器采集到图像，经过图像处理，由计算机计算接触轨几何参数。
非接触式检测的优点是：①检测装置不安装在集电靴上，不增加集电靴的重量，不影响集电靴和接触轨的接触；②在算法合理的情况下，可以达到很高的检测精度；③检测数据可以实时处理，检测速度较高。
这种检测方式的缺点是：①检测装置的成本较高，对检测装置的安装要求高；②受光照和天气的影响大；③检测过程中检测车的振动会影响检测的准确性。
国外有很多关于非接触式接触轨几何参数检测的研究，广州地铁与意大利MerMec公司共同研发了非接触式接触轨检测系统，该系统基于计算机视觉，使用激光发射装置和视觉传感器对接触轨几何参数进行检测。北京地铁和美国的ENSCO公司合作研发了接触轨检测装置，在轨检车测量平台上扩展了检测接触轨几何参数的功能，用于北京地铁线路的检测，该装置根据北京地铁上接触式接触轨安装方式进行设计，使用视觉传感器拍摄接触轨的轮廓图像，在轨检车的轨距等测量信息的基础上，实现对接触轨几何参数的检测。
## 设计思路
以往关于我国对接触轨的检测主要以人工手动检测为主，在地铁运行的“天窗”时间内手持接触轨检测尺检测接触轨几何参数，这种检测方式需要大量人力，且检测精度和效率都比较低。而对精度高的接触轨几何参数检测装置研究关注较少，本课题通过对理解轨道交通的牵引动力馈送方式及原理基础上，综述接触轨和架空接触悬挂方式、第三轨馈电结构现状及其技术要求明确走行轨和第三轨的关系及第三轨检测的目的及意义。在此基础上构建第三轨测量机构的几何特征参数，分析2D激光扫描的光学特性，建立光学参数和测量机构几何参数的标定方案。采集标定样块的实测点云数据，通过霍夫线变换完成相关参数的标定参数计算及软件的设计。后提炼研究结论，指出不足之处和提出研究展望。课题将理论与实践相结合，在第三轨检测领域的研究有一定的研究价值及可行性。
## 部分算法
### 霍夫空间演示
<img decoding="async" src="https://raw.githubusercontent.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform/main/%E9%9C%8D%E5%A4%AB%E7%A9%BA%E9%97%B44.jpg" width="50%">
### 交点投票
未完待续
<img decoding="async" src="https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform/blob/main/4_with_line.png" width="50%">


<img decoding="async" src="https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform/blob/main/%E9%80%89%E7%82%B9.png">
<img decoding="async" src="https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform/blob/main/%E9%80%89%E7%82%B9%E6%94%BE%E5%A4%A71.png">
<img decoding="async" src="https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform/blob/main/%E9%80%89%E7%82%B9%E6%94%BE%E5%A4%A71%E5%B8%A6%E6%A0%BC%E7%BA%BF.png">
<img decoding="async" src="https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform/blob/main/%E9%80%89%E7%82%B9%E6%94%BE%E5%A4%A72.png">
<img decoding="async" src="https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform/blob/main/%E9%80%89%E7%82%B9%E6%94%BE%E5%A4%A72%E5%B8%A6%E6%A0%BC%E7%BA%BF.png">

<img decoding="async" src="https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform/blob/main/%E5%8A%A0%E6%9D%83%E5%B9%B3%E5%9D%87%E7%82%B9.png">
<img decoding="async" src="https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform/blob/main/%E5%8A%A0%E6%9D%83%E5%B9%B3%E5%9D%87%E7%82%B9%E6%94%BE%E5%A4%A71.png">
<img decoding="async" src="https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform/blob/main/%E5%8A%A0%E6%9D%83%E5%B9%B3%E5%9D%87%E7%82%B9%E6%94%BE%E5%A4%A72.png">

<img decoding="async" src="https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform/blob/main/4_select_line1.png" width="50%">
<img decoding="async" src="https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform/blob/main/4_select_line2.png" width="50%">
<img decoding="async" src="https://github.com/Ryan-dodo/The-third-track-optical-calibration-based-on-Hough-transform/blob/main/%E9%9C%8D%E5%A4%AB%E5%B8%A6%E7%BD%91%E6%A0%BC.png">
## 总结
未完待续
