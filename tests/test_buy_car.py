import pytest
from pytest_check import check
from pom.buy_car import BuyCar
import time


@pytest.mark.usefixtures('setup')
class TestBuyCar:
    #TODO add annotations

    @pytest.mark.all_tests
    @pytest.mark.buy_modelx
    def test_buy_car(self):
        instance_class = BuyCar(self.driver)
        instance_class.go_to_modelx()
        # time.sleep(15)
