import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from Pages.LoginPage import LoginPage
from Pages.Buzz import BuzzPage
from playwright.sync_api import expect
import pytest

images = ['/Users/google/Downloads/qrcode_www.google.com.png']
more_mb_img = ['/Users/google/Downloads/gemini.jpeg']
more_images = ['/Users/google/Documents/orange/Testing.png', '/Users/google/Documents/orange/Tests/drop.png']


@pytest.mark.regression
def test_login_with_valid_credentials(page):
    lp = LoginPage(page)
    lp.login('Admin','admin123')
    bp = BuzzPage(page)
    bp.clicking_buzz_link()

# @pytest.mark.skip
def test_add_and_remove_photo(page):
    bp = BuzzPage(page)
    bp.clicking_buzz_link()
    bp.clicking_on_share_photo()
    expect(bp.share).to_be_disabled()
    bp.uploading_the_image(images)
    expect(bp.images_uploaded).to_be_visible()
    expect(bp.share).to_be_enabled()
    bp.click_remove_photo_icon()
    expect(bp.share).to_be_disabled()
    bp.click_close_share_photo_popup()
    expect(bp.share_popup_title).not_to_be_visible()
    
#@pytest.mark.skip
def test_upload_more_mb_image(page):
    bp = BuzzPage(page)
    bp.clicking_buzz_link()
    bp.clicking_on_share_photo()
    bp.uploading_the_image(more_mb_img)
    expect(bp.more_mb_error_message).to_be_visible()

#@pytest.mark.skip
def test_upload_more_images(page):
    bp = BuzzPage(page)
    bp.uploading_the_image(more_images)
    total_images = bp.images_uploaded.all()
    assert len(total_images) == len(more_images)
    bp.click_close_share_photo_popup()

#@pytest.mark.skip
def test_share_vedio(page):
    bp = BuzzPage(page)
    bp.clicking_buzz_link()
    bp.click_share_video_button()
    bp.enter_video_url('https://www.youtube.com/shorts/M-PKFDoR24I')
    expect(bp.video_details.locator("div#player-controls")).to_be_visible()
    bp.clear_entered_link()
    expect(page.get_by_text('Required')).to_be_visible()
    bp.click_close_video_popup()
    expect(bp.share_video_popup_close).not_to_be_visible()


#@pytest.mark.skip
def test_most_recent_posts(page):
    bp = BuzzPage(page)
    bp.clicking_on_share_photo()
    bp.uploading_the_image(images)
    total_images = bp.images_uploaded.all()
    # print(len(total_images))
    assert len(total_images) == len(images)
    bp.click_close_video_popup()

# #@pytest.mark.skip
def test_most_recent_posts_action(page):
    bp = BuzzPage(page)
    if  bp.no_posts_available() != 'No Posts Available':
        print('pOSt AVIALABLE')
        bp.post_action_message()
        bp.post_action_share()
        expect(bp.most_recent_post_actions_share_title).to_be_visible()
        bp.post_action_share_close()
        expect(bp.most_recent_post_actions_share_title).not_to_be_visible()
    else:
        expect(bp.no_posts).to_be_visible()
        print('No Posts available')

@pytest.mark.regression
#@pytest.mark.skip
def test_most_liked_posts(page):
    bp = BuzzPage(page)
    bp.click_most_liked_posts()
    # bp.no_posts_available()
    if  bp.no_posts_available() != 'No Posts Available':
        print('pOSt AVIALABLE')
        bp.post_action_message()
        bp.post_action_share()
        expect(bp.most_recent_post_actions_share_title).to_be_visible()
        bp.post_action_share_close()
        expect(bp.most_recent_post_actions_share_title).not_to_be_visible()
        mostlike, maxlike = bp.most_no_liked_post()
        assert mostlike == maxlike
        bp.click_most_comment_post()
        bp.post_action_message()
        bp.post_action_share()
        expect(bp.most_recent_post_actions_share_title).to_be_visible()
        bp.post_action_share_close()
        expect(bp.most_recent_post_actions_share_title).not_to_be_visible()
        print(bp.most_no_liked_post())
    else :
        print('No Posts available')
        expect(bp.no_posts).to_be_visible()
        


def test_logout(page):
    lp = LoginPage(page)
    lp.click_profile_icon()
    lp.click_logout_button()





