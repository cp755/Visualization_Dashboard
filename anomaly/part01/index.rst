Metatron Anomaly 소개
-------------------------------------------------

이상 탐지 확장팩 Anomaly는 Machine Learning 예측 모델을 기반으로 데이터 흐름의 비정상적인 상황을 감지하여 사용자가 즉각적으로 확인할 수 있도록 도와주는 도구입니다.

.. _basic_principles:

기본 원리
==================================

아래 그림과 같이 Anomaly는 대상 데이터 소스의 집계값을 실시간으로 예측하고 실제 값을 모니터링합니다.

	.. figure:: /_static/img/anomaly/part01/features_01.png
	   :align: center
	   :alt: aggregation monitoring

여기서 **Predict**\로 표시된 값은 머신러닝 기반으로 예측한 데이터 집계값이고, **Actual**\로 표시된 값은 실제로 모니터링한 결과 값입니다. 아래 그림과 같이 두 값 간의 격차가 커질수록 **total abnormal score**\가 증가하게 됩니다. 즉, 실제치가 예상치와 다르면 데이터 집계값이 그만큼 정상 범위를 벗어났다고 간주하는 것입니다.

	.. figure:: /_static/img/anomaly/part01/features_02.png
	   :align: center
	   :alt: total abnormal score

이 예시에서는 abnormal score가 20점에 도달하면 ``Low`` 레벨의 알람을 발생시키고, 40점을 넘으면 ``Moderate``, 60점을 넘으면 	``Major``, 80점을 넘으면 ``Critical`` 알람을 발생시키도록 설정되어 있습니다. traning data에 따르면 사용자들은 4월 6일 15시에 Critical 등급의 알람을 받았을 것이라고 예측할 수 있습니다.

이렇게 설정된 알람 룰은 데이터가 갱신되면서 알람을 발생시키고 다양한 채널로 사용자에게 통보됩니다. 따라서 관련 시스템 운영자 및 사용자들은 데이터 이상 상황에 즉각 대처할 수 있습니다.

주요 기능
==================================

Anomaly의 주요 기능은 다음과 같습니다.

* **Auto Machine Learning** : 머신러닝 기반 예측 모델을 자동으로 추천하여 사용자 편의성 증진

* **Alarm & Report** : 비정상적인 상황 발생 시 즉각 알람 발생 및 보고서 생성 지원

* **Analyze** : 데이터 원천을 분석할 수 있는 실시간 대시보드 및 실시간 검색 기능 지원

* **Link with Learning System** : 신규 알고리즘 모델을 적용할 수 있도록 3rd-party 시스템 연계를 지원

구조
==================================

Anomaly의 메뉴 구성은 다음과 같이 크게 **이상 탐지**\와 **데이터 관제**\ 두 개의 카테고리로 나누어 집니다.

	.. figure:: /_static/img/anomaly/part01/structure_01.png
	   :align: center
	   :alt: metatron anomaly structure


**Anomaly Detection** 메뉴에서는 전반적인 이상 탐지 알람 통계(Statistics), 발생한 알람들의 정보(Alarm), 알람이 발생하는 규칙 설정(Alarm Rule), 신규 알고리즘 추가(Algorithm)를 지원합니다.

**Data Monitoring** 메뉴에서는 알람이 발생할 경우 데이터 소스 원천에 대해서 분석할 수 있도록 실시간 대시보드(Dashboard)와 원천을 쿼리할 수 있도록 하는 실시간 검색(Search) 기능을 제공합니다.

주요 메뉴 간 이동이 간편하고 세부 항목 간 참조 기능이 구축되어 있어 발생한 알람 내역 및 설정된 알람 룰, 그리고 전반적인 알람 현황 간의 유기적인 파악이 용이합니다. 또한 알람 발생 시 동일한 시스템 내에서 원천을 탐색할 수 있는 기능도 있어서 원인 파악에 더욱 용이합니다.
