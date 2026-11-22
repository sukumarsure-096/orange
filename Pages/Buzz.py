from playwright.sync_api import Page
from pathlib import Path

class BuzzPage:
    def __init__(self, page:Page):
        self.page = page
        self.buzz_link = self.page.locator("//span[text()='Buzz']")
        # Locators related to share photo
        self.share_photos_button = self.page.get_by_text(' Share Photos')
        self.file_upload = self.page.locator("input[type='file']")
        self.images_uploaded = self.page.locator("div.orangehrm-photo-input div.orangehrm-buzz-photos-item")
        self.more_mb_error_message = self.page.get_by_text("Maximum allowed file size is 2MB")
        self.remove_image = self.page.locator("button.oxd-icon-button.orangehrm-photo-input-remove")
        self.add_photos = self.page.get_by_text("Add Photos")
        self.close_share_photos_popup = self.page.locator("button.oxd-dialog-close-button.oxd-dialog-close-button-position")
        self.share = self.page.get_by_role('button', name='Share').last
        self.share_popup_title = self.page.locator("//p[text()='Share Photos']")

        # Locators related to vedio
        self.share_vedio_button = self.page.get_by_role('button', name='Share Video')
        self.enter_vedio_link = self.page.get_by_placeholder('Paste Video URL')
        self.video_details = self.page.frame_locator("[title='OrangeHRM buzz video frame']")
        self.video_popup_title = self.page.locator("//p[text()='Share Video']")
        self.video_error_meesage = self.page.get_by_text('Required')
        self.close_share_video_popup_button = self.page.locator("button.oxd-dialog-close-button.oxd-dialog-close-button-position")
        self.share_video_popup_close = self.page.locator("[role='document']")
        
        #locator related to recent posts
        self.posted_time = self.page.locator('p.oxd-text.oxd-text--p.orangehrm-buzz-post-time')
        self.first_time_posted = self.page.locator("p.oxd-text.oxd-text--p.orangehrm-buzz-post-time").nth(0)
        self.most_recent_posts = self.page.get_by_text(" Most Recent Posts ")
        self.most_recent_post_actions = self.page.locator("div.orangehrm-buzz-post-actions").first
        self.most_recent_post_actions_message = self.most_recent_post_actions.locator(">button").first
        self.most_recent_post_actions_message_comment = self.page.get_by_placeholder('Write your comment...')
        self.most_recent_post_actions_share = self.most_recent_post_actions.locator(">button").nth(1)
        self.most_recent_post_actions_share_comment = self.page.get_by_placeholder("What's on your mind?").nth(1)
        self.most_recent_post_actions_share_title = self.page.get_by_text('Share Post')
        self.most_recent_post_actions_share_close = self.page.locator("//button[text()='×']")
        self.most_recent_posts_item = self.page.locator("div.orangehrm-buzz-post").all()

        #locator -> most liked posts
        self.most_liked_post = self.page.get_by_text(' Most Liked Posts ')
        self.most_liked_post_card = self.page.locator("div.oxd-grid-item oxd-grid-item--gutters")
        self.most_no_likes = self.page.locator("p:has-text('Like')").all()

        #locator -> most recent comment posts
        self.most_comment_post = self.page.get_by_text(' Most Commented Posts ')
        self.no_posts = self.page.get_by_text('No Posts Available')

        # Images
        self.images = ['drop.png']
        self.more_mb_img = ['gemini.jpeg']
        self.more_images = ['Testing.png', 'drop.png']


    def clicking_buzz_link(self):
        self.buzz_link.click()
        self.page.wait_for_timeout(5000)

    def clicking_on_share_photo(self):
        try:
            self.share_photos_button.click()
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f"exception while entering the post data {e}")
            raise e

    def uploading_the_image(self, image):
        try:
            for img in image:
                image_path = Path(__file__).parent.parent / "images" /img
                self.file_upload.set_input_files(str(image_path))
                self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f"exception while entering the post data {e}")
            raise e

    def most_recent_post(self):
        try:
            self.most_recent_posts.click()
            self.page.wait_for_timeout(5000)
            if len(self.posted_time.all()) > 0:
                first_time = self.posted_time.all_inner_texts()[0]
                sec_time = self.first_time_posted.inner_text()
                assert first_time == sec_time
            else :
                print('no posts')

        except Exception as e:
            print(f"exception while entering the post data {e}")
            raise e
    
    def click_remove_photo_icon(self):
        try:
            self.remove_image.click()
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f"exception while entering the post data {e}")
            raise 

    def click_close_share_photo_popup(self):
        try:
            self.close_share_photos_popup.click()
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f"exception while entering the post data {e}")
            raise e

    def click_share_video_button(self):
        try:
            self.share_vedio_button.click()
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f"exception while entering the post data {e}")
            raise e

    def enter_video_url(self, link):
        try:
            self.enter_vedio_link.fill(link)
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f"exception while entering the post data {e}")
            raise e

    def click_close_video_popup(self):
        try:
            self.close_share_video_popup_button.click()
        except Exception as e:
            print(f"exception while entering the post data {e}")
            raise e

    def clear_entered_link(self):
        try:
            self.enter_vedio_link.click()
            self.enter_vedio_link.clear()
            self.page.wait_for_timeout(5000)
        except Exception as e:
                print(f"exception while entering the post data {e}")
                raise e

    def post_action_message(self):
        try:
            self.most_recent_post_actions_message.click()
            self.most_recent_post_actions_message_comment.type('hi')
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f'exception while clicking and adding comment message icon {e}')
            raise e

    def post_action_share(self):
        try:
            self.most_recent_post_actions_share.click()
            self.most_recent_post_actions_share_comment.click()
            self.most_recent_post_actions_share_comment.fill('hi')
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f'exception while clicking and adding comment message icon {e}')
            raise e

    def post_action_share_close(self):
        try:
            self.most_recent_post_actions_share_close.click()
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f'exception while clicking and adding comment message icon {e}')
            raise e

    def click_most_liked_posts(self):
        try:
            self.most_liked_post.click()
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f'exception while clicking and adding comment message icon {e}')
            raise e
    
    def most_no_liked_post(self):
        l = []
        self.page.wait_for_timeout(5000)
        for like in self.most_no_likes:
            l.append(int(like.inner_text().split(' ')[0]))
        l.sort(reverse=True)
        return max(l), l[0]

    def click_most_comment_post(self):
        try:
            self.most_comment_post.click()
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f'exception while clicking and adding comment message icon {e}')
            raise e

    def no_posts_available(self):
        try:
            nopost = self.no_posts.inner_text()
            # print('nopost------->', nopost)
            return nopost
        except Exception as e:
            print(f'exception while clicking and adding comment message icon {e}')
            raise e
        
       
    
    