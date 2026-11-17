from playwright.sync_api import expect, Page

class Buzz:

    def __init__(self, page:Page):
        self.page = page
        # self.buzz_link = self.page.locator("//span[text()='Buzz']")       
        self.buzz_link = self.page.locator("//span[text()='Directory']")
        self.input = self.page.get_by_placeholder("What's on your mind?")
        self.file_upload = self.page.locator("input[type='file']")
        self.post_button = self.page.get_by_text(" Post ")
        self.share_photos_button = self.page.get_by_text(' Share Photos')
        self.share_video_button = self.page.get_by_text(" Share Video")
        self.most_recent_posts = self.page.get_by_text(" Most Recent Posts ")
        self.most_post_liked = self.page.get_by_text(" Most Liked Posts ")
        self.most_commented_posts = self.page.get_by_text(" Most Commented Posts ")
        self.share_disable = self.page.get_by_role('button', name='Share', disabled=True).last
        self.share_enable = self.page.get_by_role('button', name='Share', disabled=False).last
        self.Add_photos = self.page.locator("//p[text()='Add Photos']")
        self.more_mb_error_message = self.page.get_by_text("Maximum allowed file size is 2MB")
        self.photos_uploaded = self.page.locator("div.orangehrm-buzz-photos-item>img")
        self.post_time = self.page.locator("p.orangehrm-buzz-newsfeed-title").inner_text()


    def click_on_buzz_link(self):
        try:
            self.buzz_link.click()
        except Exception as e:
            print(f"exception while clicking on buzz link {e}")
            raise e

    def enter_post_data(self):
        try:
            self.input.click()
            self.input.type('Testing Automation', delay=5)
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f"exception while entering the post data {e}")
            raise e

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
                self.file_upload.set_input_files(img)
                self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f"exception while entering the post data {e}")
            raise e

    def most_recent_post(self):
        try:
            self.most_recent_posts.click()
            print(self.post_time)
        except Exception as e:
            print(f"exception while entering the post data {e}")
            raise e
        
        
        
        
