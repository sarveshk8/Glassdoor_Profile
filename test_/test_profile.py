from POM.profile import Profile
from Data import reading_object
import  pytest

data_obj = reading_object.read_data()
@pytest.mark.parametrize("data_",data_obj)
class TestProfile:

    def test_login(self,_driver,data_):
        lp = Profile(_driver)
        lp.enter_username(data_)
        lp.click_next()
        lp.enter_pass(data_)
        lp.click_login()
        lp.profile_icon()
        lp.job_status()
        lp.name(data_)
        lp.job_role(data_)
        lp.company(data_)
        lp.current_location(data_)
        lp.checkbox()
        lp.des_job(data_)
        lp.des_loc(data_)
        lp.cvs(data_)
